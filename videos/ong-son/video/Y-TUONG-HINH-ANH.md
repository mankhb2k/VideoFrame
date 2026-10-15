# Ý tưởng hình ảnh: Ông Sơn và tiệm tạp hoá

Bản nháp để duyệt trước khi tạo ảnh. Chưa có ảnh nào được tạo. Mục tiêu của hình ảnh là giúp người mới học lập trình **thấy** từng khái niệm, nên mỗi khái niệm gắn với một vật hoặc một người trong tiệm, và lặp lại đúng hình ấy ở mọi cảnh sau.

## 1. Ý tưởng chủ đạo

1. **Tiệm là một mô hình cắt ngang (diorama).** Nhìn thẳng từ phía trước, như cắt đôi một căn nhà: người xem thấy quầy, kệ, kho, phòng kế toán cùng lúc. Cùng một bối cảnh xuyên suốt, mỗi cảnh **thêm** một thứ (quầy, kệ, phòng kế toán, tờ lịch...). Người xem không phải làm quen lại chỗ mới.
2. **Hai thế giới cạnh nhau.** Bên trái: thế giới tiệm (hoạt hình). Bên phải: thế giới code (cửa sổ code). Một dòng code sáng lên đúng lúc vật tương ứng trong tiệm sáng lên. Người xem nối được "cái nhãn" với `gia_gao_st25`.
3. **Kệ năm viên gạch** ở góc trên bên trái. Mỗi khái niệm xong thì một viên gạch mang tên nó rơi xuống kệ. Cảnh 5 kệ đã đủ năm viên, và câu "tiệm chỉ xây từ năm viên gạch" thành hình ảnh có sẵn.
4. **Màu theo khái niệm** (cũng là bảng tô màu đoạn code ở Cảnh 0 và Cảnh 5): người xem học "màu cam là if/else" mà không phải đọc chữ.
5. **Camera bay lên ở Cảnh 5:** từ mái tiệm lên sơ đồ mặt bằng, rồi nhân bản thành toà nhà. Đây là cú "nhìn từ trên cao" cho cả video.

## 2. Bảng màu và quy tắc (thương hiệu THO CODE, nền trắng ngà)

Nguồn duy nhất: ảnh [bang-mau-thuong-hieu.png](../../../VideoKit/brand/bang-mau-thuong-hieu.png), `VideoKit/templates/thuong-hieu.css`, `VideoKit/styles/design-sang.md`.

- **Nền trắng ngà `#F8F7F4`** (không dùng trắng tinh), **chữ thường đen `#111113`**. **Màu chữ theo nghĩa, không theo thương hiệu:** giá liệt kê xanh dương đậm `#1E3A8A` (hoặc đen), **giá bán và tổng xanh lá đậm `#15803D`**, **cảnh báo đỏ `#B91C1C`**. Cam THO CODE `#F26A21` (từ logo) chỉ để tô nền, logo, gạch chân, không làm màu chữ.
- **Vật thể kiểu giao diện thường:** viền mảnh và bóng mềm, không dùng viền đen dày hay bóng đổ cứng (kiểu game).
- **Code luôn nằm trong cửa sổ nền đen kiểu macOS có 3 chấm** ở thanh tiêu đề (đỏ, vàng, xanh, chỉ là trang trí), tối đa 6 dòng hiển thị.
- **Năm màu khái niệm** (tươi để tô, đậm để làm chữ, nhạt để làm nền thẻ): BIẾN vàng `#FACC15`, HÀM xanh dương `#3B82F6`, DATABASE tím `#8B5CF6`, IF/ELSE lục lam `#14B8A6`, VÒNG LẶP hồng `#EC4899`. Đây cũng là bảng tô màu đoạn code ở Cảnh 0 và Cảnh 5.
- Đỏ chỉ để báo lỗi, xanh lá chỉ cho điều ổn, luôn kèm biểu tượng. **Nhân vật không mặc đỏ, xanh lá hoặc trắng tinh.** Cái "khoanh đỏ" ngày 27/11 trong kịch bản đổi thành khoanh cam.
- Chữ trên bảng hiệu, nhãn giá, tờ giấy luôn là **chữ HTML**, không để AI vẽ chữ. Không dùng logo thật: Angular, React, Zustand chỉ hiện dạng hộp có tên.

## 3. Bố cục màn hình

- Cảnh có code: tiệm chiếm khoảng 58% bên trái, code bên phải (tối đa 6 dòng, chữ 30 px trở lên).
- Cảnh không có code: tiệm chiếm toàn khung.
- Kệ năm viên gạch: góc trên bên trái, nhỏ, cố định. Logo ở góc phải bên dưới như mọi video.

## 4. Tiệm lớn dần theo cảnh

