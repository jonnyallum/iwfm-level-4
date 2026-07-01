#!/usr/bin/env python3
"""Quality checks for the IWFM Level 4 FM Academy repo.

Runs three checks over the Markdown content:

1. Links      - every relative Markdown/JSON link resolves to a file on disk.
2. Metadata   - every learning/content Markdown file carries an ai_metadata block.
3. Structure  - every course module file contains the required section headings.

Usage:
    python3 tools/check_repo.py            # run all checks
    python3 tools/check_repo.py --quiet    # only print failures and the summary

Exit code is 0 when everything passes and 1 when any check fails, so it can be
used in a pre-commit hook, a SessionStart hook or CI.
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys

# Repo root is the parent of this tools/ directory.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LINK_RE = re.compile(r"\]\(([^)]+?\.(?:md|json))(#[^)]*)?\)")
MODULE_GLOB = "[0-1][0-9]-*/module-*.md"

# Files that are pure trackers/utilities and are not expected to carry metadata.
METADATA_EXEMPT = {
    "CHANGELOG.md",
    "TODO.md",
    "CONTRIBUTING.md",
    "COMMIT_GUIDE.md",
    "tools/README.md",
}

REQUIRED_MODULE_SECTIONS = [
    "## Learning Outcomes",
    "## Practical FM Application",
    "## Scenario Questions",
    "## Model Answers",
    "## Marking Guide",
]


def rel(path: str) -> str:
    return os.path.relpath(path, ROOT)


def md_files() -> list[str]:
    return sorted(glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True))


def check_links(quiet: bool) -> list[str]:
    failures: list[str] = []
    checked = 0
    for f in md_files():
        d = os.path.dirname(f)
        text = open(f, encoding="utf-8").read()
        for m in LINK_RE.finditer(text):
            link = m.group(1)
            if link.startswith("http"):
                continue
            checked += 1
            target = os.path.normpath(os.path.join(d, link))
            if not os.path.exists(target):
                failures.append(f"{rel(f)}: broken link -> {link}")
    if not quiet:
        print(f"[links]     checked {checked} internal links")
    return failures


def check_metadata(quiet: bool) -> list[str]:
    failures: list[str] = []
    checked = 0
    for f in md_files():
        r = rel(f)
        if r in METADATA_EXEMPT:
            continue
        checked += 1
        text = open(f, encoding="utf-8").read()
        if "ai_metadata:" not in text:
            failures.append(f"{r}: missing ai_metadata block")
    if not quiet:
        print(f"[metadata]  checked {checked} files for ai_metadata")
    return failures


def check_structure(quiet: bool) -> list[str]:
    failures: list[str] = []
    # Course module files only: exclude workbook files (module-NN-workbook.md),
    # which live in 14-workbook/ and intentionally use a different structure.
    modules = [
        f for f in sorted(glob.glob(os.path.join(ROOT, MODULE_GLOB)))
        if not os.path.basename(f).endswith("-workbook.md")
    ]
    for f in modules:
        text = open(f, encoding="utf-8").read()
        for section in REQUIRED_MODULE_SECTIONS:
            if section not in text:
                failures.append(f"{rel(f)}: missing required section '{section}'")
    if not quiet:
        print(f"[structure] checked {len(modules)} module files for required sections")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="IWFM Level 4 repo quality checks.")
    parser.add_argument("--quiet", action="store_true", help="only print failures and summary")
    args = parser.parse_args()

    all_failures: list[str] = []
    for name, fn in (("links", check_links), ("metadata", check_metadata), ("structure", check_structure)):
        failures = fn(args.quiet)
        for line in failures:
            print(f"FAIL {line}")
        all_failures.extend(failures)

    if all_failures:
        print(f"\n{len(all_failures)} problem(s) found.")
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
