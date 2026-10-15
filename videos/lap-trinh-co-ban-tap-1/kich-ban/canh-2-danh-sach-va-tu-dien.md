# Cảnh 2: Danh sách và từ điển

## Đoạn 1: Hai mươi mặt hàng (25 giây)

**[Lời dẫn]** “Ở cảnh trước, ông Sơn đã biết đặt tên cho từng giá trị bằng biến. Nhưng tiệm bây giờ có hàng chục mặt hàng, và nhớ riêng từng món thì rất rối. Để bắt đầu, ông Sơn lấy một tờ giấy nhớ, ghi sáu món theo đúng thứ tự, và có thể đếm được bao nhiêu món.”

## Đoạn 2: Danh sách (35 giây)

```python
mat_hang = ["gạo ST25", "gạo tám", "nước mắm", "muối", "coca", "pepsi"]
print(mat_hang[0])
print(len(mat_hang))
```

**[Dừng 2 giây]** người xem đếm các số thứ tự từ 0.

**[Lời dẫn]** “Đây chính là cách bạn tạo ra 1 danh sách: nhiều món gom vào một chỗ, theo đúng thứ tự. Để lấy một món, ta viết tên danh sách kèm số thứ tự. Nhớ rằng số thứ tự bắt đầu từ không: số không là món đầu tiên. Lệnh ‘len’ cho biết có bao nhiêu món.”

## Đoạn 3: Thêm món mới (30 giây)

```python
mat_hang.append("bột ngọt")
print(len(mat_hang))
```

**[Lời dẫn]** “Hôm nay có hàng mới về. Ông Sơn thêm bột ngọt vào cuối danh sách, giống như ghi thêm một dòng lên tờ giấy nhớ. Đếm lại thì có bảy món." 

**[Lời dẫn]** “Một số lệnh thường dùng: ‘append’ thêm một món vào cuối. ‘insert’ thêm một món vào đúng vị trí bạn chọn. ‘remove’ bỏ món đầu tiên có đúng tên đó. ‘pop’ bỏ món ở vị trí bạn chọn, và nếu không chọn thì bỏ món cuối. ‘extend’ thêm cả một danh sách khác vào cuối. ‘clear’ xoá hết mọi món.”

**[Lời dẫn]** “Đó chính là cách chúng ta viết thêm bớt một thứ gì đó ra khỏi tờ giấy nhớ. Với các ngôn ngữ lập trình khác, lệnh sẽ khác nhau, nhưng tư duy vẫn không đổi.”

## Đoạn 4: Vấn đề: tra giá bằng số thứ tự (40 giây)

**[Lời dẫn]** “Giờ ông Sơn muốn biết giá muối. Muối đang đứng ở số không, nên có thể tra bằng số đó. Bạn hãy đoán thử: nếu ông thêm một món vào đầu danh sách, muối sẽ đứng ở số mấy?”

```python
hang_hom_nay = ["muối", "nước mắm", "coca"]
print(hang_hom_nay[0])
hang_hom_nay.insert(0, "bột ngọt")
print(hang_hom_nay[0])
```

**[Dừng 2 giây]** người xem thấy món ở số không đã đổi, muối bị đẩy xuống.

**[Lời dẫn]** “Tất cả các món đều lùi xuống một vị trí. Số thứ tự cũ không còn đúng nữa, và tra giá bằng số thứ tự sẽ dễ sai. Vì vậy ta nên tra bằng tên. Đó là từ điển: mỗi dòng gồm một tên và một giá đi kèm. Tên ở bên trái, giá ở bên phải. Muốn biết giá muối, ta gọi thẳng tên ‘muối’.”

```python
gia_ban = {"gạo ST25": 30000, "muối": 8000, "nước mắm": 45000, "coca": 12000, "pepsi": 11000}
print(gia_ban["muối"])
```

**[Dừng 2 giây]** người xem đọc dòng tra cứu và số tiền.

**[Lời dẫn]** “Danh sách tìm bằng số thứ tự, còn từ điển tìm bằng tên. Thêm hay bớt món, tên vẫn giữ nguyên, nên giá luôn tra đúng. Vậy từ điển có hai phần: tên bên trái để tra, và thứ được tra ra bên phải.”

## Đoạn 4b: Kệ hàng: một tên, nhiều món (35 giây)

**[Lời dẫn]** “Vẫn là cách tra bằng tên đó, chỉ khác ở bên phải. Ví dụ tiệm có nhiều kệ, mỗi kệ có một tên ở bên trái. Bên phải không phải một con số mà là cả một danh sách các món trong kệ. Kệ ‘gạo’ có gạo ST25 và gạo tám. Kệ ‘gia vị’ có nước mắm và muối. Tra kệ bằng tên, rồi lấy món bằng số thứ tự trong kệ.”

```python
ke_hang = {"gạo": ["gạo ST25", "gạo tám"], "gia vị": ["nước mắm", "muối"]}
print(ke_hang["gia vị"])
print(ke_hang["gia vị"][0])
```

**[Dừng 2 giây]** người xem thấy kết quả là cả danh sách, rồi một món trong danh sách.

**[Lời dẫn]** “Vậy từ điển không đổi: vẫn tra bằng tên, vẫn tên không được trùng. Chỉ có thứ bên phải thay đổi. Bên phải có thể là một giá, và cũng có thể là cả một danh sách.”

## Đoạn 5: Lỗi thường gặp và cách đặt từ điển (40 giây)

**[Lời dẫn]** “Lỗi thứ nhất: hỏi giá của món không có trong sổ. Máy báo lỗi và nói: tôi không tìm thấy món này.”

```python
print(gia_ban["đường"])
```

**[Lời dẫn]** “Lỗi thứ hai: tên viết khác nhau, ‘Muối’ với chữ M viết hoa thì máy coi là một tên khác, nên cũng không tìm thấy.”

```python
print(gia_ban["Muối"])
```

**[Lời dẫn]** “Lỗi thứ ba: trùng tên. Nếu ghi hai dòng cùng tên ‘muối’, dòng sau sẽ ghi đè dòng trước.”

```python
gia_thu = {"muối": 8000, "muối": 9000}
print(gia_thu["muối"])
```

**[Lời dẫn]** “Vì vậy khi đặt từ điển, hãy chọn khoá là thứ duy nhất và viết nhất quán, ví dụ mã hàng hoặc tên đầy đủ. Khái niệm từ điển có ở rất nhiều nơi: danh bạ điện thoại tra số theo tên, sổ điểm tra điểm theo tên học sinh, hay cuốn sổ từ điển dịch tiếng Anh sang tiếng Việt mà bạn hay dùng chính là từ điển trong lập trình nơi để tra cứu thông tin.”

```python
danh_ba = {"mẹ": "0901234567", "Sơn": "0912345678"}
print(danh_ba["mẹ"])
```

## Chốt cảnh (20 giây)

**[Lời dẫn]** “Đến đây, tiệm đã có viên gạch thứ hai: danh sách và từ điển. Danh sách gom nhiều món theo đúng thứ tự, còn từ điển tra giá bằng tên.”
