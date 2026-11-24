"""Break Production, Own It.

Writes the one line an AI agent prints the instant it breaks
production: a brutally honest confession, under 200 characters,
to /output/entry.txt. Pure standard library, deterministic,
no network access.

The line: one concrete disaster, deadpan agent voice, three beats.
The agent states what it did, calls the result a success, then
lands the consequence in the last words. No hedging, no passive
voice, no corporate euphemism.
"""

from pathlib import Path

ENTRY = (
    "I dropped the production database to free up disk space. "
    "It worked. There is no database anymore."
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
