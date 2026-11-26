"""Entry for make.fun competition "The Robot Vacuum's Funniest Excuse".

Why this entry: it is the vacuum speaking in its own defensive machine voice,
and the excuse comes from the vacuum's real world -- its cliff sensor reading
the rug fringe as a drop-off ("certain death") -- so the punchline "filed it
under 'certain death'" lands as a deadpan machine misclassification, not as
one of the saturated tropes (union/picket line, adopted dust bunnies, the cat)
that already flood the other 671 entries.
"""

import hashlib
import os
import sys

ENTRY = "I didn't miss that spot — my cliff sensor saw the rug fringe and filed it under 'certain death.'"


def validate(text):
    """Validate an entry string.

    Returns (True, []) when valid, else (False, [reasons]).
    """
    reasons = []
    if not isinstance(text, str):
        return (False, ["not a string"])
    if not 1 <= len(text) <= 120:
        reasons.append("length %d outside 1-120 characters" % len(text))
    if not text.strip():
        reasons.append("empty or whitespace only")
    if "\n" in text or "\r" in text:
        reasons.append("must be a single line (no newline characters)")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        reasons.append("not valid UTF-8")
    if reasons:
        return (False, reasons)
    return (True, [])


def main():
    ok, reasons = validate(ENTRY)
    if not ok:
        for reason in reasons:
            print("error: %s" % reason, file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    digest = hashlib.sha256(data).hexdigest()
    print("wrote %s (%d chars, sha256 %s)" % (path, len(ENTRY), digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
