#!/usr/bin/env python3
"""Rasterise a PDF and report how full each page is.

Fill = lowest non-background row inside the text area / text-area height.
Flags pages under --min (default 0.70). Cover (page 1) and pages listed in
--skip are exempt. No dependencies beyond poppler's pdftoppm.

usage: check_pages.py file.pdf [--top 0.7] [--bottom 0.75] [--skip 1,16] [--min 0.7]
"""
import argparse, glob, os, subprocess, sys, tempfile

DPI = 40


def read_pgm(path):
    with open(path, "rb") as f:
        data = f.read()
    parts, i = [], 0
    while len(parts) < 4:  # magic, width, height, maxval
        while data[i:i + 1].isspace():
            i += 1
        j = i
        while not data[j:j + 1].isspace():
            j += 1
        parts.append(data[i:j]); i = j
    i += 1
    w, h = int(parts[1]), int(parts[2])
    return w, h, data[i:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--top", type=float, default=0.7, help="top margin, inches")
    ap.add_argument("--bottom", type=float, default=0.75, help="bottom margin, inches")
    ap.add_argument("--skip", default="1")
    ap.add_argument("--min", type=float, default=0.70)
    a = ap.parse_args()
    skip = {int(x) for x in a.skip.split(",") if x}
    tmp = tempfile.mkdtemp()
    subprocess.run(["pdftoppm", "-gray", "-r", str(DPI), a.pdf, os.path.join(tmp, "p")], check=True)
    bad = []
    for n, path in enumerate(sorted(glob.glob(os.path.join(tmp, "p-*.pgm"))), 1):
        w, h, px = read_pgm(path)
        bg = px[w * int(h * 0.5) + 2]  # left margin pixel = page background
        top, bottom = int(a.top * DPI), h - int(a.bottom * DPI)
        last = top
        for y in range(top, bottom):
            row = px[y * w:(y + 1) * w]
            if any(abs(p - bg) > 24 for p in row[int(0.5 * DPI):w - int(0.5 * DPI)]):
                last = y
        fill = (last - top) / (bottom - top)
        flag = "" if n in skip or fill >= a.min else "  <-- UNDER-FILLED"
        if flag:
            bad.append(n)
        print(f"page {n:2d}: {fill:4.0%}{flag}")
    for f in glob.glob(os.path.join(tmp, "*")):
        os.remove(f)
    os.rmdir(tmp)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
