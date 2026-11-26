"""Your AI Therapist's Diagnosis — make.fun bounty entry.

Writes one funny single-line diagnosis an AI therapist hands its human,
at most 200 characters, to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back
to /output/entry.txt).

The diagnosis plays on a universal modern habit: tab hoarding as
avoidance. The turn lands at the very end — the browser itself ends up
needing therapy more than the patient does. The final line tightens the
first draft: "refuses to load" is replaced by the sharper twist that the
browser needs therapy more, and "like your life" is cut so every word
earns its place.
"""

import os
import sys

DIAGNOSIS = (
    "Diagnosis: chronic tab-hoarding — you open 47 tabs to avoid one "
    "feeling, and now your browser needs therapy more than you do."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(DIAGNOSIS)
    print(f"wrote {len(DIAGNOSIS)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
