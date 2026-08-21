#!/usr/bin/env python3

import copy
import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "design_system_knowledge.py"
SPEC = importlib.util.spec_from_file_location("design_system_knowledge", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class DesignSystemKnowledgeTests(unittest.TestCase):
    def test_current_knowledge_tree_is_valid(self):
        validated = MODULE.validate_all(ROOT)

        self.assertEqual(len(validated["libraries"]), 7)
        self.assertEqual(len(validated["components"]), 27)
        self.assertEqual(len(validated["data"]["mappings"]["supportedRoutes"]), 6)

    def test_generated_outputs_are_current(self):
        outputs = MODULE.expected_outputs(ROOT)

        for path, expected in outputs.items():
            self.assertTrue(path.exists())
            self.assertEqual(path.read_text(encoding="utf-8"), expected)

    def test_planned_component_requires_target_quarter(self):
        data = MODULE.read_sources(ROOT)
        lifecycle = MODULE.validate_lifecycle(data["lifecycle"])
        libraries = MODULE.validate_libraries(data["libraries"])
        gaps = MODULE.validate_gaps(data["gaps"])
        components = copy.deepcopy(data["components"])
        components["components"][0]["snapshot"]["status"] = "planned"
        components["components"][0].pop("lifecycle", None)

        with self.assertRaisesRegex(MODULE.KnowledgeError, "targetQuarter"):
            MODULE.validate_components(components, lifecycle, libraries, gaps, ROOT)

    def test_requires_all_six_cross_platform_routes(self):
        data = MODULE.read_sources(ROOT)
        components = MODULE.validate_all(ROOT)["components"]
        mappings = copy.deepcopy(data["mappings"])
        mappings["supportedRoutes"].pop()

        with self.assertRaisesRegex(MODULE.KnowledgeError, "шесть направлений"):
            MODULE.validate_mappings(mappings, components)

    def test_only_confirmed_cases_enter_agent_index(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "design-system", root / "design-system")
            cases_path = root / MODULE.PATHS["cases"]
            source = "https://www.figma.com/design/example/file?node-id=1-2"
            cases = {
                "schemaVersion": 1,
                "cases": [
                    {
                        "id": "confirmed-case",
                        "status": "confirmed",
                        "title": "Подтверждённый кейс",
                        "platforms": ["ios"],
                        "deviceClasses": ["phone"],
                        "componentIds": ["button"],
                        "situation": "Нужно основное действие.",
                        "decision": "Использовать Button.",
                        "constraints": ["Одна основная кнопка."],
                        "sourceLinks": [source]
                    },
                    {
                        "id": "draft-case",
                        "status": "draft",
                        "title": "Черновик",
                        "platforms": ["ios"],
                        "deviceClasses": ["phone"],
                        "componentIds": ["button"],
                        "situation": "Непроверенная ситуация.",
                        "decision": "Непроверенное решение.",
                        "constraints": [],
                        "sourceLinks": [source]
                    }
                ]
            }
            cases_path.write_text(json.dumps(cases, ensure_ascii=False), encoding="utf-8")

            index = MODULE.build_index(MODULE.validate_all(root))

            self.assertEqual([item["id"] for item in index["confirmedCases"]], ["confirmed-case"])


if __name__ == "__main__":
    unittest.main()
