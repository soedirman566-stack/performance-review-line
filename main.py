#!/usr/bin/env python3
"""Entrypoint for the Funniest One-Line Performance Review entry.

Reads the review line from line.txt (shipped beside this file) and writes
it to /output/entry.txt, where the competition harness picks it up.
The output directory is only ever written into, never removed.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LINE_FILE = os.path.join(HERE, "line.txt")
OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def read_line(path=LINE_FILE):
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read().strip()


def check_gate(line):
    """Mirror the sealed scorer's gate: UTF-8 text of 1 to 140
    characters, not only white space."""
    if not line or not line.strip():
        raise ValueError("entry is empty or only white space")
    if len(line) > 140:
        raise ValueError("entry is %d characters; the gate allows 140" % len(line))
    line.encode("utf-8")  # raises if the text cannot be encoded


def main():
    line = read_line()
    check_gate(line)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as handle:
        handle.write(line)
    with open(OUTPUT_FILE, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != line:
        raise SystemExit("round-trip mismatch: /output/entry.txt differs from line.txt")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
