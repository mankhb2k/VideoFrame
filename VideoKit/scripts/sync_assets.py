#!/usr/bin/env python3
"""Chép asset từ VideoKit vào một dự án video HyperFrames và ghi manifest (chỉ dùng thư viện chuẩn).

HyperFrames đọc asset theo đường dẫn tương đối trong dự án, nên VideoKit không dùng symlink mà chép theo nhu cầu.

    python VideoKit/scripts/sync_assets.py --characters khi chuoi --sfx --fonts --logo   # chạy trong thư mục dự án
    python VideoKit/scripts/sync_assets.py --project videos/ong-son/video --characters all --sfx
    python VideoKit/scripts/sync_assets.py --lietke            # xem VideoKit đang có gì

Đích: <project>/assets/images (nhân vật, logo), <project>/assets/sfx, <project>/assets/fonts.
Ghi <project>/assets/videokit-manifest.json: nguồn, đích và sha256 của từng file đã chép.
Chạy lại an toàn: file giống hệt thì bỏ qua, file khác thì cảnh báo và chỉ ghi đè khi có --ghi-de.
"""
import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _du_an import KIT, du_an  # noqa: E402


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def chep(nguon, dich, ghi_de, nhat_ky):
    dich.parent.mkdir(parents=True, exist_ok=True)
    trang_thai = "mới"
    if dich.exists():
        if sha(dich) == sha(nguon):
            trang_thai = "giữ nguyên"
        elif not ghi_de:
            print(f"  cảnh báo: {dich} khác bản trong VideoKit, bỏ qua (dùng --ghi-de để ghi đè)")
            return
        else:
            trang_thai = "ghi đè"
    if trang_thai != "giữ nguyên":
        shutil.copy2(nguon, dich)
    nhat_ky.append({"nguon": str(nguon.relative_to(KIT)), "dich": str(dich), "sha256": sha(nguon), "trang_thai": trang_thai})
    print(f"  {trang_thai:10} {nguon.relative_to(KIT)} -> {dich}")


def liet_ke():
    print("Nhân vật:", ", ".join(sorted(p.name for p in (KIT / "characters").iterdir() if p.is_dir())))
    print("Âm thanh:", ", ".join(sorted(p.stem for p in (KIT / "sfx").glob("*.wav"))))
    print("Font:", len(list((KIT / "brand" / "fonts").glob("*.woff2"))), "file woff2 (Be Vietnam Pro)")
    print("Logo:", ", ".join(p.name for p in (KIT / "brand").glob("logo*.png")))


def main():
    ap = argparse.ArgumentParser(description="Chép asset VideoKit vào dự án video")
    ap.add_argument("--project", default=None, help="thư mục dự án HyperFrames (chứa index.html); mặc định lấy từ du-an.json")
    ap.add_argument("--characters", nargs="*", default=[], help="tên nhân vật hoặc 'all'")
    ap.add_argument("--sfx", action="store_true", help="chép thư viện âm thanh")
    ap.add_argument("--fonts", action="store_true", help="chép font Be Vietnam Pro")
    ap.add_argument("--logo", action="store_true", help="chép logo và logo tròn")
    ap.add_argument("--ghi-de", action="store_true")
    ap.add_argument("--lietke", action="store_true")
    a = ap.parse_args()

    if a.lietke:
        liet_ke()
        return
    proj = Path(a.project) if a.project else du_an().video
    if not proj.exists():
        sys.exit(f"Không thấy thư mục dự án: {proj}")
    assets = proj / "assets"
    nhat_ky = []
    ten = [p.name for p in (KIT / "characters").iterdir() if p.is_dir()] if a.characters == ["all"] else a.characters
    for t in ten:
        d = KIT / "characters" / t
        if not d.exists():
            sys.exit(f"VideoKit chưa có nhân vật '{t}' (xem: --lietke)")
        for f in sorted(d.glob("*.png")):
            chep(f, assets / "images" / f.name, a.ghi_de, nhat_ky)
    if a.sfx:
        for f in sorted((KIT / "sfx").glob("*.wav")):
            chep(f, assets / "sfx" / f.name, a.ghi_de, nhat_ky)
    if a.fonts:
        for f in sorted((KIT / "brand" / "fonts").glob("*")):
            chep(f, assets / "fonts" / f.name, a.ghi_de, nhat_ky)
        print("  nhớ dán templates/font-face.css vào <style> của index.html và mỗi cảnh (HyperFrames yêu cầu @font-face trong từng file)")
    if a.logo:
        for f in sorted((KIT / "brand").glob("logo*.png")):
            chep(f, assets / "images" / f.name, a.ghi_de, nhat_ky)

    mf = assets / "videokit-manifest.json"
    cu = json.loads(mf.read_text(encoding="utf-8")) if mf.exists() else []
    gop = {m["dich"]: m for m in cu}
    gop.update({m["dich"]: m for m in nhat_ky})
    assets.mkdir(parents=True, exist_ok=True)
    mf.write_text(json.dumps(list(gop.values()), indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"Manifest: {mf} ({len(gop)} mục)")


if __name__ == "__main__":
    main()
