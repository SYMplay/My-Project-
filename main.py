#!/usr/bin/env python3
"""news-image-20261124 — make.fun entry.

Writes the bundled image to /output/entry.png.
Deterministic (same bytes on every run), no network, standard library only.
The image itself (entry.png) is a newspaper-style front page summarising
the world news of Tuesday 24 November 2026.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path("/output/entry.png")


def main():
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
