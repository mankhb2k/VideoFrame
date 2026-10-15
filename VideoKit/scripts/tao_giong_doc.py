#!/usr/bin/env python3
"""Tạo giọng đọc bằng Gemini TTS: MỖI CẢNH MỘT YÊU CẦU (chỉ dùng thư viện chuẩn; Python 3.9+).

    cd videos/<du-an>
    python3 ../../VideoKit/scripts/tach_kich_ban.py            # bước trước: tạo loi-thoai/<canh>.json (lời dẫn từng khối)
    python3 ../../VideoKit/scripts/tao_giong_doc.py            # đọc mọi cảnh chưa có
    python3 ../../VideoKit/scripts/tao_giong_doc.py --canh canh3 --ghi-de
    python3 ../../VideoKit/scripts/tao_giong_doc.py --khoa-env GOOGLE_API_KEY_2    # dùng khóa khác trong .env
    python3 ../../VideoKit/scripts/tao_giong_doc.py --chia 2   # cảnh quá dài: tách mỗi cảnh làm 2 yêu cầu theo ranh giới đoạn

Giọng, model và độ trễ lấy từ `giong` trong du-an.json. Toàn bộ lời dẫn của cảnh được ghép thành MỘT văn bản (mỗi khối một đoạn văn),
đọc trong MỘT yêu cầu để Gemini tự ngắt nghỉ theo câu; KHÔNG chèn khoảng dừng hay nhịp thở nhân tạo (đổi `[Dừng N giây]` trong kịch bản
thành giữ hình ở bước dựng nếu cần). Bảng đọc từ nước ngoài: `loi-thoai/bang-phat-am.csv` (cột `tu,doc`), chỉ thay khi gửi đi đọc.
Nếu âm thanh trả về ngắn bất thường so với số ký tự (có thể bị cắt), tự tách đôi theo ranh giới đoạn và nối lại.

Kết quả: video/assets/audio/<tep_loi_thoai>.wav (24 kHz, mono, đã cắt lặng thừa đầu/cuối, chừa 0,12 giây) và loi-thoai/thoi-luong.json.
Mốc từng từ lấy sau đó bằng phien_am_openai.py, SAU KHI âm thanh đã chốt.
"""
import argparse
import array
import base64
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
import wave
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _du_an import KIT, du_an  # noqa: E402

DA = du_an()
API = "https://generativelanguage.googleapis.com/v1beta"
GIA_USD_TRIEU_TOKEN_AM_THANH = 9.0   # gemini-3.8-flash-tts, giá chuẩn đầu ra âm thanh (nguồn thứ ba, kiểm lại khi thanh toán)
GIA_USD_TRIEU_TOKEN_CHU = 0.5
NGHI_CUNG_DOAN, NGHI_DOAN_MOI = 0.5, 0.8
LE_GIU = 0.12   # giữ lại chừng này giây im lặng quanh lời sau khi cắt


def lay_khoa(ten_bien=None):
    for ten in ([ten_bien] if ten_bien else ["GOOGLE_API_KEY", "GEMINI_API_KEY"]):
        if os.environ.get(ten):
            return os.environ[ten]
    for env in (DA.goc / ".env", DA.goc.parent / ".env", DA.goc.parent.parent / ".env"):
        if env.exists():
            for dong in env.read_text(encoding="utf-8").splitlines():
                ten, _, gt = dong.partition("=")
                if ten.strip() in ([ten_bien] if ten_bien else ["GOOGLE_API_KEY", "GEMINI_API_KEY"]) and gt.strip():
                    return gt.strip().strip("\"'")
    sys.exit(f"Không tìm thấy {ten_bien or 'GOOGLE_API_KEY'} (biến môi trường hoặc file .env).")


def doc_bang_phat_am():
    f = DA.loi_thoai / "bang-phat-am.csv"
    if not f.exists():
        return []
    with open(f, encoding="utf-8", newline="") as fh:
        hang = [r for r in csv.DictReader(fh) if r.get("tu") and r.get("doc")]
    return sorted(((r["tu"], r["doc"]) for r in hang), key=lambda x: -len(x[0]))   # cụm dài thay trước


def ap_phat_am(van_ban, bang):
    for tu, doc in bang:
        van_ban = re.sub(rf"(?<![\w]){re.escape(tu)}(?![\w])", doc, van_ban, flags=re.IGNORECASE)
    return van_ban


