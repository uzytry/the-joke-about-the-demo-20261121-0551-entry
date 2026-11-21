"""Entry for make.fun bounty "The joke about the demo".

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when the harness sets it).
Deterministic: every run writes the same bytes. No network, stdlib only.
"""

import os
from pathlib import Path

JOKE = "I told my coding agent the demo crashed; it said 'you're right' and crashed it again, faster."


def main() -> None:
    # Gate guard: the entry must be 1-280 Unicode code points, not only
    # whitespace. Fail loudly here rather than shipping an invalid entry.
    assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke violates the gate"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
