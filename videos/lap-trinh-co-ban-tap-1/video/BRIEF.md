---
workflow: general-video
flow: companion
storyboard: yes
message: "Năm viên gạch của lập trình (biến, danh sách và từ điển, câu điều kiện, vòng lặp, hàm) là nền móng của phần mềm, từ tiệm tạp hoá đến phần mềm triệu đô: khác quy mô, không khác tư duy."
destination: youtube
aspect: 1920x1080
language: vi
audience: "người chưa biết lập trình"
length: theo giọng đọc (khoảng 14 đến 16 phút, 6 cảnh)
angle: "Tiệm tạp hoá của ông Sơn lớn dần: mỗi cảnh thêm một viên gạch, mỗi khái niệm gắn với một việc có thật ở quầy, kệ, băng chuyền hay người làm."
voice: vi-vn-advisor-2
---

## Intent

Loạt "Lập trình cơ bản", tập 1: dạy người chưa từng viết code hiểu năm khái niệm nền móng và cách chúng ghép lại, bằng câu chuyện ông Sơn mở tiệm tạp hoá. Dạy tư duy dùng được cho gần mọi ngôn ngữ; code dùng Python, tên biến tiếng Việt không dấu, chạy được.

Giọng kể gần gũi, xưng "bạn" khi mời người xem làm, "ông Sơn" khi kể chuyện. Người xem luôn có việc nhỏ để làm: đoán, đếm, tự nghĩ. Không khẳng định quá mức; tránh "chắc chắn", "luôn luôn".

Cấu trúc sáu cảnh (mỗi cảnh một viên gạch, kịch bản ở `../kich-ban/`):

1. Biến và kiểu dữ liệu: ông Sơn với 20 triệu, tên để nhớ giá trị, chữ, số, đúng/sai.
2. Danh sách và từ điển: sáu món trên kệ, tra giá theo tên.
3. Câu điều kiện: giảm giá theo số kg, if/elif/else, and/or.
4. Vòng lặp: băng chuyền tính tiền, for, while, khi nào dùng loại nào (hai ví dụ).
5. Hàm: thuê cô Lan, anh Tâm, chị Hương (quản lý), chị Mai (đóng gói); mỗi hàm một việc.
6. Nhìn tiệm từ trên cao: năm viên gạch, bình cũ rượu mới, đổi sang bán bún, framework, thử thách, treo sang database.

Quy tắc kịch bản: `../../../VideoKit/templates/kich-ban-tu-duy/QUY-TAC.md`.

## Assets

- ../kich-ban/ — kịch bản sáu cảnh (đã duyệt), kèm `ghi-chu-danh-cho-tap-sau.md`.
- ../loi-thoai/ — lời thoại tách ra để đọc (sinh bằng script, chưa tạo).
- assets/images/ — ảnh nhân vật và đạo cụ đã có sẵn: ông Sơn (5 dáng), cô Lan (5 dáng), anh Tâm (2 dáng), 14 đạo cụ, 2 nền.
- anh-ong-son-cu.json — định danh nhân vật đã dùng trước đây, làm gốc cho nhân vật mới để đồng bộ nét vẽ.
- Tham khảo HTML/CSS dựng cảnh (chỉ để lấy ý tưởng, không dùng trực tiếp): `../tham-khao-html/`.
- Cửa sổ code: component `vk.ide` ở `VideoKit/components/ide/`.

## Customizations

- **Khung hình chính là cửa sổ code** (vk.ide kiểu VS Code), tên trong code được tô sáng đúng lúc lời dẫn nhắc tới; lời dẫn không đọc tên biến.
- **Ảnh tối thiểu**, theo quy tắc gộp ảnh trong CLAUDE.md: HTML và animation làm được thì không tạo ảnh; chữ, giá, nhãn luôn là HTML.
- **Nhân vật mới cần tạo:** chị Hương (quản lý) và chị Mai (đóng gói), ảnh gốc, tạo trước các dáng; cô Lan, anh Tâm, ông Sơn dùng ảnh có sẵn.
- **Mỗi đoạn là một khung dựng riêng** (`compositions/frames/cN-dM.html`), nhịp hình gán theo mốc giây thật sau khi chốt giọng.

## Notes

- Giọng đọc: vi-vn-advisor-2 (gemini-3.8-flash-tts). Mỗi cảnh một yêu cầu TTS, không chèn khoảng dừng nhân tạo; chỗ cần giữ hình thì chèn lặng sau khi nghe bản đọc.
- Thứ tự làm: brief, danh sách ảnh và tạo ảnh, giọng đọc, nghe và chốt giọng, whisper lấy mốc từng từ, storyboard theo mốc thật, dựng cảnh, sfx, render. Chốt giọng trước khi dựng; đổi lời dẫn sau đó phải tạo lại giọng cảnh đó.
- Render 60 fps khoảng 3,3 phút cho mỗi phút video; chỉ render khi được yêu cầu.
- Phiên bản HyperFrames CLI: 0.8.152.
- Độ dài video do giọng đọc quyết định; mỗi cảnh có thể thêm giây giữ hình trong `du-an.json` (`giu_them_giay`).

## Việc còn mở trước khi tạo hình

- `du-an.json` mới chỉ có cảnh 1 và tên cũ "Biến và kiểu dữ liệu"; cần khai báo đủ sáu cảnh và đổi tên tập.
- Chốt thứ tự các tập sau: cảnh 6 hẹn "tập sau là database"; cần thống nhất với kế hoạch các video tiếp theo.
