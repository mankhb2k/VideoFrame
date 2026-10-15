# Cảnh 4: Vòng lặp

## Đoạn 1: Ba món trên quầy (25 giây)

**[Lời dẫn]** “Ở cảnh trước, ông Sơn đã biết dùng câu điều kiện để chọn đường đi. Bây giờ một khách đặt ba món lên quầy: gạo ST25, muối và nước mắm. Ông Sơn muốn biết món nào đang khuyến mãi, rồi tính xem khách phải trả bao nhiêu. Với ba món, ông còn tự làm được.”

## Đoạn 2: Kiểm khuyến mãi từng món (40 giây)

**[Lời dẫn]** “Ông viết một câu điều kiện cho từng món: nếu là muối thì báo khuyến mãi giảm 2000 đồng, không thì báo không khuyến mãi.”

> Ghi chú dựng: đoạn này hiện một loạt dữ liệu rất dài trong VS Code, người xem phải cuộn liên tục qua hàng loạt khối if-else giống nhau. Cảm giác choáng ngợp là có chủ đích, để khi giải pháp vòng lặp xuất hiện ở Đoạn 3, người xem thấy rõ giá trị của nó.

```python
mon_1 = "gạo ST25"
if mon_1 == "muối":
    print("Muối đang khuyến mãi, giảm 2000đ")
else:
    print("Không khuyến mãi")

mon_2 = "muối"
if mon_2 == "muối":
    print("Muối đang khuyến mãi, giảm 2000đ")
else:
    print("Không khuyến mãi")

mon_3 = "nước mắm"
if mon_3 == "muối":
    print("Muối đang khuyến mãi, giảm 2000đ")
else:
    print("Không khuyến mãi")
```

**[Dừng 2 giây]** người xem thấy ba khối giống hệt nhau, chỉ khác tên món.

**[Lời dẫn]** “Ba món thì ba khối. Nếu có một trăm món thì sao? Đoạn code sẽ dài đến mức không ai đọc nổi. Và nếu cần đổi điều kiện, ta phải sửa một trăm chỗ.”

## Đoạn 3: Cùng việc đó, viết một lần (40 giây)

**[Lời dẫn]** “Giỏ hàng được đặt vào một biến tên là gio_hang, rồi in ra để thấy cả giỏ. Thay vì viết lại từng khối if/else, trong lập trình ta có khái niệm vòng lặp, viết một lần rồi nhờ máy làm lần lượt với từng món trong giỏ. Ở đây ta có ‘for’, nghĩa là ‘với mỗi’. Dòng for có chữ ‘mon’: đây là tên tạm máy đặt cho từng món khi món đó đi qua. Lần đầu, mon là gạo ST25. Lần hai, mon là muối. Lần ba, mon là nước mắm.”

> Ghi chú dựng: chuyển cảnh từ khối if-else dài sang một khối for ngắn, với cùng nội dung kiểm tra.

```python
gio_hang = ["gạo ST25", "muối", "nước mắm"]
for mon in gio_hang:
    if mon == "muối":
        print("Muối đang khuyến mãi, giảm 2000đ")
    else:
        print("Không khuyến mãi")
```

**[Dừng 2 giây]** người xem đọc dòng `for`, và `mon` được tô sáng.

**[Lời dẫn]** “Ba món, một khối. Đây chính là lý do ta cần vòng lặp: để viết việc lặp lại một lần, và từng bước.”

## Đoạn 4: Băng chuyền tính tiền (40 giây)

**[Lời dẫn]** “Ông Sơn mua một chiếc băng chuyền để tính tiền. Khách đặt món lên, băng chuyền chở tên từng món, còn máy tra giá trong sổ giá. Ông chỉ cài cho máy một quy tắc: với mỗi món trên băng chuyền, cộng giá vào tổng tiền. Máy sẽ làm đi làm lại cùng một việc cho từng món.”

```python
gia_ban = {"gạo ST25": 30000, "muối": 8000, "nước mắm": 45000}
bang_chuyen = ["gạo ST25", "muối", "nước mắm"]
tong_tien = 0
for mon in bang_chuyen:
    tong_tien = tong_tien + gia_ban[mon]
print("Tổng tiền:", tong_tien)
```

**[Dừng 2 giây]** người xem đọc dòng `for`, và `mon` được tô sáng. Mon vẫn là tên tạm của từng món, như đã thấy ở đoạn trước.

**[Lời dẫn]** “Ban đầu chưa có món nào được cộng, nên ta gán tổng tiền bằng 0. Bên trái dấu bằng là nơi ghi số mới. Máy làm đúng ba bước: lấy tổng tiền đang có, cộng giá của món, rồi ghi kết quả lại vào tổng tiền. Với mỗi món trên băng chuyền, máy tra giá của món đó rồi cộng vào tổng tiền. Hãy xem cách từng món đi qua:”

```text
mặc định: tổng tiền = 0
gạo ST25 (30.000): tổng tiền = 30.000
muối (8.000):      tổng tiền = 38.000
nước mắm (45.000): tổng tiền = 83.000
```

**[Lời dẫn]** “Mỗi món đi qua một lần, và tổng tiền được cộng dồn. Ông không cần biết có bao nhiêu món, băng chuyền tự chạy hết rồi dừng.”

## Đoạn 5: Quét đến khi băng chuyền hết (40 giây)

**[Lời dẫn]** “Băng chuyền chạy ở quầy, nhưng ông không biết trước sẽ có bao nhiêu món đang chờ. Ông chỉ cần hỏi: băng chuyền còn món nào không? Lúc đó ta dùng ‘while’, nghĩa là ‘trong khi’. Trong khi còn món trên băng chuyền, thì lấy món đầu tiên ra và quét. Bạn thử đoán xem khi nào máy sẽ dừng?”

