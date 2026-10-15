# Ghi chú: nội dung đã rút khỏi tập 1, dùng cho tập sau

## Từ Cảnh 2: Lồng nhiều tầng (40 giây)

Rút khỏi Cảnh 2 vì cảnh đã dày (danh sách, sáu lệnh, từ điển, kệ hàng, ba lỗi). Từ điển lồng hai tầng hợp với tập nói về cấu trúc dữ liệu hoặc database.

**[Lời dẫn]** “Từ điển còn có thể lồng nhau. Tiệm có nhiều khu, trong mỗi khu có nhiều kệ, trong mỗi kệ có món và giá. Muốn biết giá muối, đi từ khu gia vị, xuống kệ muối, rồi đến giá.”

```python
cua_hang = {
    "gạo": {"ST25": 30000, "tám": 22000},
    "gia vị": {"nước mắm": 45000, "muối": 8000},
}
print(cua_hang["gia vị"]["muối"])
```

**[Dừng 2 giây]** người xem đi theo một đường từ tên khu xuống đến giá cần tìm.

**[Lời dẫn]** “Bạn có thể lồng nhiều tầng, và gọi đúng thành phần mình muốn. Nhưng để làm được điều đó khi dự án lớn lên, bạn phải hiểu được cấu trúc mình muốn lưu trữ. Tư duy vẫn không đổi, chỉ có quy mô thay đổi.”

## Từ Cảnh 3: ví dụ "người yêu đẹp trai và có tiền"

Bỏ khỏi Cảnh 3 để giữ giọng trung tính. Ví dụ điều kiện `and` còn lại: lái xe (đủ 18 tuổi và có bằng lái).

## Từ Cảnh 4: hai ví dụ vòng lặp

Cảnh 4 đã giảm từ bốn ví dụ còn hai (gửi email với for, tải trang khi mạng yếu với while). Hai ví dụ bị bỏ: đăng bài lên ba nền tảng (trùng ý với gửi email), và nhập mật khẩu (bản while có lỗi nếu cả ba lần nhập đều sai).
