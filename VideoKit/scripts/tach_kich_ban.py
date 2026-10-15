#!/usr/bin/env python3
"""Tách lời thoại từ kịch bản: mỗi `**[Lời dẫn]**` thành một khối đọc riêng (chỉ dùng thư viện chuẩn).

    cd videos/<du-an> && python3 ../../VideoKit/scripts/tach_kich_ban.py

Đọc kich-ban/canh-N-*.md theo `canh[].tep_kich_ban` trong du-an.json, ghi `loi-thoai/<tep_loi_thoai>.json`:
  {"canh": "canh1", "khoi": [{"id": "canh1-d1-k1", "doan": 1, "tieu_de": "...", "van_ban": "...", "dung_sau_giay": 2.0}, ...]}
và `loi-thoai/<tep_loi_thoai>.txt` (lời dẫn thuần, để đọc lại bằng mắt).

`**[Dừng N giây]**` đứng ngay sau một lời dẫn thành `dung_sau_giay` của khối đó (cộng dồn nếu có nhiều dòng Dừng liên tiếp).
Dừng đứng trước mọi lời dẫn của cảnh thành `dung_dau_giay` của cảnh. Chữ trong ngoặc “ ” là lời đọc; không đọc mô tả hình và code.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _du_an import du_an  # noqa: E402

DA = du_an()

RE_DOAN = re.compile(r"^##\s*Đoạn\s*(\d+)\s*:\s*(.*?)\s*(?:\(\s*[\d,.]+\s*giây\s*\))?\s*$")
RE_LOI = re.compile(r"^\*\*\[Lời dẫn\]\*\*\s*(.*)$")
RE_DUNG = re.compile(r"^\*\*\[Dừng\s*([\d.,]+)\s*giây\]\*\*")


def lam_sach(s):
    s = s.strip()
    s = re.sub(r"^[“\"]|[”\"]$", "", s)
    return re.sub(r"\s+", " ", s).strip()


def tach(text, canh_id):
    khoi, dung_dau = [], 0.0
    doan, tieu_de, k_trong_doan, phan = 0, "", 0, 0
    dang_loi = None   # lời dẫn có thể kéo dài nhiều dòng cho tới dòng trống
    for dong in text.splitlines():
        if dong.startswith("## "):
            phan += 1   # mọi tiêu đề ## (đoạn hoặc chốt cảnh) mở một phần mới; ghép giọng dùng nó để chọn khoảng nghỉ sang phần mới
        m = RE_DOAN.match(dong)
        if m:
            doan, tieu_de, k_trong_doan = int(m.group(1)), m.group(2), 0
            dang_loi = None
            continue
        m = RE_LOI.match(dong)
        if m:
            k_trong_doan += 1
            dang_loi = {"id": f"{canh_id}-d{doan}-k{k_trong_doan}", "doan": doan, "tieu_de": tieu_de, "phan": phan, "van_ban": m.group(1), "dung_sau_giay": 0.0}
            khoi.append(dang_loi)
            continue
        m = RE_DUNG.match(dong)
        if m:
            giay = float(m.group(1).replace(",", "."))
            if khoi:
                khoi[-1]["dung_sau_giay"] = round(khoi[-1]["dung_sau_giay"] + giay, 2)
            else:
                dung_dau += giay
            dang_loi = None
            continue
        if dang_loi is not None and dong.strip() and not dong.startswith(("*", "#", "|", "`")):
            dang_loi["van_ban"] += " " + dong
        else:
            dang_loi = None
    for k in khoi:
        k["van_ban"] = lam_sach(k["van_ban"])
    return khoi, round(dung_dau, 2)


def main():
    if not DA.cfg:
        sys.exit(f"Không thấy du-an.json (tìm từ {DA.goc}).")
    DA.loi_thoai.mkdir(parents=True, exist_ok=True)
    tong_khoi = tong_ky_tu = 0
    for c in DA.cfg["canh"]:
        f = DA.goc / DA.cfg.get("thu_muc", {}).get("kich_ban", "kich-ban") / c["tep_kich_ban"]
        khoi, dung_dau = tach(f.read_text(encoding="utf-8"), c["id"])
        if not khoi:
            print(f"CẢNH {c['id']}: không có lời dẫn nào trong {f.name}")
            continue
        out = {"canh": c["id"], "ten": c["ten"], "dung_dau_giay": dung_dau, "khoi": khoi}
        (DA.loi_thoai / f"{c['tep_loi_thoai']}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
        (DA.loi_thoai / f"{c['tep_loi_thoai']}.txt").write_text("\n\n".join(k["van_ban"] for k in khoi) + "\n", encoding="utf-8")
        ky_tu = sum(len(k["van_ban"]) for k in khoi)
        dung = sum(k["dung_sau_giay"] for k in khoi) + dung_dau
        print(f"{c['id']}: {len(khoi):2d} khối, {ky_tu:5d} ký tự, dừng có chủ đích {dung:4.1f}s")
        tong_khoi += len(khoi)
        tong_ky_tu += ky_tu
    print(f"Tổng: {tong_khoi} khối, {tong_ky_tu} ký tự (ước lượng ~{tong_ky_tu / 16.5 / 60:.1f} phút giọng đọc, chưa tính dừng)")


if __name__ == "__main__":
    main()
