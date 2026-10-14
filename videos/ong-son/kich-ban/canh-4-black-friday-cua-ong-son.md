# Cảnh 4: Black Friday của ông Sơn

## Đoạn 1: Luật của ông Sơn (25 giây)

**[Hình]** Lịch treo tường, ngày 27/11 khoanh đỏ. Ông Sơn viết lên tờ giấy: “Chỉ giảm 5%. Chỉ hôm nay.”

**[Lời dẫn]** “Ngày 27 tháng 11 là Black Friday. Ông Sơn muốn giảm giá, nhưng lãi tạp hoá mỏng. Nên ông đặt đúng một luật: chỉ giảm 5%, và chỉ trong ngày hôm đó. Hôm sau, giá trở lại bình thường.”

## Đoạn 2: If/else là “nếu... thì... không thì...” (30 giây)

**[Hình]** Hình một người đứng nhìn ra cửa sổ. Nhánh trái: “Nếu trời mưa thì mang ô”. Nhánh phải: “Không thì thôi”. Sau đó thay bằng cô Lan trước tờ lịch: “Nếu hôm nay là 27/11 thì giảm 5%. Không thì giữ giá thường”.

**[Lời dẫn]** “Bạn dùng if/else cả ngày mà không biết. Nếu trời mưa thì mang ô, không thì thôi. Cô Lan cũng vậy: nếu hôm nay là 27 tháng 11 thì giảm 5%, không thì giữ giá thường. Cô nhìn lịch và tự chọn, không cần ông Sơn đứng cạnh nhắc.”

## Đoạn 3: Viết thành code (25 giây)

**[Hình]** Bên trái là tờ giấy luật, bên phải là code. Mỗi dòng sáng lên khi lời dẫn đọc tới.

```python
if black_friday == "27/11":
    giam_gia = 5
else:
    giam_gia = 0
```

**[Lời dẫn]** “Đọc là bạn hiểu: nếu ngày Black Friday đúng là 27/11 thì giảm giá bằng 5. Không thì giảm giá bằng 0. Chỉ có vậy.”

## Đoạn 4: Chạy thử hai ngày (20 giây)

**[Hình]** Hai hoá đơn cạnh nhau. Trái, ngày 27/11: 300.000đ trừ 5% còn 285.000đ. Phải, ngày 28/11: 300.000đ giữ nguyên.

**[Lời dẫn]** “Ngày 27, khách mua 300 nghìn, được giảm 5%, trả 285 nghìn. Ngày 28, cùng đơn hàng, trả đủ 300 nghìn. Không ai phải gỡ giấy khuyến mãi. Luật tự dừng đúng ngày.”

## Đoạn 5: Vòng lặp là if/else hỏi đi hỏi lại (35 giây)

**[Hình]** Giỏ hàng đầy ắp trước mặt cô Lan. Cô quét một món, ngẩng lên hỏi: “Còn món nào không?”. Rồi lại quét, lại hỏi. Hết món thì dừng và nhấn máy tính.

**[Lời dẫn]** “Một khách mua cả giỏ hàng đầy. Cô Lan quét một món, rồi tự hỏi: còn món nào không? Còn thì quét tiếp, hết thì tính tiền. Để ý: đây vẫn là câu if/else, chỉ khác là cô hỏi nó đi hỏi lại. Việc hỏi đi hỏi lại đó gọi là vòng lặp.”

```python
while con_mon_trong_gio:
    quet_mot_mon()
```

**[Lời dẫn]** “Đọc là: trong khi còn món trong giỏ thì quét một món. Hết món, máy tự dừng.”

## Đoạn 6: Cú lật, nếu không có if/else (20 giây)

**[Hình]** Ông Sơn quên gỡ tờ giấy “GIẢM 5%”. Một tuần sau, giấy vẫn còn, sổ sách lãi bằng không.

**[Lời dẫn]** “Không có if/else, ông Sơn phải tự dán giấy giảm giá sáng 27 và tự gỡ sáng 28. Chỉ cần quên một lần, cả tuần lãi bốc hơi. Máy tính không quên, miễn là bạn dạy nó luật đúng.”

## Chốt cảnh (10 giây)

**[Lời dẫn]** “Biến để gọi tên. Hàm để chia việc. Database để nhớ. If/else để tự quyết định. Giờ mọi mảnh ghép đã đủ. Mời bạn nhìn tiệm ông Sơn từ trên cao.”
