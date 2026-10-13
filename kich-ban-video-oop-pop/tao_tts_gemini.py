#!/usr/bin/env python3
"""Tạo giọng đọc cho video bằng Gemini TTS của Google.

Viết theo tài liệu Gemini API (speech generation và voice design); CHƯA được chạy thử
với khóa thật, nên nếu API đổi tên trường, hãy đối chiếu lại với tài liệu.

Chuẩn bị:
    pip install "google-genai>=2.25.0"
    export GEMINI_API_KEY="khóa của bạn"          # Windows PowerShell: $env:GEMINI_API_KEY="khóa của bạn"

Bước 1 - tạo giọng nam nhiệt huyết, nghe thử preview_giong.wav:
    python tao_tts_gemini.py --tao-giong

Bước 2 - đọc toàn bộ lời thoại bằng giọng vừa tạo (ID lưu trong giong.txt):
    python tao_tts_gemini.py
    python tao_tts_gemini.py --canh canh3            # chỉ chạy một cảnh
    python tao_tts_gemini.py --voice Fenrir          # hoặc dùng giọng có sẵn thay vì giọng tự thiết kế

Kết quả nằm trong thư mục dau-ra/ (từng đoạn, từng cảnh, và toan-bo.wav).
Đừng ghi khóa API vào file hoặc dán vào chat; dùng biến môi trường như trên.
"""
import argparse
import base64
import os
import sys
import time
from pathlib import Path

from tien_ich import THU_MUC_DAU_RA, THU_MUC_GOC, doc_cac_canh, gop_wav

MODEL = "gemini-3.8-flash-tts"
FILE_GIONG = THU_MUC_GOC / "giong.txt"

MO_TA_GIONG = (
    "A male Vietnamese teacher in his early 30s with a clear, warm baritone and a standard Hanoi accent. "
    "Passionate and energetic like a tech instructor who loves his subject: lively pace, rising intonation "
    "on key points, expressive and emotional, with a smile in his voice and short pauses before important ideas."
)
PHONG_CACH = "enthusiastic, passionate teacher, warm and emotional"


def lay_client():
    if not (os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")):
        sys.exit("Chưa đặt biến môi trường GEMINI_API_KEY (xem hướng dẫn ở đầu file).")
    from google import genai
    return genai.Client()


def tao_giong(client, mo_ta, ten="Manh"):
    giong = client.voices.create(
        store=True,
        voice={
            "model": MODEL,
            "type": "prompted",
            "display_name": ten,
            "gender": "male",
            "language_code": "vi-VN",
            "prompted": {"input": mo_ta},
        },
    )
    if giong.sample_audio and giong.sample_audio.data:
        Path("preview_giong.wav").write_bytes(base64.b64decode(giong.sample_audio.data))
        print("Đã lưu preview_giong.wav, hãy nghe thử trước khi chạy cả kịch bản.")
    FILE_GIONG.write_text(giong.id, encoding="utf-8")
    print("ID giọng:", giong.id, "(đã lưu vào giong.txt)")


def doc_mot_doan(client, van_ban, giong, phong_cach=PHONG_CACH, thu_lai=3):
    for lan in range(1, thu_lai + 1):
        try:
            r = client.interactions.create(
                model=MODEL,
                input=[{
                    "type": "user_input",
                    "content": [{
                        "type": "text",
                        "text": van_ban,
                        "annotations": [{"type": "speech_metadata", "style": phong_cach}],
                    }],
                }],
                response_format={"type": "audio"},
                generation_config={"speech_config": [{"voice": giong}]},
            )
            return base64.b64decode(r.output_audio.data)
        except Exception as e:  # noqa: BLE001
            print(f"  lỗi lần {lan}/{thu_lai}: {e}")
            if lan == thu_lai:
                raise
            time.sleep(5 * lan)


def main():
    ap = argparse.ArgumentParser(description="Tạo giọng đọc bằng Gemini TTS")
    ap.add_argument("--tao-giong", action="store_true", help="tạo giọng tự thiết kế rồi thoát")
    ap.add_argument("--mo-ta", default=MO_TA_GIONG, help="mô tả giọng (tiếng Anh, 1-2 câu)")
    ap.add_argument("--voice", help="ID giọng (voice_...) hoặc tên giọng có sẵn; mặc định đọc từ giong.txt")
    ap.add_argument("--canh", help="chỉ chạy cảnh có tên bắt đầu bằng chuỗi này, ví dụ canh3")
    ap.add_argument("--phong-cach", default=PHONG_CACH, help="chỉ dẫn cảm xúc cho từng đoạn")
    args = ap.parse_args()

    client = lay_client()
    if args.tao_giong:
        tao_giong(client, args.mo_ta)
        return

    giong = args.voice or (FILE_GIONG.read_text(encoding="utf-8").strip() if FILE_GIONG.exists() else None)
    if not giong:
        sys.exit("Chưa có giọng: chạy --tao-giong trước, hoặc truyền --voice TEN_GIONG.")

    THU_MUC_DAU_RA.mkdir(exist_ok=True)
    cac_canh = doc_cac_canh(chi_canh=args.canh)
    if not cac_canh:
        sys.exit("Không tìm thấy file canh*.txt trong thư mục loi-thoai.")

    file_canh = []
    for ten, doan in cac_canh:
        print(f"{ten}: {len(doan)} đoạn")
        file_doan = []
        for i, van_ban in enumerate(doan, 1):
            f = THU_MUC_DAU_RA / f"{ten}_{i:02d}.wav"
            if not f.exists():  # chạy lại sẽ bỏ qua đoạn đã có, đỡ tốn hạn mức
                f.write_bytes(doc_mot_doan(client, van_ban, giong, args.phong_cach))
            file_doan.append(f)
        f_canh = THU_MUC_DAU_RA / f"{ten}.wav"
        gop_wav(file_doan, f_canh)
        file_canh.append(f_canh)
    if len(file_canh) > 1:
        gop_wav(file_canh, THU_MUC_DAU_RA / "toan-bo.wav", nghi_giay=0.8)
    print("Xong. Xem thư mục dau-ra/")


if __name__ == "__main__":
    main()
