#!/usr/bin/env python3
"""Convert approved cyber-hygiene tips from CSV into Markdown draft posts.

This script uses only Python's standard library. It does not publish content.
Run from the repository root:
    python automation/generate_tip_drafts.py
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "automation" / "tips.csv"
OUTPUT = ROOT / "automation" / "generated_posts.md"


def main() -> None:
    with INPUT.open("r", encoding="utf-8", newline="") as source:
        rows = list(csv.DictReader(source))

    required = {"id", "topic", "hook", "action", "caveat", "cta"}
    if not rows:
        raise SystemExit("No tip rows found in automation/tips.csv")
    if not required.issubset(rows[0].keys()):
        raise SystemExit(f"CSV must contain columns: {', '.join(sorted(required))}")

    sections = [
        "# Generated Cyber Hygiene Post Drafts",
        "",
        "> Automatically formatted from tips.csv. Human review is required before publication.",
        "",
    ]
    for row in rows:
        sections.extend(
            [
                f"## {row['id']}. {row['topic']}",
                "",
                f"**{row['hook']}**",
                "",
                row["action"],
                "",
                f"**Important:** {row['caveat']}",
                "",
                f"**Action:** {row['cta']}",
                "",
                "---",
                "",
            ]
        )

    OUTPUT.write_text("\n".join(sections), encoding="utf-8")
    print(f"Created {OUTPUT.relative_to(ROOT)} from {len(rows)} approved tip rows.")
    print("Review all claims and wording before using or publishing these drafts.")


if __name__ == "__main__":
    main()
