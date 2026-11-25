#!/usr/bin/env python3
"""Worst Superpower — writes one line inventing the most useless superpower.

Entry: stopping time, but only for the second hand of my own wristwatch —
the ultimate power reduced to a broken watch.
"""
import os

ENTRY = "I can stop time, but only for the second hand of my own wristwatch."

def main():
    # Gate self-check: the sealed scorer accepts only UTF-8 text of
    # 1-140 characters, not only white space, on a single line.
    if not (1 <= len(ENTRY) <= 140):
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-140")
    if "\n" in ENTRY or not ENTRY.strip():
        raise SystemExit("entry must be one non-blank line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
