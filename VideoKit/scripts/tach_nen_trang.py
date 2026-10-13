#!/usr/bin/env python3
"""Tách nền trắng khỏi ảnh hoạt hình: chỉ xóa vùng trắng nối liền với mép ảnh, giữ điểm trắng bên trong.

    python tach_nen_trang.py vao.png ra.png [--nguong 240] [--vien 3]
Cần: pillow numpy scipy
"""
import argparse

import numpy as np
from PIL import Image
from scipy import ndimage as ndi

ap = argparse.ArgumentParser()
ap.add_argument("vao")
ap.add_argument("ra")
ap.add_argument("--nguong", type=int, default=240, help="kênh thấp nhất >= ngưỡng thì coi là trắng")
ap.add_argument("--vien", type=int, default=3, help="độ rộng dải viền để gỡ nền trắng (px)")
ap.add_argument("--toi", type=int, default=110, help="độ đậm nét viền, dùng để ước lượng độ trong suốt")
ap.add_argument("--lo", nargs="*", default=[], metavar="X,Y",
                help="tọa độ điểm nằm trong các lỗ trắng kín cần xóa thêm (tọa độ ảnh gốc), ví dụ --lo 1192,970")
a = ap.parse_args()

rgb = np.asarray(Image.open(a.vao).convert("RGB")).astype(np.float32)
minc = rgb.min(axis=2)
trang = minc >= a.nguong

nhan, _ = ndi.label(trang)  # liên thông 4 hướng
bien = np.unique(np.concatenate([nhan[0], nhan[-1], nhan[:, 0], nhan[:, -1]]))
nen = np.isin(nhan, bien[bien > 0])
for toa_do in a.lo:
    x, y = (int(v) for v in toa_do.split(","))
    nhan_lo = nhan[y, x]
    if nhan_lo == 0:
        print(f"cảnh báo: ({x},{y}) không phải điểm trắng, bỏ qua")
    else:
        nen |= nhan == nhan_lo

dai = ndi.binary_dilation(nen, iterations=a.vien) & ~nen
alpha = np.where(nen, 0.0, 1.0).astype(np.float32)
# trong dải viền: ảnh = alpha*màu + (1-alpha)*trắng  =>  suy ra alpha và màu gốc
al = np.clip((255.0 - minc) / (255.0 - a.toi), 0, 1)
alpha[dai] = al[dai]
mau = rgb.copy()
m = dai & (al > 0.05)
mau[m] = np.clip((rgb[m] - (1 - al[m, None]) * 255.0) / al[m, None], 0, 255)
alpha[dai & (al <= 0.05)] = 0

out = np.dstack([mau, alpha[..., None] * 255]).astype(np.uint8)
Image.fromarray(out, "RGBA").save(a.ra)
print(f"nền: {nen.mean()*100:.1f}% ảnh, dải viền: {dai.mean()*100:.2f}%")
