import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / ".agents"
    / "skills"
    / "design-ds-librarian"
    / "scripts"
    / "token_studio_read.py"
)
SPEC = importlib.util.spec_from_file_location("token_studio_read", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class TokenStudioReadTests(unittest.TestCase):
    def test_flatten_tokens_supports_tokens_studio_and_dtcg_shapes(self):
        data = {
            "spacing": {
                "$type": "dimension",
                "small": {"value": 4},
                "large": {"$value": 16},
            }
        }

        records = list(MODULE.flatten_tokens(data, "Semantic/Numbers/WebMobile/Main"))

        self.assertEqual([record.path for record in records], ["spacing.small", "spacing.large"])
        self.assertEqual([record.token_type for record in records], ["dimension", "dimension"])

    def test_exact_query_can_be_limited_by_token_set(self):
        records = [
            MODULE.TokenRecord("Semantic/Numbers/WebMobile/Main", "spacing.400", 16, "spacing"),
            MODULE.TokenRecord("Semantic/Numbers/TV/Main", "spacing.400", 24, "spacing"),
        ]

        matches = MODULE.selected_records(records, "spacing.400", exact=True, token_set="TV/Main")

        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0].value, 24)

    def test_output_exposes_aliases_without_guessing_resolution(self):
        record = MODULE.TokenRecord(
            "Semantic/Colors/Main",
            "color.text-icon.primary",
            "rgba( {primitives.white} , 0.96)",
            "color",
        )

        self.assertEqual(record.as_dict()["aliases"], ["primitives.white"])

    def test_read_only_remote_is_fixed(self):
        self.assertEqual(
            MODULE.REPOSITORY_URL,
            "https://github.com/bulatovmsk/token-studio-repo.git",
        )
        self.assertEqual(MODULE.BRANCH, "main")

    def test_archived_sets_are_excluded_by_default(self):
        with tempfile.TemporaryDirectory() as directory:
            themes = Path(directory) / "themes"
            (themes / "_archive").mkdir(parents=True)
            (themes / "Current.json").write_text("{}", encoding="utf-8")
            (themes / "_archive" / "Old.json").write_text("{}", encoding="utf-8")

            current = list(MODULE.token_json_files(Path(directory)))
            all_sets = list(MODULE.token_json_files(Path(directory), include_archive=True))

            self.assertEqual([path.name for path in current], ["Current.json"])
            self.assertEqual([path.name for path in all_sets], ["Current.json", "Old.json"])


if __name__ == "__main__":
    unittest.main()
