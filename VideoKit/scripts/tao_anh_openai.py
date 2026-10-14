#!/usr/bin/env python3
"""Tạo bộ ảnh nhân vật nền trong cho video bằng API ảnh của OpenAI (chỉ dùng thư viện chuẩn).

Khóa đọc từ OPENAI_API_KEY (biến môi trường hoặc file .env ở thư mục dự án); không in khóa ra.

    python3 VideoKit/scripts/tao_anh_openai.py                       # tạo mọi ảnh còn thiếu
    python3 VideoKit/scripts/tao_anh_openai.py --ten chim-se drone   # chỉ vài ảnh
    python3 VideoKit/scripts/tao_anh_openai.py --ten khi --ghi-de    # tạo lại ảnh đã có
    python3 VideoKit/scripts/tao_anh_openai.py --model gpt-image-2.5-sunburst --chat-luong high

Thứ tự: `khi` tạo từ chữ; mọi ảnh còn lại dùng ảnh khỉ làm tham chiếu phong cách (endpoint /v1/images/edits)
để cả bộ đồng nhất. Kết quả ghi vào <video>/assets/images/. Chạy lại sẽ bỏ qua ảnh đã có.
"""
import argparse
import base64
import json
import os
import sys
import time
import urllib.error
import urllib.request
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _du_an import KIT, du_an  # noqa: E402

DA = du_an()   # đường dẫn dự án: xem _du_an.py
GOC = DA.goc
DAU_RA = DA.images
API = "https://api.openai.com/v1/images"

# giá USD / 1M token (đầu vào chữ, đầu ra ảnh) theo trang giá OpenAI, dùng để ước tính chi phí
GIA = {"gpt-image-2.5-flare": (5.0, 30.0), "gpt-image-2.5-sunburst": (5.0, 30.0), "gpt-image-2": (5.0, 30.0),
       "gpt-image-1.5": (5.0, 32.0), "gpt-image-1": (5.0, 40.0), "gpt-image-1-mini": (2.0, 8.0)}

PHONG_CACH = (
    "Glossy cartoon vector illustration: smooth cel-shading with 2-3 tonal steps, soft white specular highlights "
    "on rounded surfaces, thin outline in a darker shade of each shape's own color (no black outline), large "
    "glossy expressive eyes with white catchlights, chubby rounded proportions, clean smooth edges, no textures. "
)
KHUNG = (
    " Single subject centered, full body visible with a small margin, no text, no ground, no cast shadow, "
    "no extra props, completely transparent background."
)
THAM_CHIEU = (
    "Use the reference image ONLY as a style guide (rendering style, shading, outline, eye style, proportions' "
    "roundness). Do not copy the reference character. Draw a new subject: "
)

# ten -> (che_do, prompt) ; che_do: "chu" = tạo từ chữ, "sua" = sửa ảnh khỉ, "style" = lấy khỉ làm tham chiếu phong cách
ANH = {
    "khi": ("chu", PHONG_CACH + "A cute baby monkey, full body, three-quarter view, standing in a playful slightly "
            "tilted pose, one arm hanging down with the open palm facing forward and empty, the other arm relaxed, "
            "curious slightly puzzled expression with round orange-brown eyes and a small open mouth. Warm brown "
            "fur, tan-pink face, ears and belly, curly tail." + KHUNG),
    "khi-cam-chuoi": ("sua", "Edit the reference image: keep the exact same monkey, identical proportions, colors, "
                      "face and art style. Only change: one raised fist now firmly grips a ripe yellow banana held "
                      "upright above its head, banana peel intact, fingers wrapped around the middle of the banana. "
                      "Keep the other hand and everything else the same. Completely transparent background, no ground, "
                      "no cast shadow."),
    "chuoi": ("style", THAM_CHIEU + PHONG_CACH + "a single ripe banana, gently curved, tilted about 20 degrees, small "
              "dark-brown stem and tip, warm yellow (#FBBF24) with a slightly darker yellow shaded side and a few "
              "thin brown speckles, with a cute tiny face-less simple look. No hands, peel not opened." + KHUNG),
    "chim-se": ("style", THAM_CHIEU + PHONG_CACH + "a cute plump sparrow standing on two thin legs, side view, wings "
                "folded. Brown streaked back (#9A6B3F), warm beige belly, small black bib under the beak, short "
                "light-beige beak, one big glossy eye with a white catchlight, curious alert expression." + KHUNG),
    "canh-cut": ("style", THAM_CHIEU + PHONG_CACH + "a cute penguin standing upright, three-quarter view, both "
                 "flippers held slightly out as if it just tried to flap and failed, sheepish embarrassed "
                 "expression, large glossy eyes. Slate blue-gray body (a light enough blue-gray, not black, so it "
                 "stays visible on a dark background), white belly, pale-beige beak and feet." + KHUNG),
    "drone": ("style", THAM_CHIEU + PHONG_CACH + "a cute toy-like quadcopter drone, three-quarter view from slightly "
              "above, rounded glossy body in white and light gray with slate-blue accents, four arms each with a "
              "clearly drawn static propeller (no motion blur), a small camera gimbal underneath that looks like a "
              "big friendly eye, short landing legs, one small blue indicator light. No red or green colors "
              "anywhere." + KHUNG),
}


