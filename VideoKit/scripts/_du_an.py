"""Tìm thư mục dự án video cho mọi script của VideoKit.

Thứ tự: biến VIDEOKIT_PROJECT, nếu không có thì thư mục hiện tại; nếu ở đó (hoặc thư mục cha gần nhất) có `du-an.json`
thì đọc đường dẫn từ file đó; nếu không thì dùng bố cục chuẩn mặc định (video/, loi-thoai/).
Có thể ghi đè từng đường dẫn bằng VIDEOKIT_VIDEO và VIDEOKIT_LOI_THOAI.
"""
import json
import os
from pathlib import Path
from types import SimpleNamespace

KIT = Path(__file__).resolve().parent.parent


def tim_goc():
    bat_dau = Path(os.environ.get("VIDEOKIT_PROJECT") or Path.cwd()).resolve()
    for p in [bat_dau, *bat_dau.parents]:
        if (p / "du-an.json").exists():
            return p
    return bat_dau


def du_an():
    goc = tim_goc()
    cfg_file = goc / "du-an.json"
    cfg = json.loads(cfg_file.read_text(encoding="utf-8")) if cfg_file.exists() else {}
    td = cfg.get("thu_muc", {})
    if cfg:
        video = goc / td.get("video", "video")
        loi = goc / td.get("loi_thoai", "loi-thoai")
    else:
        video = goc / "video"
        loi = goc / "loi-thoai"
    if os.environ.get("VIDEOKIT_VIDEO"):
        video = Path(os.environ["VIDEOKIT_VIDEO"])
    if os.environ.get("VIDEOKIT_LOI_THOAI"):
        loi = Path(os.environ["VIDEOKIT_LOI_THOAI"])
    return SimpleNamespace(
        goc=goc, cfg=cfg, video=video, loi_thoai=loi,
        audio=video / "assets" / "audio", images=video / "assets" / "images",
        frames=video / "compositions" / "frames", thumbnail=goc / td.get("thumbnail", "thumbnail"),
    )
