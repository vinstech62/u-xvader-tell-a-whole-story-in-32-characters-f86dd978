#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters -- make.fun entry.

Writes a single Wi-Fi network name to /output/entry.txt: one line,
at most 32 UTF-8 characters, a joke that implies a whole story.
"""

import os

ENTRY = "SheTookTheDogAndTheRouter"


def main():
    text = ENTRY.strip()
    if not text or len(text) > 32:
        raise SystemExit("entry must be 1-32 characters, got %d" % len(text))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
