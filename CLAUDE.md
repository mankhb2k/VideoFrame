# CLAUDE.md — quy ước làm video giải thích (VideoKit + videos/)

Trả lời người dùng bằng tiếng Việt. Repo chỉ giữ `VideoKit/` (công cụ, asset dùng chung) và `videos/<slug>/` (từng video). Tổng quan: `VideoKit/README.md`.

## Quy trình tạo ảnh (làm trước khi tạo giọng đọc)

1. **Lập danh sách tối thiểu** trong `videos/<slug>/video/anh.json`. Mỗi ảnh phải có lý do tồn tại: nếu HTML + animation làm được thì không tạo ảnh.
2. Chạy `python3 ../../VideoKit/scripts/tao_anh.py --liet-ke` để sinh `DANH-SACH-ANH.md`, đưa người dùng duyệt (số ảnh, chi phí ước tính).
3. Tạo theo thứ tự: nhân vật gốc → đạo cụ → dáng (dáng cầm vật thì cần vật trước, khai báo `tham_chieu_phu`) → nền. Mỗi nhóm: `--nhom goc|vat-pham|dang|nen`.
4. Duyệt bằng mắt (`ghep_xem.py`) và `tao_anh.py --kiem-tra` (chiều cao các dáng lệch ≤ vài % so với ảnh gốc). Ảnh lệch thì `--id ... --ghi-de`.
5. Ghi chi phí vào `VideoKit/ledger/chi-phi-api.csv` (đúng model: ảnh gốc/đạo cụ là `flare`, dáng chỉnh sửa là `sunburst`). Ảnh dùng lại được thì chuyển vào `VideoKit/characters/<tên>/` kèm `prompt.md`.

## Quy tắc gộp ảnh (tiết kiệm tiền, và nhìn gọn hơn)

Hỏi trước khi thêm một ảnh mới: **gộp được không, hay làm bằng path motion được không?**

**Gộp vào một ảnh khi:**
- Nhân vật luôn đi cùng một vật cố định (người + quầy, người + bàn): tạo **một ảnh người cùng vật**, không tạo riêng.
- Nhiều nhân vật phụ chỉ xuất hiện cùng nhau ở một đoạn (ví dụ ba kế toán ngồi chung một bàn): **một ảnh nhóm** (`nhan_vat_them` trong `anh.json`), nhân vật chính lấy ảnh gốc làm tham chiếu, người phụ không cần ảnh gốc riêng.
- Cùng một vật nhưng khác nhãn hoặc màu (bao gạo ST25/Jasmine/thường, chai nước mắm hãng A/B, sổ hai màu bìa): **một ảnh trơn, nhãn trống**; phần khác biệt là nhãn HTML.
- Hai dáng cùng ý nghĩa cảm xúc (gọi to và sửng sốt): một dáng.
- Cần "nhìn người xem", "đứng yên", "mỉm cười nhẹ": dùng ảnh gốc, không tạo dáng.

**Dùng path motion, không tạo ảnh, khi hành động là một vật di chuyển giữa hai chỗ:**
- đưa giấy cho ai, dán nhãn, dán mã, treo biển hiệu, vẽ bằng bút, đặt tiền, bao gạo trượt từ xe tải lên kệ;
- cái "đầy" từ cái "trống": giỏ đầy, kệ đầy, đống bao ngổn ngang → thả các đạo cụ đã có vào giỏ/kệ trống, xoay lệch vài độ;
- chữ, tờ giấy, nhãn giá, biển hiệu, tờ tiền cận cảnh: luôn là phần tử HTML/CSS (chữ do AI vẽ hay sai dấu tiếng Việt), không bao giờ vẽ trong ảnh.

Chỉ tạo dáng riêng khi **cơ thể hoặc nét mặt** mang ý nghĩa (bối rối, mệt, vẫy chào đi ra, hỏi, ôm hộp đồ, đội năm cái mũ). Nếu một hành động bằng path motion nhìn gượng khi dựng (ví dụ bao gạo bay mà không ai khuân), lúc đó mới bổ sung dáng.

### Cách viết path motion (HyperFrames)

- Animation phải xác định (seek-safe): không `Math.random()`, không `Date.now()`; xoay lệch ngẫu nhiên thì ghi giá trị cố định.
- Cung bay: tween `x` với `ease:"none"` hoặc `power1.inOut` song song với tween `y` có ease khác (`sine.inOut`), cộng xoay nhẹ; hoặc GSAP MotionPathPlugin. Plugin này không nằm trong gsap lõi mà `build_index.py` đang nạp, nên nếu dùng phải thêm thẻ script đúng phiên bản và chạy `hyperframes check` để chắc chắn nó nạp được.
- Vật đến nơi thì có nhịp kết thúc rõ (nảy nhẹ hoặc scale 1.0 → 1.08 → 1.0) và một cue sfx khớp thời điểm chạm.
- Vật bay phải nằm trên nhân vật hoặc quầy đích (z-index) và không che chữ quan trọng. Kiểm tra bằng `hyperframes check`.

## Quy tắc nhất quán nhân vật

