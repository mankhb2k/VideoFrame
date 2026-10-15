#!/usr/bin/env python3
"""Áp các chỉnh sửa âm thanh làm trong Studio (cắt, chia, kéo clip lưu trong index.html) vào file wav từng cảnh, mốc khối và khoảng giữa các cảnh.
Chỉ dùng thư viện chuẩn. Chạy SAU khi đóng Studio và TRƯỚC build_index.py (build_index sẽ ghi đè index.html).

    cd videos/<du-an>
    python3 ../../VideoKit/scripts/ap_chinh_sua_am_thanh.py            # xem và áp
    python3 ../../VideoKit/scripts/ap_chinh_sua_am_thanh.py --thu      # chỉ in kế hoạch, không ghi

Với mỗi cảnh (file wav): các clip <audio> cùng file được ghép lại theo thứ tự `data-start`; mỗi clip lấy đoạn [data-media-start, +data-duration] của file gốc,
khoảng trống giữa hai clip thành lặng. Bản wav mới ghi đè file cảnh (bản trước chép vào loi-thoai/truoc-chinh-sua/). Mốc khối trong
loi-thoai/<tep>.moc-khoi.json được dịch theo; khối bị cắt hết thì bỏ, khối bị cắt một phần thì rút ngắn. Khoảng giữa các cảnh được ghi vào
`giu_them_giay` của từng cảnh trong du-an.json để build_index.py dựng đúng mốc cảnh hình theo mốc âm thanh bạn đã đặt.
"""
import argparse
import array
import json
import re
import shutil
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tao_giong_doc as G  # noqa: E402

DA = G.DA


