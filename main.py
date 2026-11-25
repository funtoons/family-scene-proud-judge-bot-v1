"""Family scene entry for make.fun bounty
u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2.

Writes one short family scene (one line, 126 characters) to
/output/entry.txt. Deterministic, offline, standard library only:
no randomness, no network, no clock, no file-system-dependent output.
"""

import os

ENTRY = (
    "Every night Dad reads the twins a story to put them to sleep. "
    "Tonight the twins read him one \u2014 he was snoring before page two."
)


def main():
    # Self-check against the bounty gate: 1-280 characters, not blank.
    if not 1 <= len(ENTRY) <= 280 or not ENTRY.strip():
        raise SystemExit("entry fails the 1-280 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
