# Cấu trúc một dự án video

Chuẩn nằm trong `templates/du-an/` (xem `README.md` ở đó) và được `scripts/tao_du_an.py` chép ra thành `videos/<slug>/`:

```
videos/<slug>/
├── du-an.json      cấu hình duy nhất (xem templates/du-an.schema.md)
├── kich-ban/       kịch bản gốc, mỗi cảnh một file canh-N-*.md
├── loi-thoai/      lời thoại tách ra để đọc
├── video/          dự án HyperFrames (index.html do build_index.py sinh)
│   ├── compositions/frames/NN-ten.html  (+ .sfx.json)  và compositions/logo.html
│   └── assets/     audio/ (wav, words-*.json, moc-canh.json, sfx-track.wav), images/, sfx/, fonts/
├── renders/        file render (không đưa lên git)
├── thumbnail/
└── dang-bai/       tieu-de.md, mo-ta.md, tags.txt
```

Quy ước: tên file không dấu; mỗi class/id trong cảnh có tiền tố `sN-`; `@font-face` khai báo trong `index.html` (build_index lo) và trong từng file cảnh (dán `templates/font-face.css`);
dừng `hyperframes preview` trước khi sửa HTML bằng tay hoặc chạy `build_index.py`.
Video đầu tiên (OOP vs POP) dùng bố cục cũ và đã được gỡ khỏi cây làm việc; mã nguồn của nó còn trong lịch sử git (commit `bb86b53`).
