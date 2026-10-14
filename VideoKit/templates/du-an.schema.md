# `du-an.json`: cấu hình duy nhất của một dự án video

Mọi script của VideoKit đọc file này (tìm từ thư mục hiện tại đi lên). Sinh bởi `tao_du_an.py`, sửa tay khi cần rồi chạy lại `build_index.py`.

| Trường | Ý nghĩa |
|---|---|
| `slug`, `ten` | tên ngắn không dấu và tên hiển thị |
| `phien_ban_hyperframes` | phiên bản CLI đã dùng (khóa trong `package.json` để render lại giống nhau) |
| `khung` | `rong`, `cao` (mặc định 1920x1080), `fps_nhap` (30), `fps_cuoi` (60) |
| `thu_muc` | `kich_ban`, `loi_thoai`, `video`, `thumbnail` (đường dẫn trong dự án) |
| `giong` | `nha_cung_cap`, `model`, `giong` (ví dụ `vi-vn-advisor-2`), `do_tre_giay` (0,3: lặng đầu và cuối mỗi cảnh), `am_luong` |
| `logo` | `hien`, `file`, `vi_tri` (`phai-duoi` hoặc `trai-duoi`), `kich_thuoc` (132), `le` (44), `bong` (false; true thì thêm bóng đổ nhẹ) |
| `sfx` | `track` (file sfx đã ghép), `am_luong` (0,65) |
| `canh[]` | `id`, `ten`, `tep_kich_ban`, `tep_loi_thoai` (tên file giọng, không đuôi), `du_kien_giay` (ước tính trước khi có giọng), `giu_them_giay` (giữ hình thêm sau giọng), tùy chọn `tep_composition` |

Độ dài cảnh = độ dài file giọng + 2 x `do_tre_giay` + `giu_them_giay`. Cảnh chưa có giọng dùng `du_kien_giay` và được đánh dấu ước tính.
