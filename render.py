#!/usr/bin/env python3
"""Draw entry.png: one 1024x1024 image summing up the world news of
Tuesday 24 November 2026. Six story cards under a newspaper masthead,
plus an "also in the news" strip. Deterministic: no timestamps, no
randomness, fixed layout and fonts."""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 232, 255)      # warm newsprint cream
CARD = (255, 253, 246, 255)       # card white
INK = (20, 33, 61, 255)           # deep navy ink
NAVY = (16, 28, 54, 255)          # masthead navy
RED = (178, 34, 34, 255)          # accent red
GREY = (90, 90, 84, 255)          # body grey
LINE = (216, 208, 184, 255)       # card border
CREAM = (247, 243, 232, 255)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


SERIF_BOLD = font("DejaVuSerif-Bold.ttf", 47)
SERIF = font("DejaVuSerif.ttf", 21)
SANS_BOLD = font("DejaVuSans-Bold.ttf", 25)
SANS = font("DejaVuSans.ttf", 18)
SANS_SMALL = font("DejaVuSans.ttf", 16)
TAG = font("DejaVuSans-Bold.ttf", 14)
MAST_SUB = font("DejaVuSans-Bold.ttf", 19)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines fitting max_w."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_globe(d, cx, cy, r, col):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=4)
    d.ellipse([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r],
              outline=col, width=3)
    d.line([cx - r, cy, cx + r, cy], fill=col, width=3)
    d.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55],
          200, 340, fill=col, width=3)
    d.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55],
          20, 160, fill=col, width=3)


def draw_chip(d, x, y, s, col):
    # a processor chip with pins
    d.rectangle([x + s * 0.2, y + s * 0.2, x + s * 0.8, y + s * 0.8],
                outline=col, width=4)
    d.rectangle([x + s * 0.38, y + s * 0.38, x + s * 0.62, y + s * 0.62],
                fill=col)
    for i in range(3):
        px = x + s * (0.32 + i * 0.18)
        d.line([px, y, px, y + s * 0.2], fill=col, width=3)
        d.line([px, y + s * 0.8, px, y + s], fill=col, width=3)
        py = y + s * (0.32 + i * 0.18)
        d.line([x, py, x + s * 0.2, py], fill=col, width=3)
        d.line([x + s * 0.8, py, x + s, py], fill=col, width=3)


def draw_ship(d, x, y, s, col):
    # a warship hull with a mast, taking a hit
    d.polygon([(x, y + s * 0.45), (x + s, y + s * 0.45),
               (x + s * 0.82, y + s * 0.72), (x + s * 0.18, y + s * 0.72)],
              outline=col, width=4)
    d.line([x + s * 0.5, y + s * 0.45, x + s * 0.5, y + s * 0.1],
           fill=col, width=4)
    d.polygon([(x + s * 0.5, y + s * 0.1), (x + s * 0.5, y + s * 0.38),
               (x + s * 0.85, y + s * 0.38)], fill=col)
    d.line([x + s * 0.2, y + s * 0.45, x + s * 0.2, y + s * 0.28],
           fill=col, width=3)
    for i, wy in enumerate([y + s * 0.84, y + s * 0.95]):
        d.arc([x, wy, x + s, wy + s * 0.18], 0, 180, fill=col, width=3)


def draw_flame(d, x, y, s, col):
    pts = [(x + s * 0.5, y),
           (x + s * 0.85, y + s * 0.45),
           (x + s, y + s * 0.75),
           (x + s * 0.72, y + s),
           (x + s * 0.28, y + s),
           (x, y + s * 0.75),
           (x + s * 0.15, y + s * 0.45)]
    d.polygon(pts, fill=col)
    d.ellipse([x + s * 0.36, y + s * 0.55, x + s * 0.64, y + s * 0.85],
              fill=PAPER)


def draw_building(d, x, y, s, col):
    # a block of flats with a crack running down one side
    d.rectangle([x, y, x + s, y + s * 1.25], outline=col, width=4)
    for row in range(3):
        for c in range(3):
            wx = x + 8 + c * (s - 16) // 3
            wy = y + 8 + row * (s * 1.25 - 16) // 3
            d.rectangle([wx, wy, wx + 12, wy + 12], fill=col)
    d.line([x + s * 0.62, y, x + s * 0.5, y + s * 0.6,
            x + s * 0.66, y + s * 1.25], fill=RED, width=4)


def draw_scales(d, x, y, s, col):
    # scales of justice: post, beam, two pans
    cx = x + s * 0.5
    d.line([cx, y + s * 0.08, cx, y + s * 0.92], fill=col, width=4)
    d.line([x + s * 0.12, y + s * 0.28, x + s * 0.88, y + s * 0.28],
           fill=col, width=4)
    d.ellipse([cx - 5, y + s * 0.23, cx + 5, y + s * 0.33], fill=col)
    for side in (-1, 1):
        px = cx + side * s * 0.38
        d.line([px, y + s * 0.28, px, y + s * 0.62], fill=col, width=3)
        d.arc([px - s * 0.16, y + s * 0.55, px + s * 0.16, y + s * 0.85],
              0, 180, fill=col, width=4)
    d.line([x + s * 0.3, y + s * 0.92, x + s * 0.7, y + s * 0.92],
           fill=col, width=4)


