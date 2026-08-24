#!/usr/bin/env python3

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "figma_components.py"
SPEC = importlib.util.spec_from_file_location("figma_components", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class FigmaComponentsTests(unittest.TestCase):
    def setUp(self):
        self.payload = json.loads(
            (ROOT / "tests/fixtures/figma-component-node.json").read_text(encoding="utf-8")
        )
        self.url = (
            "https://www.figma.com/design/baseKey/branch/branchKey/Lib-iOS"
            "?node-id=42-7"
        )

    def test_parses_branch_url_and_normalizes_node_id(self):
        source = MODULE.parse_figma_url(self.url)

        self.assertEqual(source["fileKey"], "baseKey")
        self.assertEqual(source["branchKey"], "branchKey")
        self.assertEqual(source["apiFileKey"], "branchKey")
        self.assertEqual(source["nodeId"], "42:7")

    def test_parses_main_file_url(self):
        source = MODULE.parse_figma_url(
            "https://figma.com/file/baseKey/Library?node-id=10%3A20"
        )

        self.assertIsNone(source["branchKey"])
        self.assertEqual(source["apiFileKey"], "baseKey")
        self.assertEqual(source["nodeId"], "10:20")

    def test_lifecycle_markers_and_default_ready(self):
        self.assertEqual(MODULE.status_from_name("Button"), "ready")
        self.assertEqual(MODULE.status_from_name("🟢 Button"), "ready")
        self.assertEqual(MODULE.status_from_name("🔵 Button"), "design-only")
        self.assertEqual(MODULE.status_from_name("🟡 Button"), "work-in-progress")
        self.assertEqual(
            MODULE.status_from_name("Rail - 🟡Catalog [Нет в проде]"),
            "work-in-progress",
        )
        self.assertEqual(MODULE.status_from_name("⚪ Button"), "planned")
        self.assertEqual(MODULE.status_from_name("🔴 Button"), "deprecated")
        self.assertEqual(MODULE.status_from_name("Button [Deprecated]"), "deprecated")

    def test_extracts_properties_variants_sizes_and_dependencies(self):
        snapshot = MODULE.snapshot_from_payload(self.payload, "42:7")

        self.assertEqual(snapshot["nodeType"], "COMPONENT_SET")
        self.assertEqual(snapshot["publishStatus"], "CHANGED")
        self.assertEqual(snapshot["status"], "ready")
        self.assertEqual(snapshot["variantCount"], 2)
        self.assertEqual(snapshot["variants"]["Device"], ["iPad", "iPhone"])
        self.assertEqual(snapshot["variants"]["State"], ["Disabled", "Rest"])
        self.assertEqual(snapshot["dimensions"][0]["height"], 36.0)
        self.assertEqual(snapshot["dependencies"][0]["name"], "Icon / Close")
        self.assertEqual(snapshot["dependencies"][0]["componentSetId"], "90:0")

    def test_registers_component_for_explicit_platform_library(self):
        registry = MODULE.empty_registry()
        record, _ = MODULE.upsert_component(
            registry,
            MODULE.parse_figma_url(self.url),
            MODULE.snapshot_from_payload(self.payload, "42:7"),
            slug="android-control",
            platform="android",
            library_id="lib-android",
        )

        self.assertEqual(record["platform"], "android")
        self.assertEqual(record["libraryId"], "lib-android")

    def test_strips_figma_internal_suffix_from_property_name(self):
        payload = json.loads(json.dumps(self.payload))
        definitions = payload["nodes"]["42:7"]["document"]["componentPropertyDefinitions"]
        definitions["Status Bar#33052:1"] = definitions.pop("Enabled")

        snapshot = MODULE.snapshot_from_payload(payload, "42:7")
        prop = next(item for item in snapshot["properties"] if item["name"] == "Status Bar")

        self.assertEqual(prop["key"], "Status Bar#33052:1")

    def test_managed_block_refresh_preserves_manual_text(self):
        source = MODULE.parse_figma_url(self.url)
        registry = MODULE.empty_registry()
        record, _ = MODULE.upsert_component(
            registry, source, MODULE.snapshot_from_payload(self.payload, "42:7"), slug="test-control"
        )
        original = "# Test\n\n## Назначение\n\nРучное описание.\n"

        first = MODULE.replace_managed_block(original, MODULE.format_managed_block(record))
        record["snapshot"]["status"] = "deprecated"
        second = MODULE.replace_managed_block(first, MODULE.format_managed_block(record))

        self.assertIn("Ручное описание.", second)
        self.assertEqual(second.count(MODULE.MANAGED_START), 1)
        self.assertIn("статус `deprecated`", second)
        self.assertIn("### Состояния", second)

    def test_diff_names_added_and_removed_variant_values(self):
        before = MODULE.snapshot_from_payload(self.payload, "42:7")
        after = json.loads(json.dumps(before))
        after["name"] = "🟡 Renamed Control"
        after["status"] = "work-in-progress"
        after["variants"]["State"] = ["Rest", "Touch"]
        after["properties"].append(
            {"name": "Label", "type": "text", "defaultValue": "Текст"}
        )

        changes = MODULE.snapshot_changes(before, after)

        self.assertIn("name: '🟢 Test Control' → '🟡 Renamed Control'", changes)
        self.assertIn("status: 'ready' → 'work-in-progress'", changes)
        self.assertIn("variant State: +Touch; -Disabled", changes)
        self.assertIn("property added: Label", changes)

    def test_persists_registry_card_and_generated_library_table(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "design-system/components").mkdir(parents=True)
            map_path = root / MODULE.LIBRARIES_MAP_PATH
            map_path.parent.mkdir(parents=True)
            map_path.write_text("# Map\n\n## Продуктовые файлы\n", encoding="utf-8")

            registry = MODULE.empty_registry()
            source = MODULE.parse_figma_url(self.url)
            record, _ = MODULE.upsert_component(
                registry,
                source,
                MODULE.snapshot_from_payload(self.payload, "42:7"),
                slug="test-control",
            )
            MODULE.persist(root, registry, [record])

            card = (root / "design-system/components/test-control.md").read_text(encoding="utf-8")
            registry_data = json.loads((root / MODULE.REGISTRY_PATH).read_text(encoding="utf-8"))
            library_map = map_path.read_text(encoding="utf-8")

            self.assertIn("# 🟢 Test Control", card)
            self.assertIn("`branchKey`", card)
            self.assertEqual(registry_data["components"][0]["source"]["nodeId"], "42:7")
            self.assertIn(MODULE.MAP_START, library_map)
            self.assertIn("test-control.md", library_map)

    def test_rejects_frame_as_primary_component(self):
        payload = {"document": {"name": "Guide", "type": "FRAME"}}
        snapshot = MODULE.snapshot_from_payload(payload, "42:7")

        with self.assertRaises(MODULE.ComponentError):
            MODULE.upsert_component(
                MODULE.empty_registry(), MODULE.parse_figma_url(self.url), snapshot
            )

    def test_registers_canvas_as_collection_with_component_members(self):
        payload = {
            "document": {
                "id": "42:7",
                "name": "Layouts",
                "type": "CANVAS",
                "children": [
                    {
                        "id": "42:8",
                        "name": "Layout - Phone",
                        "type": "COMPONENT",
                        "absoluteBoundingBox": {"width": 393, "height": 852},
                        "componentPropertyDefinitions": {
                            "Status Bar#1:2": {"type": "BOOLEAN"}
                        },
                    },
                    {
                        "id": "42:9",
                        "name": "_Layout - Internal Part",
                        "type": "COMPONENT",
                        "absoluteBoundingBox": {"width": 24, "height": 24},
                    }
                ],
            }
        }
        snapshot = MODULE.collection_snapshot_from_payload(payload, "42:7")
        registry = MODULE.empty_registry()
        record, changes = MODULE.upsert_collection(
            registry,
            MODULE.parse_figma_url(self.url),
            snapshot,
            slug="layouts",
        )

        self.assertEqual(changes, ["new"])
        self.assertEqual(snapshot["memberCount"], 1)
        self.assertEqual(snapshot["members"][0]["properties"][0]["name"], "Status Bar")
        self.assertEqual(record["kind"], "collection")
        self.assertEqual(registry["collections"][0]["slug"], "layouts")

    def test_rejects_internal_component_as_primary_card(self):
        snapshot = MODULE.snapshot_from_payload(self.payload, "42:7")
        snapshot["name"] = "_Button / Icon"

        with self.assertRaisesRegex(MODULE.ComponentError, "внутренними запчастями"):
            MODULE.upsert_component(
                MODULE.empty_registry(), MODULE.parse_figma_url(self.url), snapshot
            )

    def test_explicit_slug_migrates_source_without_duplicate_component(self):
        registry = MODULE.empty_registry()
        snapshot = MODULE.snapshot_from_payload(self.payload, "42:7")
        branch_source = MODULE.parse_figma_url(self.url)
        MODULE.upsert_component(registry, branch_source, snapshot, slug="test-control")
        main_source = MODULE.parse_figma_url(
            "https://www.figma.com/design/baseKey/Lib-iOS?node-id=42-7"
        )

        record, changes = MODULE.upsert_component(
            registry, main_source, snapshot, slug="test-control"
        )

        self.assertEqual(changes, [])
        self.assertEqual(len(registry["components"]), 1)
        self.assertEqual(record["source"]["apiFileKey"], "baseKey")
        self.assertIsNone(record["source"]["branchKey"])


if __name__ == "__main__":
    unittest.main()
