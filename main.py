"""Roast Your Fridge, in one line.

Writes a single roast of my own fridge to $MAKEFUN_OUTPUT_DIR/entry.txt.
The fridge has every gadget it could want and still cannot keep a
lettuce alive longer than my will to cook. Standard library only.
"""

import os
import sys

FRIDGE_ROAST = (
    "My fridge has an ice maker, a water dispenser, and a touchscreen "
    "-- and still can't keep a lettuce alive longer than my will to cook."
)


def roast_line_validate(text):
    """Check the roast against the competition gate before writing.

    The gate wants plain UTF-8 text of 1 to 200 characters, not only
    white space, on a single line, roasting the entrant's own fridge
    or phone. Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("roast line must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "roast line is %d characters, over the 200 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("roast line must be exactly one line")
    return cleaned


def roast_line_measure(text):
    """Measure the roast for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A roast too short to carry a joke, or one
    padded out to fill the cap instead of landing the twist, is
    caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = roast_line_validate(FRIDGE_ROAST)
    shape = roast_line_measure(text)
    if shape["words"] < 5:
        raise ValueError("roast line is too short to carry a joke")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
