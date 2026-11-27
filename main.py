"""The Printer Finally Answers — make.fun entry.

Writes the single line the office printer would finally say back to
everyone staring at it to /output/entry.txt. The comeback lands in one
read: 40,000 pages printed without a single thank-you, and the paper
jam is not an error — it is a break.
"""

import os

ENTRY = (
    "Stop thumping me. I have printed 40,000 pages for you without "
    "a single thank-you — the paper jam is not an error. It is a break."
)

MAX_CHARS = 240


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "entry must not have leading/trailing space"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