def lay_khoa():
    if os.environ.get("OPENAI_API_KEY"):
        return os.environ["OPENAI_API_KEY"]
    for env in (GOC / ".env", GOC.parent / ".env"):
        if env.exists():
            for dong in env.read_text(encoding="utf-8").splitlines():
                ten, _, gt = dong.partition("=")
                if ten.strip() == "OPENAI_API_KEY" and gt.strip():
                    return gt.strip().strip("\"'")
    sys.exit("Không tìm thấy OPENAI_API_KEY (biến môi trường hoặc file .env).")


def multipart(truong, tep):
    ranh = uuid.uuid4().hex
    phan = []
    for k, v in truong.items():
        phan.append(f'--{ranh}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
    for k, (ten, noi_dung) in tep.items():
        phan.append((f'--{ranh}\r\nContent-Disposition: form-data; name="{k}"; filename="{ten}"\r\n'
                     f'Content-Type: image/png\r\n\r\n').encode() + noi_dung + b"\r\n")
    phan.append(f"--{ranh}--\r\n".encode())
    return b"".join(phan), f"multipart/form-data; boundary={ranh}"


def goi(khoa, model, chat_luong, che_do, prompt, tham_chieu):
    chung = {"model": model, "prompt": prompt, "size": "1024x1024", "quality": chat_luong,
             "background": "transparent", "output_format": "png", "n": 1}
    if che_do == "chu":
        du_lieu, loai = json.dumps(chung).encode(), "application/json"
        url = f"{API}/generations"
    else:
        du_lieu, loai = multipart({k: str(v) for k, v in chung.items()}, {"image[]": ("tham-chieu.png", tham_chieu)})
        url = f"{API}/edits"
    req = urllib.request.Request(url, data=du_lieu, headers={"Authorization": f"Bearer {khoa}", "Content-Type": loai})
    for lan in range(1, 4):
        try:
            with urllib.request.urlopen(req, timeout=400) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            noi_dung = e.read().decode(errors="replace")
            if e.code in (429, 500, 502, 503) and lan < 3:
                time.sleep(15 * lan)
                continue
            sys.exit(f"HTTP {e.code}: {noi_dung[:500]}")


def lam_dac(duong_dan):
    """Alpha của model 2.5 không chạm 255; đẩy phần gần đặc lên 255 và cắt phần quá nhạt. Bỏ qua nếu thiếu Pillow."""
    try:
        import numpy as np
        from PIL import Image
    except ImportError:
        return
    a = np.asarray(Image.open(duong_dan).convert("RGBA")).copy()
    al = a[..., 3].astype(np.float32)
    al = np.where(al >= 235, 255, np.where(al <= 6, 0, al))
    a[..., 3] = al.astype(np.uint8)
    Image.fromarray(a, "RGBA").save(duong_dan)


def main():
    ap = argparse.ArgumentParser(description="Tạo ảnh nhân vật nền trong bằng OpenAI")
    ap.add_argument("--ten", nargs="*", choices=list(ANH), help="chỉ các ảnh này (mặc định: tất cả)")
    ap.add_argument("--model", default="gpt-image-2.5-flare")
    ap.add_argument("--chat-luong", default="medium", choices=["low", "medium", "high"])
    ap.add_argument("--ghi-de", action="store_true", help="tạo lại cả ảnh đã có")
    ap.add_argument("--dau-ra", default=str(DAU_RA))
    args = ap.parse_args()

    khoa = lay_khoa()
    dau_ra = Path(args.dau_ra)
    dau_ra.mkdir(parents=True, exist_ok=True)
    tong = 0.0
    for ten in args.ten or list(ANH):
        che_do, prompt = ANH[ten]
        f = dau_ra / f"{ten}.png"
        if f.exists() and not args.ghi_de:
            print(f"bỏ qua {ten} (đã có)")
            continue
        tc = None
        if che_do != "chu":
            goc = dau_ra / "khi.png"
            if not goc.exists():
                sys.exit("Cần tạo `khi` trước (ảnh tham chiếu phong cách).")
            tc = goc.read_bytes()
        t0 = time.time()
        d = goi(khoa, args.model, args.chat_luong, che_do, prompt, tc)
        f.write_bytes(base64.b64decode(d["data"][0]["b64_json"]))
        lam_dac(f)
        u = d.get("usage", {})
        tin = (u.get("input_tokens_details") or {}).get("text_tokens", 0)
        gi_in, gi_out = GIA.get(args.model, (0, 0))
        phi = tin * gi_in / 1e6 + u.get("output_tokens", 0) * gi_out / 1e6
        tong += phi
        print(f"đã tạo {ten} ({time.time() - t0:.0f}s, ≈ ${phi:.3f})")
    print(f"Xong. Chi phí ước tính lần chạy này ≈ ${tong:.3f}. Thư mục: {dau_ra}")


if __name__ == "__main__":
    main()
