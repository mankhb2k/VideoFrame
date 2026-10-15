#!/usr/bin/env python3
"""Sinh bảng nhận diện thương hiệu từ templates/thuong-hieu*.css (mã màu và độ tương phản đọc/tính từ chính file CSS).

    python VideoKit/scripts/tao_bang_mau.py                # bảng sáng + bảng tối + ảnh so sánh
    python VideoKit/scripts/tao_bang_mau.py --che-do sang  # chỉ một chế độ (sang hoặc toi)

Kết quả trong VideoKit/brand/: bang-mau-thuong-hieu.png (sáng), bang-mau-thuong-hieu-toi.png, so-sanh-sang-toi.png (cùng một khung hình ở hai chế độ).
Cần Google Chrome (chụp ảnh); Pillow và numpy (tùy chọn, để cắt gọn phần trống ở đáy).
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _thuong_hieu import KIT, TPL, doc_css, lay_bien  # noqa: E402

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT = KIT / "brand"
FONT = (TPL / "font-face.css").read_text(encoding="utf-8").replace("url('assets/fonts/", "url('fonts/")

CHE_DO = {
    "sang": dict(file="bang-mau-thuong-hieu", tieu_de="Bảng <u>nhận diện</u> video học thuật (nền sáng)",
                 sub="Nền trắng ngà · chữ đen · màu chữ theo nghĩa (giá, tổng, cảnh báo) · thẻ viền mảnh, bóng mềm · code trong cửa sổ đen",
                 nen="Nền trắng ngà", chinh="Đen", cam="Cam đậm (chữ)", xanh="Xanh đậm (chữ)", nhat="chữ đậm trên nền nhạt",
                 mau="Chữ thường màu đen. Màu chữ khác chỉ để chỉ nghĩa: <span class=\"th-gia\">giá khi liệt kê</span> xanh dương đậm, <span class=\"th-gia-ban\">giá bán</span> và <span class=\"th-tong\">tổng</span> xanh lá đậm, <span class=\"th-canh-bao\">cảnh báo</span> đỏ.",
                 khong_vien_nen="#FFFFFF"),
    "toi": dict(file="bang-mau-thuong-hieu-toi", tieu_de="Bảng <u>nhận diện</u> video học thuật (nền tối)",
                sub="Nền đen than · chữ sáng · màu chữ theo nghĩa (giá, tổng, cảnh báo) · thẻ viền mảnh, bóng mềm · code trong cửa sổ đen hơn nền",
                nen="Nền đen than", chinh="Chữ sáng", cam="Cam sáng (chữ)", xanh="Xanh sáng (chữ)", nhat="chữ sáng trên nền thẻ tối",
                mau="Chữ thường màu sáng. Màu chữ khác chỉ để chỉ nghĩa: <span class=\"th-gia\">giá khi liệt kê</span> xanh dương sáng, <span class=\"th-gia-ban\">giá bán</span> và <span class=\"th-tong\">tổng</span> xanh lá sáng, <span class=\"th-canh-bao\">cảnh báo</span> đỏ sáng.",
                khong_vien_nen="#202026"),
}


def lum(h):
    h = h.lstrip("#")
    r, g, b = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4  # noqa: E731
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def cr(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)


def chup(html_path, png, rong, cao, nen_hex):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={rong},{cao}", f"--screenshot={png}", f"file://{html_path}"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    try:  # cắt gọn phần trống ở đáy
        import numpy as np
        from PIL import Image
        im = Image.open(png).convert("RGB")
        a = np.asarray(im).astype(int)
        bg = np.array([int(nen_hex[i:i + 2], 16) for i in (1, 3, 5)])
        rows = np.where((np.abs(a - bg).sum(2) > 12).any(1))[0]
        im.crop((0, 0, im.width, min(im.height, rows.max() + 70))).save(png)
    except Exception as e:  # noqa: BLE001
        print("không cắt gọn được ảnh:", e, file=sys.stderr)


def bang_mau(che_do):
    T = CHE_DO[che_do]
    css = doc_css(che_do)
    V = lay_bien(css)

    def sw(ten, var, ghi, do_tuong_phan=False):
        h = V[var]
        nhan = f"{cr(h, V['nen']):.1f} : 1 trên nền" if do_tuong_phan else ghi
        return (f'<div class="sw"><div class="chip" style="background:var(--{var})"></div>'
                f'<b>{ten}</b><span>{h}</span><i>{nhan}</i></div>')

    kn = [("BIẾN", "bien"), ("HÀM", "ham"), ("DATABASE", "db"), ("IF / ELSE", "re"), ("VÒNG LẶP", "lap")]
    vd = {"bien": "Biến là cái nhãn", "ham": "Hàm là người làm một việc", "db": "Database là cuốn sổ", "re": "if/else là ngã ba đường", "lap": "Vòng lặp là hỏi đi hỏi lại"}
    cot = "".join(
        f'<div class="kn"><div class="th-gach th-gach-{k}" style="font-size:30px">{t}</div>'
        f'<div class="th-vat" style="background:var(--{k}-nhat);padding:14px 16px;margin-top:22px"><div style="font-size:22px;font-weight:800;color:var(--{k}-dam)">{vd[k]}</div>'
        f'<div style="font-size:15px;color:var(--muc-phu);margin-top:4px">{T["nhat"]}</div></div>'
        f'<div class="hexs">tươi {V[k]}<br>đậm/sáng {V[k + "-dam"]}<br>nhạt {V[k + "-nhat"]}</div></div>' for t, k in kn)
    html = f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>
{FONT}
{css}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1600px;background:var(--nen);color:var(--muc);font-family:'Be Vietnam Pro',sans-serif;padding:56px 64px 60px}}
h1{{font-size:46px;font-weight:800;letter-spacing:-.01em}} h1 u{{text-decoration:none;border-bottom:8px solid var(--cam)}}
.top{{display:flex;align-items:center;gap:26px;margin-bottom:34px}} .top img{{width:96px;height:96px;border-radius:50%}}
.sub{{font-size:21px;color:var(--muc-phu);margin-top:6px}}
h2{{font-size:26px;font-weight:800;margin:38px 0 16px;color:var(--muc)}}
.bill{{width:760px;padding:22px 28px;margin-top:24px}} .bill .bd{{font-size:26px;font-weight:800;margin-bottom:10px}} .r1{{display:flex;justify-content:space-between;font-size:24px;padding:7px 0;border-bottom:1px solid var(--ke)}} .r1.tt{{border-bottom:none;font-size:30px;padding-top:12px}} .r1.gb{{border-bottom:none;font-size:22px;padding-top:2px}}
.row{{display:flex;gap:18px;flex-wrap:wrap}}
.sw{{width:172px}} .sw .chip{{height:84px;border:var(--vien);border-radius:12px;box-shadow:var(--bong);margin-bottom:12px}}
.sw b{{display:block;font-size:17px}} .sw span{{display:block;font-size:15px;color:var(--muc-phu);font-family:'JetBrains Mono',monospace}} .sw i{{display:block;font-size:14px;color:var(--muc-mo);font-style:normal}}
.kn{{flex:1}} .hexs{{font-family:'JetBrains Mono',monospace;font-size:14px;color:var(--muc-phu);margin-top:16px;line-height:1.55}}
.cmp{{display:flex;gap:36px;align-items:flex-start}} .cmp>div{{flex:1}}
.sem{{display:flex;gap:18px}} .sem .th-vat{{padding:14px 22px;font-size:22px;font-weight:800;display:flex;align-items:center;gap:12px;color:var(--chu-tren-mau)}}
.th-ma{{font-size:25px;line-height:1.7}} .c{{color:var(--ma-chu-thich)}} .b{{color:var(--ma-bien)}} .h{{color:var(--ma-ham)}} .d{{color:var(--ma-db)}} .r{{color:var(--ma-re)}} .l{{color:var(--ma-lap)}} .o{{color:var(--ma-cam)}}
.mau p{{font-size:30px;line-height:1.5;font-weight:600}}
</style></head><body>
<div class="top"><img src="logo-tron.png"><div><h1>THO CODE · {T["tieu_de"]}</h1><div class="sub">{T["sub"]}</div></div></div>
<h2>1. Nền và chữ (độ tương phản đo trên nền)</h2>
<div class="row">
{sw(T["nen"],"nen","nền chính")}{sw("Nền phụ","nen-phu","dải, chia khu")}{sw("Mặt thẻ","be-mat","thẻ, giấy, hoá đơn")}{sw("Đường kẻ","ke","lưới, kẻ nhạt")}
{sw(T["chinh"],"muc","",True)}{sw("Chữ phụ","muc-phu","",True)}{sw("Chú thích","muc-mo","",True)}
{sw("Giá liệt kê, số liệu","chu-gia","",True)}{sw("Giá bán, tổng","chu-gia-ban","",True)}{sw("Cảnh báo, lỗi","chu-canh-bao","",True)}{sw("Cam THO CODE","cam","chỉ tô nền, logo")}
</div>
<div class="mau" style="margin-top:26px"><p>{T["mau"]}</p></div>
<div class="th-vat bill"><div class="bd">Hoá đơn HD001</div>
<div class="r1"><span>Gạo ST25 × 10 ký</span><span class="th-gia">300.000đ</span></div>
<div class="r1"><span>Nước mắm hãng A × 2 chai</span><span class="th-gia">90.000đ</span></div>
<div class="r1"><span>Muối × 1 gói</span><span class="th-gia">8.000đ</span></div>
<div class="r1"><span class="th-canh-bao">⚠ Hết hàng: nước mắm hãng B</span><span></span></div>
<div class="r1 tt"><span>Tổng cộng</span><span class="th-tong">398.000đ</span></div>
<div class="r1 gb"><span class="th-chu-phu">Giá bán lẻ hôm nay: gạo ST25</span><span class="th-gia-ban">30.000đ / ký</span></div></div>
<h2>2. Năm khái niệm: tươi để tô vật thể, đậm/sáng để làm chữ, nhạt để làm nền thẻ</h2>
<div class="row">{cot}</div>
<h2>3. Vật thể kiểu giao diện thường: viền mảnh, bóng mềm</h2>
<div class="cmp">
 <div><div style="display:flex;gap:14px;align-items:center"><div style="background:var(--bien);border-radius:10px;padding:8px 20px;font-weight:800;font-size:30px;color:var(--chu-tren-mau)">BIẾN</div><div style="background:var(--be-mat);border-radius:14px;padding:16px 22px;font-size:22px">Hoá đơn HD001</div></div><div class="sub" style="margin-top:12px;font-size:18px">Không viền, không bóng: dẹt, dễ chìm vào nền.</div></div>
 <div><div style="display:flex;gap:14px;align-items:center"><div class="th-gach th-gach-bien" style="font-size:30px">BIẾN</div><div class="th-vat" style="padding:16px 22px;font-size:22px">Hoá đơn HD001</div></div><div class="sub" style="margin-top:12px;font-size:18px">Viền mảnh và bóng mềm: nổi vừa đủ, sạch, nhất quán mọi cảnh.</div></div>
</div>
<h2>4. Code luôn nằm trong cửa sổ đen kiểu macOS có 3 chấm; từ khoá tô theo màu khái niệm</h2>
<div class="th-cuaso"><div class="th-cuaso-dau"><i></i><i></i><i></i><span>mot_ngay_ban_hang.py</span></div>
<pre class="th-ma"><span class="b">tong_tien</span> = 0   <span class="c"># biến: cái nhãn</span>
<span class="r">while</span> con_mon_trong_gio:   <span class="c"># vòng lặp</span>
    gia = <span class="d">hoi_ke_toan</span>(<span class="o">"gia_ban"</span>)   <span class="c"># database</span>
    tong_tien += <span class="h">tinh_tien</span>(gia, so_ky=1)   <span class="c"># hàm</span>
<span class="r">if</span> black_friday == <span class="o">"27/11"</span>:   <span class="c"># ngã ba đường</span></pre></div>
<h2>5. Ngữ nghĩa: luôn kèm biểu tượng, không chỉ dựa vào màu</h2>
<div class="sem"><div class="th-vat" style="background:var(--on)">✓ ổn / đúng</div><div class="th-vat" style="background:var(--loi)">✗ lỗi / sai</div><div class="th-vat" style="background:var(--nen-phu);color:var(--chu-canh-bao)">⚠ cảnh báo (chữ đỏ)</div></div>
</body></html>'''
    h = OUT / f"{T['file']}.html"
    h.write_text(html, encoding="utf-8")
    chup(h, OUT / f"{T['file']}.png", 1600, 2400, V["nen"])
    print("Đã ghi", OUT / f"{T['file']}.png")


def so_sanh():
    sang, toi = doc_css("sang"), doc_css("toi")
    goc = re.search(r":root \{.*?\n\}", sang, re.S).group(0)
    lop = sang.replace(goc, "")
    bien_sang = goc.replace(":root", ".t-sang")
    bien_toi = re.search(r":root \{.*?\n\}", toi, re.S).group(0).replace(":root", ".t-toi")

    def khung(cls):
        return f'''<div class="khung {cls}"><div class="man">
<div class="gach-hang"><span class="th-gach th-gach-bien" style="font-size:26px">BIẾN</span><span class="th-gach th-gach-ham" style="font-size:26px">HÀM</span></div>
<h3>Biến là cái nhãn</h3>
<p class="phu">Ông Sơn dán nhãn <span class="th-gia">gia_gao_st25</span> lên thùng gạo, giá bán <span class="th-gia-ban">30.000đ</span></p>
<div class="th-vat hd"><b style="font-size:34px">Hoá đơn HD001</b>
<div class="dong"><span>Gạo ST25 × 10 ký</span><span class="th-gia">300.000đ</span></div>
<div class="dong"><span>Nước mắm × 2 chai</span><span class="th-gia">90.000đ</span></div>
<div class="dong"><span class="th-chu-phu">Cộng</span><span class="th-tong">390.000đ</span></div></div>
<div class="th-cuaso code"><div class="th-cuaso-dau"><i></i><i></i><i></i><span>gia_gao.py</span></div>
<pre class="th-ma"><span style="color:var(--ma-bien)">gia_gao_st25</span> = 30000
<span style="color:var(--ma-bien)">gia_gao_jasmine</span> = 20000
<span style="color:var(--ma-bien)">gia_gao_thuong</span> = 15000
<span style="color:var(--ma-ham)">tinh_tien</span>(gia_gao_st25, 10)</pre></div>
<img class="nv th-nhanvat" src="../characters/khi/khi-cam-chuoi.png">
<img class="lg" src="logo-tron.png">
</div></div>'''
    html = f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>
{FONT}
{lop}
{bien_sang}
{bien_toi}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:2020px;background:#888;padding:34px 30px 40px;font-family:'Be Vietnam Pro',sans-serif}}
.cot{{display:inline-block;vertical-align:top;margin-right:30px}} .cot:last-child{{margin-right:0}}
.nhan{{font:800 26px 'Be Vietnam Pro';color:#fff;margin-bottom:12px}}
.ngoai{{width:960px;height:540px;overflow:hidden;border-radius:6px;box-shadow:0 8px 24px rgba(0,0,0,.35)}}
.khung{{width:1920px;height:1080px;transform:scale(.5);transform-origin:0 0;background:var(--nen);color:var(--muc);position:relative}}
.man{{position:absolute;inset:0}}
.gach-hang{{position:absolute;left:60px;top:44px;display:flex;gap:14px}}
h3{{position:absolute;left:60px;top:150px;font-size:104px;font-weight:800;letter-spacing:-.01em;color:var(--muc)}}
.phu{{position:absolute;left:60px;top:290px;font-size:38px;font-weight:600;color:var(--muc-phu);width:900px;line-height:1.35}}
.hd{{position:absolute;left:60px;top:470px;width:720px;padding:30px 34px;font-size:32px}}
.dong{{display:flex;justify-content:space-between;margin-top:18px}}
.code{{position:absolute;left:900px;top:300px;width:960px}} .code .th-ma{{font-size:34px;line-height:1.65;padding:24px 30px}} .code .th-cuaso-dau{{font-size:22px;padding:16px 24px}} .code .th-cuaso-dau i{{width:20px;height:20px}}
.nv{{position:absolute;left:1330px;top:610px;width:420px}}
.lg{{position:absolute;right:44px;bottom:44px;width:132px;height:132px}}
</style></head><body>
<div class="cot"><div class="nhan">NỀN SÁNG · trắng ngà #F8F7F4</div><div class="ngoai">{khung("t-sang")}</div></div><div class="cot"><div class="nhan">NỀN TỐI · đen than #121214</div><div class="ngoai">{khung("t-toi")}</div></div>
</body></html>'''
    h = OUT / "so-sanh-sang-toi.html"
    h.write_text(html, encoding="utf-8")
    chup(h, OUT / "so-sanh-sang-toi.png", 2020, 700, "#888888")
    print("Đã ghi", OUT / "so-sanh-sang-toi.png")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--che-do", choices=["sang", "toi"], help="chỉ một chế độ; mặc định cả hai kèm ảnh so sánh")
    a = ap.parse_args()
    for cd in ([a.che_do] if a.che_do else ["sang", "toi"]):
        bang_mau(cd)
    if not a.che_do:
        so_sanh()
