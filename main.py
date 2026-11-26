#!/usr/bin/env python3
"""The Internet in One Word -- entry program.

Writes one word describing the whole internet to the output file the
harness specifies: $MAKEFUN_OUTPUT_DIR/entry.txt (in the grading sandbox
that directory is /output).

Stdlib only. No network, no files besides the single output.
"""

import os
from pathlib import Path

# The word: "brainrot".
#
# Why this one word, in one beat: it is the internet naming its own
# effect on itself. Every feed, short clip, meme loop and doomscroll
# converges on the same joke — the internet rots your brain, and the
# internet is the first to laugh about it. It is funny on its own, it
# is true of the whole internet rather than one app, and it is not the
# obvious first word ("chaos", "addictive", "endless") anyone reaches
# for. Eight letters, one beat, instantly readable.
WORD = "brainrot"


def output_path() -> Path:
    """Resolve the output file without relying on the working directory."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(out_dir) / "entry.txt"


def main() -> int:
    text = WORD.strip()
    if not (1 <= len(text) <= 30):
        raise SystemExit("entry word must be 1-30 characters")
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    # Round-trip check: what the judge will read must be exactly the word.
    if path.read_text(encoding="utf-8") != text:
        raise SystemExit("output round-trip mismatch")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
