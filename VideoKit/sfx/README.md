# Thư viện hiệu ứng âm thanh

Tạo bằng code (`../scripts/tao_sfx.py --thu-vien`), hạt giống cố định nên chạy lại cho ra cùng kết quả; không dùng mẫu âm của bên thứ ba nên không vướng bản quyền.
Mức đã chuẩn hóa cho nhỏ hơn giọng đọc. Khi ghép video, đặt track sfx ở `data-volume="0.65"` (đo trên video đầu tiên: sfx thấp hơn giọng trung bình khoảng 20 dB).
Quy ước loại âm và định dạng cue: `../templates/sfx-cue-format.md`.

whoosh · pop · tick · click · ding · error · glitch · thud · sparkle (+ `type`: gõ phím, tạo theo độ dài cue, không có file riêng).
Chưa nghe thử bằng tai khi tạo; chỉnh trong `tao_sfx.py` nếu thấy chưa vừa tai.