- Mỗi nhân vật có một khối nhận diện tiếng Anh cố định trong `anh.json` (`nhan_dang`): tạo ảnh gốc trước, mọi dáng chỉnh sửa từ chính ảnh gốc đó (`model_chinh_sua`).
- Khung chuẩn: thân người cao khoảng 88% khung, chân cách đáy 4%, nền trong suốt, không chữ, không bóng đổ.
- Không dùng quần áo trắng, đỏ hoặc xanh lá thuần (trùng màu chữ có nghĩa của thương hiệu).
- Chiều cao tương đối giữa các nhân vật chỉnh khi dựng cảnh, không chỉnh trong ảnh.
- Dáng ngồi hoặc đứng sau quầy chỉ lấy nửa thân trên.

## Thứ tự làm một video (rút kinh nghiệm từ video trước)

1. Kịch bản → danh sách ảnh và ảnh (tối thiểu, gộp, path motion) → **giọng đọc → nghe và chốt giọng → whisper lấy mốc từng từ** → storyboard theo mốc thật → dựng cảnh → sfx → render.
2. **Chốt giọng trước khi dựng cảnh.** Giọng đọc rẻ (vài chục cent) nhưng mọi nhịp hình trong cảnh gán theo mốc giây của giọng; đổi giọng sau khi dựng là phải co giãn lại toàn bộ.
3. Mỗi cảnh **một yêu cầu TTS**, không đọc từng khối rồi ghép, **không chèn khoảng dừng** `[Dừng N giây]` và nhịp thở nhân tạo: Gemini tự ngắt nghỉ theo câu. Chỗ cần giữ hình cho người xem đọc thì chèn lặng 1 giây ở vài chỗ do người làm video chọn sau khi nghe bản đọc.
4. OpenAI whisper chỉ để lấy mốc từng từ (không tạo hay cắt giọng); chạy **sau khi** âm thanh đã chốt (mọi lần cắt sau đó làm lệch mốc).
5. Duyệt hình ảnh (bố cục, chữ, nhân vật) có thể làm sớm bằng ảnh tĩnh hoặc Studio, nhưng nhịp xuất hiện chỉ gán sau khi giọng đã chốt.

## Thương hiệu

Nền trắng ngà `#F8F7F4`, chữ đen, màu chữ theo nghĩa (giá liệt kê xanh dương đậm, giá bán và tổng xanh lá đậm, cảnh báo đỏ), cam chỉ tô nền, code trong cửa sổ đen 3 chấm, vật thể kiểu giao diện thường (không bóng cứng kiểu game). Nguồn duy nhất: `VideoKit/templates/thuong-hieu.css`.

## Ngôn ngữ: mã component và nội dung video

- **Mã dùng chung trong `VideoKit/components/`** (tên hàm, tuỳ chọn, class CSS mới) viết **tiếng Anh**, ví dụ `vk.ide`, `type`, `show`, `highlight`. Phần cũ của `core/` còn tên tiếng Việt (`vao`, `pop`, `cung`...), không đổi khi chưa có bí danh.
- **Nội dung hiển thị trong video** (code demo, chữ trên màn hình, lời dẫn, tên nhân vật) giữ **tiếng Việt**: tên biến trong code demo không dấu (`ten_cua_hang`), chuỗi chữ có dấu (`"Tạp hoá Ông Sơn"`).

## Kịch bản dạy tư duy lập trình

Khi viết hoặc sửa kịch bản loạt "lập trình cơ bản" (thư mục `videos/lap-trinh-co-ban-*/kich-ban/`), đọc và làm theo `VideoKit/templates/kich-ban-tu-duy/QUY-TAC.md` trước. Tóm tắt: lời dẫn tiếng Việt không đọc tên biến, tên trong code được tô sáng trên hình; mỗi khái niệm có một câu chuyện; dạy tư duy chung, hạn chế chi tiết cú pháp Python; tên biến rõ nghĩa và không trùng; code phải chạy được; kịch bản trước, hình sau; câu chốt do người viết tự viết.

## Render

- Lệnh render trong `package.json` đã kèm `HF_CAPTURE_PARALLEL_STREAM=true` để đưa khung hình thẳng sang ffmpeg, **không lưu ảnh tạm xuống đĩa**. Không bật thì nhiều worker lưu mỗi khung hình thành một file ảnh (video 13 phút ở 60 fps cần khoảng 97 GB) và lỗi nếu đĩa không đủ.
- Ước thời gian render 60 fps: khoảng 3,3 phút cho mỗi phút video trên máy này (video 13 phút trước đây mất 43 phút). Đừng ước từ tốc độ của vài chục giây đầu.
- Chỉ render khi người dùng yêu cầu; trước đó tắt `hyperframes preview` và kiểm `index.html` khớp bản vừa dựng.

## Chuyện cần nhớ

- Dừng `hyperframes preview` trước khi sửa HTML (Studio tự ghi đè file).
- Đừng commit hoặc push khi người dùng chưa yêu cầu. Không đưa `.env`, `*.mp4`, `*.zip` lên repo (đã có trong `.gitignore`).
- Script cần Pillow/numpy chạy bằng Python 3.14 có cài các gói đó, không dùng Python hệ thống.
- Script sửa kịch bản nhằm giúp người xem hiểu, không nhằm rút ngắn thời gian.