```python
bang_chuyen = ["gạo ST25", "muối", "nước mắm"]
while len(bang_chuyen) > 0:
    mon = bang_chuyen.pop(0)
    print("Quét:", mon)
print("Băng chuyền đã hết món")
```

**[Dừng 2 giây]** người xem theo dõi `bang_chuyen` ngắn dần sau mỗi lần quét: 3 món, 2 món, 1 món, rồi 0.

**[Lời dẫn]** “Mỗi lần quét, một món được lấy ra khỏi băng chuyền. Khi băng chuyền hết món, điều kiện ‘còn món’ sai, và vòng lặp dừng. Nếu quên lấy món ra, băng chuyền không bao giờ hết, và máy sẽ quét mãi không dừng. Đó là lỗi vòng lặp vô hạn, và cả lập trình viên giỏi cũng từng gặp.”

## Đoạn 6: Khi nào dùng for: có sẵn danh sách (60 giây)

**[Lời dẫn]** “Trong thực tế, chọn sai loại vòng lặp cũng giống như việc bạn dùng dao mổ trâu để gọt hoa quả, hoặc lấy tay không đi bắt cá mập. Có hai loại bài toán rạch ròi, và mỗi loại bắt buộc phải dùng đúng vũ khí của nó.”

**[Lời dẫn]** “Loại thứ nhất: đã biết trước số lượng hoặc có sẵn một danh sách cố định. Ví dụ: gửi email xác nhận cho ba người An, Bình, Chi. Món này sinh ra là dành riêng cho for. Đây là cách dùng for, chuẩn bài, thanh thoát.”

```python
nguoi_nhan = ["An", "Bình", "Chi"]
for ten in nguoi_nhan:
    print("Gửi email xác nhận cho", ten)
```

**[Lời dẫn]** “Nhìn xem: for tự động bốc từng người ra đi qua danh sách một cách mượt mà, ngắn gọn, không rườm rà.”

**[Lời dẫn]** “Còn đây là cách cố chấp dùng while cho danh sách có sẵn: rườm rà, máy móc.”

```python
nguoi_nhan = ["An", "Bình", "Chi"]
while len(nguoi_nhan) > 0:
    ten = nguoi_nhan.pop(0)
    print("Gửi email xác nhận cho", ten)
```

**[Lời dẫn]** “Dùng while, bạn phải tự đi kiểm tra danh sách còn người không, rồi dùng lệnh ‘pop’ để lôi từng người vứt đi. Code dài dòng hơn, khó đọc hơn, và sau khi chạy xong thì cái danh sách gốc cũng... bay màu luôn vì bị lột sạch!”

**[Lời dẫn]** “Tóm lại, với những việc đã biết trước số lượng hay có sẵn danh sách, cứ for mà táng, tội gì phải dùng while cho khổ sở.”

## Đoạn 7: Khi nào dùng while: không biết trước số lần (70 giây)

**[Lời dẫn]** “Loại thứ hai: không biết trước khi nào dừng, phụ thuộc hoàn toàn vào kết quả thực tế. Ví dụ: ứng dụng tải trang khi mạng yếu, không ai biết lần thứ mấy sẽ thành công. Lúc này, dùng for là một thảm họa. Đây là cách cố chấp dùng for, đoán mò số lần, dễ sập bẫy. Ta cố tình đoán là sẽ thử ba lần. Chữ ‘break’ nghĩa là thoát khỏi vòng lặp ngay.”

```python
# Cố tình đoán mò danh sách có 3 lần thử
ket_qua_thu = ["lỗi", "lỗi", "thành công"]

for lan in ket_qua_thu:
    if lan == "thành công":
        print("Kết nối thành công")
        break
    else:
        print("Lỗi, thử lại")
```

**[Lời dẫn]** “Hậu quả là gì? Nếu mạng hôm nay xui xẻo cần đến 5 lần thử mới thành công, thì vòng lặp for chỉ có sẵn 3 phần tử. Khi hết danh sách, for dừng lại, và không hề biết mạng vẫn đang lỗi. Nó dừng âm thầm, không báo gì thêm.”

**[Lời dẫn]** “Còn đây là while chuẩn chỉnh: thử đến khi thành công, nhưng có giới hạn 5 lần. Dấu chấm than bằng nghĩa là ‘khác’.”

```python
ket_qua = "lỗi"
so_lan = 0

while ket_qua != "thành công" and so_lan < 5:
    so_lan = so_lan + 1
    print("Lần thử", so_lan, "- mạng lỗi, đang thử lại...")
    # Giả lập: lần thứ 7 mạng mới tốt
    if so_lan == 7:
        ket_qua = "thành công"

if ket_qua == "thành công":
    print("Kết nối thành công, vào web thôi!")
else:
    print("Thử 5 lần vẫn lỗi, báo người dùng")
```

**[Lời dẫn]** “Dùng while, ta không cần đoán mò số lần. Cứ giao cho nó quy tắc: ‘miễn là chưa thành công và chưa hết 5 lần thì còn thử tiếp’. Ở đây ta giả sử lần thứ bảy mạng mới tốt. Mạng thật thì máy không biết trước điều đó, nên ta đặt giới hạn 5 lần. Hết lượt mà vẫn lỗi, máy báo người dùng.”

## Chốt cảnh (20 giây)

**[Lời dẫn]** “Tóm lại, quy tắc vàng gói gọn trong hai câu:
Có sẵn danh sách, biết trước số lần dùng for cho nhanh gọn, an toàn.
Không biết trước bao giờ xong, chờ đến khi đạt mục đích hoặc điều kiện thay đổi dùng while để linh hoạt nắm đằng chuôi. Vậy là chúng ta đã có được viên gạch thứ tư: vòng lặp.”
