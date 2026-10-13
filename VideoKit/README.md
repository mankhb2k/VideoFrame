# VideoKit

Bộ asset và công cụ dùng chung cho các video giải thích làm bằng [HyperFrames](https://hyperframes.heygen.com). Sinh ra từ video đầu tiên (OOP vs POP).

## Cấu trúc

| Thư mục | Nội dung |
|---|---|
| `brand/` | logo, logo tròn viền trắng, font Be Vietnam Pro (giấy phép OFL) |
| `characters/` | mỗi nhân vật một thư mục: PNG nền trong suốt + `prompt.md` (prompt gốc, model, cách tạo) |
| `sfx/` | thư viện 9 hiệu ứng tổng hợp bằng code (loại thứ 10, `type`, tạo theo độ dài cue) |
| `music/` | nhạc nền; chỉ thêm nhạc có giấy phép rõ ràng và ghi nguồn vào `NGUON.md` |
| `styles/` | khối prompt phong cách ảnh, `design.md` mẫu |
| `scripts/` | công cụ dòng lệnh (bảng dưới) |
| `templates/` | `font-face.css`, `BRIEF.md`, `STORYBOARD.md`, định dạng cue âm thanh, cấu trúc dự án |
| `ledger/` | sổ chi phí API (`chi-phi-api.csv`) |

## Script

Chạy từ thư mục gốc của dự án video (hoặc đặt `VIDEOKIT_PROJECT`). Cần Python 3.10+; script chỉ dùng thư viện chuẩn, trừ `tao_sfx.py` (numpy) và các script xử lý ảnh (pillow).

| Script | Việc |
|---|---|
| `sync_assets.py` | chép nhân vật, sfx, font, logo vào dự án và ghi manifest |
| `tao_anh_openai.py` | tạo ảnh nhân vật nền trong bằng API ảnh OpenAI (lấy `khi.png` làm tham chiếu phong cách) |
| `phien_am_openai.py` | lấy mốc **từng từ** của giọng đọc (whisper-1) |
| `can_nhip_loi.py` | mốc câu ước lượng từ khoảng lặng; kém chính xác hơn mốc từng từ, chỉ dùng khi không có API |
| `tao_sfx.py` | tổng hợp thư viện sfx và ghép track từ các file `*.sfx.json` |
| `logo_tron.py` | cắt logo thành khung tròn viền trắng và ghép thử vào khung hình |
| `tao_thumbnail_nen.py` | tạo nền thumbnail 16:9 (không chữ); chữ và logo ghép sau bằng HTML |
| `tach_nen_trang.py` | tách nền trắng khỏi ảnh hoạt hình (xóa vùng trắng nối với mép) |
| `ghep_xem.py` | xếp nhiều PNG nền trong lên nền video để xem nhanh |

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
