# Định dạng cue hiệu ứng âm thanh (`<cảnh>.sfx.json`)

Mỗi cảnh xuất một file cạnh file HTML của cảnh: `compositions/frames/NN-ten.sfx.json`.

```json
{"scene": "scene-4", "cues": [
  {"t": 42.35, "type": "click", "gain": 1.0, "note": "Flyable khớp vào Sparrow"},
  {"t": 31.9,  "type": "type",  "d": 3.2, "note": "gõ protocol Flyable"}
]}
```

- `t`: giây tính từ đầu cảnh, lấy đúng vị trí bắt đầu tween trong timeline GSAP của cảnh (không đoán).
- `type`: một trong `whoosh` (chuyển động lớn), `pop` (phần tử nhỏ hiện), `tick` (hàng bảng/danh sách), `click` (khớp Lego, nhấn nút),
  `ding` (thành công, dấu tích), `error` (lỗi, bị từ chối), `glitch`, `thud` (chữ lớn đập xuống), `sparkle` (nhấn từ khóa), `type` (gõ code).
- `d`: chỉ cho `type`, độ dài đoạn gõ (giây).
- `gain`: 0.3 đến 1.2, mặc định 1.
- Mật độ gợi ý: khoảng 1 tiếng mỗi 2 đến 3 giây; `tao_sfx.py` tự lọc thưa theo độ ưu tiên và khoảng cách tối thiểu.
- Track ghép ra: `python VideoKit/scripts/tao_sfx.py`, gắn vào `index.html` bằng `<audio id="sfx" src="assets/audio/sfx-track.wav" data-volume="0.65">`.
