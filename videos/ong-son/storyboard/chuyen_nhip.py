#!/usr/bin/env python3
"""Tính bảng co giãn thời gian cho từng đoạn khi giọng đọc đổi: ghép mốc CŨ của từng nhịp (theo giọng cũ trong storyboard/cu/) với mốc MỚI
(theo giọng hiện tại), ghi video/compositions/src/<id>.warp.json = {"pts": [[giây_cũ, giây_mới], ...]} (giây trong đoạn).
build_canh.py đọc file này và dịch mọi vị trí tween của đoạn theo đường gấp khúc đó, nên không phải sửa tay 35 file.

    python3 storyboard/tao_storyboard.py     # trước: sinh doan mới trong du-an.json
    python3 storyboard/chuyen_nhip.py        # rồi: bảng co giãn
    python3 ../../VideoKit/scripts/build_index.py && cd video && python3 ../../../VideoKit/scripts/build_canh.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tao_storyboard as T  # noqa: E402

DA = T.DA
CU = DA / "storyboard" / "cu"
doan_cu = json.load(open(CU / "doan-cu.json", encoding="utf-8"))
moc_cu = {r["id"]: r for r in json.load(open(CU / "moc-canh.json", encoding="utf-8"))}
cfg = json.load(open(DA / "du-an.json", encoding="utf-8"))
moc_moi = {r["id"]: r for r in json.load(open(T.AUD / "moc-canh.json", encoding="utf-8"))}


def nhip_theo_doan(cn, nd):
    """Mốc từng nhịp theo từng đoạn của cảnh (None nếu không tìm thấy cụm)."""
    pos, ket = 0, []
    for dm in nd["doan"]:
        ds = []
        for neo, _ in dm["nhip"]:
            try:
                t = cn.tim(neo, pos)
                pos = max(pos, cn.dau + 1)
            except SystemExit:
                t = None
            ds.append(t)
        ket.append(ds)
    return ket


def main():
    tong = 0
    for c in cfg["canh"]:
        nd = T.CANH[c["id"]]
        cu, moi = doan_cu[c["id"]], c["doan"]
        cn_cu = T.Canh(c, CU / "words")
        cn_moi = T.Canh(c, kep_theo_khoi=True)
        beats_cu, beats_moi = nhip_theo_doan(cn_cu, nd), nhip_theo_doan(cn_moi, nd)
        dur_cu, dur_moi = moc_cu[c["id"]]["duration"], moc_moi[c["id"]]["duration"]
        for j, d in enumerate(moi):
            if d["id"] == "c5-chot" and (CU / "c5-chot-nhip.json").exists():
                # đoạn dựng theo bản giọng một mạch: mốc cũ lấy từ gói lúc dựng
                cc = json.load(open(CU / "c5-chot-nhip.json"))
                ket_moi = dur_moi
                pts = [(0.0, 0.0)]
                for tc, tm in zip(cc["nhip"], beats_moi[j]):
                    if tm is None:
                        continue
                    n = tm - d["bat_dau"]
                    if tc > pts[-1][0] + 0.05 and n > pts[-1][1] + 0.05 and tc < cc["thoi_luong"] - 0.1 and n < ket_moi - d["bat_dau"] - 0.1:
                        pts.append((round(tc, 3), round(n, 3)))
                pts.append((cc["thoi_luong"], round(ket_moi - d["bat_dau"], 3)))
                (DA / "video/compositions/src" / "c5-chot.warp.json").write_text(json.dumps({"pts": [list(p) for p in pts]}), encoding="utf-8")
                print(f"c5-chot: {pts[-1][0]:.1f}s -> {pts[-1][1]:.1f}s, {len(pts) - 1} điểm neo (từ bản một mạch)")
                tong += 1
                continue
            if j >= len(cu) or cu[j]["id"] != d["id"]:
                print(f"{d['id']}: đoạn mới, không co giãn")
                continue
            bd_cu, bd_moi = cu[j]["bat_dau"], d["bat_dau"]
            ket_cu = cu[j + 1]["bat_dau"] if j + 1 < len(cu) else dur_cu
            ket_moi = moi[j + 1]["bat_dau"] if j + 1 < len(moi) and j + 1 < len(cu) else dur_moi
            if j + 1 < len(moi) and j + 1 >= len(cu):
                ket_moi = moi[j + 1]["bat_dau"]   # sau đoạn này có đoạn mới thêm: đoạn này kết thúc ở đó
            pts = [(0.0, 0.0)]
            for tc, tm in zip(beats_cu[j], beats_moi[j]):
                if tc is None or tm is None:
                    continue
                o, n = tc - bd_cu, tm - bd_moi
                if o > pts[-1][0] + 0.05 and n > pts[-1][1] + 0.05 and o < ket_cu - bd_cu - 0.1 and n < ket_moi - bd_moi - 0.1:
                    pts.append((round(o, 3), round(n, 3)))
            # đuôi 0,6 giây cuối đoạn giữ nguyên tỉ lệ 1:1 (các chuyển động kết đoạn không bị kéo giãn qua khoảng nghỉ thêm vào cuối)
            o_e, n_e = ket_cu - bd_cu, ket_moi - bd_moi
            if o_e - 0.6 > pts[-1][0] + 0.2 and n_e - 0.6 > pts[-1][1] + 0.2:
                pts.append((round(o_e - 0.6, 3), round(n_e - 0.6, 3)))
            pts.append((round(o_e, 3), round(n_e, 3)))
            out = DA / "video/compositions/src" / f"{d['id']}.warp.json"
            out.write_text(json.dumps({"pts": [list(p) for p in pts]}), encoding="utf-8")
            tong += 1
            print(f"{d['id']}: {pts[-1][0]:.1f}s -> {pts[-1][1]:.1f}s, {len(pts) - 1} điểm neo")
    print(f"Đã ghi {tong} bảng co giãn")


if __name__ == "__main__":
    main()
