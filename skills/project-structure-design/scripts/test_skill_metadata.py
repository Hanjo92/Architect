import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_MD = ROOT / "SKILL.md"


class SkillMetadataTests(unittest.TestCase):
    def test_description_is_trigger_oriented_and_concise(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8")
        match = re.search(r"^description:\s*(.+)$", text, re.MULTILINE)

        self.assertIsNotNone(match)
        description = match.group(1)
        self.assertTrue(description.startswith("Use when"))
        self.assertLessEqual(len(description), 500)


if __name__ == "__main__":
    unittest.main()
