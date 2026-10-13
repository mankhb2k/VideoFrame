#!/usr/bin/env python3
"""Lấy mốc thời gian từng từ của giọng đọc bằng API phiên âm OpenAI (whisper-1), chỉ dùng thư viện chuẩn.

Khóa đọc từ OPENAI_API_KEY (biến môi trường hoặc .env). Chi phí khoảng $0,006 mỗi phút âm thanh.

    python3 VideoKit/scripts/phien_am_openai.py canh0_hook            # một cảnh
    python3 VideoKit/scripts/phien_am_openai.py                       # mọi cảnh
Kết quả: my-video/assets/audio/words-<cảnh>.json  (giây tính từ đầu cảnh, đã cộng 0,3 giây lặng đầu cảnh)
"""
import os
import json
import sys
import urllib.request
import uuid
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent                       # thư mục VideoKit
GOC = Path(os.environ.get("VIDEOKIT_PROJECT") or Path.cwd())  # thư mục gốc dự án video (mặc định: nơi bạn đang đứng)
AUDIO = GOC / "my-video" / "assets" / "audio"
DO_TRE = 0.3  # giọng bắt đầu sau 0,3 giây so với đầu cảnh (xem index.html)


def lay_khoa():
    import os
    if os.environ.get("OPENAI_API_KEY"):
        return os.environ["OPENAI_API_KEY"]
    for env in (GOC / ".env", GOC.parent / ".env"):
        if env.exists():
            for dong in env.read_text(encoding="utf-8").splitlines():
                ten, _, gt = dong.partition("=")
                if ten.strip() == "OPENAI_API_KEY" and gt.strip():
                    return gt.strip().strip("\"'")
    sys.exit("Không tìm thấy OPENAI_API_KEY")


def phien_am(khoa, wav):
    ranh = uuid.uuid4().hex
    truong = [("model", "whisper-1"), ("response_format", "verbose_json"), ("language", "vi"),
              ("timestamp_granularities[]", "word")]
    phan = [f'--{ranh}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode() for k, v in truong]
    phan.append((f'--{ranh}\r\nContent-Disposition: form-data; name="file"; filename="{wav.name}"\r\n'
                 f'Content-Type: audio/wav\r\n\r\n').encode() + wav.read_bytes() + b"\r\n")
    phan.append(f"--{ranh}--\r\n".encode())
    req = urllib.request.Request("https://api.openai.com/v1/audio/transcriptions", data=b"".join(phan), headers={
        "Authorization": f"Bearer {khoa}", "Content-Type": f"multipart/form-data; boundary={ranh}"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.load(r)


def main():
    if any(a in ("-h", "--help") for a in sys.argv[1:]):
        print(__doc__)
        return
    khoa = lay_khoa()
    ten_canh = sys.argv[1:] or [f.stem for f in sorted(AUDIO.glob("canh*.wav"))]
    for ten in ten_canh:
        kq = phien_am(khoa, AUDIO / f"{ten}.wav")
        tu = [{"tu": w["word"], "bat_dau": round(w["start"] + DO_TRE, 2), "ket_thuc": round(w["end"] + DO_TRE, 2)}
              for w in kq.get("words", [])]
        (AUDIO / f"words-{ten}.json").write_text(json.dumps({"van_ban": kq.get("text", ""), "cac_tu": tu},
                                                            ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{ten}: {len(tu)} từ")


if __name__ == "__main__":
    main()
