# Cảnh 3: Câu điều kiện

## Đoạn 1: Tiệm bắt đầu có khách (25 giây)

**[Lời dẫn]** “Tiệm đã nhớ được hàng và giá bằng danh sách và từ điển. Tiệm khai trương được một tuần thì khách đến ngày càng đông. Có người mua một kg, có người mua mười kg, có người mua cả thùng. Ông Sơn nhận ra một điều: cách tính giá không thể giống nhau cho mọi người.”

**[Lời dẫn]** “Nếu là bạn đứng quầy, bạn sẽ tính giá cho từng người thế nào?”

## Đoạn 2: Ông Sơn viết luật đầu tiên (35 giây)

**[Lời dẫn]** “Ông Sơn quyết định viết một luật rất đơn giản: nếu khách mua từ mười kg trở lên, thì giảm giá. Nếu không, thì giữ giá cũ. Trong lập trình, luật này gọi là câu điều kiện, viết bằng chữ ‘if’, nghĩa là ‘nếu’.”

**[Dừng 2 giây]** người xem nhớ từ “if”.

```python
so_kg = 12
if so_kg >= 10:
    print("Được giảm giá")
```

**[Lời dẫn]** “Đọc dòng thứ hai: nếu số kg lớn hơn hoặc bằng mười, thì làm việc được ghi ngay sau đó. Dấu hai chấm báo rằng bên dưới là việc cần làm, và dòng thụt vào là việc máy làm khi điều kiện đúng. Ở đây số kg là mười hai, nên máy làm việc đó và in ra ‘Được giảm giá’.”

**[Dừng 3 giây]** người xem đọc lại ba dòng code.

## Đoạn 3: Nếu không thì sao (35 giây)

**[Lời dẫn]** “Nhưng khách mua ba kg thì sao? Luật chưa nói. Đó là lý do cần thêm phần ‘else’, nghĩa là ‘không thì’. Nếu không đủ điều kiện, máy làm việc trong nhánh còn lại.”

```python
so_kg = 3
if so_kg >= 10:
    print("Được giảm giá")
else:
    print("Giữ giá cũ")
```

**[Dừng 2 giây]** người xem nhớ từ “else”.

**[Lời dẫn]** “Bây giờ có đủ hai đường đi. Đúng thì đi lối này, sai thì đi lối kia. Máy không phân vân, chỉ cần điều kiện được viết đúng.”

## Đoạn 4: Nhiều hơn hai đường (40 giây)

**[Lời dẫn]** “Tiệm có ba loại khách. Dưới mười kg thì không giảm. Từ mười đến năm mươi kg thì giảm năm phần trăm. Trên năm mươi kg thì giảm mười phần trăm. Để viết được như vậy, ta thêm ‘elif’, viết tắt của ‘else if’, nghĩa là ‘không thì nếu’.”

```python
so_kg = 30
if so_kg > 50:
    giam = 10
elif so_kg >= 10:
    giam = 5
else:
    giam = 0
print("Giảm:", giam, "phần trăm")
```

**[Dừng 3 giây]** người xem đọc lại đoạn code. Ba cửa tương ứng ba dòng `if`, `elif`, `else`.

**[Lời dẫn]** “Máy kiểm tra từ trên xuống. Trường hợp đầu tiên đúng thì làm, và bỏ qua các trường hợp còn lại. Vì vậy thứ tự viết rất quan trọng: nếu viết điều kiện ‘từ mười kg’ lên trước, khách mua năm mươi lăm kg sẽ chỉ được năm phần trăm.”

## Đoạn 5: Điều kiện ghép (30 giây)

**[Lời dẫn]** “Có lúc điều kiện phải đúng cả hai: vừa mua từ mười kg, vừa là khách quen. Trong code, chữ ‘and’ nghĩa là ‘và’. Ví dụ dưới đây chỉ giảm giá khi cả hai điều kiện cùng đúng. Còn ‘or’ nghĩa là ‘hoặc’, chỉ cần một trong hai đúng là đủ.”

```python
so_kg = 12
khach_quen = True
if so_kg >= 10 and khach_quen:
    print("Giảm 5 phần trăm")
```

**[Dừng 2 giây]** người xem đọc từng vế của điều kiện.

## Đoạn 6: Điều kiện trong đời sống (80 giây)

**[Lời dẫn]** “Thật ra bạn đang dùng câu điều kiện cả ngày mà không nhận ra. Nếu hôm nay trời mưa thì mang áo mưa, không thì không cần. Đó chính là if và else.”

**[Lời dẫn]** “Có lúc chỉ cần một trong các điều kiện đúng là đủ. Ví dụ mở khoá điện thoại: bạn có thể mở bằng Face ID hoặc nhập mật khẩu sáu số. Chỉ cần một cách khớp là điện thoại mở, bạn không cần làm cả hai.”

```python
dung_face_id = False  # quét mặt không thành công, ví dụ đang đeo khẩu trang
dung_mat_khau = True  # nhưng nhập đúng mật khẩu

if dung_face_id or dung_mat_khau:
    print("Mở khóa thành công!")
```

**[Lời dẫn]** “Rạp chiếu phim giảm giá cho học sinh, sinh viên hoặc khách đi xem vào thứ Ba. Bạn không phải sinh viên, nhưng đi xem đúng thứ Ba vẫn được giảm.”

```python
la_sinh_vien = False  # đã đi làm, không phải sinh viên
di_xem_vao_thu_ba = True  # nhưng hôm nay đúng là thứ Ba

if la_sinh_vien or di_xem_vao_thu_ba:
    print("Chúc mừng bạn được giảm giá vé!")
```

**[Lời dẫn]** “Có lúc phải đủ tất cả điều kiện, thiếu một cái là hỏng việc. Muốn tự lái xe ô tô, bạn phải đủ 18 tuổi và có bằng lái hợp lệ. Dù đã 25 tuổi, nếu chưa thi bằng thì vẫn không được lái.”

```python
du_18_tuoi = True
co_bang_lai = False  # chưa thi bằng lái

if du_18_tuoi and co_bang_lai:
    print("Được phép lái ô tô ra đường!")
else:
    print("Chưa đủ điều kiện, cấm lái xe!")
```

## Chốt cảnh (10 giây)

**[Lời dẫn]** “Vậy là bạn đã biết cách để máy chọn đường: if và else cho hai đường, elif cho nhiều đường, và ‘or’, ‘and’ để ghép điều kiện. Đến đây, chúng ta đã có viên gạch thứ ba: câu điều kiện.”
