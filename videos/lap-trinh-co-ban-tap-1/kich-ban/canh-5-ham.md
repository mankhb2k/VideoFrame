# Cảnh 5: Hàm

## Đoạn 1: Ông Sơn làm không xuể (30 giây)

**[Lời dẫn]** “Đến đây, tiệm đã có biến, danh sách, từ điển, câu điều kiện và vòng lặp. Tiệm đông khách hơn, và ông Sơn làm đủ thứ một mình: tính tiền, xếp hàng lên kệ, nhập hàng, ghi sổ. Mỗi ngày ông làm đi làm lại những việc giống nhau, đến tối thì mệt rã rời. Ông quyết định thuê người, nhưng mỗi người chỉ làm đúng một việc.”

## Đoạn 2: Thuê cô Lan, đóng gói việc tính tiền (40 giây)

**[Lời dẫn]** “Ông thuê cô Lan và giao đúng một việc: tính tiền. Khách đưa cho cô hai thứ: giá một kg và số kg. Cô đưa lại tổng tiền. Ông không cần biết cô tính thế nào, chỉ cần biết đưa gì vào và nhận gì ra. Trong lập trình, cách đóng gói một việc có tên như vậy gọi là hàm.”

**[Dừng 2 giây]** người xem nhớ từ “hàm”.

```python
def tinh_tien(gia_mot_kg, so_kg):
    return gia_mot_kg * so_kg
```

**[Lời dẫn]** “Dòng đầu có chữ ‘def’, nghĩa là ‘định nghĩa’, rồi đến tên hàm là ‘tinh_tien’. Hai thứ trong ngoặc là những thứ cô Lan cần nhận, gọi là tham số. Dòng sau là việc cô làm: nhân giá với số kg, rồi trả lại kết quả. Mỗi ngôn ngữ lập trình sẽ có cách viết khác nhau, nhưng tư duy định nghĩa hàm và tham số là không đổi.”

## Đoạn 3: Dùng hàm (30 giây)

```python
tong_tien = tinh_tien(30000, 10)
print(tong_tien)
```

**[Dừng 2 giây]** người xem đọc dòng gọi hàm, và `tong_tien` được tô sáng.

**[Lời dẫn]** “Khách mua mười kg gạo ST25, giá ba mươi nghìn một kg. Ta gọi tên hàm rồi đưa hai số vào. Kết quả trả về được lưu vào biến ‘tong_tien’, và in ra là ba trăm nghìn. Cô Lan làm việc, còn ông chỉ cần biết đưa gì vào và nhận gì ra.”

## Đoạn 4: Thuê anh Tâm, đóng gói việc xếp kệ (40 giây)

**[Lời dẫn]** “Việc thứ hai là xếp hàng lên kệ. Ông thuê anh Tâm và cũng giao đúng một việc: khi kệ hết hàng thì lấy hàng từ kho ra xếp. Anh chỉ cần biết số kg còn trên kệ, không cần biết khách mua gì.”

```python
def kiem_ke(so_kg_tren_ke):
    if so_kg_tren_ke == 0:
        print("Kệ hết hàng, lấy hàng từ kho ra xếp")
```

**[Dừng 2 giây]** người xem nhớ rằng bên trong hàm này có một câu điều kiện ‘if’ đã học ở cảnh trước.

```python
kiem_ke(5)
kiem_ke(0)
```

**[Lời dẫn]** “Kệ còn 5 kg thì không cần làm gì. Kệ hết hàng, 0 kg, thì anh Tâm mới lấy hàng ra. Lưu ý: cô Lan trả kết quả về cho người gọi, còn anh Tâm chỉ làm việc và báo ra màn hình. Một hàm có thể trả kết quả về, hoặc chỉ làm việc. Vậy là hai người, hai hàm, mỗi người một việc, và tên hàm nói đúng việc họ làm.”

## Đoạn 5: Thuê người quản lý, thêm hàm là thêm người (60 giây)

**[Lời dẫn]** “Ông Sơn không đứng quầy nữa. Ông thuê chị Hương làm quản lý, và việc của chị chỉ có một: mỗi khi có khách, gọi đúng người, theo đúng thứ tự. Chị Hương không tự kiểm kệ, không tự tính tiền. Khách mua mười kg gạo ST25, chị gọi anh Tâm kiểm kệ, rồi gọi cô Lan tính tiền.”

```python
def kiem_ke(so_kg_tren_ke):
    if so_kg_tren_ke == 0:
        print("Kệ hết hàng, lấy hàng từ kho ra xếp")

def tinh_tien(gia_mot_kg, so_kg):
    return gia_mot_kg * so_kg

def quan_ly_quay(gia_mot_kg, so_kg, so_kg_tren_ke):
    kiem_ke(so_kg_tren_ke)
    tong_tien = tinh_tien(gia_mot_kg, so_kg)
    return tong_tien

print(quan_ly_quay(30000, 10, 5))
```

**[Dừng 2 giây]** người xem thấy hàm `quan_ly_quay` không tự làm việc nào. Nó chỉ gọi hai hàm nhỏ theo đúng thứ tự.

**[Lời dẫn]** “Kiểm kệ xong, cô Lan tính ra ba trăm nghìn, và chị Hương đưa kết quả đó lại cho ông Sơn. Người đọc chỉ cần đọc ‘quan_ly_quay’ là biết quy trình, không cần mở từng hàm bên trong.”

**[Lời dẫn]** “Quầy đông dần, ông cần thêm người đóng gói. Ông thuê thêm chị Mai và giao đúng một việc: đóng hàng vào túi. Trong lập trình, thuê thêm người là viết thêm một hàm, rồi viết lại hàm của chị Hương, thêm một dòng để gọi chị Mai ở cuối quy trình.”

```python
def dong_goi(so_kg):
    print("Đóng", so_kg, "kg vào túi")

def quan_ly_quay(gia_mot_kg, so_kg, so_kg_tren_ke):
    kiem_ke(so_kg_tren_ke)
    tong_tien = tinh_tien(gia_mot_kg, so_kg)
    dong_goi(so_kg)
    return tong_tien

print(quan_ly_quay(30000, 10, 5))
```

**[Dừng 2 giây]** người xem thấy hàm `dong_goi` mới, và một dòng gọi mới trong `quan_ly_quay`. Các hàm khác không đổi.

**[Lời dẫn]** “Thêm người mới không cần viết lại người cũ. Chỉ cần thêm một hàm, và thêm một dòng gọi ở chị Hương. Đó là cách một chương trình lớn lên mà vẫn dễ đọc.”

## Đoạn 6: Dùng lại nhiều lần, sửa một chỗ (30 giây)

```python
print(tinh_tien(30000, 10))
print(tinh_tien(8000, 3))
print(tinh_tien(45000, 2))
```

**[Lời dẫn]** “Ba khách, ba lần gọi, cùng một hàm. Nếu tiệm đổi cách tính, ta chỉ sửa một chỗ trong hàm, và cả ba lần gọi tự động đổi theo.”

**[Lời dẫn]** “Nguyên tắc quan trọng: mỗi hàm chỉ làm một việc, và tên hàm nói đúng việc đó. Hàm càng ôm nhiều việc thì càng khó đọc và khó sửa.”

## Chốt cảnh (15 giây)

**[Lời dẫn]** “Hàm đã vào tiệm. Mỗi người làm đúng một việc, có tên nói rõ việc đó, nhận đầu vào và trả kết quả. Người quản lý không cần biết từng người làm thế nào, chỉ cần gọi đúng người, đúng lúc. Đến đây, chúng ta đã có năm viên gạch đầu tiên.”
