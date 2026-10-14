# {{ten}}

Dự án video tạo từ khuôn `VideoKit/templates/du-an`. Mọi dự án có cùng bố cục nên mọi script dùng chung.

```
du-an.json         cấu hình duy nhất: khung hình, giọng, logo, sfx, danh sách cảnh
kich-ban/          kịch bản gốc (mỗi cảnh một file)
loi-thoai/         lời thoại tách ra để đọc
video/             dự án HyperFrames (index.html do build_index.py sinh; cảnh ở compositions/frames/)
renders/           file render (không đưa lên git)
thumbnail/         thumbnail YouTube
dang-bai/          tiêu đề, mô tả, thẻ
```

## Lệnh thường dùng

Chạy từ thư mục dự án này (script tự tìm `du-an.json`):

```
python3 ../../VideoKit/scripts/build_index.py        # sinh lại video/index.html + moc-canh.json từ độ dài giọng đọc
cd video && npm run check                             # kiểm tra lint, bố cục, tương phản
cd video && npm run dev                               # xem trước trong Studio
cd video && npm run render:nhap                       # render nháp 30 fps
cd video && npm run render:cuoi                       # bản cuối 60 fps
```

Dừng Studio (`npx hyperframes preview --stop`) trước khi sửa HTML bằng tay hoặc chạy `build_index.py`.
Quy trình đầy đủ và các bẫy đã gặp: `VideoKit/README.md`.
