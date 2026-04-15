import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_boundaries.py"
SKILL_MD = ROOT / "SKILL.md"
COMMON_PATTERNS = ROOT / "references" / "common-boundary-patterns.md"


class BoundaryCheckerSkillTests(unittest.TestCase):
    def test_current_python_reports_supported_runtime_or_shows_help(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--help"],
            capture_output=True,
            text=True,
            check=False,
        )

        if sys.version_info >= (3, 11):
            self.assertEqual(result.returncode, 0)
            self.assertIn("Check dependency boundary rules.", result.stdout)
            return

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Python 3.11+", result.stderr)
        self.assertIn("uv run --python 3.11", result.stderr)
        self.assertNotIn("ModuleNotFoundError", result.stderr)

    def test_skill_documents_supported_runtime_commands(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8")

        self.assertIn("uv run --python 3.11", text)
        self.assertIn("python3.11", text)

    def test_cross_context_guidance_uses_dependency_strings(self) -> None:
        text = COMMON_PATTERNS.read_text(encoding="utf-8")

        self.assertNotIn("src/contexts/.+/(domain|application|infrastructure)/", text)
        self.assertIn("dependency strings such as C# namespaces", text)


if __name__ == "__main__":
    unittest.main()
