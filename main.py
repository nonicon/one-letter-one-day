#!/usr/bin/env python3
"""One Letter, One Day — make.fun entry for "One Letter for Your Day".

The entry is exactly one character: the letter M.
Behind it sits the word "mush" — the day turned to mush: soft, formless,
low-stakes, nothing quite holding its shape. The letter is the whole entry;
the word stays hidden, doing its work from behind the letter.
"""

import os

LETTER = "M"
HIDDEN_WORD = "mush"


def main() -> None:
    # The entry is exactly one character, A–Z, and nothing else:
    # no word, no gloss, no punctuation, not even a trailing newline.
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        raise ValueError("entry must be exactly one letter A-Z")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    print(LETTER)


if __name__ == "__main__":
    main()
