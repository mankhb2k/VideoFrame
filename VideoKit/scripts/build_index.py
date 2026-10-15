#!/usr/bin/env python3
"""Sinh video/index.html và assets/audio/moc-canh.json từ du-an.json và độ dài giọng đọc thật (chỉ dùng thư viện chuẩn).

Đây là "khuôn" chung: khung hình, font, giọng đọc từng cảnh, track sfx, logo góc video đều do script này đặt,
nên mọi dự án ra cùng một chuẩn và đổi độ dài một cảnh chỉ cần chạy lại, không sửa tay.

    cd videos/<du-an> && python3 ../../VideoKit/scripts/build_index.py
    python3 VideoKit/scripts/build_index.py --khong-stub     # không tạo file cảnh tạm cho cảnh chưa có

Độ dài cảnh = độ dài file giọng + 2 x độ trễ (đầu và cuối) + `giu_them_giay` của cảnh. Cảnh chưa có file giọng dùng `du_kien_giay`
(chỉ để xem trước khung; moc-canh.json ghi `uoc_tinh: true`). Cảnh chưa có file HTML sẽ được tạo file cảnh tạm.
Nếu cảnh có `doan` (danh sách đoạn: id, bat_dau tính từ đầu cảnh, thoi_luong) thì mỗi đoạn là một sub-composition riêng
`compositions/frames/<id>.html` (đặt lên timeline tại start cảnh + bat_dau); cảnh không có `doan` dùng một file cho cả cảnh.
Logo được ghi thành sub-composition `compositions/logo.html` (HyperFrames không cho thẻ lồng nhau trong index.html).
Dừng `hyperframes preview` trước khi chạy: Studio tự sửa file HTML đang mở.
"""
import argparse
import json
import sys
import wave
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _du_an import KIT, du_an  # noqa: E402
from _thuong_hieu import doc_css, lay_bien  # noqa: E402

DA = du_an()


def thoi_luong_wav(p):
    with wave.open(str(p), "rb") as w:
        return w.getnframes() / w.getframerate()


def tinh_moc(cfg):
    do_tre = float(cfg.get("giong", {}).get("do_tre_giay", 0.3))
    hang, t = [], 0.0
    for i, c in enumerate(cfg["canh"], 1):
        wav = DA.audio / f"{c['tep_loi_thoai']}.wav"
        co_giong = wav.exists()
        L = thoi_luong_wav(wav) if co_giong else float(c.get("du_kien_giay", 30))
        dur = round(L + 2 * do_tre + float(c.get("giu_them_giay", 0)), 1)
        ten_file = c.get("tep_composition") or f"{i:02d}-{c['id']}"
        dd = []
        for j, d in enumerate(c.get("doan", [])):
            bd = float(d["bat_dau"])
            tl_ = (float(c["doan"][j + 1]["bat_dau"]) if j + 1 < len(c["doan"]) else dur) - bd
            dd.append({"id": d["id"], "ten": d.get("ten", ""), "start": round(t + bd, 2), "duration": round(tl_, 2),
                       "composition": f"compositions/frames/{d['id']}.html"})
        hang.append({"canh": c["tep_loi_thoai"], "id": c["id"], "stt": i, "audio": round(L, 2), "start": round(t, 1),
                     "duration": dur, "uoc_tinh": not co_giong, "composition": f"compositions/frames/{ten_file}.html", "doan": dd})
        t = round(t + dur, 1)
    return hang, t, do_tre


def stub(i, W, H, nen, chu, cid=None, nhan=None):
    cid = cid or f"scene-{i}"
    nhan = nhan or f"cảnh {i} (đang dựng)"
    return f'''<!doctype html>
<html>
  <head><meta charset="UTF-8" /></head>
  <body>
    <template>
      <style>
        #root {{ position: absolute; inset: 0; }}
        .s{i}-stub {{ position: absolute; inset: 0; background: {nen}; display: flex; align-items: center; justify-content: center; color: {chu}; font-family: sans-serif; font-size: 64px; }}
      </style>
      <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H}">
        <div class="s{i}-stub">{nhan}</div>
      </div>
      <script>
        const tl = gsap.timeline({{ paused: true }});
        window.__timelines["{cid}"] = tl;
      </script>
    </template>
  </body>
</html>
'''


def sinh_logo(lg, W, H):
    ks, le = int(lg.get("kich_thuoc", 132)), int(lg.get("le", 44))
    canh = "left" if lg.get("vi_tri", "phai-duoi") == "trai-duoi" else "right"
    bong = " filter: drop-shadow(0 6px 10px rgba(0,0,0,0.55));" if lg.get("bong", False) else ""
    return f'''<!doctype html>
<html>
  <head><meta charset="UTF-8" /></head>
  <body>
    <template>
      <style>
        #root {{ position: absolute; inset: 0; pointer-events: none; }}
        .logo-img {{ position: absolute; {canh}: {le}px; bottom: {le}px; width: {ks}px; height: {ks}px;{bong} }}
      </style>
      <div id="root" data-composition-id="logo" data-width="{W}" data-height="{H}">
        <img class="logo-img" src="{lg["file"]}" alt="" />
      </div>
      <script>
        const tl = gsap.timeline({{ paused: true }});
        tl.fromTo(".logo-img", {{ opacity: 0 }}, {{ opacity: 1, duration: 1.0, ease: "power1.out" }}, 0.3);
        window.__timelines["logo"] = tl;
      </script>
    </template>
  </body>
</html>
'''


