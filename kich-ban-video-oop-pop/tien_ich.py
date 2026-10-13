"""Hàm dùng chung cho các script tạo giọng đọc (không cần cài thêm thư viện)."""
import csv
import re
import wave
from pathlib import Path

THU_MUC_GOC = Path(__file__).resolve().parent
THU_MUC_LOI_THOAI = THU_MUC_GOC / "loi-thoai"
THU_MUC_DAU_RA = THU_MUC_GOC / "dau-ra"


def doc_cac_canh(thu_muc=None, chi_canh=None):
    """Trả về danh sách (ten_canh, [doan_van, ...]) theo thứ tự canh0, canh1, ...

    Mỗi file canh*.txt gồm các đoạn cách nhau bằng một dòng trống.
    chi_canh: chuỗi như "canh3" để chỉ lấy một cảnh.
    """
    thu_muc = Path(thu_muc) if thu_muc else THU_MUC_LOI_THOAI
    ket_qua = []
    for f in sorted(thu_muc.glob("canh*.txt")):
        ten = f.stem
        if chi_canh and not ten.startswith(chi_canh):
            continue
        doan = [d.strip() for d in f.read_text(encoding="utf-8").split("\n\n") if d.strip()]
        ket_qua.append((ten, doan))
    return ket_qua


def gop_wav(danh_sach_file, file_ra, nghi_giay=0.4):
    """Ghép nhiều file wav cùng định dạng thành một file, chèn khoảng lặng giữa các đoạn."""
    danh_sach_file = [Path(f) for f in danh_sach_file]
    if not danh_sach_file:
        return None
    with wave.open(str(danh_sach_file[0]), "rb") as w0:
        thong_so = w0.getparams()
    khung_lang = int(thong_so.framerate * nghi_giay)
    byte_lang = b"\x00" * (khung_lang * thong_so.nchannels * thong_so.sampwidth)
    with wave.open(str(file_ra), "wb") as out:
        out.setnchannels(thong_so.nchannels)
        out.setsampwidth(thong_so.sampwidth)
        out.setframerate(thong_so.framerate)
        for i, f in enumerate(danh_sach_file):
            with wave.open(str(f), "rb") as w:
                if w.getparams()[:3] != thong_so[:3]:
                    raise ValueError(f"{f.name} khác định dạng (kênh/độ sâu/tần số) so với file đầu")
                out.writeframes(w.readframes(w.getnframes()))
            if i < len(danh_sach_file) - 1:
                out.writeframes(byte_lang)
    return Path(file_ra)


def ap_dung_phat_am(van_ban, file_csv=None):
    """Thay các từ tiếng Anh bằng cách viết gần phát âm tiếng Việt (theo bang-phat-am.csv).

    Thay theo từ nguyên vẹn, không phân biệt hoa thường, từ dài thay trước từ ngắn.
    """
    file_csv = Path(file_csv) if file_csv else THU_MUC_LOI_THOAI / "bang-phat-am.csv"
    with open(file_csv, encoding="utf-8", newline="") as f:
        cap = [(r["tu_goc"], r["viet_lai_cho_tts"]) for r in csv.DictReader(f)]
    cap.sort(key=lambda c: len(c[0]), reverse=True)
    for goc, moi in cap:
        van_ban = re.sub(r"(?<![\w-])" + re.escape(goc) + r"(?![\w-])", moi, van_ban, flags=re.IGNORECASE)
    return van_ban
