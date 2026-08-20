#!/usr/bin/env python3

import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from figma_variables import VariableError, apply_target, resolve_payload  # noqa: E402


class FigmaVariablesTest(unittest.TestCase):
    def setUp(self):
        self.payload = json.loads((ROOT / "tests/fixtures/mobile-web.json").read_text())

    def test_resolves_alias_across_collections_by_mode_name(self):
        values = resolve_payload(self.payload, "Web&Mobile")
        self.assertEqual(values["spacing/200"], 4)
        self.assertEqual(values["screen-padding/ios/iphone"], 15)

    def test_applies_spacing_table_and_removes_marker(self):
        with tempfile.TemporaryDirectory() as directory:
            design_system = Path(directory)
            token_dir = design_system / "tokens"
            token_dir.mkdir()
            output = token_dir / "spacing.md"
            output.write_text("## Токены\n\n<!-- VARDEFS_FROM_PLUGIN_API:spacing — test -->\n")

            result = apply_target(self.payload, design_system, "spacing")
            text = output.read_text()

            self.assertEqual(result["variables"]["VARDEFS_FROM_PLUGIN_API:spacing"], 3)
            self.assertIn("`spacing.200` | `4`", text)
            self.assertNotIn("VARDEFS_FROM_PLUGIN_API", text)

    def test_rejects_alias_cycle(self):
        payload = {
            "collections": [{"id": "c", "modes": [{"modeId": "m", "name": "TV"}]}],
            "variables": [
                {"id": "a", "name": "spacing/100", "variableCollectionId": "c", "valuesByMode": {"m": {"type": "VARIABLE_ALIAS", "id": "b"}}},
                {"id": "b", "name": "spacing/200", "variableCollectionId": "c", "valuesByMode": {"m": {"type": "VARIABLE_ALIAS", "id": "a"}}}
            ]
        }
        with self.assertRaises(VariableError):
            resolve_payload(payload, "TV")

    def test_tv_regular_and_focus_markers_do_not_overlap(self):
        payload = {
            "resolvedValues": {
                "corner-radius/100": 4,
                "corner-radius/focus/100": 10,
            }
        }
        with tempfile.TemporaryDirectory() as directory:
            design_system = Path(directory)
            token_dir = design_system / "tokens"
            token_dir.mkdir()
            output = token_dir / "corner-radius-tv.md"
            output.write_text(
                "## Токены\n\n<!-- VARDEFS_FROM_PLUGIN_API:corner-radius-tv — regular -->\n\n"
                "### Focus\n\n<!-- VARDEFS_FROM_PLUGIN_API:corner-radius-tv-focus — focus -->\n"
            )

            apply_target(payload, design_system, "corner-radius-tv")
            text = output.read_text()

            self.assertEqual(text.count("`corner-radius/100`"), 1)
            self.assertEqual(text.count("`corner-radius/focus/100`"), 1)
            self.assertNotIn("VARDEFS_FROM_PLUGIN_API", text)

    def test_formats_resolved_color_values(self):
        payload = {
            "resolvedValues": {
                "color/fill/primary": {"r": 1, "g": 0.5, "b": 0, "a": 1},
                "brand/partner": "#123456",
            }
        }
        with tempfile.TemporaryDirectory() as directory:
            design_system = Path(directory)
            token_dir = design_system / "tokens"
            token_dir.mkdir()
            output = token_dir / "colors.md"
            output.write_text(
                "<!-- VARDEFS_FROM_MCP:semantic — semantic -->\n"
                "<!-- VARDEFS_FROM_MCP:brand — brand -->\n"
            )

            apply_target(payload, design_system, "colors")
            text = output.read_text()

            self.assertIn("`color.fill.primary` | `#FF8000`", text)
            self.assertIn("`brand.partner` | `#123456`", text)


if __name__ == "__main__":
    unittest.main()
