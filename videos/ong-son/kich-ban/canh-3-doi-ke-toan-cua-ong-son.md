# Cảnh 3: Đội kế toán của ông Sơn

## Đoạn 1: Làm ăn thuận lợi, bán thêm hàng (20 giây)

**[Hình]** Tiệm đông khách, bảng hiệu mới “Tạp hoá Sơn”. Xe tải dỡ thêm thùng nước mắm, bao muối, gói mì chính.

**[Lời dẫn]** “Gạo bán chạy, ông Sơn làm ăn thuận lợi. Ông không chỉ bán gạo nữa, mà nhập thêm nước mắm, muối, mì chính. Sáu mặt hàng, rồi mười, rồi hai mươi.”

## Đoạn 2: Nhớ trong đầu bắt đầu sai (30 giây)

**[Hình]** Cô Lan cau mày nhìn món hàng, giá hiện lên lộn xộn trên đầu cô: “nước mắm 45? hay 54?”. Anh Tâm đứng trước kệ trống, hỏi: “Trong kho còn bao nhiêu chai?”. Không ai trả lời được.

**[Lời dẫn]** “Hai mươi mặt hàng, mỗi mặt hàng một giá, một số lượng trong kho. Cô Lan bắt đầu nhớ nhầm giá. Anh Tâm không biết kho còn bao nhiêu để lấy ra xếp. Nhớ trong đầu thì được với ba loại gạo, nhưng với hai mươi mặt hàng thì không còn được nữa.”

## Đoạn 3: Thuê đội kế toán (40 giây)

**[Hình]** Ông Sơn thuê một phòng kế toán nhỏ với ba người, bàn đầy sổ sách. Sơ đồ: cô Lan và anh Tâm cùng gửi câu hỏi vào phòng kế toán, kế toán trả lời.

**[Lời dẫn]** “Ông Sơn thuê một đội kế toán. Việc của họ không phải bán hàng, không phải xếp kệ. Việc của họ là giữ sổ: mặt hàng nào giá bao nhiêu, kho còn bao nhiêu, hôm nay bán gì. Cô Lan cần giá thì hỏi kế toán. Anh Tâm cần biết số lượng trong kho thì hỏi kế toán. Đội kế toán chính là database.”

## Đoạn 4: Kế toán phân loại, khoá chính (35 giây)

**[Hình]** Kế toán dán mã lên từng mặt hàng: G001, NM01, MC01. Hai chai nước mắm khác hãng nhận hai mã khác nhau.

| Mã | Tên hàng | Giá bán | Còn trong kho |
|---|---|---|---|
| G001 | Gạo ST25 | 30.000 | 120 |
| G002 | Gạo Jasmine | 20.000 | 200 |
| NM01 | Nước mắm hãng A | 45.000 | 60 |
| NM02 | Nước mắm hãng B | 38.000 | 80 |
| M01 | Muối | 8.000 | 90 |

**[Lời dẫn]** “Việc đầu tiên của kế toán là gán cho mỗi mặt hàng một mã riêng, không bao giờ trùng. Vì hai chai đều tên ‘nước mắm’, hỏi ‘nước mắm giá bao nhiêu’ thì kế toán không biết trả lời loại nào. Hỏi ‘NM01 giá bao nhiêu’ thì chỉ có đúng một đáp án. Mã riêng đó, trong database, gọi là khoá chính. Giống như số căn cước của mỗi người: tên có thể trùng, số thì không.”

## Đoạn 5: Hoá đơn chỉ ghi mã, khoá ngoại (45 giây)

**[Hình]** Kế toán mở cuốn sổ thứ hai, ghi hoá đơn. Mỗi dòng chỉ viết mã hàng. Mũi tên nối mã trong sổ hoá đơn về đúng dòng có mã đó trong sổ hàng hoá.

| Mã hoá đơn | Mã hàng | Số lượng | Ngày |
|---|---|---|---|
| HD001 | G001 | 10 | 14/10 |
| HD001 | NM01 | 2 | 14/10 |
| HD002 | M01 | 1 | 14/10 |

**[Lời dẫn]** “Cuốn sổ thứ hai ghi hoá đơn: khách nào mua gì. Để ý: kế toán không chép lại tên hàng và giá, mà chỉ ghi mã. Muốn biết ‘NM01’ là gì, giá bao nhiêu, lần theo mã sang cuốn sổ hàng hoá. Cột ‘Mã hàng’ trong sổ hoá đơn, mượn mã từ cuốn sổ khác, gọi là khoá ngoại. Lý do ghi như vậy: hôm nay đổi giá nước mắm, kế toán chỉ sửa một chỗ trong sổ hàng hoá, mọi hoá đơn tự đúng theo. Không có chuyện chỗ này ghi 45, chỗ kia ghi 54.”

## Đoạn 6: Cô Lan không cần nhớ nữa (30 giây)

**[Hình]** Cô Lan cầm giỏ hàng của khách, quay sang cửa sổ phòng kế toán hỏi, nhận về tờ giấy ghi giá. Cô tính tiền, không còn nhăn mặt.

```python
gia = hoi_ke_toan("gia_ban", ma="NM01")      # kế toán trả: 45000
tinh_tien(gia, so_ky=2)                      # 90000

con_lai = hoi_ke_toan("con_trong_kho", ma="NM01")   # anh Tâm hỏi
```

**[Lời dẫn]** “Bây giờ cô Lan hỏi kế toán giá của mã NM01 rồi mới tính tiền. Anh Tâm hỏi kế toán kho còn bao nhiêu NM01 rồi mới biết có cần lấy thêm không. Không ai phải nhớ trong đầu nữa. Hàm làm việc, kế toán giữ thông tin.”

## Đoạn 7: Cú lật, nhớ trong đầu và ghi vào sổ (25 giây)

**[Hình]** Cô Lan nghỉ việc, ngày mai không còn ai nhớ giá. Chuyển cảnh: phòng kế toán, cuốn sổ vẫn nằm trên bàn, người mới đến mở ra là biết.

**[Lời dẫn]** “Còn một lý do nữa phải thuê kế toán. Cô Lan nhớ trong đầu thì cô Lan nghỉ, thông tin biến mất. Máy tính cũng vậy: biến chỉ sống lúc máy đang chạy, tắt đi là quên sạch. Kế toán ghi vào sổ thì ai đến thay cũng đọc được, điện tắt rồi bật lại vẫn còn nguyên. Biến là trí nhớ tạm. Database là trí nhớ lâu dài.”

## Chốt cảnh (15 giây)

**[Lời dẫn]** “Giờ tiệm ông Sơn có đủ ba thứ: nhãn để gọi tên, nhân viên để làm việc, kế toán để giữ sổ. Nhưng ba thứ này đang đứng rời nhau. Điều gì biến một tiệm tạp hoá thành một hệ thống? Mời bạn nhìn tiệm từ trên cao.”