def goi_tts(khoa, model, giong, van_ban, thu_lai=4):
    body = {"contents": [{"parts": [{"text": van_ban}]}],
            "generationConfig": {"responseModalities": ["AUDIO"],
                                 "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": giong}}}}}
    req = urllib.request.Request(f"{API}/models/{model}:generateContent", data=json.dumps(body).encode(),
                                 headers={"x-goog-api-key": khoa, "Content-Type": "application/json"})
    for lan in range(1, thu_lai + 1):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                kq = json.load(r)
            phan = kq["candidates"][0]["content"]["parts"][0]["inlineData"]
            return base64.b64decode(phan["data"]), phan.get("mimeType", ""), kq.get("usageMetadata", {})
        except urllib.error.HTTPError as e:
            nd = e.read().decode(errors="replace")
            het_ngay = e.code == 429 and "PerDay" in nd
            if e.code in (429, 500, 503) and not het_ngay and lan < thu_lai:
                time.sleep(15 * lan)
                continue
            sys.exit(f"HTTP {e.code} ({'hết hạn mức ngày' if het_ngay else 'lỗi'}): {nd[:500]}")
        except (KeyError, IndexError):
            if lan < thu_lai:
                time.sleep(5)
                continue
            sys.exit("Phản hồi không có âm thanh (có thể câu bị chặn hoặc model trả văn bản).")


