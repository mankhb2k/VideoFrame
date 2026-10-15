---
name: THO CODE nền trắng ngà (video học thuật)
colors:
  background: "#F8F7F4"
  background-alt: "#EFEDE8"
  surface: "#FFFFFF"
  line: "#DDD9D0"
  ink: "#111113"
  ink-soft: "#4B4B52"
  ink-faint: "#6B6B73"
  brand: "#F26A21"
  text-price-list: "#1E3A8A"
  text-price-sale: "#15803D"
  text-total: "#15803D"
  text-warning: "#B91C1C"
  concept-bien: "#FACC15"
  concept-ham: "#3B82F6"
  concept-database: "#8B5CF6"
  concept-if-else: "#14B8A6"
  concept-vong-lap: "#EC4899"
  ok: "#22C55E"
  error: "#EF4444"
  code-background: "#111113"
typography:
  display:
    fontFamily: Be Vietnam Pro
    fontWeight: 800
  body:
    fontFamily: Be Vietnam Pro
    fontWeight: 500
  code:
    fontFamily: JetBrains Mono
    fontWeight: 400
spacing:
  safe-margin: 96px
  code-max-lines: 6
components:
  object:
    border: 1.5px solid #D2CCBE
    shadow: 0 1px 2px rgba(17,17,19,0.06), 0 8px 24px rgba(17,17,19,0.08)
    radius: 14px
  code-window:
    background: "#111113"
    header: "#1E1E22"
    dots: ["#FF5F57", "#FEBC2E", "#28C840"]
    border: 1px solid #000000
    shadow: 0 14px 36px rgba(17,17,19,0.28)
---

## Overview

Nền **trắng ngà** `#F8F7F4` (không dùng `#FFFFFF` làm nền: chói). Chữ **đen** `#111113`; màu chữ khác chỉ để chỉ **nghĩa** (giá liệt kê xanh dương đậm, giá bán và tổng xanh lá đậm, cảnh báo đỏ), không theo màu thương hiệu. Cam `#F26A21` lấy từ logo THO CODE là màu nhận diện, chỉ dùng để tô nền, logo, gạch chân, **không làm màu chữ**. Vật thể theo kiểu giao diện thường: viền mảnh và bóng mềm, không dùng viền dày hay bóng đổ cứng. **Code luôn nằm trong cửa sổ nền đen kiểu macOS có 3 chấm** ở thanh tiêu đề.
Bảng đầy đủ và nguồn sinh: `VideoKit/templates/thuong-hieu.css`, `VideoKit/brand/colors.json`, ảnh `VideoKit/brand/bang-mau-thuong-hieu.png`.

## The Frame

Khung 1920×1080, lề an toàn 96 px. Một tiêu điểm mỗi cảnh. Chữ chính 56 px trở lên, chú thích 28 px trở lên, code 30 px trở lên. Góc phải bên dưới dành cho logo kênh: không đặt nội dung vào vùng đó.

## Colors: text and objects

| Loại chữ | Màu | Độ tương phản trên nền |
|---|---|---|
| Chữ thường, tên hàng, tiêu đề, viền | `#111113` đen | 17,6:1 |
| Chữ phụ | `#4B4B52` | 8,1:1 |
| Chú thích | `#6B6B73` | 4,9:1, chỉ chữ nhỏ vừa đủ |
| **Giá khi liệt kê**, số liệu | `#1E3A8A` xanh dương đậm (hoặc đen) | 9,7:1 |
| **Giá bán** | `#15803D` xanh lá đậm | 4,7:1 |
| **Tổng cộng** | `#15803D` xanh lá đậm, in đậm và lớn hơn dòng thường | 4,7:1 |
| **Cảnh báo, lỗi, sai** | `#B91C1C` đỏ đậm | 6,0:1 |
| Tô nền thương hiệu (logo, vòng) | `#F26A21` cam | không bao giờ làm chữ (2,9:1) |

Lớp CSS: `.th-gia`, `.th-gia-ban`, `.th-tong`, `.th-canh-bao`. Trên nền tối dùng bản sáng của cùng vai trò (biến CSS tự đổi).

Năm khái niệm (tươi để tô nền vật thể, đậm để làm chữ, nhạt để làm nền thẻ):

| Khái niệm | Tươi | Đậm | Nhạt |
|---|---|---|---|
| BIẾN | `#FACC15` | `#854D0E` | `#FEF9C3` |
| HÀM | `#3B82F6` | `#1D4ED8` | `#DBEAFE` |
| DATABASE | `#8B5CF6` | `#6D28D9` | `#EDE9FE` |
| IF / ELSE | `#14B8A6` | `#0F766E` | `#CCFBF1` |
| VÒNG LẶP | `#EC4899` | `#BE185D` | `#FCE7F3` |

Ngữ nghĩa: ổn `#22C55E` (đậm `#15803D`), lỗi `#EF4444` (đậm `#B91C1C`), luôn kèm biểu tượng dấu tích hoặc dấu X.

## Code window

```html
<div class="th-cuaso">
  <div class="th-cuaso-dau"><i></i><i></i><i></i><span>tinh_tien.py</span></div>
  <pre class="th-ma">...</pre>
</div>
```

Nền đen, thanh tiêu đề `#1E1E22` có 3 chấm đỏ, vàng, xanh (`#FF5F57`, `#FEBC2E`, `#28C840`; chỉ để trang trí, không mang nghĩa lỗi/ổn) và tên file. Chữ `#F4F4F5`, chú thích `#9CA3AF`; từ khoá tô theo màu khái niệm (biến vàng, hàm xanh dương, database tím, if/while lục lam, vòng lặp hồng). Tối đa 6 dòng hiển thị (ngoại lệ: đoạn code Cảnh 0 và Cảnh 5).

## Composition Rules

- Chữ trên màu tươi là đen, cỡ lớn và đậm. Chữ nhỏ dùng màu đậm trên nền nhạt hoặc trên nền chính.
- Mọi vật thể (thẻ, viên gạch, sổ, hoá đơn, biển) kiểu giao diện thường: viền mảnh `1.5px solid #D2CCBE` và bóng mềm (`--bong`), không dùng viền đen dày hay bóng đổ cứng. Dùng lớp `.th-vat`, `.th-gach`, `.th-cuaso`.
- Nhân vật và đạo cụ AI (PNG nền trong) giữ viền riêng của ảnh, chỉ thêm bóng mềm (`.th-nhanvat`). Nhân vật không mặc trắng tinh, đỏ hoặc xanh lá.
- Chữ trong ảnh luôn là chữ HTML, không để AI vẽ chữ.
- Mọi hiệu ứng neo vào mốc từng từ của giọng đọc: hình hiện trước lời khoảng 0,1 giây, không bao giờ sau lời.

## Typography

Be Vietnam Pro cho chữ thường và tiêu đề; JetBrains Mono cho code. `@font-face` khai báo trong `index.html` (do `build_index.py` chèn) và trong từng file cảnh (dán `compositions/frames/_font-face.css`).