def doc_clip(thẻ):
    def lay(k, mac_dinh=None):
        m = re.search(rf'{k}="([^"]*)"', thẻ)
        return m.group(1) if m else mac_dinh
    return {"id": lay("id"), "src": lay("src"), "start": float(lay("data-start")), "dai": float(lay("data-duration")),
            "media": float(lay("data-media-start", "0"))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--thu", action="store_true")
    a = ap.parse_args()
    html = (DA.video / "index.html").read_text(encoding="utf-8")
    clips = [doc_clip(t) for t in re.findall(r"<audio[^>]*>", html)]
    do_tre = float(DA.cfg.get("giong", {}).get("do_tre_giay", 0.3))
    cfg = DA.cfg
    bak = DA.loi_thoai / "truoc-chinh-sua"
    lan = bak / time.strftime("lan-%H%M%S")   # bản trước MỖI lần áp (bản gốc đầu tiên vẫn ở truoc-chinh-sua/)
    ket_qua, dau_canh = {}, {}
    for c in cfg["canh"]:
        ten = f"{c['tep_loi_thoai']}.wav"
        cc = sorted((x for x in clips if x["src"].endswith(ten)), key=lambda x: x["start"])
        if not cc:
            sys.exit(f"Không thấy clip âm thanh của {c['id']} trong index.html")
        f = DA.audio / ten
        goc = bak / ten
        if not a.thu:
            bak.mkdir(exist_ok=True)
            lan.mkdir(exist_ok=True)
            if not goc.exists():
                shutil.copy2(f, goc)
            shutil.copy2(f, lan / ten)
        # Studio chỉnh trên file đang phát (assets/audio/<cảnh>.wav), nên mốc data-media-start tính theo CHÍNH file này
        pcm, fs = G.doc_wav(f)
        moi, pos_moi, map_ = array.array("h"), 0.0, []
        truoc_ket = None
        for x in cc:
            if truoc_ket is not None:
                khoang = x["start"] - truoc_ket
                if khoang < -0.01:
                    sys.exit(f"{c['id']}: clip {x['id']} chồng lên clip trước {-khoang:.2f} giây; cần tách bằng tay")
                if khoang > 0:
                    moi.extend([0] * int(round(khoang * fs)))
            a0 = int(round(x["media"] * fs))
            b0 = min(len(pcm), a0 + int(round(x["dai"] * fs)))
            seg = pcm[a0:b0]
            map_.append((x["media"], x["media"] + len(seg) / fs, len(moi) / fs))   # đoạn gốc [m0,m1) bắt đầu ở giây s trong bản mới
            moi.extend(seg)
            truoc_ket = x["start"] + len(seg) / fs
        dai = len(moi) / fs
        dau_canh[c["id"]] = cc[0]["start"] - do_tre
        ket_qua[c["id"]] = {"dai": dai, "clip": [{"id": x["id"], "start": x["start"], "media": x["media"], "dai": x["dai"]} for x in cc]}
        print(f"{c['id']}: {len(cc)} clip, {len(pcm) / fs:.1f} giây gốc -> {dai:.1f} giây; clip đầu bắt đầu {cc[0]['start']:.2f}s")
        # mốc khối
        fm = DA.loi_thoai / f"{c['tep_loi_thoai']}.moc-khoi.json"
        if fm.exists():
            if not a.thu:
                if not (bak / fm.name).exists():
                    shutil.copy2(fm, bak / fm.name)
                shutil.copy2(fm, lan / fm.name)
            goc_m = json.loads(fm.read_text(encoding="utf-8"))
            moi_m = []
            for k in goc_m:
                b0_, e0_ = k["bat_dau"], k["ket_thuc"]
                phan = [(m0, m1, s) for (m0, m1, s) in map_ if e0_ > m0 and b0_ < m1]
                if not phan:
                    print(f"  khối {k['id']} bị cắt hết, bỏ")
                    continue
                m0, m1, s = phan[0]
                nb = s + max(b0_, m0) - m0
                m0e, m1e, se = phan[-1]
                ne = se + min(e0_, m1e) - m0e
                if e0_ > m1e + 0.01 or b0_ < m0 - 0.01:
                    print(f"  khối {k['id']} bị cắt một phần: {b0_:.1f}-{e0_:.1f} -> {nb:.1f}-{ne:.1f}")
                moi_m.append({**k, "bat_dau": round(nb, 3), "ket_thuc": round(ne, 3)})
            ket_qua[c["id"]]["moc_khoi"] = moi_m
        ket_qua[c["id"]]["wav"] = moi
        ket_qua[c["id"]]["fs"] = fs
    # khoảng giữa các cảnh -> giu_them_giay
    ds = cfg["canh"]
    for i, c in enumerate(ds):
        L = ket_qua[c["id"]]["dai"]
        if i + 1 < len(ds):
            thoi_luong = dau_canh[ds[i + 1]["id"]] - dau_canh[c["id"]]
            extra = round(thoi_luong - (L + 2 * do_tre), 2)
        else:
            extra = 0.0
        ket_qua[c["id"]]["giu_them_giay"] = extra
        print(f"  {c['id']}: giu_them_giay = {extra:+.2f}")
        if extra < -0.3:
            print(f"    cảnh báo: khoảng giữa {c['id']} và cảnh sau ngắn hơn hai nhịp lặng đầu cuối ({-extra:.2f} giây)")
    if a.thu:
        return
    for c in ds:
        r = ket_qua[c["id"]]
        G.luu_wav(DA.audio / f"{c['tep_loi_thoai']}.wav", r["wav"], r["fs"])
        if "moc_khoi" in r:
            (DA.loi_thoai / f"{c['tep_loi_thoai']}.moc-khoi.json").write_text(json.dumps(r["moc_khoi"], ensure_ascii=False, indent=1), encoding="utf-8")
        c["giu_them_giay"] = r["giu_them_giay"]
    (DA.goc / "du-an.json").write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tom = {c["id"]: {k: v for k, v in ket_qua[c["id"]].items() if k not in ("wav", "moc_khoi", "fs")} for c in ds}
    (DA.loi_thoai / "chinh-sua.json").write_text(json.dumps(tom, ensure_ascii=False, indent=1), encoding="utf-8")
    print("Đã áp chỉnh sửa. Bước kế: whisper (phien_am_openai.py), tao_storyboard.py, chuyen_nhip.py, build_index.py, build_canh.py")


if __name__ == "__main__":
    main()
