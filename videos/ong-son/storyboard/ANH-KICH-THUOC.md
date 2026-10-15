# Ảnh: kích thước và vùng nhìn thấy

Cột *nội dung* là rộng×cao phần nhìn thấy so với cả ảnh; cột *khung* là góc trên-trái → dưới-phải (0..1) của phần nhìn thấy. Đặt ảnh bằng `vk.nv(parent,{src,size,cx,base})` (đáy ảnh tại `base`) rồi tính theo cột *khung* khi cần căn chân hoặc căn mép.

| id | ảnh | nội dung | khung | mô tả |
|---|---|---|---|---|
| `anh-hung/goc` | 1024×1024 | 0.48×0.97 | 0.26,0.01 → 0.74,0.99 | Anh Hùng, người làm hết mọi việc (ảnh gốc, chưa đội mũ) |
| `anh-hung/nam-mu` | 1024×1024 | 0.51×0.99 | 0.26,0.00 → 0.77,0.99 | đội năm cái mũ, hai tay bận đủ thứ |
| `anh-hung/vay-chao` | 1024×1024 | 0.53×0.98 | 0.26,0.01 → 0.79,0.99 | nghỉ việc, vẫy chào đi ra |
| `anh-tam/goc` | 1024×1024 | 0.35×0.97 | 0.33,0.02 → 0.67,0.99 | Anh Tâm đứng thả lỏng (ảnh gốc) |
| `anh-tam/hoi` | 1024×1024 | 0.45×0.97 | 0.30,0.02 → 0.76,0.99 | giơ tay hỏi 'trong kho còn bao nhiêu chai?' |
| `ba-tu/goc` | 1024×1024 | 0.48×0.97 | 0.25,0.02 → 0.73,0.99 | Bà Tư, khách hàng (ảnh gốc) |
| `binh/boi-roi` | 1024×1024 | 0.44×1.00 | 0.28,0.00 → 0.72,1.00 | bối rối nhìn code a, b, c |
| `binh/goc` | 1024×1024 | 0.45×1.00 | 0.27,0.00 → 0.72,1.00 | Bình, nhân viên mới (ảnh gốc) |
| `chi-hanh/ban-ke-toan` | 1024×1024 | 1.00×0.86 | 0.00,0.14 → 1.00,1.00 | bàn kế toán: Hạnh ghi sổ, An bấm máy, Mai viết giấy, cùng một ảnh |
| `chi-hanh/goc` | 1024×1024 | 0.40×0.98 | 0.30,0.01 → 0.70,0.99 | Chị Hạnh, kế toán trưởng, đứng thả lỏng (ảnh gốc) |
| `co-lan/cau-may` | 1024×1024 | 0.41×0.98 | 0.27,0.01 → 0.68,0.99 | cau mày, nhớ nhầm giá |
| `co-lan/chao-tam-biet` | 1024×1024 | 0.56×0.98 | 0.28,0.01 → 0.83,0.99 | nghỉ việc, ôm hộp đồ vẫy chào |
| `co-lan/goc` | 1024×1024 | 0.41×0.98 | 0.28,0.01 → 0.69,0.99 | Cô Lan đứng thả lỏng (ảnh gốc) |
| `co-lan/mim-cuoi` | 1024×1024 | 0.41×0.98 | 0.28,0.01 → 0.69,0.99 | mỉm cười nhẹ nhõm, đưa tay nhận (tờ giá là HTML bay tới) |
| `co-lan/quay-thu-ngan` | 1024×1024 | 0.69×0.98 | 0.16,0.01 → 0.84,0.99 | Lan đứng sau quầy thu ngân, cầm máy quét (hỏi 'còn món nào không?' bằng bong bóng HTML) |
| `nen/mat-bang-trong` | 1536×864 | 1.00×1.00 | toàn khung | mặt bằng trống nhỏ, sẵn sàng mở tiệm |
| `nen/ngoai-that-tiem` | 1536×864 | 1.00×1.00 | toàn khung | ngoại thất tiệm tạp hoá, bảng hiệu để trống (chữ ghép bằng HTML) |
| `ong-son/ban-ron` | 1024×1024 | 0.54×0.98 | 0.24,0.01 → 0.77,0.99 | mồ hôi nhễ nhại, bấm máy tính, bận rộn |
| `ong-son/cam-tien` | 1024×1024 | 0.43×0.98 | 0.29,0.01 → 0.73,0.99 | cầm xấp tiền 20 triệu, hy vọng |
| `ong-son/goc` | 1024×1024 | 0.46×0.98 | 0.27,0.01 → 0.73,0.99 | Ông Sơn đứng thả lỏng, nhìn người xem (ảnh gốc) |
| `ong-son/khuan-gao` | 1024×1024 | 0.63×0.97 | 0.21,0.01 → 0.84,0.98 | khuân bao gạo ra kệ |
| `ong-son/ngac-nhien` | 1024×1024 | 0.48×0.98 | 0.28,0.01 → 0.76,0.99 | ngạc nhiên / sửng sốt / gọi to (giấy GIẢM 5% là HTML ghép vào tay) |
| `thanh-nien/goc` | 1024×1024 | 0.36×0.99 | 0.32,0.01 → 0.68,0.99 | Thanh niên, khách hàng (ảnh gốc) |
| `vat/bao-gao` | 1024×1024 | 0.80×0.88 | 0.10,0.06 → 0.90,0.94 | bao gạo (nhãn trống; ST25/Jasmine/thường ghép nhãn HTML) |
| `vat/bao-muoi` | 1024×1024 | 0.66×0.93 | 0.17,0.04 → 0.83,0.97 | bao muối |
| `vat/chai-nuoc-mam` | 1024×1024 | 0.31×0.98 | 0.34,0.01 → 0.66,0.99 | chai nước mắm (nhãn trống; hãng A/B ghép nhãn HTML) |
| `vat/gio-hang-trong` | 1024×1024 | 0.94×0.95 | 0.03,0.03 → 0.97,0.97 | giỏ hàng (giỏ đầy = thả đạo cụ vào bằng animation) |
| `vat/goi-mi-chinh` | 1024×1024 | 0.66×0.89 | 0.17,0.05 → 0.83,0.94 | gói mì chính |
| `vat/ke-gao-trong` | 1024×1024 | 0.75×0.97 | 0.12,0.01 → 0.87,0.99 | kệ gạo trống (kệ đầy = thả bao gạo vào bằng animation) |
| `vat/may-tinh-tien-cu` | 1024×1024 | 0.93×0.91 | 0.06,0.04 → 0.99,0.95 | máy tính tiền cũ |
| `vat/may-tinh-tien-moi` | 1024×1024 | 0.80×0.87 | 0.13,0.08 → 0.93,0.95 | máy tính tiền đời mới màn hình cảm ứng |
| `vat/noi-nuoc-dung` | 1024×1024 | 0.94×0.96 | 0.03,0.02 → 0.97,0.98 | nồi nước dùng |
| `vat/ro-bun` | 1024×1024 | 0.92×0.81 | 0.04,0.11 → 0.96,0.92 | rổ bún |
| `vat/so` | 1024×1024 | 0.89×0.87 | 0.05,0.06 → 0.94,0.94 | sổ (bìa trơn; sổ hàng hoá/hoá đơn đổi màu bằng HTML) |
| `vat/thung-gao` | 1024×1024 | 0.92×0.85 | 0.04,0.09 → 0.96,0.94 | thùng gạo (nhãn trống; loại gạo ghép nhãn HTML) |
| `vat/thung-nuoc-mam` | 1024×1024 | 0.91×0.89 | 0.05,0.06 → 0.96,0.95 | thùng nước mắm |
| `vat/xe-tai` | 1024×1024 | 0.98×0.70 | 0.01,0.16 → 0.99,0.85 | xe tải chở hàng (hàng xếp lên sau bằng ảnh khác) |