def sinh_html(cfg, hang, tong, do_tre, W, H):
    font_css = (KIT / "templates" / "font-face.css").read_text(encoding="utf-8")
    thuong_hieu_css = doc_css(cfg.get("khung", {}).get("chu_de", "sang"))   # "sang" (mặc định) hoặc "toi"
    mau = lay_bien(thuong_hieu_css)
    nen = cfg.get("khung", {}).get("nen", mau["nen"])
    chu = cfg.get("khung", {}).get("chu", mau["muc"])
    hosts, audio = [], []
    am_giong = float(cfg.get("giong", {}).get("am_luong", 1))
    for r in hang:
        i = r["stt"]
        if r.get("doan"):
            for d in r["doan"]:
                hosts.append(f'      <div id="host-{d["id"]}" data-composition-id="{d["id"]}" data-composition-src="{d["composition"]}" '
                             f'data-start="{d["start"]}" data-duration="{d["duration"]}" data-track-index="0" data-width="{W}" data-height="{H}"></div>')
        else:
            hosts.append(f'      <div id="host-scene-{i}" data-composition-id="scene-{i}" data-composition-src="{r["composition"]}" '
                         f'data-start="{r["start"]}" data-duration="{r["duration"]}" data-track-index="0" data-width="{W}" data-height="{H}"></div>')
        if not r["uoc_tinh"]:
            audio.append(f'      <audio id="vo{i - 1}" src="assets/audio/{r["canh"]}.wav" data-start="{round(r["start"] + do_tre, 1)}" '
                         f'data-duration="{r["audio"]}" data-track-index="1" data-volume="{am_giong}"></audio>')
    sfx = cfg.get("sfx", {})
    if sfx.get("track") and (DA.video / sfx["track"]).exists():
        audio.append(f'      <audio id="sfx" src="{sfx["track"]}" data-start="0" data-duration="{tong}" data-track-index="2" '
                     f'data-volume="{sfx.get("am_luong", 0.65)}"></audio>')
    lg = cfg.get("logo", {})
    if lg.get("hien", True) and lg.get("file") and (DA.video / lg["file"]).exists():
        hosts.append(f'      <div id="host-logo" data-composition-id="logo" data-composition-src="compositions/logo.html" '
                     f'data-start="0" data-duration="{tong}" data-track-index="9" data-width="{W}" data-height="{H}" style="z-index:100"></div>')
    return f'''<!doctype html>
<!-- Sinh bởi VideoKit/scripts/build_index.py từ du-an.json. Đừng sửa tay: sửa du-an.json rồi chạy lại. -->
<html lang="vi">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={W}, height={H}" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
{font_css}
{thuong_hieu_css}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: {W}px; height: {H}px; overflow: hidden; background: {nen}; }}
      #root {{ position: relative; width: 100%; height: 100%; background: {nen}; color: {chu}; font-family: 'Be Vietnam Pro', ui-sans-serif, sans-serif; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{tong}" data-width="{W}" data-height="{H}">
{chr(10).join(hosts)}
{chr(10).join(audio)}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
'''


def main():
    ap = argparse.ArgumentParser(description="Sinh index.html và moc-canh.json từ du-an.json")
    ap.add_argument("--khong-stub", action="store_true", help="không tạo file cảnh tạm cho cảnh chưa có")
    a = ap.parse_args()
    cfg = DA.cfg
    if not cfg:
        sys.exit(f"Không thấy du-an.json (tìm từ {DA.goc}). Chạy trong thư mục dự án hoặc đặt VIDEOKIT_PROJECT.")
    hang, tong, do_tre = tinh_moc(cfg)
    W, H = int(cfg.get("khung", {}).get("rong", 1920)), int(cfg.get("khung", {}).get("cao", 1080))
    DA.audio.mkdir(parents=True, exist_ok=True)
    (DA.audio / "moc-canh.json").write_text(json.dumps(hang, indent=1, ensure_ascii=False), encoding="utf-8")
    lg = cfg.get("logo", {})
    if lg.get("hien", True) and lg.get("file") and (DA.video / lg["file"]).exists():
        (DA.video / "compositions").mkdir(parents=True, exist_ok=True)
        (DA.video / "compositions" / "logo.html").write_text(sinh_logo(lg, W, H), encoding="utf-8")
    (DA.video / "index.html").write_text(sinh_html(cfg, hang, tong, do_tre, W, H), encoding="utf-8")
    tao = 0
    mau = lay_bien(doc_css(cfg.get("khung", {}).get("chu_de", "sang")))
    nen_, chu_ = cfg.get("khung", {}).get("nen", mau["nen"]), cfg.get("khung", {}).get("chu", mau["muc"])
    for r in hang:
        muc = [(r["composition"], r["stt"], None, None)] if not r.get("doan") else [(d["composition"], r["stt"], d["id"], d["ten"] or d["id"]) for d in r["doan"]]
        for comp, stt, cid, nhan in muc:
            f = DA.video / comp
            if not f.exists() and not a.khong_stub:
                f.parent.mkdir(parents=True, exist_ok=True)
                f.write_text(stub(stt, W, H, nen_, chu_, cid, nhan), encoding="utf-8")
                tao += 1
    print(f"index.html: {len(hang)} cảnh, tổng {tong} giây ({int(tong // 60)}:{tong % 60:04.1f}); tạo {tao} file cảnh tạm")
    for r in hang:
        print(f"  scene-{r['stt']} ({r['id']}): bắt đầu {r['start']:7.1f}s, dài {r['duration']:6.1f}s" + ("  (ước tính, chưa có giọng đọc)" if r["uoc_tinh"] else "") + (f", {len(r['doan'])} đoạn" if r.get("doan") else ""))


if __name__ == "__main__":
    main()
