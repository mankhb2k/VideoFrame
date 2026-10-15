#!/usr/bin/env python3
"""Ghép nhiều ảnh PNG nền trong lên một nền màu thành tờ xem nhanh. Cần: pillow.

    python VideoKit/scripts/ghep_xem.py ra.png anh1.png anh2.png ...                 # nền trắng ngà (thương hiệu)
    python VideoKit/scripts/ghep_xem.py ra.png --nen "#121214" anh1.png anh2.png     # nền khác
    python VideoKit/scripts/ghep_xem.py ra.png --cot 5 --o 360 anh1.png ...          # số cột và cỡ ô
"""
import sys

from PIL import Image, ImageDraw

args = sys.argv[1:]
ra = args.pop(0)
nen, cot, o = "#F8F7F4", 0, 480
while args and args[0].startswith("--"):
    k = args.pop(0)
    v = args.pop(0)
    if k == "--nen":
        nen = v
    elif k == "--cot":
        cot = int(v)
    elif k == "--o":
        o = int(v)
vao = args
cot = cot or len(vao)
hang = -(-len(vao) // cot)
mau = tuple(int(nen.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
to = Image.new("RGB", (o * cot, (o + 30) * hang), mau)
d = ImageDraw.Draw(to)
chu = (17, 17, 19) if sum(mau) > 380 else (226, 232, 240)
for i, f in enumerate(vao):
    im = Image.open(f).convert("RGBA")
    nen_o = Image.new("RGBA", im.size, mau + (255,))
    nen_o.alpha_composite(im)
    x, y = (i % cot) * o, (i // cot) * (o + 30)
    to.paste(nen_o.convert("RGB").resize((o, o), Image.LANCZOS), (x, y + 30))
    d.text((x + 8, y + 8), "/".join(f.split("/")[-2:]), fill=chu)
to.save(ra)
