#!/usr/bin/env python3
"""Cắt logo vuông thành PNG hình tròn, nền trong suốt, KHÔNG viền (mặc định). Cần: pillow.

    python VideoKit/scripts/logo_tron.py                         # tạo VideoKit/brand/logo-tron.png (512x512, không viền)
    python VideoKit/scripts/logo_tron.py --kich-thuoc 1024       # bản lớn hơn
    python VideoKit/scripts/logo_tron.py --vien 0.018 --mau-vien 255,255,255   # nếu muốn thêm viền
    python VideoKit/scripts/logo_tron.py khung-hinh.png ra.png   # thử ghép vào góc phải dưới của một khung hình

Nguồn: VideoKit/brand/logo.png. Mép tròn khử răng cưa (siêu lấy mẫu x4), phần ngoài hình tròn trong suốt hoàn toàn.
"""
import argparse
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _du_an import KIT  # noqa: E402

LOGO = KIT / "brand" / "logo.png"
RA = KIT / "brand" / "logo-tron.png"
SS = 4  # siêu lấy mẫu để mép tròn mượt


def logo_tron(kich_thuoc=512, tam=(0.54, 0.52), phan_cat=0.88, be_day_vien=0.0, mau_vien=(255, 255, 255)):
    """tam: tâm cắt (tỉ lệ so với ảnh gốc); phan_cat: cạnh vùng cắt / cạnh ảnh gốc; be_day_vien = 0 là không viền."""
    im = Image.open(LOGO).convert("RGB")
    w, h = im.size
    c = int(min(w, h) * phan_cat)
    cx, cy = int(w * tam[0]), int(h * tam[1])
    x0 = max(0, min(w - c, cx - c // 2))
    y0 = max(0, min(h - c, cy - c // 2))
    n = kich_thuoc * SS
    im = im.crop((x0, y0, x0 + c, y0 + c)).resize((n, n), Image.LANCZOS)
    mask = Image.new("L", (n, n), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, n - 1, n - 1), fill=255)
    out = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    out.paste(im, (0, 0), mask)
    if be_day_vien > 0:
        bd = int(n * be_day_vien)
        ImageDraw.Draw(out).ellipse((0, 0, n - 1, n - 1), outline=tuple(mau_vien) + (255,), width=bd)
    return out.resize((kich_thuoc, kich_thuoc), Image.LANCZOS)


def ghep_goc_phai_duoi(khung, logo, duong_kinh=132, le=44):
    nen = Image.open(khung).convert("RGBA")
    lg = logo.resize((duong_kinh, duong_kinh), Image.LANCZOS)
    nen.alpha_composite(lg, (nen.width - le - duong_kinh, nen.height - le - duong_kinh))
    return nen.convert("RGB")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Logo tròn nền trong suốt")
    ap.add_argument("khung", nargs="?", help="khung hình để ghép thử")
    ap.add_argument("ra", nargs="?", help="file ảnh ghép thử")
    ap.add_argument("--kich-thuoc", type=int, default=512)
    ap.add_argument("--vien", type=float, default=0.0, help="độ dày viền theo tỉ lệ đường kính; 0 = không viền")
    ap.add_argument("--mau-vien", default="255,255,255")
    a = ap.parse_args()
    lg = logo_tron(a.kich_thuoc, be_day_vien=a.vien, mau_vien=tuple(int(x) for x in a.mau_vien.split(",")))
    lg.save(RA)
    print("Đã lưu", RA, f"({a.kich_thuoc}x{a.kich_thuoc}, " + ("không viền" if a.vien == 0 else f"viền {a.vien}") + ")")
    if a.khung and a.ra:
        ghep_goc_phai_duoi(a.khung, lg).save(a.ra)
        print("Đã lưu", a.ra)
