---
workflow: general-video
flow: companion
storyboard: yes
message: "Biến là hộp có nhãn, kiểu dữ liệu quyết định hộp chứa gì"
destination: youtube
aspect: 1920x1080
language: vi
audience: "người chưa biết lập trình"
length: theo giọng đọc
angle: "Ông Sơn và tiệm tạp hoá: mỗi khái niệm là một hộp hoặc vật trong tiệm"
voice: vi-vn-advisor-2
---

## Intent

<video này là gì, cho ai, giọng điệu>

## Assets

- ../kich-ban/ — kịch bản gốc (mỗi cảnh một file).
- ../loi-thoai/ — lời thoại tách ra để đọc (sinh bằng script).

## Customizations

-

## Notes

- Giọng đọc: vi-vn-advisor-2 (gemini-3.8-flash-tts), tạo ngày 2026-10-15.
- Phiên bản HyperFrames CLI: 0.8.152.
- Độ dài video do giọng đọc quyết định; mỗi cảnh có thể thêm giây giữ hình trong `du-an.json` (`giu_them_giay`).
