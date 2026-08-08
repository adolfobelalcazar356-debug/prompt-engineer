from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class ReleaseContractTests(unittest.TestCase):
    def test_version_has_matching_changelog_section(self):
        version = text("VERSION").strip()
        changelog = text("CHANGELOG.md")
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")
        self.assertIn(f"## {version} -", changelog)

    def test_release_workflow_guards_version_drift(self):
        workflow = text(".github/workflows/release.yml")
        self.assertIn('fetch-depth: 0', workflow)
        self.assertIn('git diff --quiet "$TAG" -- prompt-engineer', workflow)
        self.assertIn('Bump VERSION and CHANGELOG', workflow)

    def test_release_zip_includes_license_without_expanding_skill_core(self):
        workflow = text(".github/workflows/release.yml")
        self.assertIn('zf.write("LICENSE", "LICENSE")', workflow)
        self.assertIn('"LICENSE"', workflow)
        self.assertIn('prompt-engineer-skill.zip', workflow)

    def test_versioned_release_asset_is_never_clobbered(self):
        workflow = text(".github/workflows/release.yml")
        repair = workflow.split("- name: Repair missing release assets", 1)[1]
        self.assertNotIn("--clobber", repair)

    def test_ci_runs_official_github_skill_dry_run(self):
        workflow = text(".github/workflows/ci.yml")
        self.assertIn("gh skill publish --dry-run .", workflow)
        self.assertIn("GH_TOKEN", workflow)

    def test_readme_distinguishes_opencode_stable_and_v2(self):
        readme = text("README.md")
        self.assertIn("OpenCode stable", readme)
        self.assertIn("OpenCode V2", readme)


if __name__ == "__main__":
    unittest.main()
