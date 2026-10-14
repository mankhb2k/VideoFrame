# Cảnh 2: Ông Sơn bắt đầu thuê người

## Đoạn 1: Ông Sơn làm hết mọi việc (25 giây)

**[Hình]** Tiệm đông khách. Ông Sơn một mình vừa bấm máy tính, vừa đóng gói gạo, vừa chạy ra sau lấy hàng. Mồ hôi nhễ nhại.

**[Lời dẫn]** “Tiệm bắt đầu có khách. Ông Sơn một mình làm tất cả: tính tiền, đóng gạo, chạy vào kho. Ông nhận ra có một việc ông làm đi làm lại cả ngày: nhân giá với số ký rồi cộng lại. Làm 50 lần mỗi ngày.”

## Đoạn 2: Thuê người thứ nhất, hàm tính tiền (40 giây)

**[Hình]** Ông Sơn thuê cô Lan ngồi quầy thu ngân. Sơ đồ bên phải: bỏ vào hai thứ (giá, số ký), cô Lan tính, trả ra tổng tiền.

**[Lời dẫn]** “Ông thuê cô Lan, và giao đúng một việc: tính tiền. Khách mua gì, bao nhiêu ký, cô Lan đưa lại tổng tiền. Ông Sơn không cần biết cô bấm máy thế nào, chỉ cần biết đưa gì vào và nhận gì ra. Trong lập trình, cô Lan chính là một hàm.”

```python
def tinh_tien(gia_mot_ky, so_ky):
    return gia_mot_ky * so_ky

tinh_tien(gia_gao_st25, 10)   # trả về 300000
```

**[Lời dẫn]** “Để ý tên hàm: ‘tính tiền’, bắt đầu bằng một động từ, giống như chức danh của cô Lan.”

## Đoạn 3: Thuê người thứ hai, hàm xếp hàng lên kệ (45 giây)

**[Hình]** Cuối ngày, kệ gạo trống trơn. Ông Sơn chạy vào kho khuân gạo ra xếp, rồi lại quay ra bán. Lặp lại mỗi ngày. Chuyển cảnh: ông thuê anh Tâm, dán tờ giấy lên tường: “Hết hàng trên kệ thì vào kho lấy ra xếp”.

**[Lời dẫn]** “Rồi một việc nữa lặp lại mỗi ngày: kệ hết gạo thì ông phải vào kho lấy ra xếp. Ông thuê thêm anh Tâm và dán cho anh một quy tắc rất ngắn: ‘Thấy kệ hết hàng thì vào kho lấy ra xếp.’ Thế thôi. Anh Tâm không cần biết khách mua bao nhiêu hay tính tiền ra sao. Anh chỉ nhìn kệ.”

```python
def xep_hang_len_ke(so_ky_tren_ke):
    if so_ky_tren_ke == 0:
        lay_hang_tu_kho()
        xep_len_ke()
```

**[Lời dẫn]** “Đó là một hàm thứ hai, có một điều kiện: nếu hết hàng thì làm. Ông Sơn không cần nhắc anh Tâm mỗi ngày nữa.”

## Đoạn 4: Ghép các hàm thành quy trình (45 giây)

**[Hình]** Sơ đồ dây chuyền. Khách đến, cô Lan tính tiền, khách trả tiền, anh Tâm kiểm tra kệ. Ông Sơn đứng giữa nhìn bao quát, tay cầm cốc trà.

**[Lời dẫn]** “Bây giờ nhìn tiệm ông Sơn: khách đến, cô Lan tính tiền, anh Tâm lo kệ. Mỗi người một việc, ông Sơn đứng nhìn và điều phối. Khi ghép nhiều người làm nhiều việc nối tiếp nhau, bạn có một thứ gọi là quy trình. Trong code, đó là một hàm lớn gọi các hàm nhỏ.”

```python
def mot_ngay_ban_hang():
    don_hang = tiep_khach()
    tong_tien = tinh_tien(don_hang)
    thu_tien(tong_tien)
    xep_hang_len_ke(so_ky_tren_ke)
```

**[Lời dẫn]** “Đọc từ trên xuống, nó kể lại đúng một ngày bán hàng. Không cần giải thích gì thêm.”

## Đoạn 5: Cú lật, một người làm hết (30 giây)

**[Hình]** Một người đứng giữa tiệm, đội năm cái mũ khác nhau (thu ngân, thủ kho, bán hàng, kế toán, bảo vệ). Ông Sơn gọi: “Anh Hùng nghỉ rồi!”. Cả tiệm đứng im.

```python
def lam_het_moi_viec():
    # tính tiền, xếp kệ, nhập hàng, in hoá đơn, ghi sổ...
```

**[Lời dẫn]** “Giả sử ông Sơn thuê một người làm hết mọi việc. Lúc đầu ổn, vì tiệm nhỏ. Rồi tiệm lớn lên, người đó nghỉ, và cả tiệm đứng im vì không ai biết người đó làm gì ở đâu. Thuê nhiều người, mỗi người một việc, nghe có vẻ tốn hơn. Nhưng đó là cách một hệ thống không sập khi mất một người.”

## Chốt cảnh (15 giây)

**[Lời dẫn]** “Cô Lan tính tiền. Anh Tâm xếp kệ. Nhưng anh Tâm nhìn vào đâu để biết trong kho còn bao nhiêu gạo? Và ai nhớ giúp ông Sơn khách nào đã mua gì?”
