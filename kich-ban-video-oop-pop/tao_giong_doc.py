#!/usr/bin/env python3
"""Đọc toàn bộ lời thoại bằng giọng thư viện Gemini TTS, mỗi cảnh một yêu cầu API (tiết kiệm hạn mức).

Chỉ dùng thư viện chuẩn (Python 3.9+). Khóa đọc từ GOOGLE_API_KEY / GEMINI_API_KEY hoặc file .env.

    python3 tao_giong_doc.py                                  # đọc mọi cảnh, giọng vi-vn-advisor-2
    python3 tao_giong_doc.py --canh canh3                     # chỉ một cảnh
    python3 tao_giong_doc.py --model gemini-3.8-flash-tts     # đổi model
    python3 tao_giong_doc.py --phat-am                        # viết lại từ tiếng Anh theo bang-phat-am.csv

Kết quả: <dau-ra>/canhN_*.wav (24 kHz, mono) và <dau-ra>/thoi-luong.json (giây, từng cảnh).
Chạy lại sẽ bỏ qua cảnh đã có; xóa file .wav của cảnh nào thì cảnh đó được đọc lại.
"""
import argparse
import base64
import json
import sys
import time
import urllib.error
import wave
from pathlib import Path

from thu_giong import API, goi, lay_khoa  # noqa: F401  (dùng lại phần gọi REST)
from tien_ich import THU_MUC_GOC, ap_dung_phat_am, doc_cac_canh

GIONG = "vi-vn-advisor-2"
MODEL = "gemini-3.8-flash-lite-tts"
DAU_RA = THU_MUC_GOC.parent / "my-video" / "assets" / "audio"


def doc_mot_canh(khoa, model, giong, van_ban, thu_lai=3):
    body = {
        "contents": [{"parts": [{"text": van_ban}]}],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": giong}}},
        },
    }
    for lan in range(1, thu_lai + 1):
        try:
            kq = goi(khoa, f"models/{model}:generateContent", body)
            return base64.b64decode(kq["candidates"][0]["content"]["parts"][0]["inlineData"]["data"])
        except urllib.error.HTTPError as e:
            noi_dung = e.read().decode(errors="replace")
            het_ngay = e.code == 429 and "PerDay" in noi_dung
            if e.code in (429, 500, 503) and not het_ngay and lan < thu_lai:
                time.sleep(15 * lan)
                continue
            sys.exit(f"HTTP {e.code} ({'hết hạn mức ngày' if het_ngay else 'lỗi'}): {noi_dung[:400]}")


def main():
    ap = argparse.ArgumentParser(description="Đọc lời thoại bằng Gemini TTS")
    ap.add_argument("--giong", default=GIONG)
    ap.add_argument("--model", default=MODEL)
    ap.add_argument("--canh", help="chỉ cảnh có tên bắt đầu bằng chuỗi này, ví dụ canh3")
    ap.add_argument("--phat-am", action="store_true", help="áp dụng bang-phat-am.csv trước khi đọc")
    ap.add_argument("--dau-ra", default=str(DAU_RA))
    args = ap.parse_args()

    khoa = lay_khoa()
    dau_ra = Path(args.dau_ra)
    dau_ra.mkdir(parents=True, exist_ok=True)
    file_tl = dau_ra / "thoi-luong.json"
    thoi_luong = json.loads(file_tl.read_text()) if file_tl.exists() else {}

    for ten, doan in doc_cac_canh(chi_canh=args.canh):
        van_ban = "\n\n".join(doan)
        if args.phat_am:
            van_ban = ap_dung_phat_am(van_ban)
        f = dau_ra / f"{ten}.wav"
        if not f.exists():
            f.write_bytes(doc_mot_canh(khoa, args.model, args.giong, van_ban))
        with wave.open(str(f), "rb") as w:
            thoi_luong[ten] = round(w.getnframes() / w.getframerate(), 2)
        print(f"{ten}: {thoi_luong[ten]} giây ({len(van_ban)} ký tự)")
        file_tl.write_text(json.dumps(thoi_luong, indent=2, ensure_ascii=False))
    print("Tổng:", round(sum(thoi_luong.values()), 1), "giây. Thư mục:", dau_ra)


if __name__ == "__main__":
    main()