def ra_pcm(du_lieu, mime):
    """Trả (mảng mẫu int16, tần số). Chấp nhận wav hoàn chỉnh hoặc PCM thô (audio/L16;rate=24000)."""
    if du_lieu[:4] == b"RIFF":
        import io
        with wave.open(io.BytesIO(du_lieu), "rb") as w:
            if w.getsampwidth() != 2 or w.getnchannels() != 1:
                sys.exit(f"Định dạng wav lạ: {w.getnchannels()} kênh, {w.getsampwidth() * 8} bit")
            a = array.array("h")
            a.frombytes(w.readframes(w.getnframes()))
            return a, w.getframerate()
    m = re.search(r"rate=(\d+)", mime)
    a = array.array("h")
    a.frombytes(du_lieu[: len(du_lieu) // 2 * 2])
    if sys.byteorder == "big":
        a.byteswap()
    return a, int(m.group(1)) if m else 24000


def cat_lang(a, fs, nguong=250):
    """Cắt khoảng lặng đầu/cuối, giữ LE_GIU giây mỗi đầu."""
    n = len(a)
    dau = next((i for i in range(n) if abs(a[i]) > nguong), 0)
    cuoi = next((i for i in range(n - 1, -1, -1) if abs(a[i]) > nguong), n - 1)
    le = int(LE_GIU * fs)
    return a[max(0, dau - le): min(n, cuoi + 1 + le)]


def luu_wav(duong_dan, a, fs):
    duong_dan.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(duong_dan), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(fs)
        w.writeframes(a.tobytes() if sys.byteorder == "little" else bytes(array.array("h", a)))


def doc_wav(duong_dan):
    with wave.open(str(duong_dan), "rb") as w:
        a = array.array("h")
        a.frombytes(w.readframes(w.getnframes()))
        return a, w.getframerate()


def ghi_so_chi_phi(model, ghi_chu, so_luong, usd):
    f = KIT / "ledger" / "chi-phi-api.csv"
    if not f.exists():
        return
    from datetime import datetime
    with open(f, "a", encoding="utf-8", newline="") as fh:
        csv.writer(fh).writerow([datetime.now().strftime("%Y-%m-%d"), DA.cfg.get("slug", DA.goc.name), "Google Gemini TTS", model,
                                 "giong doc " + ghi_chu, so_luong, f"{usd:.3f}", "uoc tinh tu usageMetadata"])


def doc_canh(c):
    jf = DA.loi_thoai / f"{c['tep_loi_thoai']}.json"
    if not jf.exists():
        sys.exit(f"Chưa có {jf.name}: chạy tach_kich_ban.py trước.")
    return json.loads(jf.read_text(encoding="utf-8"))["khoi"]


def chia_phan(khoi, n):
    """Chia danh sách khối thành n phần liên tiếp, chỉ cắt ở ranh giới đoạn, cân theo số ký tự."""
    if n <= 1:
        return [khoi]
    tong = sum(len(k["van_ban"]) for k in khoi)
    phan, hien, dem = [], [], 0
    for i, k in enumerate(khoi):
        hien.append(k)
        dem += len(k["van_ban"])
        sang_doan = i + 1 < len(khoi) and khoi[i + 1]["doan"] != k["doan"]
        if sang_doan and dem >= tong / n * (len(phan) + 1) - 1 and len(phan) < n - 1:
            phan.append(hien)
            hien = []
    if hien:
        phan.append(hien)
    return phan


def doc_phan(khoa, model, giong, khoi, bang):
    van_ban = "\n\n".join(ap_phat_am(k["van_ban"], bang) for k in khoi)
    du_lieu, mime, usage = goi_tts(khoa, model, giong, van_ban)
    pcm, fs = ra_pcm(du_lieu, mime)
    return cat_lang(pcm, fs), fs, len(van_ban), usage


def main():
    ap = argparse.ArgumentParser(description="Tạo giọng đọc mỗi cảnh một yêu cầu bằng Gemini TTS")
    ap.add_argument("--canh", nargs="*", help="chỉ các cảnh này (ví dụ canh1 canh3)")
    ap.add_argument("--ghi-de", action="store_true", help="đọc lại dù đã có")
    ap.add_argument("--chia", type=int, default=1, help="tách mỗi cảnh làm N yêu cầu (mặc định 1; tự tăng nếu âm thanh bị cắt)")
    ap.add_argument("--khoa-env", help="tên biến chứa khóa trong .env (mặc định GOOGLE_API_KEY), ví dụ GOOGLE_API_KEY_2")
    a = ap.parse_args()
    if not DA.cfg:
        sys.exit(f"Không thấy du-an.json (tìm từ {DA.goc}).")
    g = DA.cfg.get("giong", {})
    model, giong, am_luong = g.get("model", "gemini-3.8-flash-tts"), g.get("giong", "vi-vn-advisor-2"), float(g.get("am_luong", 1))
    bang = doc_bang_phat_am()
    khoa = lay_khoa(a.khoa_env)
    file_tl = DA.loi_thoai / "thoi-luong.json"
    thoi_luong = json.loads(file_tl.read_text(encoding="utf-8")) if file_tl.exists() else {}
    so_goi = tong_tok_am = tong_tok_chu = 0
    for c in DA.cfg["canh"]:
        if a.canh and c["id"] not in a.canh:
            continue
        out = DA.audio / f"{c['tep_loi_thoai']}.wav"
        if out.exists() and not a.ghi_de and c["id"] in thoi_luong.get("moi", []):
            print(f"{c['id']}: đã có, bỏ qua")
            continue
        khoi = doc_canh(c)
        n = max(1, a.chia)
        while True:
            mau, fs, ky_tu = array.array("h"), None, 0
            for phan in chia_phan(khoi, n):
                print(f"  {c['id']}: đọc {len(phan)} khối ({sum(len(k['van_ban']) for k in phan)} ký tự)...", flush=True)
                pcm, f, kt, usage = doc_phan(khoa, model, giong, phan, bang)
                fs = fs or f
                if mau:
                    mau.extend([0] * int(0.3 * fs))   # chỗ nối hai yêu cầu: nghỉ 0,3 giây như một dấu chấm
                mau.extend(pcm)
                ky_tu += kt
                so_goi += 1
                tong_tok_am += int(usage.get("candidatesTokenCount", len(pcm) / f * 25))
                tong_tok_chu += int(usage.get("promptTokenCount", 0))
            giay = len(mau) / fs
            toc_do = ky_tu / giay   # ký tự mỗi giây; giọng này khoảng 13 đến 20
            if toc_do > 24 and n < 4 and not a.chia > 1:
                print(f"  {c['id']}: âm thanh ngắn bất thường ({giay:.0f} giây cho {ky_tu} ký tự), thử tách làm {n + 1} yêu cầu")
                n += 1
                continue
            break
        if am_luong != 1:
            mau = array.array("h", (max(-32768, min(32767, int(x * am_luong))) for x in mau))
        luu_wav(out, mau, fs)
        thoi_luong[c["id"]] = round(giay, 2)
        thoi_luong.setdefault("moi", [])
        if c["id"] not in thoi_luong["moi"]:
            thoi_luong["moi"].append(c["id"])
        file_tl.write_text(json.dumps(thoi_luong, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{c['id']}: {giay:6.1f} giây, {ky_tu} ký tự ({toc_do:.1f} ký tự/giây) -> {out.relative_to(DA.goc)}")
    tong = sum(v for k, v in thoi_luong.items() if k != "moi")
    print(f"Tổng {tong:.1f} giây ({tong / 60:.1f} phút).")
    if so_goi:
        usd = tong_tok_am / 1e6 * GIA_USD_TRIEU_TOKEN_AM_THANH + tong_tok_chu / 1e6 * GIA_USD_TRIEU_TOKEN_CHU
        print(f"Đã gọi API {so_goi} lần, ~{tong_tok_am} token âm thanh, ước tính ${usd:.3f}")
        ghi_so_chi_phi(model, "moi canh mot yeu cau", so_goi, usd)


if __name__ == "__main__":
    main()
