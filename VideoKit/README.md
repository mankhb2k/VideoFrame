# VideoKit

Bộ asset và công cụ dùng chung cho các video giải thích làm bằng [HyperFrames](https://hyperframes.heygen.com). Sinh ra từ video đầu tiên (OOP vs POP).

## Cấu trúc

| Thư mục | Nội dung |
|---|---|
| `brand/` | logo, logo tròn viền trắng, font Be Vietnam Pro (giấy phép OFL) |
| `characters/` | mỗi nhân vật một thư mục: PNG nền trong suốt + `prompt.md` (prompt gốc, model, cách tạo) |
| `sfx/` | thư viện 9 hiệu ứng tổng hợp bằng code (loại thứ 10, `type`, tạo theo độ dài cue) |
| `music/` | nhạc nền; chỉ thêm nhạc có giấy phép rõ ràng và ghi nguồn vào `NGUON.md` |
| `styles/` | khối prompt phong cách ảnh; `design-sang.md` (nền trắng ngà, mặc định cho video học thuật), `design-toi.md` (nền tối, video công nghệ nhiều code) |
| `scripts/` | công cụ dòng lệnh (bảng dưới) |
| `templates/` | **`du-an/` (khuôn dự án chuẩn)**, `du-an.schema.md`, `font-face.css`, `BRIEF.md`, `STORYBOARD.md`, định dạng cue âm thanh, cấu trúc dự án |
| `ledger/` | sổ chi phí API (`chi-phi-api.csv`) |

## Thương hiệu (nền trắng ngà)

Nền trắng ngà `#F8F7F4` (không dùng trắng tinh), chữ đen `#111113`; màu chữ khác theo **nghĩa** (giá liệt kê xanh dương đậm, giá bán và tổng xanh lá đậm, cảnh báo đỏ); cam THO CODE `#F26A21` là màu nhận diện (chỉ tô nền, không làm chữ). Năm màu khái niệm: biến vàng, hàm xanh dương, database tím, if/else lục lam, vòng lặp hồng. Vật thể kiểu giao diện thường (viền mảnh, bóng mềm); **code luôn nằm trong cửa sổ nền đen kiểu macOS có 3 chấm**.
Một nguồn duy nhất: `templates/thuong-hieu.css`. `build_index.py` chèn nó vào `index.html`, nên cảnh nào cũng dùng được `var(--muc)`, `.th-vat`, `.th-gach`, `.th-cuaso` (cửa sổ code). Ảnh bảng màu sinh bằng `scripts/tao_bang_mau.py` từ chính file CSS, xem `brand/bang-mau-thuong-hieu.png`.

## Script

Chạy trong thư mục dự án video hoặc bất kỳ thư mục con nào (script tìm `du-an.json` đi lên), hoặc đặt `VIDEOKIT_PROJECT`. Cần Python 3.10+; script chỉ dùng thư viện chuẩn, trừ `tao_sfx.py` (numpy) và các script xử lý ảnh (pillow).

| Script | Việc |
|---|---|
| `tao_bang_mau.py` | sinh ảnh bảng nhận diện thương hiệu từ `templates/thuong-hieu.css` |
| `tao_du_an.py` | **tạo dự án mới từ khuôn** (`videos/<slug>/`), tự đọc các file `canh-N-*.md` |
| `build_index.py` | **sinh `index.html` và `moc-canh.json`** từ `du-an.json` và độ dài giọng đọc thật (logo, sfx, font, khung hình theo chuẩn) |
| `sync_assets.py` | chép nhân vật, sfx, font, logo vào dự án và ghi manifest |
| `tao_anh_openai.py` | tạo ảnh nhân vật nền trong bằng API ảnh OpenAI (lấy `khi.png` làm tham chiếu phong cách) |
| `phien_am_openai.py` | lấy mốc **từng từ** của giọng đọc (whisper-1) |
| `can_nhip_loi.py` | mốc câu ước lượng từ khoảng lặng; kém chính xác hơn mốc từng từ, chỉ dùng khi không có API |
| `tao_sfx.py` | tổng hợp thư viện sfx và ghép track từ các file `*.sfx.json` |
| `logo_tron.py` | cắt logo thành khung tròn viền trắng và ghép thử vào khung hình |
| `tao_thumbnail_nen.py` | tạo nền thumbnail 16:9 (không chữ); chữ và logo ghép sau bằng HTML |
| `tach_nen_trang.py` | tách nền trắng khỏi ảnh hoạt hình (xóa vùng trắng nối với mép) |
| `ghep_xem.py` | xếp nhiều PNG nền trong lên nền video để xem nhanh |

## Bắt đầu một video mới

```
python3 VideoKit/scripts/tao_du_an.py <slug> --ten "..." --kich-ban <thư mục chứa canh-N-*.md> --di-chuyen
cd videos/<slug>        # từ đây các script tự tìm du-an.json
```

Bố cục và lệnh thường dùng: `templates/du-an/README.md`. Cấu hình: `templates/du-an.schema.md`.

## Quy trình (rút gọn)

1. Kịch bản chia cảnh, mỗi cảnh một file lời thoại.
2. Giọng đọc từng cảnh, **rồi lấy mốc từng từ ngay** (`phien_am_openai.py`).
3. Thiết kế và nhân vật: `sync_assets.py` lấy từ VideoKit, thiếu thì tạo và bổ sung vào `characters/`.
4. Dựng cảnh theo mốc từ thật, mỗi cảnh xuất `.sfx.json` (xem `templates/sfx-cue-format.md`).
5. Ghép: `index.html`, track sfx (`tao_sfx.py`), logo. `hyperframes check` phải sạch.
6. Rà soát bằng ảnh tổng hợp từng cảnh; đo mức sfx so với giọng.
7. Render nháp 30 fps rồi bản cuối 60 fps.
8. Gói đăng bài: thumbnail, mô tả, mục lục.

## Bẫy đã gặp

- Mốc câu ước lượng làm hình lệch lời: luôn dùng mốc từng từ.
- Gói việc cảnh vượt 48000 byte thì công cụ từ chối: mỗi cảnh chỉ trích 1 blueprint và 2 đến 3 rule.
- Studio tự sửa HTML đang mở: dừng `hyperframes preview` trước khi sửa tay.
- Chữ trong suốt (`color: rgba(...,0)`) bị coi là lỗi bố cục; dùng `opacity`.
- Chữ trắng trên xanh ngọc sáng không đủ tương phản (cần 3:1).
- Python hệ thống macOS là 3.9; một số thư viện cần 3.10+.
- Hạn mức miễn phí TTS Gemini rất thấp (10 yêu cầu mỗi ngày mỗi model): đọc mỗi cảnh một yêu cầu.
- Render 60 fps khoảng 18 phút cho video 8,7 phút (khung hình chụp chậm vì có `mix-blend-mode`).

## Khóa API

Không lưu trong VideoKit. Mỗi máy có `.env` riêng ở gốc dự án (đã bị `.gitignore` bỏ qua) với `GOOGLE_API_KEY` và `OPENAI_API_KEY`.
