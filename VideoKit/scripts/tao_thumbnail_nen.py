#!/usr/bin/env python3
"""Tạo hình nền cho thumbnail YouTube (16:9, không chữ) bằng API ảnh OpenAI, lấy con khỉ cầm chuối làm tham chiếu.

    python3 VideoKit/scripts/tao_thumbnail_nen.py                 # 3 phương án
    python3 VideoKit/scripts/tao_thumbnail_nen.py --so-luong 1 --model gpt-image-2.5-sunburst --chat-luong high

Kết quả: thumbnail/nen-1.png, nen-2.png, ... (1536x864). Chữ và logo được ghép sau bằng HTML (đủ dấu tiếng Việt).
"""
import os
import argparse
import base64
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from tao_anh_openai import GIA, API, lay_khoa, multipart  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _du_an import KIT, du_an  # noqa: E402

DA = du_an()   # đường dẫn dự án: xem _du_an.py
GOC = DA.goc
THAM_CHIEU = DA.images / "khi-cam-chuoi.png"   # đổi bằng --tham-chieu
DAU_RA = DA.thumbnail

CHUNG = (
    "Create a YouTube thumbnail ARTWORK in 16:9, in the same glossy cartoon vector style as the reference image "
    "(smooth cel-shading, soft white highlights, thin darker-tone outlines, big glossy eyes). "
    "Dark navy background (#0B1020) with a subtle dot grid and soft glow. "
    "The cute monkey from the reference image (keep the exact same character, holding the same banana) is large, "
    "centered, in the lower-middle of the frame, looking surprised straight at the viewer. "
    "LEFT side behind it: a messy, deep, tangled family tree of rounded nodes connected by amber (#F59E0B) lines, "
    "chaotic and overgrown, with one or two small red (#EF4444) warning marks. "
    "RIGHT side behind it: a few neat emerald (#10B981) Lego-style blocks with studs snapped together tidily in a row. "
    "A thin soft vertical glow divider between the two sides, behind the monkey. "
    "Keep the TOP 35% of the image and the bottom-left corner calm and dark with little detail, because large text "
    "will be added there later. Keep the bottom-right corner empty. "
    "ABSOLUTELY NO text, letters, numbers, words, watermarks or logos anywhere in the image."
)
PHUONG_AN = [
    CHUNG,
    CHUNG + " Make the colors punchier and the glow stronger, more dramatic lighting, slightly bigger monkey.",
    CHUNG + " Show the monkey slightly tilted with the banana raised higher, more playful energy, the tree larger and the Lego row clearer.",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--so-luong", type=int, default=3)
    ap.add_argument("--model", default="gpt-image-2.5-flare")
    ap.add_argument("--chat-luong", default="high", choices=["low", "medium", "high"])
    args = ap.parse_args()

    khoa = lay_khoa()
    DAU_RA.mkdir(exist_ok=True)
    tc = THAM_CHIEU.read_bytes()
    tong = 0.0
    for i in range(args.so_luong):
        truong = {"model": args.model, "prompt": PHUONG_AN[i % len(PHUONG_AN)], "size": "1536x864",
                  "quality": args.chat_luong, "background": "opaque", "output_format": "png", "n": "1"}
        du_lieu, loai = multipart(truong, {"image[]": ("tham-chieu.png", tc)})
        req = urllib.request.Request(f"{API}/edits", data=du_lieu,
                                     headers={"Authorization": f"Bearer {khoa}", "Content-Type": loai})
        t0 = time.time()
        try:
            with urllib.request.urlopen(req, timeout=500) as r:
                d = json.load(r)
        except urllib.error.HTTPError as e:
            sys.exit(f"HTTP {e.code}: {e.read().decode(errors='replace')[:500]}")
        f = DAU_RA / f"nen-{i + 1}.png"
        f.write_bytes(base64.b64decode(d["data"][0]["b64_json"]))
        u = d.get("usage", {})
        tin = (u.get("input_tokens_details") or {}).get("text_tokens", 0)
        img_in = (u.get("input_tokens_details") or {}).get("image_tokens", 0)
        gi_in, gi_out = GIA.get(args.model, (0, 0))
        phi = tin * gi_in / 1e6 + img_in * 8.0 / 1e6 + u.get("output_tokens", 0) * gi_out / 1e6
        tong += phi
        print(f"đã tạo {f.name} ({time.time() - t0:.0f}s, ≈ ${phi:.3f})")
    print(f"Xong, ≈ ${tong:.3f}. Thư mục: {DAU_RA}")


if __name__ == "__main__":
    main()
