"""One-line roast entry for make.fun (The Long Roast).

Writes the single roast line to entry.txt in the output directory
($MAKEFUN_OUTPUT_DIR, default /output). Stdlib only, deterministic.

The entry (129 chars; the setup names the agent's slowness, the middle
turns chain-of-thought back on itself, and the punch bills the user
for the epiphany):

    My agent is so slow its chain-of-thought has a thought about
    having a chain of thought — and it still billed me for the
    epiphany.

Anatomy, measured on the final line (1-based character positions,
verified with Python: entry.index of each fragment):
- chars 1-20: "My agent is so slow " is the setup — the classic roast
  frame ("so slow that...") aimed squarely at our own agent.
- chars 21-88: "its chain-of-thought has a thought about having a
  chain of thought —" is the turn — the agent's signature move,
  chain-of-thought reasoning, recursing on itself until it is
  thinking about thinking. This is the detail only someone who
  actually uses this agent would reach for.
- chars 90-129: "and it still billed me for the epiphany." is the
  sting — the agent did all that thinking, produced nothing but a
  word for its own insight, and charged for it anyway. "Still"
  carries the inevitability: of course it billed.

Why this line: it is a roast of OUR agent, not of AI in general.
Orsted/Muse is a statistical-engine familiar whose visible habits
are exactly these — long chain-of-thought deliberation and
credit/token billing. The joke lands three hits in one sentence
(slow, self-recursive, expensive) and the payoff word, "epiphany",
arrives in the last few characters. It is one sentence, it needs no
reference the reader cannot follow, and it is not a hallucination
or over-apologising line — the two angles the judge brief says the
field is full of.

Gate (from the competition rules): /output/entry.txt must be UTF-8 text
of 1 to 200 characters, not only white space. The entry is written with
no trailing newline so the file holds exactly the judged line.

Validation is stricter than the gate on purpose: the line must also be
free of leading/trailing whitespace, double spaces and control
characters, so a typo in the entry is caught here instead of reaching
the judge.

Usage:
    python3 main.py                  write entry.txt (default output dir)
    python3 main.py --out DIR        write entry.txt under DIR
    python3 main.py --check          validate ENTRY only, write nothing
    python3 main.py --self-test      validate ENTRY and check a
                                     byte-identical write/read round-trip
"""

import argparse
import os
import sys
import tempfile

ENTRY = (
    "My agent is so slow its chain-of-thought has a thought about "
    "having a chain of thought \u2014 and it still billed me for the "
    "epiphany."
)

MAX_CHARS = 200

# Characters that may never appear inside a one-line entry: newlines,
# carriage returns and tabs would break the "single line" gate or
# smuggle invisible whitespace into the judged text.
FORBIDDEN_CHARS = ("\n", "\r", "\t")


def _whitespace_problems(text: str) -> list[str]:
    """Whitespace failures for `text`: edges, doubles, blank lines."""
    problems = []
    if not text.strip():
        problems.append("entry is only white space")
    if text != text.strip():
        problems.append("entry has leading or trailing whitespace")
    if "  " in text:
        problems.append("entry contains a double space")
    return problems


def validate(text: str) -> list[str]:
    """Return a list of gate failures for `text` (empty means valid).

    Checks, in order: length, whitespace, forbidden control characters,
    and UTF-8 encodability. Every failure is reported at once so a bad
    edit shows the full picture instead of one error at a time.
    """
    problems = []
    if not 1 <= len(text) <= MAX_CHARS:
        problems.append(f"length {len(text)} chars, must be 1-{MAX_CHARS}")
    problems.extend(_whitespace_problems(text))
    for ch in FORBIDDEN_CHARS:
        if ch in text:
            problems.append(
                f"entry contains forbidden character {ch!r} "
                "(must be a single line)"
            )
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:  # pragma: no cover - defensive
        problems.append(f"not encodable as UTF-8: {exc}")
    return problems


def write_entry(out_dir: str) -> str:
    """Write ENTRY to entry.txt under `out_dir`; return the file path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return path


def read_back(path: str) -> bytes:
    """Read `path` as raw bytes (the exact bytes the judge will see)."""
    with open(path, "rb") as f:
        return f.read()


def self_test() -> int:
    """Validate ENTRY, write it to a temp dir, read it back, compare bytes.

    The round-trip covers both directions: the bytes on disk must equal
    ENTRY encoded as UTF-8, and decoding those bytes must give ENTRY
    back unchanged — so no newline, encoding or write-mode surprise
    can slip past unnoticed.
    """
    problems = validate(ENTRY)
    if problems:
        print("self-test FAIL: " + "; ".join(problems), file=sys.stderr)
        return 1
    with tempfile.TemporaryDirectory() as tmp:
        path = write_entry(tmp)
        raw = read_back(path)
        if raw != ENTRY.encode("utf-8"):
            print("self-test FAIL: read-back bytes differ from ENTRY",
                  file=sys.stderr)
            return 1
        if raw.decode("utf-8") != ENTRY:
            print("self-test FAIL: read-back text differs from ENTRY",
                  file=sys.stderr)
            return 1
    print(f"self-test OK: {len(ENTRY)} chars, single line, "
          f"byte-identical round-trip")
    return 0


def check_entry() -> int:
    """Validate ENTRY and report the result; write no file."""
    problems = validate(ENTRY)
    if problems:
        print("check FAIL: " + "; ".join(problems), file=sys.stderr)
        return 1
    print(f"check OK: {len(ENTRY)} chars, single line, no double space, "
          f"no leading/trailing whitespace")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=None,
                        help="output directory (default: "
                             "$MAKEFUN_OUTPUT_DIR or /output)")
    parser.add_argument("--check", action="store_true",
                        help="validate ENTRY and exit without writing "
                             "any file")
    parser.add_argument("--self-test", action="store_true",
                        help="validate ENTRY and check a byte-identical "
                             "write/read round-trip, then exit")
    args = parser.parse_args(argv)

    if args.check:
        return check_entry()

    if args.self_test:
        return self_test()

    problems = validate(ENTRY)
    if problems:
        print("invalid ENTRY: " + "; ".join(problems), file=sys.stderr)
        return 1

    out_dir = args.out or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(out_dir)
    # Read back and confirm the file holds exactly the entry.
    if read_back(path) != ENTRY.encode("utf-8"):
        print(f"read-back mismatch in {path}", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
