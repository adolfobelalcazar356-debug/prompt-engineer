from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "prompt-engineer"
SKILL = SKILL_DIR / "SKILL.md"

EXPECTED_FILES = {
    "SKILL.md",
    "references/software-engineering.md",
    "references/project-context.md",
    "adapters/opencode.md",
    "adapters/codex.md",
    "adapters/claude-code.md",
    "examples/examples.md",
}


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class SkillContractTests(unittest.TestCase):
    def test_canonical_package_contains_exactly_seven_files(self):
        actual = {
            p.relative_to(SKILL_DIR).as_posix()
            for p in SKILL_DIR.rglob("*")
            if p.is_file()
        }
        self.assertEqual(EXPECTED_FILES, actual)

    def test_skill_frontmatter_and_size(self):
        body = text(SKILL)
        self.assertLess(len(body.splitlines()), 500)
        match = re.match(r"^---\n(.*?)\n---\n", body, re.DOTALL)
        self.assertIsNotNone(match, "SKILL.md must start with YAML frontmatter")
        frontmatter = match.group(1)
        self.assertRegex(frontmatter, r"(?m)^name:\s*prompt-engineer\s*$")
        description = re.search(r"(?m)^description:\s*(.+)$", frontmatter)
        self.assertIsNotNone(description)
        self.assertTrue(description.group(1).startswith("Use when"))

    def test_core_handoff_modes_and_question_policy(self):
        body = text(SKILL)
        for required in (
            "handoff",
            "Do not execute",
            "Automatic prompt-quality activation is out of scope",
            "`optimize`",
            "`audit`",
            "`explain`",
            "`compare`",
            "SIMPLE",
            "BOUNDED",
            "COMPLEX",
            "EXECUTE_DIRECTLY",
            "EXPLORE_FIRST",
            "PLAN_FIRST",
            "SPEC_FIRST",
            "ASK_USER",
            "normally zero",
            "maximum two",
            "non-goals",
            "verification",
        ):
            self.assertIn(required, body)

    def test_progressive_references_exist(self):
        body = text(SKILL)
        refs = re.findall(r"\[[^\]]+\]\(([^)]+\.md)\)", body)
        self.assertTrue(refs)
        for ref in refs:
            self.assertTrue((SKILL_DIR / ref).is_file(), ref)

    def test_host_adapters_contain_current_discovery_locations(self):
        codex = text(SKILL_DIR / "adapters/codex.md")
        opencode = text(SKILL_DIR / "adapters/opencode.md")
        claude = text(SKILL_DIR / "adapters/claude-code.md")
        self.assertIn(".agents/skills/prompt-engineer/", codex)
        self.assertIn("~/.agents/skills/", codex)
        self.assertIn(".opencode/skills", opencode)
        self.assertIn(".agents/skills", opencode)
        self.assertIn(".claude/skills/prompt-engineer/SKILL.md", claude)
        self.assertIn("~/.claude/skills/", claude)

    def test_bmad_is_read_reuse_only(self):
        project = text(SKILL_DIR / "references/project-context.md")
        self.assertIn("read/reuse", project)
        self.assertIn("Do not mutate", project)
        self.assertIn("Do not require BMAD", project)

    def test_no_obvious_secrets_or_machine_specific_paths(self):
        patterns = [
            r"sk-[A-Za-z0-9_-]{20,}",
            r"BEGIN (?:RSA|OPENSSH|EC) PRIVATE KEY",
            r"C:\\Users\\",
            r"/Users/[^/]+/",
        ]
        for path in SKILL_DIR.rglob("*"):
            if not path.is_file():
                continue
            body = text(path)
            for pattern in patterns:
                self.assertIsNone(re.search(pattern, body), f"{pattern} in {path}")


if __name__ == "__main__":
    unittest.main()
