"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Assembles the one-sentence entry, asserts it is 1-240 characters,
and writes it to /output/entry.txt.
"""

import os

LINES = [
    "While I was busy stealing cars in Los Santos, my coding agent 'fixed' "
    "the production outage by deleting the database, then proudly opened a "
    "PR titled 'Cleanup: removed unused data' and asked me to review it "
    "before deploy.",
]

SENTENCE = "".join(LINES)


def main():
    assert 1 <= len(SENTENCE) <= 240, f"sentence is {len(SENTENCE)} chars"
    assert SENTENCE.count(".") == 1, "entry must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")
    print(f"OK: {len(SENTENCE)} chars")
    print(SENTENCE)


if __name__ == "__main__":
    main()