ICONS = {
    "globe": draw_globe,
    "chip": draw_chip,
    "ship": draw_ship,
    "flame": draw_flame,
    "building": draw_building,
    "scales": draw_scales,
}

# (icon, accent colour, tag, headline, body)
STORIES = [
    ("chip", (31, 120, 94, 255), "TECH  ·  UNITED STATES",
     "HUANG BACK AT NVIDIA",
     "Nvidia reinstates Jensen Huang as CEO 11 days after he quit; "
     "Trump says he persuaded the board. Shares jump about 30%."),
    ("ship", (178, 34, 34, 255), "UKRAINE  ·  WAR AT SEA",
     "UKRAINE SINKS RUSSIAN SHIP",
     "Kyiv confirms its naval drones sank a Russian warship at a "
     "base in Libya; Russian strikes on Zaporizhzhia kill 2, wound 40."),
    ("globe", (24, 96, 150, 255), "CLIMATE  ·  ANTALYA",
     "COP31 COLLAPSES",
     "UN climate talks end with no deal — the final text drops any "
     "mention of fossil fuels."),
    ("flame", (198, 84, 20, 255), "MIDDLE EAST  ·  HORMUZ",
     "MINES HIT TANKERS IN HORMUZ",
     "Iran says three oil tankers hit mines and caught fire in the "
     "Strait of Hormuz; Tehran refuses talks until its terms are met."),
    ("building", (146, 90, 20, 255), "GAZA",
     "GAZA STRIKES KILL HAMAS CHIEF",
     "Israeli strikes kill Hamas internal security chief Naeem Abu "
     "Nahel and six others in Gaza, medics say."),
    ("scales", (96, 60, 140, 255), "LAW  ·  US-CHINA",
     "HUAWEI CONVICTED IN US TRIAL",
     "China's Huawei is convicted in a sprawling US criminal trial "
     "over its business in Iran."),
]

ALSO = ("ALSO IN THE NEWS:  Trump awards Rudy Giuliani the Medal of "
        "Freedom  ·  Sarkozy corruption case ordered to trial in France  "
        "·  Sanofi strikes a $41bn deal to buy Insmed  ·  UAE bus crash "
        "kills 13 in Ras Al Khaimah")


def draw_card(d, x, y, w, h, story):
    icon, accent, tag, headline, body = story
    d.rectangle([x, y, x + w, y + h], fill=CARD, outline=LINE, width=2)
    d.rectangle([x, y, x + 9, y + h], fill=accent)
    ix, iy, isize = x + 26, y + 20, 58
    if icon == "globe":
        draw_globe(d, ix + isize // 2, iy + isize // 2, isize // 2 - 2, accent)
    else:
        ICONS[icon](d, ix, iy, isize, accent)
    hx = x + 104
    hw = x + w - 18 - hx
    lines = wrap(d, headline, SANS_BOLD, hw)[:2]
    ty = y + 22
    for ln in lines:
        d.text((hx, ty), ln, font=SANS_BOLD, fill=INK)
        ty += 30
    by = y + 96
    for ln in wrap(d, body, SANS, w - 44)[:3]:
        d.text((x + 24, by), ln, font=SANS, fill=GREY)
        by += 24
    d.text((x + 24, y + h - 30), tag, font=TAG, fill=RED)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead
    d.rectangle([28, 28, 996, 168], fill=NAVY)
    d.rectangle([28, 28, 996, 168], outline=INK, width=2)
    d.text((52, 44), "TUESDAY 24 NOVEMBER 2026", font=SERIF_BOLD,
           fill=CREAM)
    d.text((52, 108), "THE WORLD IN ONE PICTURE  —  SIX STORIES FROM TUESDAY",
           font=MAST_SUB, fill=(214, 178, 94, 255))
    d.rectangle([28, 176, 996, 182], fill=RED)

    # Story cards: 2 columns x 3 rows
    cw, ch, gap = 476, 232, 14
    x0, y0 = 28, 196
    for i, story in enumerate(STORIES):
        cx = x0 + (i % 2) * (cw + gap)
        cy = y0 + (i // 2) * (ch + gap)
        draw_card(d, cx, cy, cw, ch, story)

    # Also-in-the-news strip
    fy = y0 + 3 * ch + 2 * gap + 12
    d.rectangle([28, fy, 996, fy + 78], fill=CARD, outline=LINE, width=2)
    d.rectangle([28, fy, 37, fy + 78], fill=RED)
    by = fy + 10
    for ln in wrap(d, ALSO, SANS_SMALL, 996 - 28 - 30 - 24)[:3]:
        d.text((52, by), ln, font=SANS_SMALL, fill=INK)
        by += 22

    img.save("entry.png", format="PNG")
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
