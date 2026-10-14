---
workflow: general-video
flow: companion
storyboard: yes
message: "{{thong_diep}}"
destination: youtube
aspect: 1920x1080
language: vi
audience: "{{khan_gia}}"
length: theo giọng đọc
angle: "{{y_tuong}}"
voice: {{giong}}
---

## Intent

{{y_dinh}}

## Assets

- ../kich-ban/ — kịch bản gốc (mỗi cảnh một file).
- ../loi-thoai/ — lời thoại tách ra để đọc (sinh bằng script).

## Customizations

-

## Notes

- Giọng đọc: {{giong}} ({{model}}), tạo ngày {{ngay}}.
- Phiên bản HyperFrames CLI: {{hyperframes}}.
- Độ dài video do giọng đọc quyết định; mỗi cảnh có thể thêm giây giữ hình trong `du-an.json` (`giu_them_giay`).
