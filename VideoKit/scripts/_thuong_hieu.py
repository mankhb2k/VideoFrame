"""Đọc hệ thống màu THO CODE theo chế độ (sang hoặc toi). Lớp .th-* luôn lấy từ thuong-hieu.css; chế độ tối chỉ thay khối :root."""
import re
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
TPL = KIT / "templates"


def doc_css(chu_de="sang"):
    css = (TPL / "thuong-hieu.css").read_text(encoding="utf-8")
    if chu_de == "toi":
        toi = (TPL / "thuong-hieu-toi.css").read_text(encoding="utf-8")
        css = re.sub(r":root \{.*?\n\}", lambda m: re.search(r":root \{.*?\n\}", toi, re.S).group(0), css, count=1, flags=re.S)
    return css


def lay_bien(css):
    return {k: v.upper() for k, v in re.findall(r"--([a-z0-9-]+):\s*(#[0-9A-Fa-f]{6})", css)}
