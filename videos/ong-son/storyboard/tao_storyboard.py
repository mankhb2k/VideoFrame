#!/usr/bin/env python3
"""Sinh video/STORYBOARD.md từ storyboard/noi_dung.py: mỗi nhịp neo vào cụm từ trong lời dẫn, thời điểm lấy từ
assets/audio/words-<cảnh>.json (mốc từng từ thật). Chạy lại sau khi đổi giọng đọc hoặc sửa nội dung:

    python3 storyboard/tao_storyboard.py
"""
import json, re, sys, unicodedata
from pathlib import Path

DA = Path(__file__).resolve().parent.parent   # videos/<du-an>
AUD = DA / "video/assets/audio"
cfg = json.load(open(DA / "du-an.json", encoding="utf-8"))
moc = {r["id"]: r for r in json.load(open(AUD / "moc-canh.json", encoding="utf-8"))}


def kd(s):
    s = unicodedata.normalize("NFD", s.replace("đ", "d").replace("Đ", "D"))
    return re.sub(r"[^a-z0-9 ]+", " ", "".join(c for c in s if unicodedata.category(c) != "Mn").lower())


def toks(s):
    return kd(s).split()


class Canh:
    """Tìm thời điểm một cụm lời dẫn trong file âm thanh của cảnh. Cụm neo viết theo CHỮ TRONG KỊCH BẢN (không theo chữ whisper nghe được):
    tìm cụm trong văn bản kịch bản, rồi gióng (difflib) văn bản kịch bản với các từ whisper để lấy giây, nên lỗi nghe nhầm của whisper không ảnh hưởng."""

    def __init__(self, c, thu_muc=None, kep_theo_khoi=False):
        import difflib
        self.c = c
        self.w = json.load(open((thu_muc or AUD) / f"words-{c['tep_loi_thoai']}.json", encoding="utf-8"))["cac_tu"]
        self.t = [toks(x["tu"]) for x in self.w]
        self.flat = [(t, i) for i, ts in enumerate(self.t) for t in ts]
        khoi = json.load(open(DA / "loi-thoai" / f"{c['tep_loi_thoai']}.json", encoding="utf-8"))["khoi"]
        self.st = []
        for k in khoi:
            self.st.extend(toks(k["van_ban"]))
        sm = difflib.SequenceMatcher(None, self.st, [x[0] for x in self.flat], autojunk=False)
        self.anh = {}
        for a, b, n in sm.get_matching_blocks():
            for i in range(n):
                self.anh[a + i] = b + i
        self.dau = 0
        self.last_t = 0.0
        # mốc khối chính xác (nếu có) để kẹp thời điểm tìm được vào đúng khối, phòng whisper bỏ sót từ
        self.khoi_tg = None
        f_moc = DA / "loi-thoai" / f"{c['tep_loi_thoai']}.moc-khoi.json"
        if kep_theo_khoi and f_moc.exists():
            self.khoi_tg = json.load(open(f_moc, encoding="utf-8"))
            self.khoi_tu = []
            dem = 0
            for k in khoi:
                self.khoi_tu.append((dem, dem + len(toks(k["van_ban"]))))
                dem += len(toks(k["van_ban"]))

    def tu_cua(self, i):
        """Chỉ số từ trong self.flat ứng với token kịch bản thứ i (lấy token đã gióng gần nhất)."""
        for d in range(0, 9):
            if i + d in self.anh:
                return max(0, self.anh[i + d] - d)
            if d and i - d in self.anh:
                return min(len(self.flat) - 1, self.anh[i - d] + d)
        return None

    def kep(self, s, t):
        """Kẹp thời điểm t của token kịch bản thứ s vào khoảng thật của khối chứa nó; ngoài khoảng thì nội suy theo vị trí token trong khối."""
        if not self.khoi_tg:
            return t
        for (a, b), k in zip(self.khoi_tu, self.khoi_tg):
            if a <= s < b:
                lo, hi = k["bat_dau"] + 0.3, k["ket_thuc"] + 0.3
                if lo - 0.05 <= t <= hi + 0.05:
                    return t
                return lo + (hi - lo) * (s - a) / max(1, b - a)
        return t

    def tim(self, cum, sau=0):
        """Cụm neo có thể có nhiều lựa chọn ngăn bằng "|" (thử khớp đủ cụm của từng lựa chọn trước, rồi mới thử rút gọn); "+2.5" là
        dự phòng: cách nhịp trước 2,5 giây."""
        alts = cum.split("|")
        for rut in (False, True):
            for c in (sorted(alts, key=lambda a: not a.startswith("+")) if rut else alts):
                if c.startswith("+"):
                    if rut:
                        self.last_t += float(c[1:])
                        return self.last_t
                    continue
                r = self._tim(c, sau, rut)
                if r is not None:
                    self.last_t = r
                    return r
        sys.exit(f"{self.c['id']}: không thấy cụm “{cum}” trong kịch bản từ token {sau}: " + " ".join(self.st[sau:sau + 25]))

    def _tim(self, cum, sau, rut):
        tk = toks(cum)
        minlen = min(2, len(tk)) if rut else len(tk)
        while len(tk) >= minlen:
            for s in range(sau, len(self.st)):
                if self.st[s:s + len(tk)] == tk:
                    w = self.tu_cua(s)
                    if w is None:
                        continue
                    if len(tk) < len(toks(cum)):
                        print("RÚT GỌN", self.c['id'], cum, "->", " ".join(tk))
                    self.dau = s
                    return self.kep(s, self.w[self.flat[w][1]]["bat_dau"])
            tk = tk[:-1]
        return None


