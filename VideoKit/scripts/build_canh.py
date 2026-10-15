#!/usr/bin/env python3
"""Ghép file nguồn của từng đoạn thành file composition HyperFrames (chỉ dùng thư viện chuẩn).

    cd videos/<du-an> && python3 ../../VideoKit/scripts/build_canh.py            # mọi file video/compositions/src/*.body.html
    python3 ../../VideoKit/scripts/build_canh.py c1-d3 c2-d1                      # chỉ các đoạn này

Mỗi `compositions/src/<id>.body.html` chứa phần thân (khối <style>, phần tử gốc `#root` có `data-composition-id="<id>"`, khối <script>)
và ba chỗ đánh dấu được thay: `/*VK_FONT*/` (khai báo @font-face của dự án), `/*VK_CSS*/` (VideoKit/components/*/*.css),
`/*VK_JS*/` (VideoKit/components/*/*.js, đặt trong <script> trước dòng tạo `tl`).
Kết quả: `compositions/frames/<id>.html` bọc trong <template> đúng chuẩn sub-composition. Không sửa file kết quả bằng tay; sửa file nguồn rồi chạy lại.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _du_an import KIT, du_an  # noqa: E402

DA = du_an()
SRC = DA.video / "compositions" / "src"
FRAMES = DA.video / "compositions" / "frames"
COMP = KIT / "components"   # mỗi thành phần một thư mục (core chạy trước, còn lại theo tên); luật dựng ở templates/dung-canh/


def ghep(nguon):
    font = (FRAMES / "_font-face.css").read_text(encoding="utf-8")
    thu = [COMP / "core"] + sorted(d for d in COMP.iterdir() if d.is_dir() and d.name != "core")
    css = "\n".join(f.read_text(encoding="utf-8") for d in thu for f in sorted(d.glob("*.css")))
    js = "\n".join(f.read_text(encoding="utf-8") for d in thu for f in sorted(d.glob("*.js")))
    s = nguon.read_text(encoding="utf-8")
    for k, v in (("/*VK_FONT*/", font), ("/*VK_CSS*/", css), ("/*VK_JS*/", js)):
        s = s.replace(k, v)
    cid = nguon.name[: -len(".body.html")]
    warp = nguon.with_name(f"{cid}.warp.json")
    if warp.exists():   # co giãn thời gian theo giọng đọc mới (xem vk.js: vkWarp, và storyboard/chuyen_nhip.py)
        pts = json.loads(warp.read_text(encoding="utf-8"))["pts"]
        goc = "const tl = gsap.timeline({ paused: true });"
        if goc not in s:
            sys.exit(f"{nguon.name}: không thấy dòng `{goc}` để gắn co giãn thời gian")
        s = s.replace(goc, f"const tl = vkWarp(gsap.timeline({{ paused: true }}), {json.dumps(pts)});", 1)
    m = re.search(r'data-composition-id="([^"]+)"', s)
    if not m or m.group(1) != cid:
        sys.exit(f"{nguon.name}: data-composition-id phải là \"{cid}\" (đang là {m.group(1) if m else 'thiếu'})")
    if "window.__timelines[" not in s or f'"{cid}"' not in s.split("window.__timelines[")[1][:60]:
        sys.exit(f"{nguon.name}: thiếu window.__timelines[\"{cid}\"] = tl;")
    out = f'<!doctype html>\n<html>\n  <head><meta charset="UTF-8" /></head>\n  <body>\n<template>\n{s}\n</template>\n  </body>\n</html>\n'
    (FRAMES / f"{cid}.html").write_text(out, encoding="utf-8")
    return len(out)


def main():
    chon = set(sys.argv[1:])
    ds = sorted(SRC.glob("*.body.html"))
    if chon:
        ds = [d for d in ds if d.name[: -len(".body.html")] in chon]
    if not ds:
        sys.exit(f"Không có file nguồn nào trong {SRC}")
    for d in ds:
        n = ghep(d)
        print(f"{d.name[:-len('.body.html')]}: {n} byte")


if __name__ == "__main__":
    main()
