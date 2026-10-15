#!/usr/bin/env python3
"""Thay một số khối giọng cũ (loi-thoai/khoi/<id>.wav) bằng đoạn cắt từ bản đọc MỘT MẠCH MỚI (loi-thoai/giong-mot-mach/), không gọi TTS.

Dùng khi lời của vài khối đổi sau khi đã đọc từng khối: tìm đầu và cuối khối trong bản một mạch bằng mốc từng từ whisper (gióng với kịch bản),
cắt, cắt lặng thừa, chỉnh âm lượng cho bằng các khối còn lại của cảnh, rồi ghi đè khối cũ (bản cũ chép vào loi-thoai/khoi/cu/).

    python3 storyboard/thay_khoi.py canh4-d6-k2 canh5-d1-k1 ...
"""
import array
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent / "VideoKit" / "scripts"))
import tao_storyboard as T  # noqa: E402
import tao_giong_doc as G  # noqa: E402

DA = T.DA
NGUON = DA / "loi-thoai" / "giong-mot-mach"
KHOI = DA / "loi-thoai" / "khoi"


def rms(a):
    return (sum(x * x for x in a) / max(1, len(a))) ** 0.5


def main():
    ids = sys.argv[1:]
    if not ids:
        sys.exit(__doc__)
    (KHOI / "cu").mkdir(exist_ok=True)
    for c in T.cfg["canh"]:
        can = [i for i in ids if i.startswith(c["id"] + "-")]
        if not can:
            continue
        # Canh đọc words của bản một mạch: đặt AUD tạm thời về thư mục nguồn
        T.AUD = NGUON
        cn = T.Canh(c, NGUON)
        mk = T.khoi_tu_phien_am(c, cn)
        wav, fs = G.doc_wav(NGUON / f"{c['tep_loi_thoai']}.wav")
        # âm lượng chuẩn: trung vị RMS của các khối cũ không bị thay trong cảnh
        giu = [k["id"] for k in mk if k["id"] not in ids and (KHOI / f"{k['id']}.wav").exists()]
        r_chuan = sorted(rms(G.doc_wav(KHOI / f"{i}.wav")[0]) for i in giu)[len(giu) // 2] if giu else None
        for k in mk:
            if k["id"] not in can:
                continue
            a, b = max(0, int((k["bat_dau"] - 0.12) * fs)), min(len(wav), int((k["ket_thuc"] + 0.05) * fs))
            cat = G.cat_lang(array.array("h", wav[a:b]), fs)
            he_so = 1.0
            if r_chuan:
                he_so = max(0.7, min(1.4, r_chuan / max(1.0, rms(cat))))
                cat = array.array("h", (max(-32768, min(32767, int(x * he_so))) for x in cat))
            f = KHOI / f"{k['id']}.wav"
            if f.exists():
                shutil.copy2(f, KHOI / "cu" / f.name)
            G.luu_wav(f, cat, fs)
            print(f"{k['id']}: {len(cat) / fs:5.1f} giây (cắt {k['bat_dau']:.1f}s→{k['ket_thuc']:.1f}s của bản một mạch, hệ số âm lượng {he_so:.2f})")


if __name__ == "__main__":
    main()
