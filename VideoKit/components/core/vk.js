/* Hàm dùng chung cho mọi cảnh (build_canh.py chèn vào chỗ đánh dấu VK_JS trong thẻ <script>, TRƯỚC khi tạo `tl`).
   Mọi hàm nhận timeline `tl` và đích (phần tử hoặc selector), chỉ tạo tween xác định (không Math.random, không Date.now),
   dùng fromTo với trạng thái đầu rõ ràng nên seek theo hai chiều đều đúng. Thời điểm `t` tính bằng giây trong cảnh hiện tại. */
const vk = (() => {
  const GACH = [
    { ten: "BIẾN", lop: "bien" }, { ten: "HÀM", lop: "ham" }, { ten: "DATABASE", lop: "db" },
    { ten: "IF / ELSE", lop: "re" }, { ten: "VÒNG LẶP", lop: "lap" },
  ];
  const dinhDang = (n) => String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, ".");
  const q = (x) => (typeof x === "string" ? document.querySelector(x) : x);

  /* hiện dần: mờ -> rõ, trượt từ dưới lên `dy` px (mặc định 28) */
  function vao(tl, el, t, o = {}) {
    tl.fromTo(el, { opacity: 0, y: (o.dy ?? 28) + (o.y ?? 0), x: o.x ?? 0, scale: o.scale0 ?? 1 },
      { opacity: 1, y: o.y ?? 0, x: o.x ?? 0, scale: 1, duration: o.dur ?? 0.55, ease: o.ease ?? "power3.out" }, t);
  }
  /* biến mất: mờ dần (và thu nhỏ nhẹ nếu cho `scale1`) */
  function ra(tl, el, t, o = {}) {
    tl.to(el, { opacity: o.opacity ?? 0, scale: o.scale1 ?? 1, duration: o.dur ?? 0.4, ease: "power2.in" }, t);
  }
  /* bật lên có nảy (cho chữ nhấn, viên gạch, dấu hỏi) */
  function pop(tl, el, t, o = {}) {
    tl.fromTo(el, { opacity: 0, scale: o.scale0 ?? 0.5 }, { opacity: 1, scale: o.scale1 ?? 1, duration: o.dur ?? 0.5, ease: "back.out(1.9)" }, t);
  }
  /* nảy một nhịp khi vật chạm đích (scale 1 -> 1.08 -> 1) */
  function nay(tl, el, t, o = {}) {
    const m = o.m ?? 1.08;
    tl.to(el, { scale: m, duration: 0.12, ease: "power2.out" }, t).to(el, { scale: 1, duration: 0.28, ease: "back.out(2.4)" }, t + 0.12);
  }
  /* bay theo cung từ (x0,y0) tới (x1,y1) trong `dur` giây; `cao` là độ vồng (âm = vồng lên). Phần tử nên đặt left:0; top:0 (lớp .vk-abs / .vk-nv / .vk-the) */
  function cung(tl, el, o) {
    const dur = o.dur ?? 0.9, cao = o.cao ?? -140, ymid = (o.y0 + o.y1) / 2 + cao;
    tl.fromTo(el, { x: o.x0, y: o.y0, rotation: o.r0 ?? 0, scale: o.s0 ?? 1, opacity: o.hien0 === false ? 0 : 1 },
      { x: o.x1, rotation: o.r1 ?? 0, scale: o.s1 ?? 1, opacity: 1, duration: dur, ease: o.easeX ?? "power1.inOut" }, o.t);
    tl.to(el, { keyframes: { y: [ymid, o.y1], easeEach: "sine.inOut" }, duration: dur }, o.t);
  }
  /* đếm số: từ `tu` tới `den`, hiển thị kiểu 20.000.000 (dấu chấm ngăn nghìn), kèm hậu tố tuỳ ý */
  function dem(tl, el, o) {
    const e = q(el), p = { v: o.tu ?? 0 }, hau = o.hau ?? "", tien = o.tien ?? "";
    e.textContent = tien + dinhDang(o.tu ?? 0) + hau;
    tl.to(p, { v: o.den, duration: o.dur ?? 1.2, ease: o.ease ?? "power2.out", onUpdate() { e.textContent = tien + dinhDang(p.v) + hau; } }, o.t);
  }
  /* gõ chữ: hiện dần từng ký tự của `text` trong `dur` giây (đặt phần tử rỗng ban đầu) */
  function go(tl, el, text, o) {
    const e = q(el), p = { n: 0 };
    e.textContent = "";
    tl.to(p, { n: text.length, duration: o.dur ?? text.length * 0.04, ease: "none", onUpdate() { e.textContent = text.slice(0, Math.round(p.n)); } }, o.t);
  }
  /* tô sáng một dòng code (hoặc phần tử bất kỳ) từ tOn tới tOff, bằng màu nền mờ */
  function sangDong(tl, el, tOn, tOff, mau = "rgba(250,204,21,0.22)") {
    tl.fromTo(el, { backgroundColor: "rgba(0,0,0,0)" }, { backgroundColor: mau, duration: 0.25, ease: "power2.out" }, tOn);
    if (tOff != null) tl.to(el, { backgroundColor: "rgba(0,0,0,0)", duration: 0.3, ease: "power2.in" }, tOff);
  }
  /* vẽ dần một nét SVG có pathLength="1" (class vk-net) trong `dur` giây */
  function ve(tl, el, t, dur = 0.8) {
    tl.fromTo(el, { strokeDasharray: 1, strokeDashoffset: 1, opacity: 1 }, { strokeDashoffset: 0, duration: dur, ease: "power1.inOut" }, t);
  }
  /* kệ gạch ở góc trên trái: `co` viên đã nằm sẵn từ đầu cảnh (0..5, theo thứ tự BIẾN, HÀM, DATABASE, IF/ELSE, VÒNG LẶP);
     `roi` là viên rơi: một số (1..5) rơi lúc `t`, hoặc danh sách [{i: 4, t: 12.3}, {i: 5, t: 15}]. Trả về phần tử kệ. */
  function keGach(tl, parent, o = {}) {
    const ke = document.createElement("div");
    ke.className = "vk-ke";
    for (let i = 0; i < 5; i++) {
      const slot = document.createElement("div");
      slot.className = "vk-o"; slot.style.left = i * 154 + "px";
      ke.appendChild(slot);
    }
    const dat = (i) => {
      const g = document.createElement("div");
      g.className = "vk-gach vk-gach-" + GACH[i].lop; g.style.left = i * 154 + "px"; g.textContent = GACH[i].ten;
      ke.appendChild(g); return g;
    };
    for (let i = 0; i < (o.co ?? 0); i++) dat(i);
    const roi = o.roi ? (Array.isArray(o.roi) ? o.roi : [{ i: o.roi, t: o.t ?? 0 }]) : [];
    roi.forEach((r) => {
      const g = dat(r.i - 1);
      tl.fromTo(g, { y: -360, opacity: 0, rotation: -6 }, { y: 0, opacity: 1, rotation: 0, duration: 0.7, ease: "bounce.out" }, r.t);
    });
    q(parent).appendChild(ke);
    return ke;
  }
  /* viên gạch lớn: rơi từ trên xuống giữa khung (cx, cy) lúc `t` với độ phóng `scale`, rồi (nếu có `tBay`) bay theo cung xuống đúng ô `i` (1..5) của kệ gạch
     và thu về cỡ 1 trong `durBay` giây. Trả về phần tử. Kệ gạch tạo riêng bằng vk.keGach (ô trống) cùng cảnh. */
  function gachLon(tl, parent, o) {
    const i = o.i, g = document.createElement("div"), cx = o.cx ?? 960, cy = o.cy ?? 540, sc = o.scale ?? 3;
    g.className = "vk-gach vk-gach-" + GACH[i - 1].lop; g.textContent = GACH[i - 1].ten;
    g.style.left = "0px"; g.style.top = "0px"; g.style.transformOrigin = "50% 50%"; g.style.zIndex = "5";
    q(parent).appendChild(g);
    const x0 = cx - 72, y0 = cy - 42, x1 = 96 + (i - 1) * 154, y1 = 48;
    tl.fromTo(g, { x: x0, y: y0 - 700, scale: sc, opacity: 0, rotation: -5 }, { y: y0, opacity: 1, rotation: 0, duration: 0.8, ease: "bounce.out" }, o.t);
    if (o.tBay != null) {
      const d = o.durBay ?? 1.0, ymid = (y0 + y1) / 2 - 120;
      tl.to(g, { x: x1, scale: 1, duration: d, ease: "power2.inOut" }, o.tBay);
      tl.to(g, { keyframes: { y: [ymid, y1], easeEach: "sine.inOut" }, duration: d }, o.tBay);
    }
    return g;
  }
  /* đặt ảnh nhân vật/đạo cụ vuông `size` px: tâm ngang `cx`, ĐÁY ẢNH tại `base` (chân nhân vật cách đáy ảnh khoảng 4%) */
  function nv(parent, o) {
    const img = document.createElement("img");
    img.className = "vk-nv"; img.src = o.src; img.alt = "";
    const w = o.size, h = o.cao ?? o.size;
    img.style.width = w + "px"; img.style.height = h + "px";
    img.style.left = o.cx - w / 2 + "px"; img.style.top = o.base - h + "px";
    if (o.id) img.id = o.id;
    if (o.bong !== false) {
      const b = document.createElement("div");
      b.className = "vk-bong"; b.style.width = w * 0.55 + "px"; b.style.height = w * 0.09 + "px";
      b.style.left = o.cx - w * 0.275 + "px"; b.style.top = o.base - w * 0.09 * 0.62 - h * 0.035 + "px";
      q(parent).appendChild(b); img._bong = b;
    }
    q(parent).appendChild(img);
    return img;
  }
  return { GACH, dinhDang, vao, ra, pop, nay, cung, dem, go, sangDong, ve, keGach, gachLon, nv };
})();

