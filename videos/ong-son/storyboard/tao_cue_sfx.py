#!/usr/bin/env python3
"""Sinh video/compositions/frames/<id>.sfx.json cho từng đoạn từ các gói storyboard (storyboard/goi/<id>.md).

Mỗi nhịp hình trong gói thành tối đa một cue; loại âm chọn theo từ khoá trong mô tả nhịp (rơi/cạch → thud, bay/dán → whoosh/click,
dấu tích/đúng → ding, dấu X/sai → error, đếm/sáng dòng → tick, hiện/bật → pop, gõ → type). `t` là giây từ đầu đoạn,
đúng mốc nhịp trong gói. `tao_sfx.py` tự lọc thưa theo độ ưu tiên. Chạy sau tao_storyboard.py:

    python3 storyboard/tao_cue_sfx.py && python3 ../../VideoKit/scripts/tao_sfx.py
"""
import json
import re
from pathlib import Path

DA = Path(__file__).resolve().parent.parent
RE = re.compile(r"^- \*\*([\d.]+)s\*\* \(“(.*?)”\) — (.*)$")


def loai_cue(mo_ta):
    s = mo_ta.lower()
    if "rơi" in s and "gạch" in s:
        return "thud", 0.4, 1.0
    if "bay" in s and ("ô " in s and "kệ" in s):
        return "click", 0.9, 1.0
    if "dấu x" in s or "gạch chéo" in s or "sai" in s.split() or "lỗi" in s:
        return "error", 0.2, 0.9
    if "dấu tích" in s or "đúng" in s.split() or "✓" in s:
        return "ding", 0.3, 0.9
    if "dán" in s or "nhãn" in s and "bay" in s:
        return "click", 0.7, 1.0
    if "gõ" in s:
        return "type", 0.0, 1.0
    if "đếm" in s:
        return "tick", 0.0, 0.9
    if "bay" in s or "trượt" in s or "lật" in s or "zoom" in s or "lùi" in s or "phóng" in s:
        return "whoosh", 0.0, 0.8
    if "sáng" in s:
        return "tick", 0.0, 0.8
    if "hiện" in s or "bật" in s or "pop" in s:
        return "pop", 0.0, 0.9
    return None


def main():
    tong = 0
    for md in sorted((DA / "storyboard/goi").glob("*.md")):
        id_ = md.stem
        cues = []
        for dong in md.read_text(encoding="utf-8").splitlines():
            m = RE.match(dong)
            if not m:
                continue
            t, neo, mo_ta = float(m.group(1)), m.group(2), m.group(3)
            r = loai_cue(mo_ta)
            if not r:
                continue
            loai, dt, gain = r
            c = {"t": round(t + dt, 2), "type": loai, "gain": gain, "note": neo}
            if loai == "type":
                c["d"] = 2.5
            cues.append(c)
        out = DA / "video/compositions/frames" / f"{id_}.sfx.json"
        out.write_text(json.dumps({"scene": id_, "cues": cues}, ensure_ascii=False, indent=1), encoding="utf-8")
        tong += len(cues)
    print(f"{tong} cue cho {len(list((DA / 'storyboard/goi').glob('*.md')))} đoạn")


main()
