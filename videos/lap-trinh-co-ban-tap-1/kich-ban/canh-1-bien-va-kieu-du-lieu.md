# Cảnh 1: Biến và kiểu dữ liệu

## Mở đầu: hook (khoảng 15 giây)

**[Lời dẫn]** “Nếu bạn chưa từng viết một dòng code nào mà vẫn muốn hiểu lập trình thực sự vận hành ra sao, video này dành cho bạn. Bạn không cần biết code trước. Đến cuối video, bạn sẽ đọc được những dòng code đầu tiên của mình.”

**[Lời dẫn nối]** “Chúng ta bắt đầu với một người tên là ông Sơn.”

## Đoạn 1: Dự án bắt đầu từ đâu (25 giây)

**[Lời dẫn]** “Ông có trong tay 20 triệu đồng và quyết định mở một cửa hàng tạp hoá. Nghe quen không? Đây chính là cách một dự án được tạo ra: một người, một ít vốn và một ý tưởng. Phần mềm triệu đô nào cũng từng bắt đầu từ một ‘cửa hàng 20 triệu’ như thế này.”

## Đoạn 2: Ghi lại ba điều về tiệm (30 giây)

**[Lời dẫn]** “Bạn hãy thử lấy một tờ giấy và ghi xuống ba dòng. Dòng đầu: tên cửa hàng là “Tạp hoá Ông Sơn”. Dòng thứ hai: vốn là 20 triệu. Dòng thứ ba: đã bắt đầu mở cửa chưa? Ghi “đúng” nếu đã mở, “sai” nếu chưa. Vậy là bạn vừa viết được chương trình đầu tiên của mình. Chúc mừng bạn!”

**[Lời dẫn]** “Trong lập trình, mỗi dòng đó được viết thành một dòng code. Cái tên như ‘von’ là tên gọi để máy và chúng ta cùng nhớ. Giá trị 20 triệu là thứ được gắn vào tên đó. Và từ giờ, mỗi lần cần số vốn, ta chỉ cần gọi tên ‘von’.”

```python
ten_cua_hang = "Tạp hoá Ông Sơn"
von = 20000000
dang_mo_cua = True
```

**[Lời dẫn]** “Dòng cuối dùng chữ True, nghĩa là đúng. Dấu bằng ở đây không phải để so sánh, mà nghĩa là gắn giá trị bên phải vào tên bên trái. Ba dòng này là lần đầu tiên bạn đặt tên cho một thứ và gắn giá trị vào đó. Trong lập trình, đó gọi là biến.”

## Đoạn 3: Ba loại giá trị (30 giây)

**[Lời dẫn]** “Ba dòng vừa rồi có ba loại giá trị khác nhau. Tên tiệm là chữ. Vốn là số. Còn tiệm đã mở cửa hay chưa chỉ có hai đáp án: đúng hoặc sai. Ba loại này gọi là kiểu dữ liệu, và ta chỉ cần nhớ ba loại chính này.”

## Đoạn 4: Ông Sơn nhập hàng (40 giây)

**[Lời dẫn]** “Giờ ông Sơn đi nhập hàng, hết mười triệu. Vốn còn lại là bao nhiêu? Ta lấy vốn trừ đi số tiền nhập hàng.”

```python
nhap_hang = 10000000
con_lai = von - nhap_hang
print("Còn lại:", con_lai, "VNĐ")
```

**[Lời dẫn]** “Lệnh ‘print’ bảo máy in kết quả ra màn hình. Máy trả lời: mười triệu. Đúng như ông Sơn tính trong đầu. Máy làm phép trừ được vì cả hai đều là số.”

## Đoạn 5: Thử viết số thành chữ (30 giây)

**[Lời dẫn]** “Bây giờ thử viết số tiền nhập hàng thành chữ, như ‘mười triệu’ có ngoặc kép.”

```python
nhap_hang = "mười triệu"
con_lai = von - nhap_hang
```

```text
TypeError: unsupported operand type(s) for -: 'int' and 'str'
```

**[Lời dẫn]** “Máy báo lỗi. Với máy, ‘mười triệu’ là một đoạn chữ, không phải một con số, nên không trừ được. Đó là lý do khi muốn cộng, trừ, nhân, chia, ta phải viết số mà không đặt trong ngoặc kép. Lỗi này không có gì đáng sợ. Nó chỉ cho biết chỗ nào đang sai.”

**[Lời dẫn]** “Vậy nếu cả hai giá trị đều là chữ thì sao? Lưu ý: bất kỳ thứ gì nằm trong dấu ngoặc kép đều được máy coi là chữ, kể cả khi trông giống số.”

```python
von = "20000000"
nhap_hang = "10000000"
print(von + nhap_hang)
print(von - nhap_hang)
```

```text
2000000010000000
TypeError: unsupported operand type(s) for -: 'str' and 'str'
```

**[Lời dẫn]** “Dòng đầu không báo lỗi, nhưng kết quả thật lạ: hai chuỗi được dán nối vào nhau thành ‘2000000010000000’. Máy không cộng, chỉ ghép chữ. Dòng thứ hai thì báo lỗi, vì máy không biết trừ chữ cho chữ. Cùng là hai con số, nhưng đặt trong ngoặc kép thì máy hiểu chúng là chữ.”

## Đoạn 6: Phân loại gạo và ghi giá (35 giây)

```python
gia_gao_tam = 22000
gia_gao_st25 = 30000
gia_gao_thuong = 15000
```

**[Lời dẫn]** “Gạo nhập về nhìn đâu cũng giống nhau, nên việc tiếp theo là phân loại và ghi giá từng loại. Thùng này là gạo tám, 22 nghìn một kg. Thùng này là ST25, 30 nghìn. Thùng này là gạo thường, 15 nghìn. Ba loại gạo, ba giá, ba tên riêng.”

## Đoạn 7: Cú lật, vì sao tên quan trọng (30 giây)

```python
# Cách ông Sơn lười đặt tên
a = 22000
b = 30000
c = 15000
```

**[Lời dẫn]** “Giờ giả sử hôm đó ông Sơn lười, đặt tên là a, b, c. Sáu tháng sau, ông mở chi nhánh thứ hai và giao cho nhân viên mới. Hỏi a là gạo gì? b là gạo gì? Không ai biết, kể cả ông Sơn. Cái tên tưởng nhỏ ấy sẽ quyết định dự án của ông lớn lên được hay sụp đổ. ” 

## Chốt cảnh (10 giây)

**[Lời dẫn]** “Chắc hẳn bạn từng gặp cảnh này: đi mua hàng ở tạp hoá, người bán nhớ giá nhưng vẫn phải hỏi lại chủ quán. việc đặt tên biến nhìn có vẻ rất đơn giản nhưng nếu bạn đặt tên mập mờ thì dự án lớn dần sẽ rối, và phần lớn lỗi khi mới học là gọi nhầm tên. Vậy là chúng ta đã có viên gạch đầu tiên, biến và kiểu dữ liệu ” 
