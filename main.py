"""Office Joke Open entry: writes one single-line office joke to entry.txt.

The joke is written fresh for this competition. It is checked against the
gate before it is written: 1-200 characters, one line, not only whitespace.
"""

import os

ENTRY = "I blocked focus time on my calendar, so my manager booked a meeting called 'Focus Time Review' to discuss it."


def validate_entry(text):
    """Return True only if the text passes the competition gate."""
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if len(text) > 200:
        return False
    if "\n" in text or "\r" in text:
        return False
    if "  " in text:
        # No accidental double spaces: the joke must read clean in one pass.
        return False
    return True


def output_path():
    """Absolute grader output dir: MAKEFUN_OUTPUT_DIR, OUTPUT_DIR, or /output."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main():
    if not validate_entry(ENTRY):
        raise SystemExit("entry failed validation")
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
