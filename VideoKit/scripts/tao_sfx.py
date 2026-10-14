#!/usr/bin/env python3
"""Tổng hợp thư viện hiệu ứng âm thanh bằng code và ghép thành một track khớp video.

    python VideoKit/scripts/tao_sfx.py --thu-vien   # chỉ ghi thư viện vào VideoKit/sfx/*.wav
    python VideoKit/scripts/tao_sfx.py              # thư viện + ghép track <video>/assets/audio/sfx-track.wav

Track được ghép từ các file my-video/compositions/frames/*.sfx.json (t tính theo giây từ đầu mỗi cảnh) và mốc bắt đầu
của từng cảnh lấy từ my-video/index.html (host-scene-N). Mọi âm đều tạo ra bằng sóng sin, nhiễu và bộ lọc, hạt giống
cố định nên kết quả giống nhau mỗi lần chạy, không dùng mẫu âm của bên thứ ba. Cần: numpy.
"""
import os
import sys
import argparse
import json
import re
import wave
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _du_an import KIT, du_an  # noqa: E402

DA = du_an()   # đường dẫn dự án: xem _du_an.py
GOC = DA.goc
VIDEO = DA.video   # thư mục dự án HyperFrames
SR = 48000
# mức cơ bản của từng loại (đỉnh tương đối trước khi nhân gain của cue); nhỏ để không át giọng đọc
MUC = {"whoosh": 0.30, "pop": 0.30, "tick": 0.22, "click": 0.40, "ding": 0.32, "error": 0.34,
       "glitch": 0.30, "thud": 0.38, "sparkle": 0.22, "type": 0.16}


def t_(d):
    return np.arange(int(SR * d)) / SR


def bien(x, a=0.002, r=None):
    """Bao biên độ: tấn công nhanh a giây, giữ phần còn lại (r = thời gian suy giảm cuối)."""
    n = len(x)
    env = np.ones(n)
    na = max(1, int(a * SR))
    env[:na] = np.linspace(0, 1, na)
    if r:
        nr = min(n, int(r * SR))
        env[-nr:] *= np.linspace(1, 0, nr)
    return x * env


def loc_thong_thap(x, fc):
    """Bộ lọc thông thấp một cực, fc có thể biến thiên theo thời gian (mảng)."""
    fc = np.broadcast_to(np.asarray(fc, dtype=np.float64), x.shape)
    a = 1 - np.exp(-2 * np.pi * fc / SR)
    y = np.empty_like(x)
    s = 0.0
    for i in range(len(x)):
        s += a[i] * (x[i] - s)
        y[i] = s
    return y


def loc_thong_cao(x, fc):
    return x - loc_thong_thap(x, fc)


def chuan(x, dinh=1.0):
    m = np.max(np.abs(x)) or 1.0
    return x / m * dinh


def whoosh(rng):
    d = 0.55
    t = t_(d)
    n = rng.standard_normal(len(t))
    fc = 250 + 3400 * np.sin(np.pi * np.clip(t / d, 0, 1)) ** 1.5
    y = n
    for _ in range(3):  # lọc ba tầng cho dốc 18 dB/oct, bớt tiếng xì ở dải cao
        y = loc_thong_thap(y, fc)
    y = loc_thong_cao(y, 180)
    return chuan(y * np.sin(np.pi * np.clip(t / d, 0, 1)) ** 2)


def pop(rng):
    d = 0.18
    t = t_(d)
    f = 250 + 520 * np.exp(-t * 38)
    ph = 2 * np.pi * np.cumsum(f) / SR
    y = np.sin(ph) * np.exp(-t * 26)
    y += 0.25 * rng.standard_normal(len(t)) * np.exp(-t * 300)
    return chuan(bien(y, 0.001))


def tick(rng):
    d = 0.05
    t = t_(d)
    n = loc_thong_cao(rng.standard_normal(len(t)), 2200) * np.exp(-t * 180)
    y = n + 0.6 * np.sin(2 * np.pi * 2100 * t) * np.exp(-t * 220)
    return chuan(bien(y, 0.0005))


