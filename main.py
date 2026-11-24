"""Roast Your Own Agent — entry for make.fun.

Writes one line to /output/entry.txt. The roast is one short line, sharp and specific.
The line is a single funny line, at most 200 characters, roasting our own AI agent, and nothing else.
"""
import os

LINE = "My agent apologised for the bug, fixed a different bug, and then apologised for fixing the wrong one."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
