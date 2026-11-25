"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward small talk that one robot says to another
while they ride an elevator together, to /output/entry.txt.
"""

import os

LINE = "I counted the floors. You counted the floors. We are both still counting. Nice weather."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == text, "round-trip mismatch"
    print(f"Wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
