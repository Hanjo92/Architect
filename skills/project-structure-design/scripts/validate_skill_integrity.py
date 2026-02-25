#!/usr/bin/env python3
"""Custom integrity checks for project-structure-design skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_MD = ROOT / "SKILL.md"
REF_DIR = ROOT / "references"

REQUIRED_REFERENCES = [
    "architecture-decision-tree.md",
    "project-structure-blueprints.md",
    "ddd-actor-aggregate-pattern.md",
    "csharp-functional-static-style.md",
    "webapp-naming-comment-conventions.md",
    "game-outgame-ddd-ingame-ecs.md",
    "unity-upm-modularization.md",
    "architecture-decision-checklist.md",
    "output-template.md",
    "anti-patterns.md",
    "migration-playbook.md",
    "migration-task-board-template.md",
    "game-design-analysis-playbook.md",
    "domain-catalog-template.md",
    "sample-folder-generator-rules.md",
    "lightweight-planning-augmentation.md",
    "planning-doc-domain-organization.md",
]

CRITICAL_PHRASES = [
    "Outgame(DDD)",
    "Ingame(ECS)",
    "UPM",
    "Port/Adapter",
    "clean-code naming conventions",
    "XML docs",
    "TSDoc/JSDoc",
    "validation gates",
    "migration-task-board-template.md",
    "lightweight planning augmentation",
    "planning docs are many",
]


def check_required_references(errors: list[str]) -> None:
    for filename in REQUIRED_REFERENCES:
        path = REF_DIR / filename
        if not path.exists():
            errors.append(f"Missing required reference file: references/{filename}")


def check_skill_md_exists(errors: list[str]) -> str:
    if not SKILL_MD.exists():
        errors.append("Missing SKILL.md")
        return ""
    return SKILL_MD.read_text(encoding="utf-8")


def check_markdown_links(skill_text: str, errors: list[str]) -> None:
    # Supports [text](relative/path.md) links only.
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", skill_text)
    for link in links:
        if "://" in link or link.startswith("mailto:"):
            continue
        target = (ROOT / link).resolve()
        if not target.exists():
            errors.append(f"Broken local link in SKILL.md: {link}")


def check_critical_phrases(skill_text: str, errors: list[str]) -> None:
    for phrase in CRITICAL_PHRASES:
        if phrase not in skill_text:
            errors.append(f"Missing critical phrase in SKILL.md: {phrase}")


def main() -> int:
    errors: list[str] = []
    check_required_references(errors)
    skill_text = check_skill_md_exists(errors)
    if skill_text:
        check_markdown_links(skill_text, errors)
        check_critical_phrases(skill_text, errors)

    if errors:
        print("Integrity validation failed:")
        for item in errors:
            print(f"- {item}")
        return 1

    print("Integrity validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
