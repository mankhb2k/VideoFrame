#!/usr/bin/env python3
"""Tạo giọng đọc bằng VieNeu-TTS chạy trên máy bạn (miễn phí, không cần khóa API).

Chuẩn bị (Python 3.10 trở lên):
    pip install vieneu

Cách chạy:
    python tao_tts_vieneu.py                                  # giọng có sẵn "Hải Đăng"
    python tao_tts_vieneu.py --ref-audio giong_cua_toi.wav    # nhân bản giọng từ file mẫu 3-5 giây
    python tao_tts_vieneu.py --canh canh3                     # chỉ chạy một cảnh
    python tao_tts_vieneu.py --khong-phat-am                  # không thay từ tiếng Anh theo bang-phat-am.csv

Lần đầu chạy, thư viện tự tải model từ Hugging Face (repo khoảng 1,7 GB).
Chỉ nhân bản giọng của chính bạn hoặc của người đã đồng ý.
"""
import argparse
import sys

from tien_ich import THU_MUC_DAU_RA, ap_dung_phat_am, doc_cac_canh, gop_wav


def main():
    ap = argparse.ArgumentParser(description="Tạo giọng đọc bằng VieNeu-TTS")
    ap.add_argument("--voice", default="Hải Đăng", help="tên giọng có sẵn")
    ap.add_argument("--ref-audio", help="file wav mẫu để nhân bản giọng (3-5 giây, ít tạp âm)")
    ap.add_argument("--canh", help="chỉ chạy cảnh có tên bắt đầu bằng chuỗi này, ví dụ canh3")
    ap.add_argument("--khong-phat-am", action="store_true", help="giữ nguyên từ tiếng Anh")
    args = ap.parse_args()

    try:
        from vieneu import Vieneu
    except ImportError:
        sys.exit("Chưa cài thư viện: pip install vieneu")

    tts = Vieneu()
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
            if not f.exists():
                if not args.khong_phat_am:
                    van_ban = ap_dung_phat_am(van_ban)
                if args.ref_audio:
                    audio = tts.infer(van_ban, ref_audio=args.ref_audio, denoise=True)
                else:
                    audio = tts.infer(van_ban, voice=args.voice)
                tts.save(audio, str(f))
            file_doan.append(f)
        f_canh = THU_MUC_DAU_RA / f"{ten}.wav"
        gop_wav(file_doan, f_canh)
        file_canh.append(f_canh)
    if len(file_canh) > 1:
        gop_wav(file_canh, THU_MUC_DAU_RA / "toan-bo.wav", nghi_giay=0.8)
    print("Xong. Xem thư mục dau-ra/")


if __name__ == "__main__":
    main()
