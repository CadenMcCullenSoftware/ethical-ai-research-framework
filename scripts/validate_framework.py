#!/usr/bin/env python3
"""Validate verbatim source-point coverage in the expanded framework document."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "source-framework.txt"
EXPANDED = ROOT / "docs" / "framework-with-examples.md"


def main() -> int:
    source_points = [line.strip() for line in SOURCE.read_text(encoding="utf-8").splitlines() if line.strip()]
    expanded_text = EXPANDED.read_text(encoding="utf-8")
    preserved_points = re.findall(r"\*\*Original point:\*\* (.+)", expanded_text)
    example_count = len(re.findall(r"\*\*Illustrative example:\*\*", expanded_text))

    problems = []
    if len(source_points) != 44:
        problems.append(f"Expected 44 source lines, found {len(source_points)}")
    if len(preserved_points) != len(source_points):
        problems.append(f"Expected {len(source_points)} preserved points, found {len(preserved_points)}")
    if source_points != preserved_points:
        for index, (source, preserved) in enumerate(zip(source_points, preserved_points), start=1):
            if source != preserved:
                problems.append(f"Point {index} differs from source: {source!r} != {preserved!r}")
        if len(source_points) != len(preserved_points):
            problems.append("Source and expanded point counts differ")
    if example_count != len(source_points):
        problems.append(f"Expected one example per source point ({len(source_points)}), found {example_count}")

    if problems:
        print("Framework validation FAILED:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print(f"Framework validation passed: {len(source_points)} verbatim points and {example_count} examples.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
