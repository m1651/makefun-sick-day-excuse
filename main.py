#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes a single line (under 200 characters) to /output/entry.txt.
Stdlib only, no network.
"""

import os

ENTRY = (
    "My sink started leaking at 3am and the plumber called it 'aggressive', "
    "so I'm staying home to supervise it \u2014 apparently it has a union rep now."
)


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry text is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and verify the file holds exactly the entry text, no
    # trailing newline or stray whitespace that would change its length.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit(
            f"verification failed: file differs from entry "
            f"({len(written)} chars on disk vs {len(text)} expected)"
        )
    print(f"wrote /output/entry.txt ({len(text)} characters)")


if __name__ == "__main__":
    main()
