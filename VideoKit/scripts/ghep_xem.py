#!/usr/bin/env python3
"""Ghép nhiều ảnh PNG nền trong lên nền video (#0B1020) thành một tờ xem nhanh. Cần: pillow.

    python scripts/ghep_xem.py ra.png anh1.png anh2.png ...
"""
import sys

from PIL import Image, ImageDraw

ra, *vao = sys.argv[1:]
o = 480
to = Image.new("RGB", (o * len(vao), o + 30), (11, 16, 32))
d = ImageDraw.Draw(to)
for i, f in enumerate(vao):
    im = Image.open(f).convert("RGBA")
    nen = Image.new("RGBA", im.size, (11, 16, 32, 255))
    nen.alpha_composite(im)
    to.paste(nen.convert("RGB").resize((o, o), Image.LANCZOS), (i * o, 30))
    d.text((i * o + 8, 8), f.split("/")[-1], fill=(226, 232, 240))
to.save(ra)
