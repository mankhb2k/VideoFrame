#!/usr/bin/env python3
"""Ghép giọng từng khối (loi-thoai/khoi/<id>.wav) thành file giọng của từng cảnh với khoảng nghỉ chọn lại, KHÔNG gọi TTS (chỉ thư viện chuẩn).

    cd videos/<du-an>
    python3 ../../VideoKit/scripts/tach_kich_ban.py     # sinh loi-thoai/<canh>.json (khối, phần, dung_sau_giay)
    python3 ../../VideoKit/scripts/ghep_giong.py        # ghép mọi cảnh
    python3 ../../VideoKit/scripts/ghep_giong.py --canh canh3 --nghi-trong 0.3 --nghi-phan 0.5 --tran 1.2

Khoảng nghỉ SAU mỗi khối:
  - có `[Dừng N giây]`: nghỉ = bảng đổi (3 giây -> 1,2; 2 -> 0,9; 1,5 -> 0,8; giá trị khác nội suy), không vượt `--tran` (mặc định 1,2 giây);
  - khối cuối của một phần (đoạn hoặc chốt cảnh, trường `phan` đổi): `--nghi-phan` (mặc định 0,6 giây);
  - còn lại: `--nghi-trong` (mặc định 0,35 giây).
Các khối đã được cắt lặng thừa, chừa 0,12 giây mỗi đầu, nên khoảng nghỉ nghe được dài hơn số trên khoảng 0,24 giây.
Kết quả: <video>/assets/audio/<tep_loi_thoai>.wav (cùng định dạng với tao_giong_doc.py), loi-thoai/<tep>.moc-khoi.json (giây bắt đầu và kết thúc CHÍNH XÁC của từng khối trong file cảnh) và loi-thoai/nghi.json.
"""
import argparse
import array
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tao_giong_doc as G  # noqa: E402

DA = G.DA
BANG_DUNG = [(0.0, 0.35), (1.0, 0.7), (1.5, 0.8), (2.0, 0.9), (3.0, 1.2)]


def nghi_tu_dung(d, tran):
    """Đổi `[Dừng d giây]` của kịch bản thành khoảng nghỉ nghe được (nội suy theo BANG_DUNG)."""
    if d >= BANG_DUNG[-1][0]:
        return min(tran, BANG_DUNG[-1][1])
    for (x0, y0), (x1, y1) in zip(BANG_DUNG, BANG_DUNG[1:]):
        if x0 <= d <= x1:
            return min(tran, y0 + (y1 - y0) * (d - x0) / (x1 - x0))
    return BANG_DUNG[0][1]


def main():
    ap = argparse.ArgumentParser(description="Ghép giọng từng khối với khoảng nghỉ mới")
    ap.add_argument("--canh", nargs="*", help="chỉ các cảnh này")
    ap.add_argument("--nghi-trong", type=float, default=0.35)
    ap.add_argument("--nghi-phan", type=float, default=0.6)
    ap.add_argument("--tran", type=float, default=1.2, help="khoảng nghỉ lớn nhất (giây)")
    a = ap.parse_args()
    if not DA.cfg:
        sys.exit(f"Không thấy du-an.json (tìm từ {DA.goc}).")
    nghi_dung = {}
    for c in DA.cfg["canh"]:
        if a.canh and c["id"] not in a.canh:
            continue
        khoi = G.doc_canh(c)
        mau, fs, tong_nghi = array.array("h"), None, 0.0
        dung_ra, moc = [], []
        for i, k in enumerate(khoi):
            f = DA.loi_thoai / "khoi" / f"{k['id']}.wav"
            if not f.exists():
                sys.exit(f"Thiếu {f.relative_to(DA.goc)}: chưa có giọng khối này.")
            pcm, f_ = G.doc_wav(f)
            fs = fs or f_
            if f_ != fs:
                sys.exit(f"Tần số khác nhau trong {c['id']}: {f_} và {fs}")
            bat_dau = len(mau) / fs
            mau.extend(pcm)
            moc.append({"id": k["id"], "bat_dau": round(bat_dau, 3), "ket_thuc": round(len(mau) / fs, 3), "dung_sau_giay": 0.0})
            if i + 1 < len(khoi):
                if k.get("dung_sau_giay", 0) > 0:
                    sau = nghi_tu_dung(k["dung_sau_giay"], a.tran)
                elif khoi[i + 1].get("phan") != k.get("phan"):
                    sau = a.nghi_phan
                else:
                    sau = a.nghi_trong
                mau.extend([0] * int(sau * fs))
                moc[-1]["dung_sau_giay"] = round(sau, 3)
                tong_nghi += sau
                dung_ra.append({"id": k["id"], "nghi_sau_giay": round(sau, 2)})
        out = DA.audio / f"{c['tep_loi_thoai']}.wav"
        G.luu_wav(out, mau, fs)
        nghi_dung[c["id"]] = dung_ra
        (DA.loi_thoai / f"{c['tep_loi_thoai']}.moc-khoi.json").write_text(json.dumps(moc, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{c['id']}: {len(mau) / fs:6.1f} giây ({len(khoi)} khối, nghỉ chèn {tong_nghi:4.1f} giây) -> {out.relative_to(DA.goc)}")
    (DA.loi_thoai / "nghi.json").write_text(json.dumps(nghi_dung, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
