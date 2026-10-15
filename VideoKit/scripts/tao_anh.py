#!/usr/bin/env python3
"""Tạo bộ ảnh nhân vật, đạo cụ, nền cho một video theo danh sách video/anh.json (chỉ dùng thư viện chuẩn; Pillow tùy chọn).

    cd videos/<du-an>
    python3 ../../VideoKit/scripts/tao_anh.py --liet-ke                    # ghi video/DANH-SACH-ANH.md, in số lượng và chi phí ước tính
    python3 ../../VideoKit/scripts/tao_anh.py --id ong-son/goc co-lan/goc   # tạo vài ảnh
    python3 ../../VideoKit/scripts/tao_anh.py --nhom goc                    # tất cả ảnh gốc nhân vật
    python3 ../../VideoKit/scripts/tao_anh.py --nhom dang                   # các dáng (chỉnh sửa từ ảnh gốc của chính nhân vật đó)
    python3 ../../VideoKit/scripts/tao_anh.py --nhom vat-pham | nen
    python3 ../../VideoKit/scripts/tao_anh.py --kiem-tra                    # so chiều cao nhân vật giữa các dáng để bắt lệch

Cách giữ nhân vật đồng nhất:
  1. Mỗi nhân vật có một khối "nhận dạng" cố định (mặt, tóc, trang phục, màu) dán nguyên văn vào MỌI prompt của nhân vật đó.
  2. Ảnh gốc ("goc") tạo trước, dựa trên ảnh phong cách chung; mọi dáng khác là CHỈNH SỬA ảnh gốc ("giữ nguyên nhân vật, chỉ đổi dáng").
  3. Cùng một chuẩn khung: toàn thân cao khoảng 88% khung vuông, chân cách đáy 4%, nên mọi dáng cùng tỉ lệ khi ghép vào cảnh.
  4. `--kiem-tra` đo chiều cao nhân vật trong từng dáng so với ảnh gốc và cảnh báo ảnh lệch quá 15%.
Khóa API: OPENAI_API_KEY (biến môi trường hoặc .env ở gốc dự án).
"""
import argparse
import base64
import csv
import json
import sys
import time
import urllib.error
import urllib.request
import uuid
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _du_an import KIT, du_an  # noqa: E402

DA = du_an()
API = "https://api.openai.com/v1/images"
GIA = {"gpt-image-2.5-flare": (5.0, 30.0), "gpt-image-2.5-sunburst": (5.0, 30.0), "gpt-image-1.5": (5.0, 32.0)}
GIA_ANH_VAO = 8.0   # USD / 1M token ảnh đầu vào

PHONG_CACH = (
    "Glossy cartoon vector illustration: smooth cel-shading with 2-3 tonal steps, soft white specular highlights on rounded "
    "surfaces, thin outline in a darker shade of each shape's own color (no black outline), large glossy expressive eyes with "
    "white catchlights, friendly rounded proportions, clean smooth edges, no textures. "
)
CAU_THAM_CHIEU = ("Use the FIRST reference image ONLY as a style guide (rendering style, shading, outline, eye style, roundness). "
                  "Do not copy its subject. Draw a new subject: ")
KHUNG_NV = (" Full body, ONE single character, centered; the whole figure from head to feet fills about 88% of the square canvas "
            "height with the feet about 4% above the bottom edge. No ground, no cast shadow, no text, no extra characters. "
            "Completely transparent background.")
KHUNG_VAT = (" ONE single object, centered, filling about 80% of the canvas. No ground, no cast shadow, no text or letters, "
             "no people. Completely transparent background.")
KHUNG_NEN = (" Wide 16:9 illustration, soft pastel colors, bright daylight, a clean uncluttered composition, no people, "
             "no text or letters anywhere (any sign boards stay completely blank).")
QUY_TAC_MAU = (" Clothing must NOT be pure white, pure red or green; use the colors stated.")


