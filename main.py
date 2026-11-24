#!/usr/bin/env python3
"""Weirdest Job Title R1 entry.

Keeper: "Senior Accountant for Imaginary Friends" (39 chars).
The job frame is real (Senior Accountant); the twist is the client
(Imaginary Friends) - the most literal, numbers-obsessed job applied
to clients who do not exist. The last two words re-read the setup:
an accountant must audit books for people with no books. Reversal
test passes: "Imaginary Friends" changes what "Senior Accountant"
means. Runner-up was "Librarian of Unsent Text Messages" (34 chars)
- same device, gentler twist; the accountant line is drier and the
frame is the more ordinary job, so the contrast is sharper.
"""
import os

ENTRY = "Senior Accountant for Imaginary Friends"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-check: the gate is 1-60 chars, UTF-8, not only whitespace.
    data = open("/output/entry.txt", "rb").read()
    text = data.decode("utf-8")
    assert 1 <= len(text) <= 60, f"gate failed: {len(text)} chars"
    assert text.strip(), "gate failed: only whitespace"
    assert data == ENTRY.encode("utf-8"), "byte mismatch"
    print(f"entry: {ENTRY!r} ({len(ENTRY)} chars, {len(data)} bytes)")


if __name__ == "__main__":
    main()
