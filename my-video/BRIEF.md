---
workflow: general-video
flow: companion
storyboard: yes
message: "Đừng bỏ OOP, hãy bỏ thói quen kế thừa mặc định: bắt đầu từ khả năng (protocol/interface), không phải từ dòng dõi (class cha)."
destination: youtube
aspect: 1920x1080
language: vi
audience: "dev web/mobile đã biết TypeScript cơ bản, chưa chắc biết Swift"
length: 522s
angle: "Cây gia phả (OOP, hổ phách) đối đầu khối Lego (POP, xanh ngọc)"
voice: vi-vn-advisor-2
---

## Intent

Video giải thích dài khoảng 8 phút 42 giây so sánh OOP (ví dụ TypeScript) với POP, tức Protocol-Oriented Programming (ví dụ Swift), kết thúc bằng bảy luật viết TypeScript theo tư duy POP. Giọng đọc tiếng Việt, thuật ngữ giữ tiếng Anh. Hình ảnh là motion graphic: cây kế thừa, con khỉ và quả chuối, khối Lego, code gõ từng ký tự. Giữ giọng công bằng, không để "OOP là cái sai".

## Assets

- ../kich-ban-video-oop-pop/kich-ban-video.md — kịch bản gốc (hình ảnh từng phần, code, bảng so sánh, bảng màu).
- assets/audio/canh0..canh7_*.wav — giọng đọc đã tạo bằng Gemini TTS, giọng `vi-vn-advisor-2`, model `gemini-3.8-flash-lite-tts`, 24 kHz mono, tổng 509,8 giây.
- assets/audio/moc-canh.json — mốc bắt đầu và độ dài từng cảnh tính từ giọng đọc thật.

## Customizations

- Dùng lại khối catalog: `code-typing`, `code-highlight` (khung code), `rgb-glitch-text` và `camera-shake` (lỗi `Penguin.fly()`), `comparison-split` (phần 4), `success-check` (checklist bảy luật).
- Mốc từng từ trong giọng đọc (transcribe) để đồng bộ highlight với lời; làm sau khi duyệt kế hoạch.

## Notes

- Đúng màu: đỏ là lỗi, xanh ngọc là ổn, hổ phách là OOP; không dùng màu để trang trí.
- Mỗi đoạn code tối đa 6 dòng, font mono, gõ từng ký tự.
- Sparrow, Penguin, Drone giữ nguyên hình dạng và vị trí ở cả hai bên so sánh.
- Giọng đọc làm bằng `flash-lite` vì `gemini-3.8-flash-tts` hết hạn mức miễn phí ngày; có thể đọc lại bằng model Flash (`python3 tao_giong_doc.py --model gemini-3.8-flash-tts`, xóa các .wav cũ) sau khi hạn mức đặt lại, hoặc khi bật thanh toán.
- Bảng phát âm `bang-phat-am.csv` chưa áp dụng; chưa nghe thử xem có từ nào đọc sai.
