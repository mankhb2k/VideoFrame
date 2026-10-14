# VideoFrame

Hệ thống làm video giải thích bằng [HyperFrames](https://hyperframes.heygen.com): một thư viện dùng chung và các dự án video làm từ cùng một khuôn.

- [`VideoKit/`](VideoKit/README.md): nhân vật, hiệu ứng âm thanh, font, logo, script, khuôn dự án và quy trình.
- `videos/<slug>/`: mỗi video một thư mục theo khuôn chuẩn (xem `VideoKit/templates/du-an/README.md`). Tạo video mới bằng `python3 VideoKit/scripts/tao_du_an.py <slug> ...`.

Video đầu tiên ("So sánh OOP và POP") dùng bố cục cũ và chỉ còn trong lịch sử git (commit `bb86b53`).
File render (`*.mp4`), khóa API (`.env`) và cache không nằm trong repo.
