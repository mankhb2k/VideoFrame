#!/usr/bin/env python3
"""Cắt logo vuông thành khung tròn (nền trong suốt, viền màu) và ghép thử vào một khung hình video. Cần: pillow.

    python VideoKit/scripts/logo_tron.py                      # chỉ tạo logo-tron.png
    python VideoKit/scripts/logo_tron.py khung-hinh.png ra.png  # tạo logo tròn + ghép vào góc phải dưới của khung hình
"""
import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

KIT = Path(__file__).resolve().parent.parent                       # thư mục VideoKit
GOC = Path(os.environ.get("VIDEOKIT_PROJECT") or Path.cwd())  # thư mục gốc dự án video (mặc định: nơi bạn đang đứng)
LOGO = KIT / "brand" / "logo.png"
RA = KIT / "brand" / "logo-tron.png"

VIEN = (255, 255, 255)  # viền trắng
SS = 4                  # siêu lấy mẫu để mép tròn mượt


def logo_tron(kich_thuoc=512, tam=(0.54, 0.52), phan_cat=0.88, be_day_vien=0.018):
    """tam: tâm cắt (tỉ lệ so với ảnh gốc); phan_cat: cạnh vùng cắt / cạnh ảnh gốc."""
    im = Image.open(LOGO).convert("RGB")
    w, h = im.size
    c = int(min(w, h) * phan_cat)
    cx, cy = int(w * tam[0]), int(h * tam[1])
    x0 = max(0, min(w - c, cx - c // 2))
    y0 = max(0, min(h - c, cy - c // 2))
    im = im.crop((x0, y0, x0 + c, y0 + c)).resize((kich_thuoc * SS, kich_thuoc * SS), Image.LANCZOS)
    n = kich_thuoc * SS
    mask = Image.new("L", (n, n), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, n - 1, n - 1), fill=255)
    out = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    out.paste(im, (0, 0), mask)
    d = ImageDraw.Draw(out)
    bd = int(n * be_day_vien)
    d.ellipse((0, 0, n - 1, n - 1), outline=VIEN + (255,), width=bd)
    return out.resize((kich_thuoc, kich_thuoc), Image.LANCZOS)


def ghep_goc_phai_duoi(khung, logo, duong_kinh=132, le=44):
    nen = Image.open(khung).convert("RGBA")
    lg = logo.resize((duong_kinh, duong_kinh), Image.LANCZOS)
    x, y = nen.width - le - duong_kinh, nen.height - le - duong_kinh
    bong = Image.new("RGBA", nen.size, (0, 0, 0, 0))
    bong.paste((0, 0, 0, 140), (x, y + 6), lg.split()[3])
    nen.alpha_composite(bong.filter(ImageFilter.GaussianBlur(9)))
    nen.alpha_composite(lg, (x, y))
    return nen.convert("RGB")


if __name__ == "__main__":
    lg = logo_tron()
    RA.parent.mkdir(parents=True, exist_ok=True)
    lg.save(RA)
    print("Đã lưu", RA)
    if len(sys.argv) >= 3:
        ghep_goc_phai_duoi(sys.argv[1], lg).save(sys.argv[2])
        print("Đã lưu", sys.argv[2])