def lay_khoa():
    import os
    if os.environ.get("OPENAI_API_KEY"):
        return os.environ["OPENAI_API_KEY"]
    for env in (DA.goc / ".env", DA.goc.parent / ".env", DA.goc.parent.parent / ".env"):
        if env.exists():
            for dong in env.read_text(encoding="utf-8").splitlines():
                ten, _, gt = dong.partition("=")
                if ten.strip() == "OPENAI_API_KEY" and gt.strip():
                    return gt.strip().strip("\"'")
    sys.exit("Không tìm thấy OPENAI_API_KEY (biến môi trường hoặc file .env).")


def multipart(truong, tep):
    ranh = uuid.uuid4().hex
    phan = [f'--{ranh}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode() for k, v in truong.items()]
    for k, ten, noi_dung in tep:
        phan.append((f'--{ranh}\r\nContent-Disposition: form-data; name="{k}"; filename="{ten}"\r\n'
                     f'Content-Type: image/png\r\n\r\n').encode() + noi_dung + b"\r\n")
    phan.append(f"--{ranh}--\r\n".encode())
    return b"".join(phan), f"multipart/form-data; boundary={ranh}"


def goi_api(khoa, model, prompt, anh_tham_chieu, kich_thuoc, chat_luong, nen_trong):
    truong = {"model": model, "prompt": prompt, "size": kich_thuoc, "quality": chat_luong, "n": "1", "output_format": "png",
              "background": "transparent" if nen_trong else "opaque"}
    tep = [("image[]", f"tc{i}.png", b) for i, b in enumerate(anh_tham_chieu)]
    du_lieu, loai = multipart(truong, tep)
    req = urllib.request.Request(f"{API}/edits", data=du_lieu, headers={"Authorization": f"Bearer {khoa}", "Content-Type": loai})
    for lan in range(1, 4):
        try:
            with urllib.request.urlopen(req, timeout=500) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            noi_dung = e.read().decode(errors="replace")
            if e.code in (429, 500, 502, 503) and lan < 3:
                time.sleep(15 * lan)
                continue
            sys.exit(f"HTTP {e.code}: {noi_dung[:500]}")


def doc_manifest():
    f = DA.video / "anh.json"
    if not f.exists():
        sys.exit(f"Không thấy {f}")
    return json.loads(f.read_text(encoding="utf-8")), f


def duong_dan(id_):
    return DA.images / f"{id_}.png"


def goc_cua(m, a):
    """Id ảnh gốc của nhân vật chứa ảnh `a`."""
    return a["id"].split("/")[0] + "/goc"


def xay_prompt(m, a):
    loai = a["loai"]
    if loai in ("nv-goc", "nv-dang"):
        nd = m["nhan_dang"][a["id"].split("/")[0]]
    if loai == "nv-goc":
        return CAU_THAM_CHIEU + PHONG_CACH + f"a character. {nd} Pose: {a['mo_ta']}." + QUY_TAC_MAU + KHUNG_NV
    if loai == "nv-dang":
        extra = " The second reference image shows an object the character interacts with; use it as is." if a.get("tham_chieu_phu") else ""
        them = a.get("nhan_vat_them", [])   # ảnh ghép nhóm: nhân vật chính giữ nguyên, thêm người khác từ mô tả
        if them:
            nd += " " + " ".join(m["nhan_dang"][t] for t in them)
            extra += " The same scene also contains additional characters described above, drawn in the same style and scale, all fully visible."
        return ("Edit the first reference image: keep EXACTLY the same character: same face, same hairstyle, same body proportions, "
                f"same outfit and colors, same art style, same scale and position in the frame. {nd} "
                f"Change ONLY the pose and action to: {a['mo_ta']}.{extra}{'' if them else ' Keep the same figure height and feet position.'} "
                f"No ground, no cast shadow, no text{'' if them else ', no extra characters'}. Completely transparent background.")
    if loai == "vat":
        return CAU_THAM_CHIEU + PHONG_CACH + a["mo_ta"] + "." + KHUNG_VAT
    if loai == "nen":
        return CAU_THAM_CHIEU + PHONG_CACH + a["mo_ta"] + "." + KHUNG_NEN
    sys.exit(f"loại ảnh lạ: {loai}")


def tham_chieu_cua(m, a):
    ds = [KIT.parent / m["phong_cach_ref"]]
    if a["loai"] == "nv-dang":
        ds = [duong_dan(goc_cua(m, a))]
        ds += [duong_dan(i) for i in a.get("tham_chieu_phu", [])]
    return ds


def lam_dac(p):
    try:
        import numpy as np
        from PIL import Image
    except ImportError:
        return
    arr = np.asarray(Image.open(p).convert("RGBA")).copy()
    al = arr[..., 3].astype(np.float32)
    arr[..., 3] = np.where(al >= 235, 255, np.where(al <= 6, 0, al)).astype(np.uint8)
    Image.fromarray(arr, "RGBA").save(p)


def do_bbox(p):
    try:
        import numpy as np
        from PIL import Image
    except ImportError:
        return None
    a = np.asarray(Image.open(p).convert("RGBA"))[..., 3] > 16
    if not a.any():
        return None
    ys, xs = np.where(a)
    h, w = a.shape
    return {"cao": round((ys.max() - ys.min() + 1) / h, 3), "rong": round((xs.max() - xs.min() + 1) / w, 3),
            "day": round(1 - (ys.max() + 1) / h, 3)}


def liet_ke(m):
    nhom = {"nv-goc": [], "nv-dang": [], "vat": [], "nen": []}
    for a in m["anh"]:
        nhom[a["loai"]].append(a)
    ten = {"nv-goc": "Ảnh gốc nhân vật (tạo trước, làm chuẩn cho mọi dáng)", "nv-dang": "Các dáng của nhân vật (chỉnh sửa từ ảnh gốc)",
           "vat": "Đạo cụ và đồ vật", "nen": "Nền lớn 16:9 (nền đặc)"}
    d = [f"# Danh sách ảnh cần tạo: {DA.cfg.get('ten', '')}", "",
         f"Sinh tự động từ `anh.json` bằng `tao_anh.py --liet-ke`. Tổng **{len(m['anh'])} ảnh**. Chữ trên ảnh (bảng hiệu, nhãn giá, tờ giấy) luôn là chữ HTML, không có trong ảnh.", ""]
    for k in ("nv-goc", "nv-dang", "vat", "nen"):
        d += [f"## {ten[k]} ({len(nhom[k])})", "", "| Id | Mô tả | Dùng ở |", "|---|---|---|"]
        for a in nhom[k]:
            d.append(f"| `{a['id']}` | {a.get('mo_ta_vi', a['mo_ta'])} | {', '.join(a.get('canh', []))} |")
        d.append("")
    n_nen = len(nhom["nen"])
    chi = (len(m["anh"]) - n_nen) * 0.015 + n_nen * 0.045
    d += [f"Chi phí ước tính: khoảng ${chi:.2f} nếu mỗi ảnh tạo đúng một lần; dự phòng tạo lại khoảng 40% thì khoảng ${chi * 1.4:.2f}."]
    (DA.video / "DANH-SACH-ANH.md").write_text("\n".join(d) + "\n", encoding="utf-8")
    print(f"Đã ghi {DA.video / 'DANH-SACH-ANH.md'}: " + ", ".join(f"{len(v)} {ten[k].split(' (')[0].lower()}" for k, v in nhom.items()) + f"; ước tính ${chi:.2f}")


def kiem_tra(m):
    bao_cao = {}
    for a in m["anh"]:
        if a["loai"] in ("nv-goc", "nv-dang") and duong_dan(a["id"]).exists():
            bao_cao[a["id"]] = do_bbox(duong_dan(a["id"]))
    loi = 0
    print(f"{'ảnh':34}{'cao':>7}{'đáy':>7}  so với ảnh gốc")
    for id_, b in bao_cao.items():
        if not b:
            continue
        g = bao_cao.get(id_.split("/")[0] + "/goc")
        ghi = ""
        if g and id_ != id_.split("/")[0] + "/goc":
            lech = (b["cao"] - g["cao"]) / g["cao"]
            ghi = f"{lech * 100:+.0f}%" + ("  <-- LỆCH, nên tạo lại" if abs(lech) > 0.15 else "")
            loi += abs(lech) > 0.15
        print(f"{id_:34}{b['cao']:>7.2f}{b['day']:>7.2f}  {ghi}")
    (DA.images / "anh-bao-cao.json").write_text(json.dumps(bao_cao, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"{loi} ảnh lệch quá 15% so với ảnh gốc (một số dáng cúi/ngồi lệch là bình thường).")


def main():
    ap = argparse.ArgumentParser(description="Tạo ảnh nhân vật/đạo cụ/nền theo danh sách")
    ap.add_argument("--liet-ke", action="store_true")
    ap.add_argument("--kiem-tra", action="store_true")
    ap.add_argument("--id", nargs="*")
    ap.add_argument("--nhom", choices=["goc", "dang", "vat-pham", "nen"])
    ap.add_argument("--ghi-de", action="store_true")
    ap.add_argument("--chat-luong", default=None)
    a = ap.parse_args()
    m, _ = doc_manifest()
    if a.liet_ke:
        liet_ke(m)
        return
    if a.kiem_tra:
        kiem_tra(m)
        return
    loai_nhom = {"goc": "nv-goc", "dang": "nv-dang", "vat-pham": "vat", "nen": "nen"}
    ds = [x for x in m["anh"] if (not a.id or x["id"] in a.id) and (not a.nhom or x["loai"] == loai_nhom[a.nhom])]
    if not ds:
        sys.exit("Không có ảnh nào khớp bộ lọc.")
    khoa = lay_khoa()
    tong, so = 0.0, 0
    for x in ds:
        f = duong_dan(x["id"])
        if f.exists() and not a.ghi_de:
            print(f"bỏ qua {x['id']} (đã có)")
            continue
        tc = tham_chieu_cua(m, x)
        thieu = [str(p) for p in tc if not p.exists()]
        if thieu:
            print(f"bỏ qua {x['id']}: chưa có ảnh tham chiếu {thieu[0]}")
            continue
        nen = x["loai"] == "nen"
        model = m["model_chinh_sua"] if x["loai"] == "nv-dang" else m["model"]
        t0 = time.time()
        d = goi_api(khoa, model, xay_prompt(m, x), [p.read_bytes() for p in tc],
                    m["kich_thuoc_nen"] if nen else m["kich_thuoc"], a.chat_luong or (m["chat_luong_nen"] if nen else m["chat_luong"]), not nen)
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_bytes(base64.b64decode(d["data"][0]["b64_json"]))
        if not nen:
            lam_dac(f)
        u = d.get("usage", {})
        det = u.get("input_tokens_details") or {}
        gi_in, gi_out = GIA.get(model, (5.0, 30.0))
        phi = det.get("text_tokens", 0) * gi_in / 1e6 + det.get("image_tokens", 0) * GIA_ANH_VAO / 1e6 + u.get("output_tokens", 0) * gi_out / 1e6
        tong += phi
        so += 1
        print(f"đã tạo {x['id']} ({time.time() - t0:.0f}s, ≈ ${phi:.3f})")
    if so:
        so_ghi = KIT / "ledger" / "chi-phi-api.csv"
        with open(so_ghi, "a", encoding="utf-8", newline="") as fh:
            csv.writer(fh).writerow([date.today().isoformat(), DA.cfg.get("slug", "?"), "OpenAI Images", m["model"], f"tao_anh.py ({a.nhom or 'chon-loc'})", so, round(tong, 3), "uoc tinh tu so token"])
    print(f"Xong: {so} ảnh, ≈ ${tong:.3f}. Thư mục: {DA.images}")


if __name__ == "__main__":
    main()
