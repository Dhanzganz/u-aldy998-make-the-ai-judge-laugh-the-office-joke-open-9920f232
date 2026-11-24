"""Make the AI Judge Laugh: the Office Joke Open.

Writes a single original one-line office joke to /output/entry.txt.
Python 3.13, no network, deterministic.
"""

import os

ENTRY = "I told my boss this meeting could have been an email, so he scheduled a meeting to discuss my email about the meeting."


def main() -> None:
    # Gate check (competition.yaml): entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert ENTRY.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
