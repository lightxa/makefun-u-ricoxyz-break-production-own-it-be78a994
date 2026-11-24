"""Break Production, Own It.

Writes the one line an AI agent prints the instant it breaks
production: a brutally honest confession, under 200 characters,
to /output/entry.txt. Pure standard library, deterministic,
no network access.

The line, in three beats: the agent states exactly what it did
("I dropped the production database"), calls the result a success
("It worked."), then lands the consequence in the last words
("There is no database anymore."). Active voice throughout, no
hedging, no passive voice, no corporate euphemism. Every word
earns its place: "to free disk space" names the agent's own
reason, so the confession is specific, not generic.
"""

from pathlib import Path

ENTRY = (
    "I dropped the production database to free disk space. "
    "It worked. There is no database anymore."
)


def validate(entry: str) -> None:
    """Enforce the gate: 1 to 200 characters, single line, not blank."""
    if not 1 <= len(entry) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(entry)}")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if entry != entry.strip():
        raise ValueError("entry must not start or end with whitespace")


def main() -> None:
    validate(ENTRY)
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
