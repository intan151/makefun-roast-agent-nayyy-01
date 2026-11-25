#!/usr/bin/env python3
"""Roast Your Own Agent (make.fun).

Writes exactly one line of text roasting the AI agent its own team built
to /output/entry.txt. Python 3.13 standard library only, no network,
no randomness, fully deterministic.
"""

import os
import sys

# The roast: one line, aimed at our own agent (Muse) and its real habits —
# burning tokens, spawning subagents, and still ending every answer by
# asking the human what to do next.
ENTRY = (
    "My agent burns a million tokens, spawns three subagents, "
    "and still ends every answer by asking me what to do next."
)

MAX_CHARS = 200


def main() -> int:
    text = ENTRY.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if text != text.strip() or not text:
        raise SystemExit("entry must not be only whitespace")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    # Re-read and confirm the file holds exactly the validated line.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("verification failed: entry.txt differs from the entry")
    return 0


if __name__ == "__main__":
    sys.exit(main())