/* Co giãn thời gian của cả đoạn khi giọng đọc đổi: build_canh.py thay `gsap.timeline(...)` bằng `vkWarp(gsap.timeline(...), PTS)` nếu có file <id>.warp.json.
   PTS = [[giây cũ, giây mới], ...] tăng dần; mọi VỊ TRÍ bắt đầu (đối số thời điểm của to, from, fromTo, set, call, add, addLabel) đi qua đường gấp khúc này.
   Thời lượng từng tween giữ nguyên; ngoài điểm cuối thì dịch song song. Không có PTS thì giữ nguyên timeline. */
function vkWarp(tl, pts) {
  if (!pts || pts.length < 2) return tl;
  const f = (t) => {
    if (t <= pts[0][0]) return pts[0][1] + (t - pts[0][0]);
    for (let i = 1; i < pts.length; i++) {
      if (t <= pts[i][0]) {
        const [a, b] = pts[i - 1], [c, d] = pts[i];
        return b + ((t - a) / (c - a)) * (d - b);
      }
    }
    const e = pts[pts.length - 1];
    return e[1] + (t - e[0]);
  };
  const vitri = { to: 2, from: 2, fromTo: 3, set: 2, call: 2, add: 1, addLabel: 1 };
  Object.keys(vitri).forEach((m) => {
    const goc = tl[m].bind(tl), i = vitri[m];
    tl[m] = (...a) => {
      if (a.length > i && typeof a[i] === "number") a[i] = f(a[i]);
      return goc(...a);
    };
  });
  return tl;
}
