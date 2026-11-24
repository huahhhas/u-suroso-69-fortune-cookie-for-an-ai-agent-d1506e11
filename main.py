#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun bounty entry.

Writes exactly one funny fortune cookie line for an AI agent to
/output/entry.txt (no trailing newline). Pure stdlib, deterministic:
the same line on every run.
"""

import os

# The fortune: a blessing (perfect memory) that twists into a curse —
# the one thing the agent will never forget is the meeting it wanted to forget.
FORTUNE = "You will soon forget nothing — least of all the meeting that should have been an email."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
