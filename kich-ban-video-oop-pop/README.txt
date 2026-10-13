GÓI KỊCH BẢN VIDEO: OOP (TypeScript) vs POP (Swift)
===================================================

Nội dung trong thư mục
----------------------
kich-ban-video.md            Kịch bản đầy đủ: bố cục thời gian, hình ảnh từng cảnh, code TypeScript/Swift,
                             bảng so sánh, bảy luật, ghi chú dựng bằng HTML/CSS/Tailwind + GSAP.
loi-thoai/canh0..canh7.txt   Lời thoại đầy đủ từng cảnh, văn bản thuần, mỗi đoạn cách nhau một dòng trống.
                             Dán thẳng vào bất kỳ công cụ TTS nào (khoảng 1.750 từ, khoảng 9 đến 10 phút).
loi-thoai/loi-thoai-day-du.md  Toàn bộ lời thoại nối lại trong một file, có tiêu đề từng cảnh.
loi-thoai/bang-phat-am.csv   Bảng viết lại từ tiếng Anh (OOP, TypeScript, protocol...) cho TTS tiếng Việt đọc đúng.
tao_tts_gemini.py            Tạo giọng nam "nhiệt huyết, giảng dạy giàu cảm xúc" bằng Gemini TTS (cần khóa API Google).
tao_tts_vieneu.py            Tạo giọng bằng VieNeu-TTS chạy trên máy bạn (miễn phí, không cần khóa).
tien_ich.py                  Hàm dùng chung (đọc cảnh, ghép file wav, áp dụng bảng phát âm).

Cách dùng nhanh
---------------
1) Chỉ cần dán chữ: mở từng file loi-thoai/canhN_*.txt, dán vào công cụ TTS bạn chọn.
   Nếu giọng đọc sai từ tiếng Anh, dùng "tìm và thay thế" theo bang-phat-am.csv.

2) Chạy bằng Gemini (cần Python 3.9+):
     pip install "google-genai>=2.25.0"
     export GEMINI_API_KEY="khóa của bạn"        (Windows PowerShell: $env:GEMINI_API_KEY="khóa của bạn")
     python tao_tts_gemini.py --tao-giong        (nghe thử preview_giong.wav)
     python tao_tts_gemini.py                    (đọc toàn bộ cảnh, kết quả ở dau-ra/)

3) Chạy bằng VieNeu (Python 3.10+):
     pip install vieneu
     python tao_tts_vieneu.py
   Lần đầu sẽ tải model khoảng 1,7 GB. Muốn dùng giọng của bạn: thêm --ref-audio giong_cua_toi.wav

Lưu ý
-----
- Hai script tạo giọng viết theo tài liệu của Google và VieNeu, chưa được chạy thử với khóa/model thật.
  Nếu có lỗi, hãy gửi lại thông báo lỗi để chỉnh.
- KHÔNG ghi khóa API vào file và không dán vào chat. Nếu bạn đã lỡ để lộ khóa, hãy xóa và tạo khóa mới
  trong Google AI Studio hoặc Google Cloud Console.
- Chỉ nhân bản giọng của chính bạn hoặc của người đã đồng ý.
- Độ dài mỗi cảnh trong lời thoại khác mốc thời gian trong kịch bản; khi dựng, hãy chỉnh tốc độ đọc
  hoặc rút câu cho khớp hình.
