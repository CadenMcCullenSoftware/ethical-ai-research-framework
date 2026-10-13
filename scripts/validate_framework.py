#!/usr/bin/env python3
"""Validate verbatim source-point coverage in the expanded framework document."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "source-framework.txt"
EXPANDED = ROOT / "docs" / "framework-with-examples.md"


def validate_texts(source_text: str, expanded_text: str, expected_source_count: int = 44) -> list[str]:
    """Return validation problems for source-point preservation and example coverage."""
    source_points = [line.strip() for line in source_text.splitlines() if line.strip()]
    preserved_points = re.findall(r"\*\*Original point:\*\* (.+)", expanded_text)
    example_count = len(re.findall(r"\*\*Illustrative example:\*\*", expanded_text))

    problems = []
    if len(source_points) != expected_source_count:
        problems.append(f"Expected {expected_source_count} source lines, found {len(source_points)}")
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
    return problems


def main() -> int:
    """Validate repository documents and report the result to the command line."""
    source_text = SOURCE.read_text(encoding="utf-8")
    expanded_text = EXPANDED.read_text(encoding="utf-8")
    problems = validate_texts(source_text, expanded_text)

    if problems:
        print("Framework validation FAILED:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    point_count = len([line for line in source_text.splitlines() if line.strip()])
    print(f"Framework validation passed: {point_count} verbatim points and {point_count} examples.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
