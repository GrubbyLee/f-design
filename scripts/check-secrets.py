#!/usr/bin/env python3
"""Reject likely committed credentials without matching normal prose."""

from __future__ import annotations

import argparse
import pathlib
import re
import subprocess
import sys


RULES = {
    "OpenAI-style API key": re.compile(r"(?<![A-Za-z0-9])sk-[A-Za-z0-9_-]{20,}(?![A-Za-z0-9])"),
    "GitHub token": re.compile(r"(?<![A-Za-z0-9])gh[opusr]_[A-Za-z0-9]{20,}(?![A-Za-z0-9])"),
    "local absolute path": re.compile(r"/home/Arabica(?:/|\b)"),
}

DEFAULT_ALLOWED = {
    ".github/workflows/validate.yml",
    "README.md",
    "README.zh-CN.md",
    "scripts/check-secrets.py",
    "tests/test_release_tooling.py",
}


def candidate_files(root: pathlib.Path) -> list[pathlib.Path]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=root,
        capture_output=True,
        check=True,
    )
    return [root / item.decode() for item in result.stdout.split(b"\0") if item]


def scan(root: pathlib.Path, allowed: set[str] | None = None) -> list[str]:
    allowed = DEFAULT_ALLOWED if allowed is None else allowed
    findings: list[str] = []
    for path in candidate_files(root):
        relative = path.relative_to(root).as_posix()
        if relative in allowed or not path.is_file():
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line_number, line in enumerate(content.splitlines(), 1):
            for label, pattern in RULES.items():
                if pattern.search(line):
                    findings.append(f"{relative}:{line_number}: {label}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan tracked files for likely credentials and local paths.")
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = pathlib.Path(args.root).resolve()
    findings = scan(root)
    if findings:
        print("Potential secret or local-path leakage:")
        for finding in findings:
            print(f"- {finding}")
        return 1
    print("Secret and local-path scan: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
