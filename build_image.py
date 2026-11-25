#!/usr/bin/env python3
"""Draw the 1024x1024 news front page for make.fun news-image-20261124.
Deterministic, stdlib + Pillow only, no network. Run: python3 build_image.py
Output: entry.png next to this script's target dir (passed as argv[1] or default)."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("entry.png")

PAPER = (248, 244, 232)
INK = (20, 20, 20)
MUTED = (90, 86, 76)
RED = (179, 39, 30)
SEA = (30, 78, 121)
SEA_DARK = (22, 58, 90)
SKY = (214, 231, 242)
RULE = (20, 20, 20)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS_I = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
M = 36  # margin
CW = W - 2 * M  # 952

# ---- Masthead ----
f_mast = font(SERIF_B, 56)
title = "THE WORLD IN ONE DAY"
tw = d.textlength(title, font=f_mast)
d.text(((W - tw) / 2, 22), title, font=f_mast, fill=INK)

f_date = font(SANS_B, 19)
dateline = "TUESDAY, 24 NOVEMBER 2026  ·  WORLD NEWS IN ONE IMAGE"
tw = d.textlength(dateline, font=f_date)
d.text(((W - tw) / 2, 96), dateline, font=f_date, fill=RED)

d.rectangle([M, 128, W - M, 132], fill=RULE)
d.rectangle([M, 136, W - M, 137], fill=RULE)

# ---- Lead illustration: tanker on fire in the strait ----
ix0, iy0, ix1, iy1 = M, 148, W - M, 318
d.rectangle([ix0, iy0, ix1, iy1], outline=INK, width=2)
d.rectangle([ix0 + 2, iy0 + 2, ix1 - 2, iy0 + 102], fill=SKY)          # sky
d.rectangle([ix0 + 2, iy0 + 102, ix1 - 2, iy1 - 2], fill=SEA)          # sea
# sun
d.ellipse([ix0 + 40, iy0 + 18, ix0 + 88, iy0 + 66], fill=(240, 196, 90))
# distant coastline
d.polygon([(ix0 + 2, iy0 + 102), (ix0 + 260, iy0 + 78), (ix0 + 520, iy0 + 96),
           (ix0 + 700, iy0 + 82), (ix1 - 2, iy0 + 100), (ix1 - 2, iy0 + 102)],
          fill=(158, 178, 190))
# waves (drawn before the tanker so they sit behind the hull)
for wy in (iy0 + 132, iy0 + 152):
    for wx in range(ix0 + 10, ix1 - 10, 46):
        d.arc([wx, wy, wx + 34, wy + 14], 180, 360, fill=(235, 240, 245), width=2)
# tanker hull
hx0, hy0 = ix0 + 220, iy0 + 118
d.polygon([(hx0, hy0), (hx0 + 480, hy0), (hx0 + 520, hy0 + 22),
           (hx0 + 500, hy0 + 34), (hx0, hy0 + 34)], fill=(26, 26, 26))
d.rectangle([hx0, hy0 + 30, hx0 + 500, hy0 + 34], fill=RED)  # waterline stripe
# containers
for i, col in enumerate([(196, 84, 48), (46, 110, 64), (196, 84, 48), (58, 92, 140)]):
    cx = hx0 + 30 + i * 78
    d.rectangle([cx, hy0 - 34, cx + 70, hy0 - 2], fill=col, outline=(20, 20, 20), width=1)
# bridge tower
d.rectangle([hx0 + 380, hy0 - 66, hx0 + 430, hy0 - 2], fill=(235, 232, 222),
            outline=(20, 20, 20), width=1)
d.rectangle([hx0 + 386, hy0 - 60, hx0 + 424, hy0 - 48], fill=(58, 92, 140))
# funnel with smoke + flame
d.rectangle([hx0 + 330, hy0 - 52, hx0 + 356, hy0 - 2], fill=(179, 39, 30))
# flame
d.polygon([(hx0 + 336, hy0 - 52), (hx0 + 350, hy0 - 78), (hx0 + 364, hy0 - 52)],
          fill=(240, 140, 40))
d.polygon([(hx0 + 342, hy0 - 52), (hx0 + 350, hy0 - 68), (hx0 + 358, hy0 - 52)],
          fill=(250, 210, 90))
# smoke plume (kept inside the frame)
for (sx, sy, r) in [(hx0 + 343, hy0 - 64, 12), (hx0 + 354, hy0 - 80, 15),
                    (hx0 + 372, hy0 - 92, 18), (hx0 + 396, hy0 - 98, 16),
                    (hx0 + 420, hy0 - 94, 13)]:
    d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(96, 96, 96))
    d.ellipse([sx - r + 5, sy - r + 5, sx + r - 5, sy + r - 5], fill=(120, 120, 120))
# waves
for wy in ():
    pass
# caption
f_cap = font(SANS_I, 17)
cap = "Illustration: oil tankers burn after reported mine strikes in the Strait of Hormuz."
d.text((M, 324), cap, font=f_cap, fill=MUTED)

# ---- Lead headline + summary ----
f_lead = font(SERIF_B, 42)
d.text((M, 350), "Tankers ablaze in the Strait of Hormuz", font=f_lead, fill=INK)
f_body = font(SANS, 21)
lead = ("Iran says three oil tankers struck naval mines and caught fire in the strategic "
        "waterway; the claims are unverified. Maritime authorities keep the threat level "
        "at \u201csevere\u201d.")
y = draw_lines(d, wrap(d, lead, f_body, CW), M, 402, f_body, INK, 27)

d.rectangle([M, 462, W - M, 463], fill=RULE)

# ---- Story grid: 2 cols x 3 rows ----
stories = [
    ("TECH", "Huang returns as Nvidia CEO",
     "Board reinstates Jensen Huang after a White House push; shares jump about 30%. Democrats demand an inquiry."),
    ("UKRAINE", "Ukraine sinks Russian warship off Libya",
     "Naval drones hit a Russian warship at a Libyan base. An overnight Russian strike on Zaporizhzhia kills 2 and wounds about 40."),
    ("GAZA", "Israeli strikes kill Hamas security chief",
     "Naeem Abu Nahel is killed in Gaza; earlier strikes kill a UN aid worker and two others."),
    ("LAW & TECH", "States sue SpaceX over Grok images",
     "Oregon and Virginia allege the AI tool generated child sexual abuse images."),
    ("CLIMATE", "COP31 collapses without a deal",
     "Climate talks end with no agreement on fossil fuels as a divided world stalls."),
    ("WASHINGTON", "Rep. Jimmy Gomez resigns",
     "The California Democrat steps down on Dec. 1 after an ethics panel finds evidence of misconduct."),
]
f_kick = font(SANS_B, 16)
f_head = font(SERIF_B, 25)
f_txt = font(SANS, 19)
gap_x, gap_y = 20, 12
col_w = (CW - gap_x) // 2
row_h = 156
grid_y = 476
for i, (kick, head, body) in enumerate(stories):
    cx = M + (i % 2) * (col_w + gap_x)
    cy = grid_y + (i // 2) * (row_h + gap_y)
    d.text((cx, cy), kick, font=f_kick, fill=RED)
    hl = wrap(d, head, f_head, col_w)
    yy = draw_lines(d, hl, cx, cy + 22, f_head, INK, 30)
    bl = wrap(d, body, f_txt, col_w)
    draw_lines(d, bl[:3], cx, yy + 4, f_txt, (60, 58, 52), 24)
    if i % 2 == 0:
        d.line([cx + col_w + gap_x // 2, cy + 4, cx + col_w + gap_x // 2,
                cy + row_h - 6], fill=(200, 194, 178), width=1)

# ---- Also today + sources footer ----
fy = grid_y + 3 * row_h + 2 * gap_y + 4  # 476+468+24+4 = 972
d.rectangle([M, fy - 8, W - M, fy - 7], fill=RULE)
f_also = font(SANS_B, 16)
also = ("ALSO TODAY:  UK to host the 2035 Women\u2019s World Cup  ·  Super Bowl LXI heads to "
        "IMAX")
draw_lines(d, wrap(d, also, f_also, CW), M, fy, f_also, INK, 22)
f_src = font(SANS, 15)
src = "Sources: Reuters \u00b7 AP \u00b7 BBC \u00b7 The New York Times \u00b7 Just Security  —  all stories reported 24 Nov 2026"
d.text((M, fy + 26), src, font=f_src, fill=MUTED)

img.save(OUT, "PNG", optimize=True)
print("saved", OUT, img.size, OUT.stat().st_size, "bytes")