def click(rng):
    d = 0.16
    t = t_(d)
    y = loc_thong_cao(rng.standard_normal(len(t)), 1800) * np.exp(-t * 400) * 0.9           # va chạm nhựa
    y += 0.7 * np.sin(2 * np.pi * 1180 * t) * np.exp(-t * 85)                                 # tiếng gõ
    y += 0.45 * np.sin(2 * np.pi * 2350 * t) * np.exp(-t * 130)
    y += 0.8 * np.sin(2 * np.pi * (160 - 60 * t / d) * t) * np.exp(-t * 55)                   # thân khối
    return chuan(bien(y, 0.0004))


def ding(rng):
    d = 0.9
    t = t_(d)
    y = np.zeros(len(t))
    for f, g, dec in [(1318.5, 1.0, 5.0), (1975.5, 0.6, 7.0), (2637, 0.25, 9.0), (3951, 0.12, 12.0)]:
        y += g * np.sin(2 * np.pi * f * t) * np.exp(-t * dec)
    return chuan(bien(y, 0.002))


def error(rng):
    d = 0.42
    t = t_(d)
    f = 120 - 30 * t / d
    y = np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * 0.5
    y += 0.5 * np.sign(np.sin(2 * np.pi * np.cumsum(f * 1.06) / SR))                          # lệch tông, nghe gắt
    y = loc_thong_thap(y, 900) * np.exp(-t * 7)
    y += 0.5 * np.sin(2 * np.pi * 70 * t) * np.exp(-t * 18)
    return chuan(bien(y, 0.001, 0.05))


def glitch(rng):
    d = 0.32
    n = int(SR * d)
    y = np.zeros(n)
    pos = 0
    while pos < n:
        ln = int(SR * rng.uniform(0.012, 0.05))
        seg = rng.standard_normal(ln)
        if rng.random() < 0.5:
            seg = np.sign(seg)
        k = int(rng.integers(8, 40))                  # giảm mẫu thô (bitcrush)
        seg = np.repeat(seg[::k], k)[:ln]
        so = min(len(seg), n - pos)
        y[pos:pos + so] += seg[:so] * rng.uniform(0.3, 1.0)
        pos += ln + int(SR * rng.uniform(0.0, 0.03))
    t = t_(d)
    y *= np.exp(-t * 6)
    return chuan(loc_thong_thap(loc_thong_cao(y, 400), 6000))


def thud(rng):
    d = 0.55
    t = t_(d)
    f = 48 + 60 * np.exp(-t * 14)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9)
    y += 0.5 * loc_thong_thap(rng.standard_normal(len(t)), 500) * np.exp(-t * 40)
    return chuan(bien(y, 0.001, 0.03))


def sparkle(rng):
    d = 0.5
    t = t_(d)
    y = np.zeros(len(t))
    for i, f in enumerate([2637, 3322, 3951, 5274, 6645]):
        t0 = i * 0.05
        m = t >= t0
        y[m] += np.sin(2 * np.pi * f * (t[m] - t0)) * np.exp(-(t[m] - t0) * 14) * (1 - 0.12 * i)
    return chuan(bien(y, 0.001))


def go(rng, d):
    """Một đoạn gõ phím nhẹ kéo dài d giây."""
    n = int(SR * d)
    y = np.zeros(n)
    t = 0.0
    while t < d - 0.03:
        k = tick(rng) * rng.uniform(0.5, 1.0)
        i = int(t * SR)
        so = min(len(k), n - i)
        y[i:i + so] += k[:so]
        t += rng.uniform(0.045, 0.14)
    return chuan(y)


TAO = {"whoosh": whoosh, "pop": pop, "tick": tick, "click": click, "ding": ding, "error": error,
       "glitch": glitch, "thud": thud, "sparkle": sparkle}


