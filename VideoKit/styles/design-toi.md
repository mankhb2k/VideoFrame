---
name: Khuôn tối VideoKit (video công nghệ, nhiều code)
colors:
  background: "#0B1020"
  surface: "#16213E"
  text: "#E2E8F0"
  text-muted: "#94A3B8"
  accent: "#F59E0B"
  ok: "#10B981"
  error: "#EF4444"
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
  code-window:
    background: "#0F1730"
    radius: 16px
---

## Overview

Nền xanh đen sâu để chữ và code nổi. Màu có nghĩa: đỏ chỉ để báo lỗi, xanh ngọc cho điều ổn, hổ phách là màu nhấn chính; không dùng màu để trang trí.
Mỗi dự án có thể ghi đè bảng này trong `video/design.md` (đổi `accent`, thêm màu riêng của nhân vật/chủ đề).

## The Frame

Khung 1920×1080, lề an toàn 96 px. Một tiêu điểm mỗi cảnh. Chữ chính 56 px trở lên, chú thích 28 px trở lên, code 30 px trở lên.
Góc phải bên dưới dành cho logo kênh (132 px, cách mép 44 px): không đặt nội dung vào vùng đó.

## Composition Rules

- Mỗi đoạn code tối đa 6 dòng; dòng đang được nói sáng lên, các dòng còn lại mờ đi.
- Nhân vật giữ nguyên hình dạng và vị trí tương đối giữa các cảnh.
- Mọi hiệu ứng neo vào mốc từng từ của giọng đọc: hình hiện trước lời khoảng 0,1 giây, không bao giờ sau lời.

## Typography

Be Vietnam Pro cho chữ thường và tiêu đề (nhúng từ `assets/fonts/`, giấy phép OFL, đủ dấu tiếng Việt); JetBrains Mono cho code.
Khai báo `@font-face` trong `index.html` và trong từng file cảnh (dán `templates/font-face.css`).
