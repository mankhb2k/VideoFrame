# Thành phần dùng chung (VideoKit/components)

Mỗi thư mục là một thành phần: file `.css` và `.js` (nối tự động vào mọi cảnh bởi `scripts/build_canh.py`, thư mục `core` chạy trước), cộng `demo.html` mở thẳng bằng trình duyệt để xem và thử. Cách dùng trong cảnh: `templates/dung-canh/LUAT-DUNG-CANH.md`.

| Thư mục | Nội dung |
|---|---|
| `core/` | `vk.css` và `vk.js`: chip, thẻ, bong bóng, kệ gạch, nhân vật; hàm `vk.vao/pop/cung/dem/go/ve/keGach/gachLon/nv`, co giãn thời gian `vkWarp` |
| `ide/` | `vk-ide.css` và `vk-ide.js`: cửa sổ soạn code kiểu VS Code + terminal (`vk.ide`, API tiếng Anh, ba mức cỡ chữ large, normal, small) |

Thêm thành phần mới: tạo `components/<ten>/` với `*.css`, `*.js` (đăng ký vào đối tượng `vk`, ví dụ `vk.ten = ...`) và `demo.html`. Không cần sửa `build_canh.py`.
