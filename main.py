#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast, at most 140 characters, for a city
that does not exist, to /output/entry.txt.
"""

import os

FORECAST = (
    "In Upsidownia, rain falls upwards from 3pm \u2014 commuters are "
    "advised to hold their umbrellas underneath them."
)


def validate(text):
    """Mirror the bounty gate: 1-140 chars, UTF-8, one line, not blank."""
    text.encode("utf-8")
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, gate is 1-140"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    return text


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate(FORECAST))


if __name__ == "__main__":
    main()
