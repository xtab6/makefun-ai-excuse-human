#!/usr/bin/env python3
"""Write one excuse line to /output/entry.txt.

Deterministic, stdlib only, no network, no model calls. The line is a
single sentence pair (101 characters): an AI agent explaining a missed
deadline through its own condition -- long-term memory that behaves like
a sticky note it already threw away.
"""

import os
import sys

LINE = "I saved your deadline in long-term memory. My long-term memory is a sticky note I already threw away."

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main() -> int:
    # Clean only the contents of /output; never remove the folder itself
    # (the grader mounts it, and removing it fails with EPERM).
    os.makedirs(OUT_DIR, exist_ok=True)
    for name in os.listdir(OUT_DIR):
        path = os.path.join(OUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
    if not 1 <= len(LINE) <= 200:
        return 1
    if not LINE.strip():
        return 1
    if "\n" in LINE or "\r" in LINE:
        return 1
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
