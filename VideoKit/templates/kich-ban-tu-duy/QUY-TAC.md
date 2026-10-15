# Quy tắc viết kịch bản dạy tư duy lập trình

Dùng cho mọi kịch bản loạt "lập trình cơ bản". Áp dụng cho lời dẫn (lời đọc) và cách mô tả khoảng dừng. Phần hình viết sau khi kịch bản đã được duyệt.

## 1. Lời dẫn: tiếng Việt, không đọc ký hiệu

- Lời dẫn viết tiếng Việt tự nhiên. Không đọc tên biến, tên hàm hay ký hiệu trong lời dẫn (ví dụ `thu_tu`, `range(5)`, `mon_con_lai`).
- Gọi khái niệm bằng từ tiếng Việt: "số thứ tự", "số món còn lại", "tổng tiền".
- Tên trong code được **tô sáng trên hình** khi lời dẫn nói tới khái niệm đó. Trong kịch bản, ghi việc tô sáng ở khoảng dừng: `**[Dừng 2 giây]** người xem đọc dòng for, thu_tu được tô sáng.`
- Tên từ khoá của Python (`for`, `while`, `if`, `else`, `range`) được phép nói trong lời dẫn khi cần, nhưng luôn kèm nghĩa tiếng Việt ngay sau.

## 2. Mỗi khái niệm có một câu chuyện

- Dùng tiệm tạp hoá của ông Sơn hoặc đời sống hằng ngày (trời mưa, mở khoá điện thoại, mua vé rạp, băng chuyền).
- Không dùng ẩn dụ khó như "hộp", "nhãn" để giải thích biến. Biến là "thứ được đặt tên để nhớ một giá trị".
- Người xem phải tự làm một việc nhỏ: đoán, đếm, tự nghĩ ("Nếu là bạn, bạn sẽ..."), để theo kịp.

## 3. Tư duy trước, cú pháp sau

- Dạy điều dùng được cho gần mọi ngôn ngữ: biến, kiểu dữ liệu (chữ, số, đúng/sai), điều kiện, vòng lặp, hàm, danh sách, từ điển.
- Không giải thích chi tiết cú pháp riêng của Python như dấu hai chấm, thụt dòng, dấu ngoặc vuông. Nếu bắt buộc phải nhắc, chỉ một câu.
- Chú thích trong code ngắn, nói đúng việc của dòng đó.

## 4. Tên biến

- Tên rõ nghĩa, không dùng `a, b, c`, `i` trừ khi có giải thích ngay. Trường hợp `i`, dùng `thu_tu`.
- Tên không trùng giữa các cảnh với nghĩa khác nhau. Ví dụ dùng `tong_tien`, không dùng `tong` lúc thì là tổng tiền, lúc thì là kết quả hàm.
- Tên không dấu, không khoảng trắng, theo kiểu `so_ky`, `gia_gao_st25`.

## 5. Ví dụ phải chạy được

- Mọi khối code trong kịch bản chạy thử được, và kết quả in ra đúng với lời dẫn. Kiểm bằng `exec` trước khi giao.
- Khi dùng `range(n)`, luôn nói rõ máy đếm từ 0 đến n-1.
- Khi viết số thành chữ có ngoặc kép, luôn cho một ví dụ máy báo lỗi hoặc cho kết quả lạ (như nối chuỗi).

## 6. Nhịp và độ dài

- Mỗi đoạn khoảng 25 đến 45 giây giọng đọc. Cảnh khoảng 3 đến 5 đoạn cộng chốt.
- Khoảng dừng mô tả việc người xem làm: đọc dòng, đếm, nhớ từ. Không mô tả hình.
- Không chèn khoảng dừng để "cho hình kịp" trong kịch bản; nhịp do giọng đọc quyết định.

## 7. Thứ tự làm việc

1. Kịch bản (lời dẫn, khối code, khoảng dừng) được duyệt trước.
2. Chỉ sau đó mới viết phần hình.
3. Câu chốt của cảnh do người viết kịch bản tự viết, trừ khi được yêu cầu viết hộ.

## 8. Ngôn ngữ và giọng

- Giọng kể gần gũi, xưng "bạn" khi mời người xem làm, "ông Sơn" khi kể chuyện.
- Không khẳng định quá: tránh "chắc chắn", "luôn luôn" khi không đo được.
