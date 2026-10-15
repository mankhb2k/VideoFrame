#!/usr/bin/env python3
"""Tạo dự án video mới từ khuôn VideoKit/templates/du-an (chỉ dùng thư viện chuẩn).

    python3 VideoKit/scripts/tao_du_an.py ong-son --ten "Ông Sơn: từ tiệm tạp hoá đến phần mềm triệu đô" \\
        --kich-ban kich-ban-video-ong-son --di-chuyen \\
        --thong-diep "..." --khan-gia "người mới học lập trình"

Kết quả (mặc định ở <repo>/videos/<slug>/): du-an.json, kich-ban/, loi-thoai/, video/ (dự án HyperFrames),
renders/, thumbnail/, dang-bai/; font, logo và thư viện sfx đã được chép vào video/assets; index.html đã sinh.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _du_an import KIT  # noqa: E402

PHIEN_BAN_HYPERFRAMES = "0.8.152"


def khong_dau(s):
    s = unicodedata.normalize("NFD", s.replace("đ", "d").replace("Đ", "D"))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn").lower()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s)).strip("-")


def doc_canh(thu_muc):
    """Đọc các file canh-N-*.md: lấy số, tên cảnh, ước lượng độ dài giọng từ số ký tự lời dẫn (~16,5 ký tự/giây)."""
    ds = []
    for f in sorted(Path(thu_muc).glob("canh-*.md"), key=lambda p: int(re.search(r"canh-(\d+)", p.name).group(1))):
        s = f.read_text(encoding="utf-8")
        n = int(re.search(r"canh-(\d+)", f.name).group(1))
        m = re.match(r"#\s*Cảnh\s*\d+\s*:\s*(.+)", s)
        ten = m.group(1).strip() if m else f.stem
        ky_tu = sum(len(x) for x in re.findall(r"\*\*\[Lời dẫn\]\*\*\s*“(.*?)”", s, flags=re.S))
        ds.append({"id": f"canh{n}", "ten": ten, "tep_kich_ban": f.name, "tep_loi_thoai": f"canh{n}_{khong_dau(ten)}",
                   "du_kien_giay": max(10, round(ky_tu / 16.5)), "giu_them_giay": 0})
    return ds


def dien(s, thay):
    for k, v in thay.items():
        s = s.replace("{{" + k + "}}", v)
    return s


def main():
    ap = argparse.ArgumentParser(description="Tạo dự án video mới từ khuôn")
    ap.add_argument("slug", help="tên ngắn không dấu, ví dụ ong-son")
    ap.add_argument("--ten", help="tên hiển thị của video")
    ap.add_argument("--thu-muc-cha", default=str(KIT.parent / "videos"))
    ap.add_argument("--kich-ban", help="thư mục chứa các file canh-N-*.md để đưa vào dự án")
    ap.add_argument("--di-chuyen", action="store_true", help="chuyển (thay vì chép) kịch bản vào dự án")
    ap.add_argument("--thong-diep", default="<một câu: điều video phải truyền đạt>")
    ap.add_argument("--khan-gia", default="<người xem là ai>")
    ap.add_argument("--y-tuong", default="<ý tưởng hình ảnh xuyên suốt>")
    ap.add_argument("--y-dinh", default="<video này là gì, cho ai, giọng điệu>")
    ap.add_argument("--giong", default="vi-vn-advisor-2")
    ap.add_argument("--model", default="gemini-3.8-flash-tts")
    ap.add_argument("--chu-de", choices=["sang", "toi"], default="sang", help="nền sáng (mặc định, video học thuật) hoặc nền tối")
    a = ap.parse_args()

    slug = khong_dau(a.slug)
    dich = Path(a.thu_muc_cha) / slug
    if dich.exists():
        sys.exit(f"Đã có {dich}; chọn slug khác hoặc xóa thư mục cũ.")
    shutil.copytree(KIT / "templates" / "du-an", dich)

    ten = a.ten or slug
    thay = {"slug": slug, "ten": ten, "ngay": datetime.now().strftime("%Y-%m-%d"), "hyperframes": PHIEN_BAN_HYPERFRAMES,
            "thong_diep": a.thong_diep, "khan_gia": a.khan_gia, "y_tuong": a.y_tuong, "y_dinh": a.y_dinh,
            "giong": a.giong, "model": a.model}
    for f in ["README.md", "video/package.json", "video/BRIEF.md", "video/STORYBOARD.md"]:
        p = dich / f
        p.write_text(dien(p.read_text(encoding="utf-8"), thay), encoding="utf-8")

    canh = []
    if a.kich_ban:
        nguon = Path(a.kich_ban)
        canh = doc_canh(nguon)
        for c in canh:
            (shutil.move if a.di_chuyen else shutil.copy2)(str(nguon / c["tep_kich_ban"]), str(dich / "kich-ban" / c["tep_kich_ban"]))
        if a.di_chuyen and not any(nguon.iterdir()):
            nguon.rmdir()

    cfg = {
        "slug": slug, "ten": ten, "tao_ngay": thay["ngay"], "phien_ban_hyperframes": PHIEN_BAN_HYPERFRAMES,
        "khung": {"rong": 1920, "cao": 1080, "fps_nhap": 30, "fps_cuoi": 60, "chu_de": a.chu_de},
        "thu_muc": {"kich_ban": "kich-ban", "loi_thoai": "loi-thoai", "video": "video", "thumbnail": "thumbnail"},
        "giong": {"nha_cung_cap": "gemini", "model": a.model, "giong": a.giong, "do_tre_giay": 0.3, "am_luong": 1},
        "logo": {"hien": True, "file": "assets/images/logo-tron.png", "vi_tri": "phai-duoi", "kich_thuoc": 132, "le": 44},
        "sfx": {"track": "assets/audio/sfx-track.wav", "am_luong": 0.65},
        "canh": canh,
    }
    (dich / "du-an.json").write_text(json.dumps(cfg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (dich / "video" / "meta.json").write_text(json.dumps({"id": slug, "name": slug, "createdAt": datetime.now().isoformat()}, indent=2) + "\n", encoding="utf-8")

    env = {"VIDEOKIT_PROJECT": str(dich)}
    import os
    chay = lambda *args: subprocess.run([sys.executable, *args], env={**os.environ, **env}, check=True)  # noqa: E731
    chay(str(KIT / "scripts" / "sync_assets.py"), "--project", str(dich / "video"), "--fonts", "--logo", "--sfx")
    chay(str(KIT / "scripts" / "build_index.py"))

    print(f"\nĐã tạo dự án: {dich}")
    print("Việc tiếp theo:")
    print("  1. Điền video/BRIEF.md (thông điệp, khán giả) nếu còn chỗ <...>")
    print("  2. Tách lời thoại từ kịch bản -> loi-thoai/, rồi tạo giọng đọc và mốc từng từ")
    print("  3. Chạy lại build_index.py sau khi có giọng đọc để chốt độ dài từng cảnh")


if __name__ == "__main__":
    main()