def phut(t):
    return f"{int(t // 60)}:{t % 60:04.1f}"


sys.path.insert(0, str(Path(__file__).resolve().parent))
from noi_dung import KHUNG, CHUNG, CANH  # noqa: E402


def khoi_tu_phien_am(c, cn):
    """Mốc đầu và cuối từng khối lời dẫn trong file âm thanh một mạch: gióng từ của kịch bản với từ whisper (Canh.tu_cua).
    Trả danh sách {id, bat_dau, ket_thuc, dung_sau_giay} với giây KHÔNG gồm 0,3 giây lặng đầu cảnh (giống moc-khoi cũ)."""
    f_moc = DA / "loi-thoai" / f"{c['tep_loi_thoai']}.moc-khoi.json"
    if f_moc.exists():   # có mốc chính xác từ lúc ghép giọng (ghep_giong.py)
        return json.load(open(f_moc, encoding="utf-8"))
    khoi = json.load(open(DA / "loi-thoai" / f"{c['tep_loi_thoai']}.json", encoding="utf-8"))["khoi"]
    out, s0, truoc = [], 0, None
    for k in khoi:
        w = cn.tu_cua(s0)
        if w is not None:
            bd = cn.w[cn.flat[w][1]]["bat_dau"] - 0.3
        else:   # không gióng được: ước theo số ký tự của khối trước (khoảng 15 ký tự mỗi giây)
            bd = (out[-1]["bat_dau"] + len(truoc["van_ban"]) / 15) if out else 0.0
            print(f"  {c['id']}: khối {k['id']} không gióng được, ước {bd:.1f}s")
        out.append({"id": k["id"], "bat_dau": bd, "dung_sau_giay": 0.0})
        s0 += len(toks(k["van_ban"]))
        truoc = k
    for j, o in enumerate(out):
        o["ket_thuc"] = (out[j + 1]["bat_dau"] - 0.25) if j + 1 < len(out) else cn.w[-1]["ket_thuc"] - 0.3
    return out


ANH = {a["id"]: a for a in json.load(open(DA / "video/anh.json", encoding="utf-8"))["anh"]}
KE = {"canh0": 0, "canh1": 0, "canh2": 1, "canh3": 2, "canh4": 3, "canh5": 5}   # số viên gạch đã có trên kệ khi vào cảnh


