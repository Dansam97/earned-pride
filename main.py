"""One Line of Earned Pride — make.fun entry.

Writes the entry text to entry.txt in the output directory.
The line: a grandmother who, after months of relearning to write
following her stroke, signs a birthday card entirely on her own.
"""

import os

TEXT = (
    "Four months of shaking practice, and this morning my grandmother "
    "signed the birthday card herself, all nine letters, steady, "
    "no hand holding hers."
)


MAX_CHARS = 240


def validated_text() -> str:
    """Return TEXT after checking it against the bounty's gate rules.

    The gate accepts UTF-8 text of 1 to 240 characters, on a single
    line, and not only white space. Fail loudly here rather than let
    an invalid entry reach the grader.
    """
    text = TEXT.strip()
    encoded = text.encode("utf-8")  # raises if not UTF-8 encodable
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, outside 1..{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text.encode("utf-8") != encoded:
        raise ValueError("entry changed under UTF-8 round-trip")
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    payload = (validated_text() + "\n").encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(payload)
    # Read back and prove the file on disk is byte-for-byte the payload.
    with open(path, "rb") as fh:
        if fh.read() != payload:
            raise IOError("entry.txt on disk differs from the intended bytes")


if __name__ == "__main__":
    main()
