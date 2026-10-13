#!/usr/bin/env python3
"""Liệt kê giọng Gemini TTS và tạo file nghe thử cho từng giọng (chỉ dùng thư viện chuẩn, Python 3.9+).

Khóa API đọc từ biến môi trường GOOGLE_API_KEY / GEMINI_API_KEY, hoặc từ file .env ở thư mục dự án.

    python3 thu_giong.py --liet-ke                       # chỉ in danh sách giọng tiếng Việt
    python3 thu_giong.py                                 # nghe thử mọi giọng nam tiếng Việt
    python3 thu_giong.py --gioi-tinh female              # giọng nữ
    python3 thu_giong.py --giong vi-vn-tutor-2 Fenrir    # chọn đích danh (ID thư viện hoặc tên giọng có sẵn)

Kết quả: thư mục nghe-thu-giong/<ID giọng>.wav. Chạy lại sẽ bỏ qua giọng đã có.
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from tien_ich import THU_MUC_GOC

API = "https://generativelanguage.googleapis.com/v1beta"
MODEL = "gemini-3.8-flash-tts"
CAU_MAU = (
    "Bạn mở một file code, và chỉ muốn dùng đúng một hàm. Nhưng hàm đó nằm trong class cha. "
    "Class cha lại kế thừa class ông. Đến tầng thứ năm, bạn bắt đầu tự hỏi: mình đang đọc code, "
    "hay đang đọc gia phả?"
)
THU_MUC_RA = THU_MUC_GOC / "nghe-thu-giong"


def lay_khoa():
    for ten in ("GOOGLE_API_KEY", "GEMINI_API_KEY"):
        if os.environ.get(ten):
            return os.environ[ten]
    for env in (THU_MUC_GOC / ".env", THU_MUC_GOC.parent / ".env"):
        if env.exists():
            for dong in env.read_text(encoding="utf-8").splitlines():
                ten, _, gia_tri = dong.partition("=")
                if ten.strip() in ("GOOGLE_API_KEY", "GEMINI_API_KEY") and gia_tri.strip():
                    return gia_tri.strip().strip("\"'")
    sys.exit("Không tìm thấy GOOGLE_API_KEY (biến môi trường hoặc file .env).")


def goi(khoa, duong_dan, du_lieu=None, tham_so=None):
    url = f"{API}/{duong_dan}" + ("?" + urllib.parse.urlencode(tham_so) if tham_so else "")
    req = urllib.request.Request(
        url,
        data=json.dumps(du_lieu).encode() if du_lieu is not None else None,
        headers={"x-goog-api-key": khoa, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)


def liet_ke_giong(khoa, gioi_tinh=None):
    ds = goi(khoa, "voices", tham_so={"language_code": "vi-VN", "page_size": 100}).get("voices", [])
    return [v for v in ds if not gioi_tinh or v.get("gender") == gioi_tinh]


def tao_mau(khoa, giong, cau, thu_lai=4):
    body = {
        "contents": [{"parts": [{"text": cau}]}],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": giong}}},
        },
    }
    for lan in range(1, thu_lai + 1):
        try:
            kq = goi(khoa, f"models/{MODEL}:generateContent", body)
            import base64
            return base64.b64decode(kq["candidates"][0]["content"]["parts"][0]["inlineData"]["data"])
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 503) and lan < thu_lai:
                time.sleep(10 * lan)
                continue
            sys.exit(f"{giong}: HTTP {e.code} {e.read().decode(errors='replace')[:300]}")


def main():
    ap = argparse.ArgumentParser(description="Nghe thử giọng Gemini TTS")
    ap.add_argument("--liet-ke", action="store_true", help="chỉ in danh sách giọng rồi thoát")
    ap.add_argument("--gioi-tinh", default="male", choices=["male", "female", "neutral", "all"])
    ap.add_argument("--giong", nargs="+", help="đọc đích danh các giọng này thay vì lọc theo giới tính")
    ap.add_argument("--cau", default=CAU_MAU, help="câu đọc thử")
    args = ap.parse_args()

    khoa = lay_khoa()
    loc = None if args.gioi_tinh == "all" else args.gioi_tinh
    ds = liet_ke_giong(khoa, loc)
    if args.liet_ke:
        for v in ds:
            print(f"{v['id']:20} {v.get('gender'):8} {v.get('pitch'):7} {v.get('persona')}")
        print(f"Tổng: {len(ds)} giọng")
        return

    ten_giong = args.giong or [v["id"] for v in ds]
    THU_MUC_RA.mkdir(exist_ok=True)
    for g in ten_giong:
        f = THU_MUC_RA / f"{g}.wav"
        if f.exists():
            print(f"bỏ qua {g} (đã có)")
            continue
        f.write_bytes(tao_mau(khoa, g, args.cau))
        print(f"đã lưu {f.name}")
    print("Xong. Nghe thử trong", THU_MUC_RA)


if __name__ == "__main__":
    main()