| Cảnh | Tiệm trông thế nào | Thêm vào |
|---|---|---|
| 0 | chưa có tiệm, chỉ có đoạn code | |
| 1 | mặt bằng trống, rồi có ba thùng gạo trên nền | thùng gạo, nhãn giá |
| 2 | có quầy thu ngân, một kệ gạo, một góc kho | cô Lan, anh Tâm, tờ quy tắc dán tường |
| 3 | biển "Tạp hoá Sơn", kệ đầy hàng, một **phòng kế toán** có cửa sổ | hàng mới, sổ sách |
| 4 | như Cảnh 3, thêm tờ lịch treo tường và máy quét | lịch, giỏ hàng, tờ luật |
| 5 | nhìn từ trên cao thành sơ đồ phẳng, rồi toà nhà, rồi biển "Bún Sơn" | nồi nước dùng, rổ bún, bộ khung |

## 5. Nhân vật (AI tạo, nền trong suốt)

Tạo theo từng người: một ảnh gốc, duyệt xong mới tạo các dáng khác bằng cách chỉnh sửa ảnh gốc, để mặt và quần áo giữ nguyên. Ngoại hình dưới đây là **đề xuất**, bạn sửa được.

| Nhân vật | Ngoại hình đề xuất | Dáng cần tạo |
|---|---|---|
| **Ông Sơn** | khoảng 50 tuổi, hơi đậm người, áo sơ mi xanh nhạt xắn tay (không trắng để nổi trên nền trắng ngà), tạp dề cam | 1 cầm xấp tiền; 2 đứng nghiêm nhìn mặt bằng; 3 mồ hôi, bận rộn; 4 cầm cốc trà đứng quan sát; 5 viết giấy (bút đỏ); 6 gọi to, tay chỉ; 7 thất vọng nhìn tờ giấy; 8 nhìn thẳng camera |
| **Cô Lan** | khoảng 28 tuổi, tóc đen buộc đuôi ngựa, áo xanh da trời nhạt | 1 đứng quầy thu ngân; 2 cau mày nghĩ giá; 3 mỉm cười nhẹ nhõm; 4 cầm máy quét; 5 ngẩng lên hỏi |
| **Anh Tâm** | khoảng 25 tuổi, gầy, áo xám, mũ lưỡi trai vàng | 1 đứng chờ; 2 khuân bao gạo; 3 gãi đầu nhìn kệ trống; 4 xếp hàng lên kệ |
| **Chị kế toán (trưởng)** | khoảng 35 tuổi, đeo kính, áo tím nhạt | 1 ngồi ghi sổ; 2 đưa tờ giấy qua cửa sổ; 3 dán mã lên hàng |
| **Hai trợ lý kế toán** | một nam một nữ, áo tím đậm và xám | 1 dáng ngồi mỗi người |
| **Anh Hùng** | khoảng 30 tuổi, áo xám xanh, trông mệt | 1 đội năm cái mũ, hai tay bận đủ thứ; 2 vẫy tay chào rồi đi |
| **Khách hàng** | một bà cầm túi, một thanh niên | 1 đứng chờ mỗi người; 1 cầm giỏ đầy |

Khoảng **30 ảnh nhân vật**. Năm cái mũ của anh Hùng nằm chung trong ảnh (không có chữ); nhãn "thu ngân, thủ kho, bán hàng, kế toán, bảo vệ" ghép bằng HTML.

## 6. Đạo cụ (AI tạo, nền trong suốt)

- **Gạo và hàng:** bao gạo, thùng gạo mở (3 loại, mỗi loại khác màu bao), chai nước mắm (2 hãng, 2 kiểu chai), bao muối, gói mì chính, giỏ hàng đầy.
- **Thiết bị:** máy tính tiền cũ, máy tính tiền đời mới màn hình cảm ứng, máy quét mã, cốc trà.
- **Tiệm:** xe tải chở hàng, cái kệ (một ảnh trống, một ảnh đầy), quầy thu ngân, hai cuốn sổ (sổ hàng hoá và sổ hoá đơn, bìa khác màu), bàn kế toán đầy sổ.
- **Cảnh 5:** nồi nước dùng, rổ bún, xấp tiền (20 triệu).
- **Hình lớn (nền đặc, khung 16:9):** ngoại thất mặt bằng trống, ngoại thất tiệm tạp hoá, ngoại thất tiệm bún. Bảng hiệu để trống, chữ ghép sau.

Khoảng **24 ảnh đạo cụ và 3 hình lớn**.

## 7. Phần tôi tự dựng bằng HTML/SVG (không cần AI)

