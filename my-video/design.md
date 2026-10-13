---
name: Gia phả và Lego
colors:
  background: "#0B1020"
  background-pop: "#121A33"
  surface: "#16213E"
  text: "#E2E8F0"
  text-muted: "#94A3B8"
  oop: "#F59E0B"
  pop: "#10B981"
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
  lego-block:
    radius: 10px
    stud: circle on top edge
  tree-node:
    radius: 999px
    stroke: "2px"
---

## Overview

Nền xanh đen sâu để code nổi. Hai phe có hai chất liệu: OOP là cây gia phả hổ phách, sâu và phân nhánh; POP là khối Lego xanh ngọc, phẳng và khớp nhau. Mọi cảnh dùng chung một nền; phần POP sáng hơn nền chung một nấc (`background-pop`) để người xem cảm nhận "màn hình sạch lại".

## The Frame

Khung 1920×1080, lề an toàn 96 px. Một tiêu điểm mỗi cảnh. Chữ lớn tối thiểu 56 px cho câu chính, 28 px cho chú thích, code 30 px trở lên.

## Composition Rules

- Màu có nghĩa: đỏ là lỗi, xanh ngọc là ổn/POP, hổ phách là OOP, không dùng làm trang trí.
- Ba nhân vật Sparrow (chim sẻ), Penguin (cánh cụt), Drone là hình phẳng, cùng kích thước và cùng vị trí giữa hai bên so sánh.
- Con khỉ cầm quả chuối là motif lặp lại ở phần 0, 2 và 7; hình dáng giữ nguyên, chỉ đổi quy mô.
- Mỗi đoạn code hiển thị tối đa 6 dòng; dòng đang nói được tô sáng, các dòng còn lại mờ đi.

## Typography

Be Vietnam Pro cho tiêu đề và chữ thường (nhúng từ `assets/fonts/`, giấy phép OFL, đủ dấu tiếng Việt, ba độ đậm 500/700/800); JetBrains Mono cho code. Mọi chữ tiếng Việt trên màn hình dùng Be Vietnam Pro, không dùng font hệ thống.