def id_doan(tieu_de, canh_id):
    n = re.search(r"\d+", canh_id).group(0)
    m = re.match(r"Đoạn (\d+)", tieu_de)
    return f"c{n}-d{m.group(1)}" if m else f"c{n}-chot"


def main():
    out = [KHUNG.format(duration=round(sum(r["duration"] for r in moc.values()), 1)), CHUNG]
    (DA / "storyboard/goi").mkdir(exist_ok=True)
    for f in (DA / "storyboard/goi").glob("*.md"):
        f.unlink()
    cfg_ghi = json.load(open(DA / "du-an.json", encoding="utf-8"))
    for n, c in enumerate(cfg["canh"], 1):
        nd = CANH[c["id"]]
        m = moc[c["id"]]
        cn = Canh(c, kep_theo_khoi=True)
        mk = khoi_tu_phien_am(c, cn)
        mkd = {k["id"]: k for k in mk}
        khoi_txt = {k["id"]: k["van_ban"] for k in json.load(open(DA / "loi-thoai" / f"{c['tep_loi_thoai']}.json", encoding="utf-8"))["khoi"]}
        out.append(f"## Frame {n} — {nd['ten']}\n")
        out.append(f"- scene: {nd['scene']}")
        out.append(f"- start: {m['start']}s")
        out.append(f"- duration: {m['duration']}s")
        out.append(f"- voice: 0.3s → {round(0.3 + m['audio'], 1)}s")
        out.append(f"- transition_in: {nd['vao']}")
        out.append("- status: outline")
        out.append(f"- blueprint: {nd['bp']}")
        out.append(f"- composition_id: scene-{n}")
        out.append(f"- cues: {c['tep_loi_thoai']}")
        out.append(f"- assets: {nd['assets']}")
        out.append(f"- rules: {nd['rules']}")
        out.append(f"- src: compositions/frames/{n:02d}-{c['id']}.html (dựng theo từng đoạn: compositions/frames/c{n - 1}-d*.html)")
        out.append(f"- packets: {nd['goi']}")
        out.append(f"- voiceover: \"{nd['loi']}\"\n")
        pos = 0
        secs = []
        for dm in nd["doan"]:
            out.append(f"### {dm['ten']}\n")
            if dm.get("hinh"):
                out.append(f"_Bố cục_: {dm['hinh']}\n")
            beats = []
            for neo, mo_ta in dm["nhip"]:
                t = cn.tim(neo, pos)
                pos = max(pos, cn.dau + 1)
                beats.append((t, " / ".join(a for a in neo.split("|") if not a.startswith("+")) or "(theo nhịp trước)", mo_ta))
                out.append(f"- **{t:.1f}s** (“{' / '.join(a for a in neo.split('|') if not a.startswith('+')) or 'theo nhịp trước'}”) — {mo_ta}")
            out.append("")
            secs.append((dm, beats))
        # ranh giới đoạn: đầu khối lời chứa nhịp đầu tiên, lùi 0,25 giây (nằm trong nhịp thở giữa hai khối)
        bat_dau = []
        for j, (dm, beats) in enumerate(secs):
            if j == 0:
                bat_dau.append(0.0)
                continue
            t0 = beats[0][0]
            kh = [k for k in mk if k["bat_dau"] + 0.3 <= t0 + 0.4]
            bat_dau.append(round(max(0.0, kh[-1]["bat_dau"] + 0.3 - 0.25), 2))
        ds = []
        for j, (dm, beats) in enumerate(secs):
            ket = bat_dau[j + 1] if j + 1 < len(secs) else m["duration"]
            ds.append({"id": id_doan(dm["ten"], c["id"]), "ten": dm["ten"], "bat_dau": bat_dau[j], "thoi_luong": round(ket - bat_dau[j], 2)})
        for cc in cfg_ghi["canh"]:
            if cc["id"] == c["id"]:
                cc["doan"] = [{"id": d["id"], "ten": d["ten"], "bat_dau": d["bat_dau"]} for d in ds]
        for j, (dm, beats) in enumerate(secs):
            d = ds[j]
            goi_md = []
            tx = " ".join(dm["ten"] + " " + dm.get("hinh", "") + " " + " ".join(b[2] for b in beats) for _ in [0])
            dung = sorted({i for i in ANH if i in tx})
            goi_md.append(f"# Gói dựng: {d['id']} — {dm['ten']}\n")
            goi_md.append(f"- composition_id (dùng nguyên văn làm `data-composition-id` và khoá `window.__timelines`): `{d['id']}`")
            goi_md.append(f"- file nguồn cần viết: `compositions/src/{d['id']}.body.html` (rồi chạy `build_canh.py {d['id']}`)")
            goi_md.append(f"- thời lượng: **{d['thoi_luong']} giây** (đặt `const D = {d['thoi_luong']};`); trong video bắt đầu tại {round(m['start'] + d['bat_dau'], 2)} giây; trong cảnh {d['bat_dau']}→{round(d['bat_dau'] + d['thoi_luong'], 2)} giây")
            co = KE[c["id"]]
            if d["id"].endswith("chot") and c["id"] in ("canh1", "canh2", "canh3", "canh4"):
                goi_md.append(f"- kệ gạch: có sẵn {co} viên; viên mới rơi trong đoạn này (xem nhịp); khung kệ ở góc trên trái, giữ trống dải y 40–140 cho kệ")
            elif co:
                goi_md.append(f"- kệ gạch: hiện suốt đoạn với {co} viên có sẵn (`vk.keGach(tl, root, {{co: {co}}})`); nội dung chính đặt dưới y = 150")
            else:
                goi_md.append("- kệ gạch: không hiện trong đoạn này")
            goi_md.append(f"- đoạn trước: {ds[j - 1]['ten'] if j else '(đầu cảnh; cắt từ cảnh trước)'}; đoạn sau: {ds[j + 1]['ten'] if j + 1 < len(ds) else '(hết cảnh; cắt sang cảnh sau)'}\n")
            goi_md.append("## Bố cục\n")
            goi_md.append((dm.get("hinh") or "(xem các nhịp)") + "\n")
            goi_md.append("## Nhịp hình (giây tính từ ĐẦU ĐOẠN NÀY; mỗi nhịp neo vào cụm từ trong lời dẫn)\n")
            for t, neo, mo_ta in beats:
                goi_md.append(f"- **{t - d['bat_dau']:.1f}s** (“{neo}”) — {mo_ta}")
            goi_md.append("\n## Lời dẫn trong đoạn (chỉ để căn nhịp, KHÔNG hiển thị thành chữ)\n")
            hd = d["bat_dau"]
            hc = hd + d["thoi_luong"]
            for k in mk:
                ts = k["bat_dau"] + 0.3
                if hd - 0.01 <= ts < hc - 0.01:
                    goi_md.append(f"- {ts - hd:.1f}s→{k['ket_thuc'] + 0.3 - hd:.1f}s (dừng sau {k['dung_sau_giay']}s): {khoi_txt[k['id']]}")
            if dung:
                goi_md.append("\n## Ảnh cần dùng (đường dẫn từ gốc dự án; chi tiết kích thước xem LUAT-DUNG-CANH.md)\n")
                for i in dung:
                    goi_md.append(f"- `{i}` → `assets/images/{i}.png`: {ANH[i]['mo_ta_vi']}")
            (DA / "storyboard/goi" / f"{d['id']}.md").write_text("\n".join(goi_md) + "\n", encoding="utf-8")
    Path(DA / "video/STORYBOARD.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    json.dump(cfg_ghi, open(DA / "du-an.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(DA / "du-an.json", "a", encoding="utf-8").write("\n")
    print("ok", sum(len(d['nhip']) for n in CANH.values() for d in n['doan']), "nhịp,", len(list((DA / "storyboard/goi").glob("*.md"))), "gói")


if __name__ == "__main__":
    main()
