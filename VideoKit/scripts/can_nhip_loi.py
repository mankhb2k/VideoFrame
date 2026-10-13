#!/usr/bin/env python3
"""Ước lượng mốc bắt đầu/kết thúc từng câu trong giọng đọc, bằng cách khớp câu với khoảng lặng của file wav.

Không cần model nhận dạng giọng nói. Cách làm: tách lời thoại thành câu, đo khoảng lặng bằng ffmpeg
(silencedetect), rồi chọn ranh giới câu là những khoảng lặng gần nhất với vị trí dự kiến theo tỉ lệ ký tự.
Độ chính xác cỡ vài phần mười giây, đủ để đồng bộ highlight/hiệu ứng theo câu (không phải theo từng từ).

    python3 VideoKit/scripts/can_nhip_loi.py
Kết quả: my-video/assets/audio/cues.json  (giây tính từ đầu mỗi cảnh, đã cộng 0,3 giây lặng đầu cảnh)
"""
import os
import json
import re
import subprocess
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent                       # thư mục VideoKit
GOC = Path(os.environ.get("VIDEOKIT_PROJECT") or Path.cwd())  # thư mục gốc dự án video (mặc định: nơi bạn đang đứng)
def _tim_loi_thoai():
    """Thư mục lời thoại: biến VIDEOKIT_LOI_THOAI, hoặc kich-ban/loi-thoai, hoặc kich-ban*/loi-thoai đầu tiên."""
    if os.environ.get("VIDEOKIT_LOI_THOAI"):
        return Path(os.environ["VIDEOKIT_LOI_THOAI"])
    mac_dinh = GOC / "kich-ban" / "loi-thoai"
    if mac_dinh.exists():
        return mac_dinh
    ung_vien = sorted(GOC.glob("kich-ban*/loi-thoai"))
    return ung_vien[0] if ung_vien else mac_dinh


LOI = _tim_loi_thoai()
AUDIO = GOC / "my-video" / "assets" / "audio"
DO_TRE = 0.3  # giọng bắt đầu sau 0,3 giây so với đầu cảnh (xem index.html)


def tach_cau(van_ban):
    cau = []
    for doan in [d.strip() for d in van_ban.split("\n\n") if d.strip()]:
        cau += [c.strip() for c in re.split(r"(?<=[.!?…:])\s+", doan.replace("\n", " ")) if c.strip()]
    return cau


def do_lang(wav):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(wav), "-af",
                        "silencedetect=n=-38dB:d=0.18", "-f", "null", "-"], capture_output=True, text=True)
    bat_dau = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r.stderr)]
    ket_thuc = [(float(a), float(b)) for a, b in re.findall(r"silence_end: ([\d.]+) \| silence_duration: ([\d.]+)", r.stderr)]
    return [(s, e) for s, (e, _) in zip(bat_dau, ket_thuc)]


def thoi_luong(wav):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(wav)],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


def can_canh(ten):
    wav = AUDIO / f"{ten}.wav"
    cau = tach_cau((LOI / f"{ten}.txt").read_text(encoding="utf-8"))
    tong = thoi_luong(wav)
    lang = [(s, e) for s, e in do_lang(wav) if s > 0.2 and e < tong - 0.05]  # bỏ lặng đầu/cuối file
    ky_tu = [len(c) for c in cau]
    tong_ky_tu = sum(ky_tu)
    # thời gian nói thuần = tổng - các khoảng lặng giữa
    thoi_lang = sum(e - s for s, e in lang)
    noi = tong - thoi_lang
    ranh_gioi, da_dung, cum = [], -1, 0
    for k in range(len(cau) - 1):
        cum += ky_tu[k]
        mong_doi = cum / tong_ky_tu * noi  # vị trí dự kiến trên trục "thời gian nói"
        tot = None
        for i, (s, e) in enumerate(lang):
            if i <= da_dung:
                continue
            truoc = sum(b - a for a, b in lang[:i])  # lặng đã trôi qua trước khoảng lặng này
            vi_tri_noi = s - truoc
            gap = abs(vi_tri_noi - mong_doi)
            if tot is None or gap < tot[0]:
                tot = (gap, i)
        if tot is None:  # hết khoảng lặng để chọn: chia theo tỉ lệ
            ranh_gioi.append(None)
            continue
        da_dung = tot[1]
        ranh_gioi.append(lang[tot[1]])
    ket_qua, t = [], 0.0
    for k, c in enumerate(cau):
        if k < len(ranh_gioi) and ranh_gioi[k]:
            s, e = ranh_gioi[k]
            cuoi, ke_tiep = s, e
        else:
            cuoi, ke_tiep = tong, tong
        ket_qua.append({"cau": c, "bat_dau": round(t + DO_TRE, 2), "ket_thuc": round(cuoi + DO_TRE, 2)})
        t = ke_tiep
    return {"thoi_luong_giong": round(tong, 2), "so_khoang_lang": len(lang), "cac_cau": ket_qua}


def main():
    ket_qua = {}
    for f in sorted(LOI.glob("canh*.txt")):
        ten = f.stem
        if not (AUDIO / f"{ten}.wav").exists():
            sys.exit(f"thiếu {ten}.wav")
        ket_qua[ten] = can_canh(ten)
        c = ket_qua[ten]
        print(f"{ten}: {len(c['cac_cau'])} câu, {c['so_khoang_lang']} khoảng lặng")
    (AUDIO / "cues.json").write_text(json.dumps(ket_qua, ensure_ascii=False, indent=1), encoding="utf-8")
    print("Đã ghi", AUDIO / "cues.json")


if __name__ == "__main__":
    main()
