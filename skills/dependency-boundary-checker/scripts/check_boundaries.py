#!/usr/bin/env python3
"""Check repository files for dependency boundary violations."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

try:
    import tomllib
except ModuleNotFoundError as exc:
    raise SystemExit(
        "check_boundaries.py requires Python 3.11+ for TOML parsing. "
        "Run it with `python3.11 <skill-root>/scripts/check_boundaries.py ...` "
        "or `uv run --python 3.11 <skill-root>/scripts/check_boundaries.py ...`."
    ) from exc


IMPORT_PATTERNS: dict[str, list[re.Pattern[str]]] = {
    ".cs": [
        re.compile(r"^\s*using\s+([A-Za-z0-9_.]+)\s*;", re.MULTILINE),
        re.compile(r"^\s*global using\s+([A-Za-z0-9_.]+)\s*;", re.MULTILINE),
    ],
    ".ts": [
        re.compile(r"""from\s+['"]([^'"]+)['"]"""),
        re.compile(r"""require\(\s*['"]([^'"]+)['"]\s*\)"""),
    ],
    ".tsx": [
        re.compile(r"""from\s+['"]([^'"]+)['"]"""),
        re.compile(r"""require\(\s*['"]([^'"]+)['"]\s*\)"""),
    ],
    ".js": [
        re.compile(r"""from\s+['"]([^'"]+)['"]"""),
        re.compile(r"""require\(\s*['"]([^'"]+)['"]\s*\)"""),
    ],
    ".jsx": [
        re.compile(r"""from\s+['"]([^'"]+)['"]"""),
        re.compile(r"""require\(\s*['"]([^'"]+)['"]\s*\)"""),
    ],
    ".py": [
        re.compile(r"^\s*import\s+([A-Za-z0-9_., ]+)", re.MULTILINE),
        re.compile(r"^\s*from\s+([A-Za-z0-9_.]+)\s+import\s+", re.MULTILINE),
    ],
}

DEFAULT_EXCLUDES = [
    "**/bin/**",
    "**/obj/**",
    "**/node_modules/**",
    "**/Library/**",
    "**/.git/**",
]


@dataclass
class Rule:
    name: str
    severity: str
    source_globs: list[str]
    forbidden_patterns: list[str]
    allowed_patterns: list[str]
    message: str


@dataclass
class Finding:
    rule: str
    severity: str
    file: str
    dependency: str
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check dependency boundary rules.")
    parser.add_argument("--root", required=True, help="Repository root to scan.")
    parser.add_argument("--config", required=True, help="TOML config file path.")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument(
        "--include-warnings",
        action="store_true",
        help="Include warning-level findings in text output.",
    )
    parser.add_argument(
        "--fail-on",
        choices=["warning", "error", "never"],
        default="error",
        help="Exit non-zero when findings at or above this severity are present.",
    )
    return parser.parse_args()


def load_config(path: Path) -> tuple[list[str], list[Rule], bool]:
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as exc:
        raise ValueError(
            f"Failed to parse TOML config at {path}. "
            "If you are using regex patterns, prefer single-quoted TOML strings."
        ) from exc
    include_warnings = bool(data.get("include_warnings", False))
    exclude = list(data.get("exclude", []))
    raw_rules = data.get("rules", [])
    rules: list[Rule] = []
    for raw in raw_rules:
        rules.append(
            Rule(
                name=raw["name"],
                severity=raw.get("severity", "error"),
                source_globs=list(raw.get("source_globs", [])),
                forbidden_patterns=list(raw.get("forbidden_patterns", [])),
                allowed_patterns=list(raw.get("allowed_patterns", [])),
                message=raw.get("message", raw["name"]),
            )
        )
    return exclude, rules, include_warnings


def is_excluded(path: Path, root: Path, exclude_globs: Iterable[str]) -> bool:
    rel = path.relative_to(root).as_posix()
    return any(path.match(pattern) or Path(rel).match(pattern) for pattern in exclude_globs)


def gather_files(root: Path, patterns: list[str], exclude_globs: list[str]) -> list[Path]:
    files: set[Path] = set()
    for pattern in patterns:
        for path in root.glob(pattern):
            if path.is_file() and not is_excluded(path, root, exclude_globs):
                files.add(path)
    return sorted(files)


def extract_dependencies(path: Path) -> list[str]:
    patterns = IMPORT_PATTERNS.get(path.suffix.lower(), [])
    if not patterns:
        return []
    text = path.read_text(encoding="utf-8", errors="ignore")
    dependencies: list[str] = []
    for pattern in patterns:
        for match in pattern.findall(text):
            if isinstance(match, tuple):
                for item in match:
                    if item:
                        dependencies.append(item.strip())
            else:
                dependencies.extend(split_python_imports(match))
    return [dep for dep in dependencies if dep]


def split_python_imports(raw: str) -> list[str]:
    if "," not in raw:
        return [raw.strip()]
    return [part.strip() for part in raw.split(",") if part.strip()]


def matches_any(value: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, value) for pattern in patterns)


def run_rules(root: Path, rules: list[Rule], exclude_globs: list[str]) -> list[Finding]:
    findings: list[Finding] = []
    for rule in rules:
        files = gather_files(root, rule.source_globs, exclude_globs)
        for path in files:
            dependencies = extract_dependencies(path)
            for dependency in dependencies:
                if not matches_any(dependency, rule.forbidden_patterns):
                    continue
                if rule.allowed_patterns and matches_any(dependency, rule.allowed_patterns):
                    continue
                findings.append(
                    Finding(
                        rule=rule.name,
                        severity=rule.severity,
                        file=path.relative_to(root).as_posix(),
                        dependency=dependency,
                        message=rule.message,
                    )
                )
    return findings


def format_text(findings: list[Finding], include_warnings: bool) -> str:
    visible = [
        finding
        for finding in findings
        if include_warnings or finding.severity == "error"
    ]
    if not visible:
        return "No dependency boundary violations found."
    lines = []
    for finding in visible:
        lines.append(
            f"[{finding.severity.upper()}] {finding.rule}: {finding.file} -> {finding.dependency}"
        )
        lines.append(f"  {finding.message}")
    return "\n".join(lines)


def should_fail(findings: list[Finding], threshold: str) -> bool:
    if threshold == "never":
        return False
    if threshold == "warning":
        return bool(findings)
    return any(finding.severity == "error" for finding in findings)


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    config_path = Path(args.config).resolve()
    try:
        exclude_globs, rules, config_include_warnings = load_config(config_path)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    findings = run_rules(root, rules, DEFAULT_EXCLUDES + exclude_globs)

    if args.format == "json":
        payload = {
            "root": str(root),
            "config": str(config_path),
            "findings": [asdict(finding) for finding in findings],
        }
        print(json.dumps(payload, indent=2))
    else:
        print(format_text(findings, args.include_warnings or config_include_warnings))

    return 1 if should_fail(findings, args.fail_on) else 0


if __name__ == "__main__":
    sys.exit(main())