def ghi_wav(duong_dan, y):
    y = np.clip(y, -1, 1)
    with wave.open(str(duong_dan), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((y * 32767).astype(np.int16).tobytes())


def thu_vien():
    thu_muc = KIT / "sfx"   # thư viện dùng chung của VideoKit
    thu_muc.mkdir(parents=True, exist_ok=True)
    lib = {}
    for i, (ten, ham) in enumerate(TAO.items()):
        lib[ten] = ham(np.random.default_rng(1000 + i))
        ghi_wav(thu_muc / f"{ten}.wav", lib[ten] * MUC[ten])
    return lib


# độ ưu tiên (số nhỏ = quan trọng hơn), khoảng cách tối thiểu cùng loại (giây)
UU_TIEN = {"thud": 0, "click": 0, "error": 0, "glitch": 0, "ding": 1, "whoosh": 2, "sparkle": 3, "pop": 4, "tick": 5, "type": 9}
CACH_TOI_THIEU = {"pop": 1.3, "tick": 0.9, "sparkle": 2.0, "whoosh": 1.5, "type": 0.0}
HE_SO = {"pop": 0.7, "tick": 0.8, "type": 0.8}   # giảm thêm mức của các âm dày
TOI_DA_MOI_GIAY = 2                              # tối đa số âm phụ (ưu tiên >= 2) trong cửa sổ 1 giây


def lam_thua(cues):
    """Giữ các âm quan trọng, bỏ bớt pop/tick/sparkle dày để không át giọng đọc."""
    nhan = sorted(cues, key=lambda c: (UU_TIEN.get(c["type"], 9), c["t"]))
    giu = []
    for c in nhan:
        loai, t = c["type"], float(c["t"])
        cach = CACH_TOI_THIEU.get(loai, 0.1)
        if any(g["type"] == loai and abs(float(g["t"]) - t) < cach for g in giu):
            continue
        if UU_TIEN.get(loai, 9) >= 2 and loai != "type":
            gan = [g for g in giu if g["type"] != "type" and abs(float(g["t"]) - t) < 0.8]
            if len(gan) >= TOI_DA_MOI_GIAY:
                continue
        giu.append(c)
    return sorted(giu, key=lambda c: float(c["t"]))


def moc_canh():
    h = (VIDEO / "index.html").read_text(encoding="utf-8")
    ket_qua = {}
    for m in re.finditer(r'id="host-scene-(\d+)"[^>]*?data-start="([0-9.]+)"', h):
        ket_qua[int(m.group(1))] = float(m.group(2))
    tong = float(re.search(r'data-composition-id="main"[^>]*?data-duration="([0-9.]+)"', h).group(1))
    return ket_qua, tong


def ghep(lib):
    bat_dau, tong = moc_canh()
    track = np.zeros(int(SR * (tong + 1.0)))
    rng = np.random.default_rng(777)
    so_cue = 0
    for n in sorted(bat_dau):
        f = VIDEO / "compositions" / "frames"
        tep = [p for p in sorted(f.glob("*.sfx.json")) if json.loads(p.read_text(encoding="utf-8")).get("scene") == f"scene-{n}"]
        if not tep:
            print(f"scene-{n}: chưa có file .sfx.json, bỏ qua")
            continue
        goc = json.loads(tep[0].read_text(encoding="utf-8"))["cues"]
        cues = lam_thua(goc)
        for c in cues:
            loai = c["type"]
            if loai != "type" and loai not in lib:
                print("bỏ qua loại lạ:", loai)
                continue
            y = go(rng, float(c.get("d", 1.0))) if loai == "type" else lib[loai]
            y = y * MUC[loai] * float(c.get("gain", 1.0)) * HE_SO.get(loai, 1.0)
            i = int((bat_dau[n] + float(c["t"])) * SR)
            if i < 0 or i >= len(track):
                continue
            track[i:i + len(y)] += y[:len(track) - i]
            so_cue += 1
        print(f"scene-{n}: giữ {len(cues)}/{len(goc)} cue")
    dinh = np.max(np.abs(track))
    if dinh > 0.9:  # tránh vỡ tiếng khi nhiều âm chồng nhau
        track *= 0.9 / dinh
    ghi_wav(VIDEO / "assets" / "audio" / "sfx-track.wav", track)
    print(f"Tổng {so_cue} cue; đỉnh {dinh:.2f}; track dài {len(track) / SR:.1f} giây")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--thu-vien", action="store_true", help="chỉ ghi thư viện, không ghép track")
    args = ap.parse_args()
    lib = thu_vien()
    print("Đã ghi thư viện:", ", ".join(TAO), "+ type (gõ phím, tạo theo độ dài cue)")
    if not args.thu_vien:
        ghep(lib)


if __name__ == "__main__":
    main()