- Khung diorama (tường, sàn, đường chia ô), cửa sổ phòng kế toán, mặt bằng phẳng và toà nhà isometric ở Cảnh 5.
- Cửa sổ code, bảng (sổ hàng hoá, sổ hoá đơn), hoá đơn giấy, nhãn giá, tờ quy tắc, tờ lịch, biển hiệu, bong bóng nói và bong bóng suy nghĩ ("45? hay 54?").
- Biểu tượng: năm viên gạch và kệ, ngã ba đường, vòng tròn, hộp "hàm" (hai đầu vào, một đầu ra), mũi tên nối khoá ngoại, dây chuyền, hộp bộ khung, biểu tượng ứng dụng mua sắm/ngân hàng/mạng xã hội (tự vẽ đơn giản, không dùng logo thật).
- Biểu đồ lãi giảm về 0 ở cuối Cảnh 4, các hiệu ứng gõ chữ, sáng dòng code, tô màu đoạn code.

## 8. Hình chủ đạo và chuyển động đặc trưng từng cảnh

- **Cảnh 0:** cửa sổ code nền đen (3 chấm macOS) chiếm gần toàn khung trên trang trắng ngà, đoạn code 13 dòng cuộn nhẹ, chữ "Bạn thấy gì?". Cuối cảnh chữ "20" trong code phóng to thành "20.000.000đ" và cửa sổ thu nhỏ dần thành một khung bên phải, nhường chỗ cho thế giới tiệm.
- **Cảnh 1:** ông Sơn cầm tiền trước mặt bằng trống; xe tải đổ bao gạo thành đống; ba nhãn dán lên ba thùng cùng lúc với ba dòng code sáng; phiên bản a, b, c đặt cạnh nhau, bóng suy nghĩ "a là gì?" hiện trên đầu nhân viên mới. Viên gạch BIẾN rơi xuống kệ.
- **Cảnh 2:** ông Sơn bận rộn có vạch chuyển động quanh tay; cô Lan ngồi trong hộp "hàm" có hai đầu vào (giá, số ký) và một đầu ra (tổng tiền); anh Tâm nhìn kệ, tờ quy tắc dán tường; dây chuyền khách, thu ngân, kệ có dòng code sáng theo từng bước; anh Hùng đội năm mũ, "nghỉ rồi" thì cả tiệm đứng hình.
- **Cảnh 3:** thought bubble lộn xộn trên đầu cô Lan; phòng kế toán xuất hiện bên phải tiệm; dán mã lên hàng; hai cuốn sổ cạnh nhau, mũi tên nối mã; ô giá đổi 45 thành 54, các dòng hoá đơn nháy theo.
- **Cảnh 4:** tờ lịch 27/11 khoanh cam; ngã ba đường biến hình từ hai nhánh "mưa/không mưa"; hai hoá đơn cạnh nhau; cô Lan quét món, vòng tròn hồng quay lại; tuần sau tờ giấy "GIẢM 5%" vẫn dán, biểu đồ lãi tụt về 0.
- **Cảnh 5:** camera bay lên khỏi mái, tiệm thu thành sơ đồ phẳng có năm viên gạch; nhân bản thành toà nhà; biển "Tạp hoá Sơn" đổi thành "Bún Sơn" trong khi quầy, kho, phòng kế toán đứng yên; hộp bộ khung; quay lại đoạn code Cảnh 0 và tô màu năm phần.

## 9. Quy trình tạo ảnh và chi phí ước tính

1. Tạo **5 ảnh gốc** (ông Sơn, cô Lan, anh Tâm, chị kế toán, anh Hùng) với model `gpt-image-2.5-flare`, gửi kèm ảnh nhân vật có sẵn làm tham chiếu phong cách. Bạn duyệt ngoại hình.
2. Sau khi duyệt, tạo các dáng còn lại bằng chỉnh sửa ảnh gốc.
3. Tạo đạo cụ và 3 hình lớn.
4. Lưu vào `VideoKit/characters/` (ông Sơn có thể xuất hiện lại ở video sau) cùng `prompt.md`, rồi `sync_assets.py` chép vào dự án.

Tổng khoảng **57 ảnh**. Ước tính khoảng $0,9, kể cả tạo lại khoảng 40% (nhân vật và đạo cụ khoảng $0,014 mỗi ảnh, hình lớn khoảng $0,04). Đây là ước tính, số thật ghi vào sổ chi phí.

## 10. Điểm cần bạn quyết

1. Ngoại hình ông Sơn, cô Lan, anh Tâm... như mục 5, hay bạn muốn khác (tuổi, trang phục)?
2. Tiệm dựng bằng SVG kết hợp đạo cụ AI (đề xuất, dễ hoạt hình và đồng nhất), hay muốn AI vẽ toàn bộ nền tiệm từng cảnh?
3. Màu năm viên gạch có ổn không? Riêng khoanh đỏ ngày 27/11 đổi thành cam có được không?
4. Bắt đầu bằng 5 ảnh gốc để duyệt trước chứ?
