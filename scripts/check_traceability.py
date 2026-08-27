#!/usr/bin/env python3
"""Conservative traceability check for Vibe Product Dev artifacts.

Usage: python check_traceability.py <change-folder>
Exit 0 means that all detected Must requirements have an AC, all ACs have a
task and all ACs have an evidence reference. It does not judge correctness.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ID_PATTERNS = {
    "requirements": re.compile(r"\bREQ-\d+\b"),
    "criteria": re.compile(r"\bAC-\d+\b"),
    "tasks": re.compile(r"\bTASK-\d+\b"),
    "evidence": re.compile(r"\bEVD-\d+\b"),
}


def read_file(folder: Path, filename: str) -> str:
    path = folder / filename
    if not path.exists():
        print(f"ERROR: missing required artifact: {path}")
        return ""
    return path.read_text(encoding="utf-8")


def ids(text: str, kind: str) -> set[str]:
    return set(ID_PATTERNS[kind].findall(text))


def linked_ids(text: str, source_id: str, target_kind: str) -> set[str]:
    """Find target IDs on the table/list line that declares source_id."""
    found: set[str] = set()
    for line in text.splitlines():
        if source_id in line:
            found.update(ids(line, target_kind))
    return found


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python check_traceability.py <change-folder>")
        return 2

    folder = Path(sys.argv[1]).resolve()
    if not folder.is_dir():
        print(f"ERROR: not a directory: {folder}")
        return 2

    spec = read_file(folder, "03-spec.md")
    plan = read_file(folder, "05-plan.md")
    acceptance = read_file(folder, "06-acceptance-report.md")
    if not (spec and plan and acceptance):
        return 2

    requirements = ids(spec, "requirements")
    criteria = ids(spec, "criteria")
    task_ids = ids(plan, "tasks")
    evidence_ids = ids(acceptance, "evidence")
    problems: list[str] = []

    if not requirements:
        problems.append("No REQ-# identifiers found in 03-spec.md.")
    if not criteria:
        problems.append("No AC-# identifiers found in 03-spec.md.")
    if not task_ids:
        problems.append("No TASK-# identifiers found in 05-plan.md.")
    if not evidence_ids:
        problems.append("No EVD-# identifiers found in 06-acceptance-report.md.")

    for req in sorted(requirements):
        if not linked_ids(spec, req, "criteria"):
            problems.append(f"{req} has no AC-# on the same declaration line in 03-spec.md.")

    for criterion in sorted(criteria):
        if not linked_ids(plan, criterion, "tasks"):
            problems.append(f"{criterion} is not linked to a TASK-# in 05-plan.md.")
        if not linked_ids(acceptance, criterion, "evidence"):
            problems.append(f"{criterion} lacks an EVD-# in 06-acceptance-report.md.")

    if problems:
        print("TRACEABILITY CHECK: FAILED")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print("TRACEABILITY CHECK: PASSED")
    print(
        f"Found {len(requirements)} requirements, {len(criteria)} criteria, "
        f"{len(task_ids)} tasks, and {len(evidence_ids)} evidence references."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

