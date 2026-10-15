---
format: 1920x1080
duration: 779.6s
message: "Phần mềm triệu đô được xây trên những viên gạch nền móng, giống tiệm tạp hoá của ông Sơn: biến, hàm, database, if/else và vòng lặp."
arc: Hook (đoạn code lạ) → Biến → Hàm → Database → If/else và vòng lặp → Nhìn từ trên cao (framework, kiến trúc) → Khép vòng hook và thử thách
audience: người mới học lập trình
mode: collaborative
---

# Storyboard: Ông Sơn, từ tiệm tạp hoá đến phần mềm triệu đô

Mốc **giây** dưới đây là giây **trong cảnh** (đã cộng 0,3 giây lặng đầu cảnh), lấy từ `assets/audio/words-<cảnh>.json`; mỗi nhịp neo vào cụm từ ghi trong ngoặc. Sửa giọng đọc thì sinh lại file này, đừng sửa mốc bằng tay. Cảnh dài được chia thành các **gói** dưới 48.000 byte để giao cho worker.


## Ngôn ngữ hình ảnh chung (mọi cảnh)

**Nền và chữ.** Nền `#F8F7F4`, chữ đen. Giá liệt kê xanh dương đậm (`.th-gia`), giá bán và tổng xanh lá đậm (`.th-gia-ban`, `.th-tong`), cảnh báo đỏ (`.th-canh-bao`). Cam chỉ tô nền. Vật thể thẻ có viền mảnh và bóng mềm (`.th-vat`). **Code luôn trong cửa sổ đen 3 chấm** (`.th-cuaso`), tối đa 6 dòng trừ đoạn code đầu video.

**Kệ gạch (nhân vật xuyên suốt).** Góc trên bên trái, một kệ ngang năm ô, rộng khoảng 700 px, lề 96 px. Mỗi cuối cảnh một viên gạch (vuông bo góc 120 px, màu khái niệm) rơi vào ô, kèm tiếng đặt xuống: BIẾN vàng `#FACC15` (C1), HÀM xanh dương `#3B82F6` (C2), DATABASE tím `#8B5CF6` (C3), IF/ELSE lục lam `#14B8A6` và VÒNG LẶP hồng `#EC4899` (C4). Chữ trên gạch đen đậm (`--chu-tren-mau`). Kệ hiện từ cuối C1 tới C5; góc phải dưới dành cho logo kênh, không đặt nội dung.

**Nhân vật.** Mọi PNG đã chuẩn hoá cao khoảng 88% khung, nên chiều cao hiển thị do bố cục quyết định. Chuẩn (Ông Sơn luôn cao hơn Cô Lan một chút): Ông Sơn 108%; Cô Lan 98%; Anh Tâm 102%; Chị Hạnh 98%; Anh Hùng 104%; Bình 94%; Bà Tư 88%; Thanh niên 106%. Dáng ngồi và đứng sau quầy là nửa thân nên đầu to hơn dáng đứng ở cùng `size`: dùng `size` nhỏ hơn dáng đứng khoảng 10% để **giữ cùng cỡ đầu**. Bóng dưới chân bằng một elip mờ CSS, không có trong ảnh.

**Path motion thay cho dáng.** Mọi vật chuyển giữa hai chỗ là phần tử HTML bay theo cung (hai tween `x` và `y` khác ease, xoay nhẹ, nảy khi chạm, một sfx khớp lúc chạm): nhãn giá dán lên thùng, mã dán lên hàng, tờ giấy giá từ phòng kế toán tới Cô Lan, biển hiệu trượt lên, bút đỏ vạch, bao gạo từ xe tải lên kệ. Cái "đầy" là cái "trống" cộng các đạo cụ đã có thả vào (kệ gạo, giỏ hàng, đống bao). Chữ trên bao, thùng, chai, sổ luôn là nhãn HTML.

**Đạo cụ trơn và nhãn HTML.** `vat/bao-gao`, `vat/thung-gao`, `vat/chai-nuoc-mam`, `vat/so` có vùng nhãn trống; nhãn là thẻ HTML đặt đúng vùng (chip chữ đen, nền trắng viền mảnh). Sổ hàng hoá tô tím nhạt, sổ hoá đơn tô xanh dương nhạt bằng lớp phủ `mix-blend-mode: multiply`.

**Cảnh nối cảnh.** Hai cảnh kề nhau nối bằng kệ gạch: viên gạch rơi xong thì cắt cứng sang cảnh sau (vào bằng cắt, không mờ chồng). Mỗi cảnh dừng 0,3 giây đầu và cuối theo `du-an.json`.

**Âm thanh.** SFX do `tao_sfx.py` tạo theo file `.sfx.json` của từng cảnh: tiếng "tách" mỗi nhãn dán, "bịch" mỗi bao gạo, "tinh" khi giá trị đổi, "cạch" khi viên gạch chạm kệ, "ting" khi khái niệm mới hiện. Mức 0,65 so với giọng.

## Frame 1 — Mở đầu: một đoạn code lạ

- scene: Đoạn code 13 dòng của tiệm tạp hoá trong cửa sổ đen, chữ nhỏ "Bạn thấy gì?" bên dưới; cuối cảnh cửa sổ thu nhỏ rồi cắt sang câu chuyện.
- start: 0.0s
- duration: 18.8s
- voice: 0.3s → 18.3s
- transition_in: cut (mở đầu video: logo đã hiện sẵn ở góc phải dưới từ 0,3 giây)
- status: outline
- blueprint: typewriter-reveal (gần nhất, dựng tự do)
- composition_id: scene-1
- cues: canh0_mo-dau
- assets: không dùng ảnh PNG; cửa sổ code `.th-cuaso`
- rules: discrete-text-sequence (code gõ theo từng dòng), asr-keyword-glow (làm sáng cụm "thấy rối" và "câu chuyện")
- src: compositions/frames/01-canh0.html (dựng theo từng đoạn: compositions/frames/c0-d*.html)
- packets: 1 gói
- voiceover: "Đây là một đoạn code thật của một tiệm tạp hoá. Nếu bạn nhìn vào và thấy rối, bạn không đơn độc…"

### Đoạn 1: Một đoạn code trông như tiếng lạ

_Bố cục_: cửa sổ code giữa khung rộng khoảng 1240 px, font code 30 px, 13 dòng; chú thích "Bạn thấy gì?" 40 px chữ phụ nằm dưới cửa sổ, cách 40 px.

- **0.3s** (“Đây là một đoạn”) — Cửa sổ code hiện (scale 0,96→1, mờ→rõ, 0,5 giây); 13 dòng gõ lần lượt từng dòng, mỗi dòng ~0,2 giây, xong khoảng giây thứ 3.
- **3.1s** (“Nếu bạn nhìn vào”) — Gõ xong; con trỏ nhấp nháy ở cuối. Chú thích "Bạn thấy gì?" hiện dưới cửa sổ.
- **6.2s** (“ai mới học lập trình”) — Cả đoạn code **đứng yên** 3 giây (khoảng dừng có chủ đích): để người xem nhìn, không có chuyển động nào khác ngoài con trỏ.
- **8.7s** (“Nhưng cuối video này”) — Chú thích đổi thành "Cuối video này, bạn sẽ đọc được từng dòng" (chuyển kiểu cắt chữ tại chỗ).
- **12.0s** (“hiểu cách một phần mềm”) — Dòng chữ "triệu đô" phóng nhẹ (1→1,06→1) ngay khi giọng đọc tới đó.
- **15.7s** (“sẽ không bắt đầu bằng”) — Cửa sổ code mờ dần xuống 25% và thu nhỏ 0,8 về giữa khung.
- **17.3s** (“Chúng ta bắt đầu bằng một câu chuyện”) — Chữ "MỘT CÂU CHUYỆN" 96 px hiện giữa khung (spring-pop), giữ tới hết cảnh; cắt sang Cảnh 1.

## Frame 2 — Ông Sơn và 20 triệu đồng: biến

- scene: Ông Sơn mở tiệm gạo với 20 triệu: nhập ba loại gạo, dán nhãn giá lên ba thùng (biến = tên + giá trị), viết code song song, rồi vì sao tên quan trọng; kết bằng viên gạch BIẾN.
- start: 18.8s
- duration: 103.5s
- voice: 0.3s → 102.7s
- transition_in: cut từ Cảnh 0
- status: outline
- blueprint: comparison-split (đoạn 4, 5) và grid-card-assemble (đoạn 3)
- composition_id: scene-2
- cues: canh1_ong-son-va-20-trieu-dong
- assets: ong-son/goc, ong-son/cam-tien, ong-son/ngac-nhien, binh/boi-roi; vat/xe-tai, vat/bao-gao, vat/thung-gao, vat/ke-gao-trong; nen/mat-bang-trong
- rules: press-release-spring (nhãn dán), svg-path-draw (mũi tên nối nhãn với code), waterfall-entry (ba dòng code)
- src: compositions/frames/02-canh1.html (dựng theo từng đoạn: compositions/frames/c1-d*.html)
- packets: 3 gói: đoạn 1-2; đoạn 3-4; đoạn 5 và chốt cảnh
- voiceover: "Chúng ta bắt đầu với ông Sơn. Ông có trong tay 20 triệu đồng và quyết định mở một cửa hàng gạo…"

### Đoạn 1: Dự án bắt đầu từ đâu

_Bố cục_: nền `nen/mat-bang-trong` toàn khung; Ông Sơn (`ong-son/cam-tien`) đứng bên trái, cao 620 px.

- **0.3s** (“Chúng ta bắt đầu với ông Sơn”) — Mặt bằng trống hiện (cắt); Ông Sơn trượt từ trái vào, dừng bên trái giữa khung.
- **4.3s** (“mở một cửa hàng gạo”) — Chữ "20.000.000đ" 120 px đếm từ 0 lên 20.000.000 (đen, nảy nhẹ lúc dừng) bay lên phía trên xấp tiền.
- **6.5s** (“Nghe quen không”) — Ông Sơn nghiêng người nhẹ (xoay 2°) như hỏi người xem.
- **10.5s** (“một người, một ít vốn”) — Ba chip chữ lần lượt hiện bên phải: "một người", "một ít vốn", "một ý tưởng" (mỗi chip 0,5 giây).
- **13.8s** (“Phần mềm triệu đô nào”) — Chip hợp thành dòng "phần mềm triệu đô" ← "cửa hàng 20 triệu", chữ nhỏ trên chữ lớn.

### Đoạn 2: Nhập hàng

_Bố cục_: giữ nền mặt bằng; xe tải (`vat/xe-tai`) vào từ trái.

- **18.2s** (“Ông Sơn nhập về ba loại gạo”) — Xe tải trượt vào từ trái, dừng trước tiệm; Ông Sơn đổi sang `ong-son/goc` đứng cạnh.
- **20.2s** (“Bao nào cũng trắng như nhau”) — Chín bao gạo trơn (`vat/bao-gao`) bay theo cung từ thùng xe vào giữa tiệm, mỗi bao nảy một lần, xoay lệch 3 đến 12 độ (giá trị cố định) thành một đống ngổn ngang; sfx bịch rải theo nhịp.
- **23.5s** (“việc đầu tiên ông phải làm”) — Đống bao rung nhẹ, dấu hỏi nhỏ màu đen xuất hiện trên đầu Ông Sơn.
- **27.1s** (“phân loại gạo và ghi giá”) — Đống bao tách thành ba cụm (thu về ba chỗ), chuẩn bị cho đoạn sau.

### Đoạn 3: Phân loại và ghi giá

_Bố cục_: ba thùng gạo (`vat/thung-gao`) xếp hàng ngang ở giữa, cách nhau 120 px; Ông Sơn (`ong-son/goc`) đứng bên trái.

- **29.8s** (“Thùng này là”) — Thùng 1 hiện; nhãn "ST25" bay từ tay Ông Sơn vào vùng nhãn rồi chip giá "30.000đ" (xanh dương đậm `.th-gia`) hiện trên thùng; tách.
- **33.5s** (“Thùng này là”) — Thùng 2: nhãn "Jasmine", giá "20.000đ".
- **36.1s** (“Thùng này là”) — Thùng 3: nhãn "Gạo thường", giá "15.000đ".
- **39.4s** (“Ông vừa làm hai việc”) — Ông Sơn đứng giữa ba thùng; hai mũi tên cong từ nhãn về chữ "TÊN" và từ giá về chữ "GIÁ TRỊ" hiện cùng lúc.
- **40.8s** (“đặt tên cho từng thứ”) — Chữ "TÊN" sáng (vàng đậm `#854D0E` trên nền vàng nhạt).
- **42.0s** (“gắn giá trị”) — Chữ "GIÁ TRỊ" sáng cùng kiểu.
- **46.0s** (“tạo biến”) — Hai chip nối bằng dấu "+" thành khối "BIẾN = TÊN + GIÁ TRỊ" 72 px nền vàng nhạt; **giữ trên màn hình** cho tới hết khoảng dừng 2 giây.

### Đoạn 4: Cùng một việc, viết bằng code

_Bố cục_: chia đôi khung: trái ba thùng nhỏ lại (mỗi thùng 280 px) có nhãn dán sẵn; phải cửa sổ code 3 dòng (`gia_gao_st25 = 30000`…) rộng 860 px, font 38 px. Đường chia mảnh giữa khung.

- **47.8s** (“Nhìn bên phải”) — Khung chia đôi: ba thùng thu sang trái, cửa sổ code trượt vào từ phải (0,6 giây).
- **50.1s** (“Dòng đầu tiên”) — Dòng 1 sáng (nền mờ vàng sau dòng); cùng lúc nhãn thùng 1 phát sáng viền vàng, mũi tên vẽ nối `gia_gao_st25` với nhãn.
- **55.1s** (“bằng nghĩa là”) — Dấu `=` trong code phóng 1,3 lần, một chiếc nhãn nhỏ làm bằng chữ dán lên thùng (path motion).
- **60.1s** (“Đọc to lên”) — Dưới code hiện chú thích đọc: "giá gạo ST25 bằng 30 nghìn" (từng chữ sáng theo giọng đọc).
- **64.1s** (“giống hệt tờ nhãn”) — Chú thích và tờ nhãn trên thùng 1 cùng nháy một lần.
- **66.5s** (“Hai dòng còn lại”) — Dòng 2 rồi dòng 3 sáng lần lượt (0,8 giây mỗi dòng), nhãn thùng 2 và 3 sáng theo.
- **68.7s** (“Ba cái nhãn, ba giá trị”) — Cả ba dòng và ba nhãn sáng đồng thời, các mũi tên nối đủ ba.
- **71.7s** (“ba biến đầu tiên”) — Giữ nguyên hình trong 3 giây dừng, không thêm chuyển động; người xem so sánh ba thùng và ba dòng.

### Đoạn 5: Cú lật, vì sao tên quan trọng

_Bố cục_: trái: code tốt (`gia_gao_st25 = 30000` …) nhỏ lại; phải: code lười (`a = 30000`, `b = 20000`, `c = 15000`) nền đen; Bình (`binh/boi-roi`) bên phải dưới, cao 560 px.

- **74.3s** (“Giờ giả sử”) — Code tốt mờ sang trái; cửa sổ code lười hiện phải với chú thích "# cách ông Sơn lười dán nhãn".
- **78.8s** (“Sáu tháng sau”) — Lịch nhỏ lật "6 tháng sau" ở góc trên giữa; Bình trượt vào từ phải.
- **82.9s** (“Hỏi a là gì”) — Dấu hỏi đỏ `.th-canh-bao` bật ra cạnh `a`, rồi cạnh `b`, rồi `c` (mỗi dấu spring-pop).
- **85.6s** (“Không ai biết”) — Bình gãi đầu (nghiêng), ba dấu hỏi chuyển sang đỏ đậm; Ông Sơn (`ong-son/ngac-nhien`) nhỏ hiện cạnh cũng nhún vai.
- **89.3s** (“sẽ quyết định dự án”) — Toàn cảnh mờ xuống 40%, giữ dấu hỏi to ở giữa tới hết cảnh.

### Chốt cảnh: viên gạch BIẾN

_Bố cục_: kệ gạch năm ô trống (viền đứt nét) ở góc trên trái; viên gạch vàng "BIẾN" lớn (x3) rơi vào giữa khung rồi thu nhỏ bay lên ô 1; dưới viên gạch lớn là định nghĩa ngắn; cuối đoạn Ông Sơn (`ong-son/ban-ron`) hiện giữa khung.

- **93.3s** (“Viên gạch đầu tiên”) — Kệ năm ô trống hiện ở góc trên trái; viên gạch vàng "BIẾN" lớn (x3) rơi từ trên khung xuống giữa khung, nảy một lần (cạch).
- **96.4s** (“một cái nhãn gắn”) — Dưới viên gạch hiện định nghĩa ngắn: "BIẾN = cái nhãn gắn một cái tên vào một giá trị" (chữ 56 px, từ BIẾN vàng đậm).
- **99.1s** (“Nhưng một mình ông Sơn”) — Viên gạch thu nhỏ bay theo cung lên ô 1 của kệ (cạch), định nghĩa mờ đi; Ông Sơn (`ong-son/ban-ron`) hiện ở giữa khung, mồ hôi; giữ hình tới hết cảnh.

## Frame 3 — Ông Sơn bắt đầu thuê người: hàm

- scene: Ông Sơn làm hết mọi việc, thuê Cô Lan (hàm tính tiền) và Anh Tâm (hàm xếp hàng có if), ghép thành quy trình, rồi cú lật người làm hết việc nghỉ; kết bằng viên gạch HÀM.
- start: 122.3s
- duration: 128.0s
- voice: 0.3s → 127.4s
- transition_in: cut từ Cảnh 1 (sau viên gạch BIẾN)
- status: outline
- blueprint: fixed-anchor-cycle (đoạn 4: sơ đồ dây chuyền cố định, các bước sáng lần lượt)
- composition_id: scene-3
- cues: canh2_ong-son-bat-dau-thue-nguoi
- assets: ong-son/ban-ron, ong-son/goc, ong-son/khuan-gao, ong-son/ngac-nhien; co-lan/quay-thu-ngan, co-lan/cau-may; anh-tam/hoi; anh-hung/nam-mu, anh-hung/vay-chao; vat/may-tinh-tien-cu, vat/ke-gao-trong, vat/bao-gao, vat/xe-tai
- rules: svg-path-draw (sơ đồ vào/ra), asr-keyword-glow (sáng từng dòng code theo lời), physics-press-reaction (nhấn nút tính tiền)
- src: compositions/frames/03-canh2.html (dựng theo từng đoạn: compositions/frames/c2-d*.html)
- packets: 3 gói: đoạn 1-2; đoạn 3-4; đoạn 5 và chốt cảnh
- voiceover: "Tiệm bắt đầu có khách. Ông Sơn một mình làm tất cả: tính tiền, đóng gạo, chạy vào kho…"

### Đoạn 1: Ông Sơn làm hết mọi việc

_Bố cục_: trong tiệm (nền trắng ngà, sàn mờ): Ông Sơn `ong-son/ban-ron` ở giữa; ba biểu tượng việc làm (máy tính, bao gạo, kho) xếp vòng quanh ông.

- **0.3s** (“Tiệm bắt đầu có khách”) — Ba bóng khách (hình tròn xám có chân, dùng chip tròn) lần lượt vào từ phải, mỗi bóng một nhịp.
- **2.3s** (“Ông Sơn một mình làm tất cả”) — Ba biểu tượng quanh ông (máy tính tiền, bao gạo, kho) bật lên lần lượt rồi quay tròn quanh ông từ chậm tới nhanh.
- **7.3s** (“Ông nhận ra”) — Vòng quay dừng, chỉ còn biểu tượng máy tính tiền sáng, hai cái kia mờ xuống 30%.
- **10.7s** (“nhân giá với số ký”) — Phép tính "giá × số ký" hiện cạnh máy tính, chữ lớn 80 px.
- **13.7s** (“lần mỗi ngày”) — Số "50 lần / ngày" đếm từ 1 lên 50 (counting-dynamic-scale), số phóng to dần khi lên.

### Đoạn 2: Thuê người thứ nhất, hàm tính tiền

_Bố cục_: trái: Cô Lan sau quầy (`co-lan/quay-thu-ngan`), cao 600 px; phải: sơ đồ vào/ra (hai mũi tên vào, hộp "tính tiền", mũi tên ra); sau đó cửa sổ code 5 dòng.

- **15.2s** (“Ông thuê cô Lan”) — Cô Lan trượt vào sau quầy từ trái; Ông Sơn (`ong-son/goc`) nhỏ hiện cạnh quầy chỉ tay.
- **18.7s** (“Khách mua gì”) — Hai chip vào hiện bên phải: "giá một ký" và "số ký" (chữ đen, số xanh dương đậm), bay vào hộp "tính tiền".
- **22.1s** (“Ông Sơn không cần biết”) — Hộp "tính tiền" mờ thành hộp đen kín (nội dung ẩn): Ông Sơn không cần nhìn bên trong.
- **24.4s** (“đưa gì vào”) — Hai mũi tên vào sáng; sau đó mũi tên ra sáng với chip "tổng tiền" (xanh lá đậm `.th-tong`).
- **27.4s** (“cô Lan chính là một hàm”) — Chữ "HÀM" xanh dương hiện trên đầu Cô Lan (spring-pop); sfx ting.
- **29.8s** (“Để ý tên hàm”) — Cửa sổ code hiện (3 giây dừng): `def tinh_tien(gia_mot_ky, so_ky):` và dòng gọi hàm `tinh_tien(gia_gao_st25, 10)  # trả về 300000`; từ `tinh_tien` sáng viền xanh dương.
- **33.5s** (“giống như chức danh”) — Chip "động từ" bay từ `tinh_tien` sang bảng tên của Cô Lan, rồi cửa sổ code lùi sang phải.

### Đoạn 3: Thuê người thứ hai, hàm xếp hàng lên kệ

_Bố cục_: trái: kệ gạo trống (`vat/ke-gao-trong`), Ông Sơn `ong-son/khuan-gao` chạy qua lại; chuyển sang Anh Tâm (`anh-tam/hoi`) cạnh tờ quy tắc; phải: cửa sổ code 4 dòng có `if`.

- **37.6s** (“Rồi một việc nữa”) — Kệ gạo trống ở giữa; Ông Sơn (`ong-son/khuan-gao`) đi vào từ trái, bao gạo bay từ kho (trái) lên kệ rồi quay lại, lặp hai vòng.
- **43.2s** (“Ông thuê thêm anh Tâm”) — Anh Tâm (`anh-tam/hoi`) trượt vào từ phải thay chỗ Ông Sơn.
- **49.6s** (“Thế thôi”) — Tờ quy tắc (thẻ HTML ghim nghiêng 2°) "Thấy kệ hết hàng thì vào kho lấy ra xếp" bay từ tay Ông Sơn lên tường cạnh Anh Tâm (path motion), dán lại (tách).
- **54.3s** (“Anh chỉ nhìn kệ”) — Đường ngắm mảnh vẽ từ mắt Anh Tâm tới kệ trống.
- **56.3s** (“Để ý chữ”) — Cửa sổ code hiện (3 giây dừng): `def xep_hang_len_ke(so_ky_tren_ke):` / `if so_ky_tren_ke == 0:` / `lay_hang_tu_kho()` / `xep_len_ke()`; từ `if` sáng lục lam.
- **59.2s** (“Hàm này chỉ làm việc”) — Cả khối thụt vào dưới `if` sáng nền lục lam nhạt.
- **65.1s** (“không cần nhắc anh Tâm”) — Hình Ông Sơn nhỏ nhạt (xám) rời khung, tượng trưng việc không phải nhắc.
- **69.1s** (“lát nữa chúng ta sẽ quay lại”) — Chữ `if` nhấp sáng một lần rồi hạ xuống; sfx ting nhẹ (hứa quay lại).

### Đoạn 4: Ghép các hàm thành quy trình

_Bố cục_: trên: sơ đồ dây chuyền bốn nút (khách đến → Cô Lan tính tiền → khách trả tiền → Anh Tâm kiểm tra kệ) rộng 1500 px; Ông Sơn `ong-son/goc` đứng giữa phía dưới; dưới sơ đồ: cửa sổ code 4 dòng.

- **71.3s** (“Bây giờ nhìn tiệm”) — Sơ đồ dây chuyền hiện từ trái sang phải (từng nút 0,4 giây); Ông Sơn đứng giữa dưới sơ đồ.
- **73.2s** (“khách đến”) — Nút 1 sáng.
- **74.1s** (“cô Lan tính tiền”) — Nút 2 sáng, mini `co-lan/goc` hiện trong nút.
- **75.3s** (“anh Tâm lo kệ”) — Nút 3 và 4 sáng, mini `anh-tam/goc` hiện trong nút 4.
- **77.0s** (“Mỗi người một việc”) — Ông Sơn xoay nhìn sơ đồ (đảo hướng nhẹ), tay vẫy theo dây chuyền.
- **83.2s** (“bạn có một thứ gọi là quy trình”) — Khung viền cam mảnh bao quanh cả bốn nút và chữ "QUY TRÌNH" hiện trên khung.
- **86.2s** (“một hàm lớn gọi”) — Cửa sổ code hiện (4 dòng `mot_ngay_ban_hang` gọi `tiep_khach`, `tinh_tien`, `thu_tien`, `xep_hang_len_ke`).
- **89.5s** (“Đọc từ trên xuống”) — Từng dòng code sáng đồng thời với nút tương ứng (3 giây dừng): dòng 1 ↔ nút 1, dòng 2 ↔ nút 2, dòng 3 ↔ nút 3, dòng 4 ↔ nút 4.
- **93.3s** (“Không cần giải thích”) — Giữ hình, mọi dòng và nút sáng nhẹ.

### Đoạn 5: Cú lật, một người làm hết

_Bố cục_: Anh Hùng (`anh-hung/nam-mu`) ở giữa; Ông Sơn (`ong-son/ngac-nhien`) bên trái.

- **95.1s** (“Giả sử ông Sơn thuê”) — Anh Hùng trượt vào giữa tiệm; năm biểu tượng việc (thu ngân, thủ kho, bán hàng, kế toán, bảo vệ) xếp vòng trên đầu.
- **97.9s** (“Lúc đầu ổn”) — Anh Hùng nhún lên xuống nhịp nhàng, dấu tích xanh `ok` nhỏ cạnh anh.
- **101.7s** (“người đó nghỉ”) — Ông Sơn gọi: bong bóng "Anh Hùng nghỉ rồi!" (chữ đen 64 px); Anh Hùng đổi sang `anh-hung/vay-chao` rồi trượt ra khỏi khung bên phải.
- **102.9s** (“cả tiệm đứng im”) — Cả khung đóng băng: Cô Lan, Anh Tâm xám đi (30%), chuyển động dừng 2 giây, cửa sổ code `def lam_het_moi_viec():` hiện (một dòng, bình luận "# tính tiền, xếp kệ, nhập hàng...").
- **106.0s** (“Thuê nhiều người”) — Cảnh sống lại: mọi nhân vật hồi màu, năm biểu tượng việc tách thành năm người nhỏ cạnh nhau.
- **111.5s** (“không sập khi mất một người”) — Một người nhỏ biến mất, bốn người còn lại vẫn sáng; dấu tích xanh `ok` hiện.

### Chốt cảnh: viên gạch HÀM

_Bố cục_: kệ có viên BIẾN ở ô 1; viên gạch xanh dương "HÀM" lớn rơi giữa khung rồi bay lên ô 2; Cô Lan và Anh Tâm hiện với dấu hỏi ở cuối đoạn.

- **114.3s** (“Viên gạch thứ hai”) — Viên gạch xanh dương "HÀM" lớn (x3) rơi xuống giữa khung, nảy một lần (cạch).
- **116.4s** (“một người làm đúng”) — Định nghĩa hiện dưới viên gạch: "HÀM = một người làm đúng một việc" (chữ 56 px, HÀM xanh dương đậm).
- **118.4s** (“Cô Lan tính tiền”) — Hai chip nhỏ cạnh định nghĩa: "Cô Lan: tính tiền" rồi "Anh Tâm: xếp kệ".
- **120.8s** (“Nhưng anh Tâm nhìn vào đâu”) — Viên gạch thu nhỏ bay lên ô 2 của kệ (cạch), định nghĩa mờ đi; Anh Tâm (`anh-tam/hoi`) hiện bên phải với dấu hỏi trên đầu.
- **124.5s** (“Và ai nhớ giúp”) — Cô Lan (`co-lan/cau-may`) hiện cạnh Anh Tâm, dấu hỏi; hai dấu hỏi cùng nhấp; giữ hình tới hết cảnh.

## Frame 4 — Đội kế toán của ông Sơn: database

- scene: Tiệm mở rộng hai mươi mặt hàng, Cô Lan nhớ nhầm giá, ông Sơn thuê đội kế toán: khoá chính (mã hàng), khoá ngoại (sổ hoá đơn), Cô Lan không phải nhớ nữa; cú lật: trí nhớ tạm và trí nhớ lâu dài; kết bằng viên gạch DATABASE.
- start: 250.3s
- duration: 157.8s
- voice: 0.3s → 156.5s
- transition_in: cut từ Cảnh 2
- status: outline
- blueprint: panel-edit-live-sync (đoạn 5: ô giá đổi, hoá đơn đổi theo) và comparison-split
- composition_id: scene-4
- cues: canh3_doi-ke-toan-cua-ong-son
- assets: nen/ngoai-that-tiem; vat/xe-tai, vat/thung-nuoc-mam, vat/bao-muoi, vat/goi-mi-chinh, vat/chai-nuoc-mam, vat/bao-gao, vat/so, vat/ke-gao-trong; co-lan/cau-may, co-lan/mim-cuoi, co-lan/chao-tam-biet, co-lan/quay-thu-ngan; anh-tam/hoi; chi-hanh/ban-ke-toan; binh/goc
- rules: svg-path-draw (mũi tên khoá ngoại), anchored-layout-expand (bảng hàng hoá thêm hàng), counting-dynamic-scale (giá 45→54)
- src: compositions/frames/04-canh3.html (dựng theo từng đoạn: compositions/frames/c3-d*.html)
- packets: 4 gói: đoạn 1-2; đoạn 3-4; đoạn 5; đoạn 6-7 và chốt cảnh
- voiceover: "Gạo bán chạy, ông Sơn làm ăn thuận lợi. Ông không chỉ bán gạo nữa, mà nhập thêm nước mắm, muối, mì chính…"

### Đoạn 1: Làm ăn thuận lợi, bán thêm hàng

_Bố cục_: `nen/ngoai-that-tiem` với biển "Tạp hoá Sơn" (chữ HTML đặt vào vùng biển trống); xe tải vào, dỡ hàng ra trước tiệm.

- **0.3s** (“Gạo bán chạy”) — Cắt vào ngoại thất; biển "Tạp hoá Sơn" hiện (chữ đen trên nền gỗ nhạt); khách vào ra.
- **5.0s** (“nhập thêm nước mắm”) — Xe tải vào từ trái; thùng nước mắm, bao muối, gói mì chính bay theo cung từ xe xuống đất trước tiệm.
- **8.4s** (“Sáu mặt hàng”) — Số "6" hiện 120 px giữa khung (đếm nhanh).
- **10.3s** (“rồi hai mươi”) — Số đếm 6 → 10 → 20 (counting-dynamic-scale), các đạo cụ hàng hoá nhân lên thành lưới 20 ô mờ phía sau.

### Đoạn 2: Nhớ trong đầu bắt đầu sai

_Bố cục_: trái: Cô Lan (`co-lan/cau-may`) với các chip giá lộn xộn trên đầu; phải: Anh Tâm (`anh-tam/hoi`) trước kệ trống (`vat/ke-gao-trong`).

- **13.0s** (“mỗi mặt hàng một giá”) — Lưới 20 mặt hàng hiện rõ, mỗi ô một chip giá nhỏ xanh dương đậm.
- **15.9s** (“Cô Lan bắt đầu nhớ nhầm giá”) — Cô Lan hiện (trượt từ trái); trên đầu cô các chip giá xoay tít ("nước mắm 45?", "nước mắm 54?") bằng chữ đỏ `.th-canh-bao`.
- **18.1s** (“Anh Tâm không biết”) — Anh Tâm hiện bên phải trước kệ trống, bong bóng "Trong kho còn bao nhiêu chai?".
- **20.9s** (“Nhớ trong đầu”) — Hai bong bóng chạm nhau, dấu hỏi đỏ ở giữa; không ai trả lời.
- **24.4s** (“không còn được nữa”) — Cả khung rung nhẹ rồi lặng; dấu X đỏ nhỏ hiện trên chữ "nhớ trong đầu".

### Đoạn 3: Thuê đội kế toán

_Bố cục_: trên: sơ đồ ba nút (Cô Lan, Anh Tâm → phòng kế toán → trả lời); dưới trái: `chi-hanh/ban-ke-toan` rộng 760 px (ba kế toán chung bàn); chữ "DATABASE" tím hiện bên cạnh.

- **25.8s** (“Ông Sơn thuê một đội kế toán”) — Ảnh ba kế toán trượt lên từ dưới (đặt đáy ảnh sát đáy khung, che lề bằng dải nền), nhún nhẹ.
- **31.0s** (“Việc của họ là giữ sổ”) — Ba chip hiện lần lượt trên đầu họ: "giá bao nhiêu", "kho còn bao nhiêu", "hôm nay bán gì" (chữ đen).
- **37.1s** (“Cô Lan cần giá”) — Mũi tên cong từ Cô Lan mini (trái) tới phòng kế toán, chip "giá?" chạy theo mũi tên; mũi tên trả lại chip "45.000đ" (xanh dương đậm).
- **39.7s** (“Anh Tâm cần biết”) — Tương tự từ Anh Tâm mini (phải): chip "còn bao nhiêu?" đi, "60 chai" về.
- **43.0s** (“Đội kế toán chính là”) — Chữ "DATABASE" 96 px hiện tím đậm `#6D28D9` cạnh phòng kế toán (2 giây dừng), nền tím nhạt.

### Đoạn 4: Kế toán phân loại, khoá chính

_Bố cục_: trái: ba mặt hàng thật (`vat/thung-gao` hoặc `vat/bao-gao`, hai `vat/chai-nuoc-mam`, `vat/bao-muoi`) nhỏ 240 px có thẻ mã; phải: bảng 5 dòng (Mã, Tên hàng, Giá bán, Còn trong kho) tím nhạt.

- **45.8s** (“Việc đầu tiên của kế toán”) — Bảng hàng hoá hiện (5 dòng, giá xanh dương đậm); từng thẻ mã G001, G002, NM01, NM02, M01 bay theo cung từ cột Mã xuống từng hàng hoá bên trái (mỗi thẻ tách).
- **51.1s** (“Vì hai chai”) — Hai chai nước mắm sáng, hai thẻ NM01 và NM02 phóng lớn bên cạnh nhau (3 giây dừng để đọc bảng).
- **55.1s** (“kế toán không biết trả lời”) — Bong bóng "nước mắm giá bao nhiêu?" hiện (chữ đỏ), hai dấu hỏi bay lên từ hai chai.
- **60.2s** (“chỉ có đúng một đáp án”) — Bong bóng đổi "NM01 giá bao nhiêu?" và chỉ một mũi tên tới đúng dòng NM01: "45.000đ"; dấu tích xanh.
- **62.0s** (“Mã riêng đó”) — Cột Mã được tô viền tím, chip "KHOÁ CHÍNH" hiện cạnh cột.
- **63.6s** (“gọi là khoá chính”) — Chip "KHOÁ CHÍNH" phóng lớn (spring-pop).
- **65.7s** (“số căn cước”) — Hình thẻ căn cước đơn giản (chip chữ nhật có ảnh tròn và số) bay cạnh cột Mã: tên trùng (hai "Nguyễn Văn A"), số khác nhau; giữ 2 giây dừng.

### Đoạn 5: Hoá đơn chỉ ghi mã, khoá ngoại

_Bố cục_: hai bảng cạnh nhau: trái sổ hàng hoá (`vat/so` tô tím nhạt, mở thành bảng), phải sổ hoá đơn (`vat/so` tô xanh dương nhạt, mở thành bảng 3 dòng HD001-003).

- **70.3s** (“Cuốn sổ thứ hai”) — Sổ hoá đơn (xanh dương nhạt) trượt vào từ phải, mở ra thành bảng Mã hoá đơn, Mã hàng, Số lượng, Ngày.
- **74.7s** (“kế toán không chép lại”) — Hai cột "Tên hàng" và "Giá" mờ xuống và gạch chéo đỏ nhẹ: không chép lại.
- **81.3s** (“lần theo mã”) — Mũi tên cong vẽ từ ô "NM01" ở sổ hoá đơn sang đúng dòng NM01 ở sổ hàng hoá (3 giây dừng), hai ô khác cũng nối.
- **85.4s** (“Cột Mã hàng”) — Cột "Mã hàng" của sổ hoá đơn viền tím.
- **89.1s** (“gọi là khoá ngoại”) — Chip "KHOÁ NGOẠI" hiện cạnh cột Mã hàng (2 giây dừng), các mũi tên sáng cùng lúc.
- **91.1s** (“Lý do ghi như vậy”) — Zoom nhẹ vào ô giá NM01 của sổ hàng hoá.
- **94.8s** (“chỉ sửa một chỗ”) — Giá "45" đổi thành "54" (số lật dọc), ô nhấp sáng một lần.
- **99.7s** (“Không có chuyện”) — Các dòng hoá đơn nối tới NM01 đổi theo lần lượt (hiệu ứng lan theo mũi tên) trong khoảng dừng 3 giây; dấu tích xanh cạnh mỗi dòng.

### Đoạn 6: Cô Lan không cần nhớ nữa

_Bố cục_: trái: Cô Lan (`co-lan/mim-cuoi`) trước cửa sổ phòng kế toán (`chi-hanh/ban-ke-toan`) bên phải; dưới: cửa sổ code 4 dòng; Anh Tâm (`anh-tam/hoi`) hiện cuối đoạn.

- **104.1s** (“Bây giờ cô Lan hỏi”) — Cô Lan hiện bên trái, tờ giấy ghi giá (thẻ HTML "NM01: 45.000đ") bay theo cung từ phòng kế toán tới tay Cô Lan; Cô Lan đưa tay đón, mỉm cười.
- **108.5s** (“Anh Tâm hỏi kế toán”) — Cửa sổ code hiện: `gia = hoi_ke_toan("gia_ban", ma="NM01")` và `tinh_tien(gia, so_ky=2)`; Anh Tâm hiện phải với dòng `con_lai = hoi_ke_toan("con_trong_kho", ma="NM01")`.
- **114.6s** (“Không ai phải nhớ”) — Hai bong bóng suy nghĩ của Cô Lan và Anh Tâm trống (không còn chip chồng chéo), tờ giấy hiện dấu tích xanh.
- **116.3s** (“Hàm làm việc”) — Chữ "HÀM làm việc" (xanh dương) và "KẾ TOÁN giữ thông tin" (tím) hiện hai bên (2 giây dừng), hai dòng code ở trên vẫn hiện.

### Đoạn 7: Cú lật, nhớ trong đầu và ghi vào sổ

_Bố cục_: trái: Cô Lan (`co-lan/chao-tam-biet`) ôm hộp đồ; phải: cuốn sổ trên bàn; Bình (`binh/goc`) đến mở sổ.

- **119.6s** (“Còn một lý do nữa”) — Hai nửa khung: trái "trong đầu Cô Lan", phải "trong sổ".
- **121.9s** (“Cô Lan nhớ trong đầu thì cô Lan nghỉ”) — Cô Lan (`co-lan/chao-tam-biet`) vẫy chào rồi rời khung bên trái; các chip giá bay lên khỏi đầu cô rồi tan thành bụi (mất).
- **126.6s** (“biến chỉ sống lúc máy đang chạy”) — Ổ cắm điện nhỏ rút ra, cửa sổ code tắt đen, chip biến (vàng) mờ dần; sfx tắt điện nhẹ.
- **130.2s** (“Kế toán ghi vào sổ”) — Sổ hàng hoá (`vat/so`) mở trên bàn, Bình (`binh/goc`) trượt vào và lật trang, thấy giá; dấu tích xanh.
- **136.7s** (“Biến là trí nhớ tạm”) — Chữ "BIẾN = trí nhớ tạm" (vàng) hiện bên trái.
- **138.8s** (“Database là trí nhớ lâu dài”) — Chữ "DATABASE = trí nhớ lâu dài" (tím) hiện bên phải; hai dòng nằm cạnh nhau (2 giây dừng).

### Chốt cảnh: viên gạch DATABASE

_Bố cục_: kệ có hai viên (BIẾN, HÀM); viên gạch tím "DATABASE" lớn rơi giữa khung rồi bay lên ô 3; ba nhóm nhỏ (nhãn, nhân viên, kế toán) hiện; hai ô trống cuối nhấp viền.

- **141.7s** (“Viên gạch thứ ba”) — Viên gạch tím "DATABASE" lớn (x3) rơi xuống giữa khung, nảy một lần (cạch).
- **143.4s** (“nơi giữ thông tin”) — Định nghĩa hiện dưới viên gạch: "DATABASE = nơi giữ thông tin lâu dài" (chữ 56 px, DATABASE tím đậm).
- **145.6s** (“Giờ tiệm ông Sơn”) — Viên gạch thu nhỏ bay lên ô 3 (cạch); ba nhóm nhỏ hiện lần lượt giữa khung: nhãn (BIẾN), nhân viên (HÀM), kế toán (DATABASE).
- **151.8s** (“Nhưng còn thiếu một thứ”) — Hai ô trống còn lại của kệ nhấp viền đứt nét, dấu hỏi nhỏ cạnh chúng; giữ hình tới hết cảnh.

## Frame 5 — Black Friday của ông Sơn: if/else và vòng lặp

- scene: Ngày 27/11 Black Friday, luật giảm 5% một ngày: if/else qua ví dụ mang ô, code bốn dòng, so sánh hai hoá đơn; vòng lặp qua giỏ hàng đầy; cú lật quên gỡ giấy; kết bằng hai viên gạch cuối.
- start: 408.1s
- duration: 127.8s
- voice: 0.3s → 126.7s
- transition_in: cut từ Cảnh 3
- status: outline
- blueprint: comparison-split (đoạn 2 và 4)
- composition_id: scene-5
- cues: canh4_black-friday-cua-ong-son
- assets: ong-son/goc, ong-son/ngac-nhien; co-lan/goc, co-lan/quay-thu-ngan, co-lan/mim-cuoi; thanh-nien/goc; vat/gio-hang-trong, vat/bao-gao, vat/chai-nuoc-mam, vat/bao-muoi, vat/goi-mi-chinh, vat/may-tinh-tien-cu
- rules: svg-path-draw (nhánh ngã ba và vòng tròn), physics-press-reaction (nhấn máy tính), stat-bars-and-fills (lãi về 0)
- src: compositions/frames/05-canh4.html (dựng theo từng đoạn: compositions/frames/c4-d*.html)
- packets: 3 gói: đoạn 1-3; đoạn 4-5; đoạn 6 và chốt cảnh
- voiceover: "Ngày 27 tháng 11 là Black Friday. Ông Sơn muốn giảm giá, nhưng lãi tạp hoá mỏng…"

### Đoạn 1: Luật của ông Sơn

_Bố cục_: trái: lịch treo tường (thẻ HTML, tờ tháng 11 với ngày 27 khoanh đỏ); phải: Ông Sơn (`ong-son/goc`) viết lên tờ giấy.

- **1.4s** (“là Black Friday”) — Lịch hiện; vòng tròn đỏ vẽ quanh ngày 27 (svg-path-draw); chữ "BLACK FRIDAY" nhỏ trên lịch.
- **3.0s** (“Ông Sơn muốn giảm giá”) — Ông Sơn trượt vào từ phải.
- **4.7s** (“lãi tạp hoá mỏng”) — Thanh "lãi" mỏng hiện dưới Ông Sơn (thanh xanh lá mảnh).
- **6.6s** (“đặt đúng một luật”) — Tờ giấy (thẻ HTML) bay từ tay Ông Sơn lên tường cạnh lịch, chữ "Chỉ giảm 5%. Chỉ hôm nay." viết bằng bút đỏ (svg-path-draw).
- **9.7s** (“chỉ trong ngày hôm đó”) — Dấu ngoặc ôm riêng ngày 27 trên lịch.
- **11.3s** (“Hôm sau”) — Lịch lật sang 28, tờ giấy giữ nguyên; giá "trở lại bình thường" hiện nhỏ.

### Đoạn 2: If/else là nếu... thì... không thì...

_Bố cục_: chia đôi khung dọc: trên ví dụ mưa (Thanh niên `thanh-nien/goc` ở trái nhìn cửa sổ, hai nhánh phải); dưới (hoặc sau khi chuyển) ví dụ Cô Lan trước lịch. Cuối đoạn: biểu tượng ngã ba đường.

- **13.7s** (“Bạn dùng”) — Cửa sổ trời mưa vẽ giữa khung; Thanh niên đứng nhìn.
- **16.7s** (“Nếu trời mưa thì mang ô”) — Nhánh trái vẽ ra (svg-path-draw) với chip "Nếu trời mưa → mang ô" và biểu tượng ô SVG.
- **18.2s** (“không thì thôi”) — Nhánh phải vẽ ra với chip "Không thì thôi"; hai nhánh cùng sáng một lần.
- **19.2s** (“Cô Lan cũng vậy”) — Cảnh đổi (scale-swap): Cô Lan (`co-lan/goc`) trước tờ lịch 27/11; hai nhánh hiện lại: "Nếu 27/11 → giảm 5%" và "Không thì giữ giá thường".
- **25.6s** (“Cô nhìn lịch”) — Mắt Cô Lan liếc lịch (đường ngắm mảnh), nhánh "nếu" sáng.
- **29.8s** (“Một ngã ba đường”) — Hai nhánh gộp thành biểu tượng ngã ba đường (chữ Y) ở giữa khung.
- **31.4s** (“đúng thì đi lối này”) — Lối trái sáng với dấu tích xanh.
- **34.0s** (“Đó là”) — Chữ "IF / ELSE" lục lam 96 px hiện cạnh ngã ba (2 giây dừng).

### Đoạn 3: Viết thành code

_Bố cục_: trái: tờ giấy luật (thẻ HTML); phải: cửa sổ code 4 dòng (`if black_friday == "27/11":` / `giam_gia = 5` / `else:` / `giam_gia = 0`).

- **35.9s** (“Đọc là bạn hiểu”) — Tờ giấy trượt sang trái; cửa sổ code hiện bên phải; mỗi dòng sáng đúng lúc đọc: dòng `if` (lục lam), `giam_gia = 5`.
- **41.7s** (“Không thì giảm giá bằng”) — Dòng `else` rồi `giam_gia = 0` sáng.
- **43.4s** (“Để ý hai dấu bằng”) — Phóng `==` trong dòng `if` (1,3 lần) với viền đỏ nhạt.
- **45.2s** (“một dấu bằng là dán nhãn”) — Chip "=" nhỏ với nhãn dán (nhắc Cảnh 1) hiện cạnh `giam_gia = 5`.
- **47.8s** (“Hai dấu bằng là một câu hỏi”) — Chip "==" với dấu hỏi hiện cạnh `black_friday == "27/11"`.
- **51.2s** (“Chỉ có vậy”) — Giữ 3 giây cho người xem đọc lại bốn dòng; mọi chip mờ xuống.

### Đoạn 4: Chạy thử hai ngày

_Bố cục_: hai hoá đơn (thẻ HTML) cạnh nhau, mỗi thẻ rộng 760 px: trái "27/11", phải "28/11"; Cô Lan (`co-lan/mim-cuoi`) giữa dưới.

- **54.2s** (“khách mua”) — Hoá đơn trái hiện: "Tổng 300.000đ".
- **55.4s** (“được giảm”) — Dòng "−5%" (xanh lá) hiện, "300.000đ" gạch ngang, "285.000đ" xanh lá đậm lớn (`.th-tong`); hoá đơn trái sáng viền (3 giây dừng).
- **61.3s** (“cùng đơn hàng”) — Hoá đơn phải hiện: "300.000đ" giữ nguyên (đen), không có dòng giảm.
- **64.0s** (“Không ai phải gỡ giấy”) — Tờ giấy luật nhỏ trên tường tự mờ đi.
- **66.0s** (“Luật tự dừng”) — Dấu tích xanh trên cả hai hoá đơn, 2 giây dừng.

### Đoạn 5: Vòng lặp là if/else hỏi đi hỏi lại

_Bố cục_: Cô Lan (`co-lan/quay-thu-ngan`) giữa khung với giỏ hàng (`vat/gio-hang-trong` thả đồ vào) bên phải; vòng tròn hồng bao quanh; cửa sổ code hai dòng dưới.

- **67.9s** (“Một khách mua cả giỏ”) — Giỏ hàng bên phải hiện, các đạo cụ (bao gạo, chai, bao muối, mì chính) rơi vào giỏ theo cung.
- **70.4s** (“Cô Lan quét một món”) — Cô Lan quét món 1: món bay từ giỏ tới tay cô rồi biến mất; chip "vòng 1".
- **73.1s** (“còn món nào không”) — Bong bóng "Còn món nào không?"; mũi tên cong từ bong bóng quay lại giỏ (hình vòng tròn).
- **74.5s** (“Còn thì quét tiếp”) — Món 2 bay ra, chip "vòng 2"; mũi tên vòng quay lại lần thứ hai.
- **77.8s** (“đây vẫn là câu”) — Ngã ba đường nhỏ (đúng/sai) hiện cạnh bong bóng.
- **83.6s** (“gọi là vòng lặp”) — Mũi tên vòng thành vòng tròn hồng liền; chữ "VÒNG LẶP" hiện (2 giây dừng).
- **88.8s** (“Đọc là: trong khi”) — Cửa sổ code hiện `while con_mon_trong_gio:` / `quet_mot_mon()`; từ `while` sáng hồng đậm.
- **92.9s** (“Hết món”) — Giỏ trống, vòng tròn đứt rồi ngừng, Cô Lan nhấn máy tính (`vat/may-tinh-tien-cu`, nảy), "TỔNG" xanh lá đậm hiện; giữ 3 giây dừng.

### Đoạn 6: Cú lật, nếu không có if/else

_Bố cục_: Ông Sơn (`ong-son/ngac-nhien`) trước tường dán tờ giấy "GIẢM 5%"; lịch lật nhanh; thanh lãi tụt về 0.

- **95.3s** (“Không có if else”) — Tờ giấy "GIẢM 5%" dán lên tường sáng ngày 27; Ông Sơn đứng cạnh.
- **97.3s** (“tự dán giấy”) — Lịch hiện ngày 27 (dán) rồi 28 (gỡ?) — dấu ? đỏ ở ngày 28.
- **101.3s** (“Chỉ cần quên một lần”) — Ông Sơn (`ong-son/ngac-nhien`) trợn mắt, mồ hôi; lịch lật 28, 29, … 3/12 (mỗi ngày 0,3 giây) trong khi giấy vẫn dán.
- **103.0s** (“lãi bốc hơi”) — Thanh lãi (xanh lá) tụt về 0, số "Lãi: 0đ" (đỏ `.th-canh-bao`) hiện.
- **104.2s** (“Máy tính không quên”) — Dấu tích xanh hiện cạnh `if black_friday == "27/11"`; "miễn là bạn dạy nó luật đúng" (2 giây dừng).

### Chốt cảnh: hai viên gạch cuối

_Bố cục_: kệ có ba viên (BIẾN, HÀM, DATABASE); hai viên gạch lớn lần lượt rơi giữa khung rồi bay lên ô 4 và ô 5; kệ đầy; kệ phóng to ra giữa khung.

- **108.5s** (“Viên gạch thứ tư”) — Viên gạch lục lam "IF / ELSE" lớn (x2,5) rơi xuống giữa khung, nảy một lần (cạch), chữ "để tự quyết định" hiện dưới.
- **111.9s** (“Viên gạch thứ năm”) — Viên IF/ELSE bay lên ô 4 (cạch); viên hồng "VÒNG LẶP" lớn rơi xuống giữa khung, chữ "để làm đi làm lại" hiện dưới.
- **116.2s** (“Biến để gọi tên”) — Viên VÒNG LẶP bay lên ô 5 (cạch), kệ đầy; viên BIẾN sáng cùng chữ "gọi tên" hiện bên dưới kệ.
- **117.7s** (“Hàm để chia việc”) — Viên HÀM sáng ↔ "chia việc".
- **119.5s** (“Database để nhớ”) — Viên DATABASE sáng ↔ "để nhớ".
- **121.5s** (“để tự quyết định”) — Viên IF/ELSE sáng ↔ "tự quyết định".
- **122.7s** (“Vòng lặp để làm lại”) — Viên VÒNG LẶP sáng ↔ "làm lại".
- **124.5s** (“Năm viên gạch đầu tiên”) — Cả năm viên sáng cùng lúc, kệ phóng 1,15 lần, nảy nhẹ.

## Frame 6 — Từ tiệm tạp hoá đến phần mềm triệu đô

- scene: Camera lùi lên cao: tiệm thành sơ đồ mặt bằng với năm viên gạch; nhân bản thành hệ thống lớn; bình cũ rượu mới (máy tính tiền mới); đổi sang tiệm bún; framework là bộ khung đóng gói sẵn; tư duy kiến trúc sư; quay lại đoạn code, tô màu năm viên gạch, khép vòng hook và thử thách.
- start: 535.9s
- duration: 243.7s
- voice: 0.3s → 243.4s
- transition_in: cut từ Cảnh 4 (kệ gạch phóng ra rồi lùi thành sơ đồ)
- status: outline
- blueprint: zoom-out-workspace-reveal (đoạn 1-2) và camera-journey (đoạn 7)
- composition_id: scene-6
- cues: canh5_tu-tiem-tap-hoa-den-phan-mem-trieu-do
- assets: sơ đồ mặt bằng SVG (tự vẽ); nen/ngoai-that-tiem; ong-son/goc; co-lan/quay-thu-ngan; vat/may-tinh-tien-cu, vat/may-tinh-tien-moi, vat/thung-gao, vat/noi-nuoc-dung, vat/ro-bun, vat/so; anh-tam/goc
- rules: multi-phase-camera (lùi từ mái tiệm), center-outward-expansion (nhân bản tiệm thành toà nhà), asr-keyword-glow (tô màu từng phần code theo lời)
- src: compositions/frames/06-canh5.html (dựng theo từng đoạn: compositions/frames/c5-d*.html)
- packets: 4 gói: đoạn 1-2; đoạn 3-4; đoạn 5-6; đoạn 7
- voiceover: "Hãy lùi lại và nhìn tiệm ông Sơn từ trên cao. Tiệm này được xây từ những viên gạch đầu tiên…"

### Đoạn 1: Nhìn tiệm từ trên cao

_Bố cục_: sơ đồ mặt bằng tiệm vẽ SVG (đường nét mảnh, sàn nhạt): quầy thu ngân, kho, phòng kế toán, ngã ba đường, vòng tròn; năm viên gạch tên gọi đậu ở từng khu.

- **0.3s** (“Hãy lùi lại”) — Camera lùi lên khỏi mái tiệm (zoom out 1,6→1); tiệm thu nhỏ thành sơ đồ phẳng giữa khung.
- **5.1s** (“gạch đầu tiên”) — Năm ô trống viền đứt nét hiện trên sơ đồ, đánh số 1-5.
- **7.0s** (“nhãn là biến”) — Viên gạch BIẾN (vàng) bay vào khu nhãn (cạnh thùng gạo).
- **9.3s** (“một việc là hàm”) — Viên gạch HÀM (xanh dương) bay vào khu quầy thu ngân.
- **11.8s** (“Đội kế toán là database”) — Viên gạch DATABASE (tím) bay vào khu phòng kế toán.
- **14.4s** (“Ngã ba đường là”) — Viên gạch IF/ELSE (lục lam) bay vào khu ngã ba đường.
- **17.6s** (“Và vòng tròn”) — Viên gạch VÒNG LẶP (hồng) bay vào khu vòng tròn; năm viên nằm cạnh nhau trên sơ đồ (2 giây dừng).

### Đoạn 2: Hệ thống lớn là gạch nhỏ xếp lại

_Bố cục_: sơ đồ tiệm phóng to rồi nhân bản; bên cạnh ba biểu tượng ứng dụng (túi mua sắm, ngân hàng, mạng xã hội) bằng SVG đơn giản.

- **21.6s** (“Phần mềm triệu đô nào cũng giống”) — Sơ đồ tiệm nhân bản thành bốn khu, rồi thành lưới nhiều tầng (center-outward-expansion).
- **25.6s** (“Ứng dụng mua sắm”) — Biểu tượng túi mua sắm hiện bên trái, nối bằng đường mảnh với một khu.
- **26.6s** (“ứng dụng ngân hàng”) — Biểu tượng ngân hàng hiện giữa.
- **27.8s** (“mạng xã hội”) — Biểu tượng mạng xã hội hiện phải.
- **29.9s** (“nền móng của mọi hệ thống”) — Zoom vào một khu của toà nhà: lộ năm viên gạch nhỏ.
- **37.9s** (“Hệ thống lớn”) — Zoom out nhanh: toà nhà khổng lồ gồm vô số viên gạch cùng năm màu.
- **43.6s** (“xếp lại rất nhiều lần”) — Các viên gạch nhấp sáng theo từng tầng; toà nhà giữ hình tới hết đoạn.

### Đoạn 3: Bình cũ rượu mới

_Bố cục_: Cô Lan (`co-lan/quay-thu-ngan`) giữa khung; bên cạnh máy tính tiền cũ đổi thành máy tính tiền mới; chữ "bình cũ, rượu mới" hiện.

- **47.4s** (“Công nghệ đổi mới liên tục”) — Cắt vào quầy thu ngân: Cô Lan đứng sau quầy với máy tính tiền cũ (`vat/may-tinh-tien-cu`).
- **53.9s** (“bình cũ rượu mới”) — Chữ "bình cũ, rượu mới" hiện trên đầu (đen 80 px).
- **55.5s** (“Ông Sơn thay máy tính tiền”) — Máy cũ trượt ra, máy mới (`vat/may-tinh-tien-moi`) trượt vào vị trí, màn hình sáng; sfx ting.
- **59.5s** (“cô Lan vẫn làm đúng việc cũ”) — Ba chip hiện lần lượt trên đầu Cô Lan: "nhập giá" → "nhân số ký" → "ra tổng tiền" (cùng chuỗi cũ).
- **61.5s** (“nhập giá”) — Chip "nhập giá" sáng.
- **64.2s** (“Cái vỏ thay”) — Hai nửa: vỏ (máy mới, đổi) và nền móng (ba chip, giữ nguyên), nền móng viền đậm.

### Đoạn 4: Ông Sơn chuyển sang bán bún

_Bố cục_: `nen/ngoai-that-tiem` toàn khung; biển "Tạp hoá Sơn" đổi "Bún Sơn" (chữ HTML); trong tiệm các thùng gạo đổi sang nồi nước dùng và rổ bún.

- **66.8s** (“Một ngày, ông Sơn chán”) — Cắt vào ngoại thất; Ông Sơn (`ong-son/goc`) đứng trước tiệm.
- **70.7s** (“Ông có phải xây lại”) — Dấu hỏi to hiện, rồi một dấu X đỏ chéo lên hình "phá đi xây lại" (búa đập, vẽ SVG).
- **73.4s** (“vẫn cần quầy thu ngân”) — Biển cắt nhẹ để lộ bên trong tiệm; quầy thu ngân (biểu tượng) sáng với dấu tích xanh.
- **75.9s** (“vẫn cần đội kế toán”) — Biểu tượng kho rồi đội kế toán sáng lần lượt, mỗi cái một dấu tích.
- **77.3s** (“vẫn cần luật giảm giá”) — Tờ luật giảm giá sáng, dấu tích; cả ba cùng giữ nguyên.
- **79.4s** (“Cái khung của một cửa hàng”) — Khung viền cam mảnh bao ba thứ vừa kể, chữ "KHUNG CỬA HÀNG" nhỏ.
- **81.5s** (“Ông chỉ thay hàng”) — Biển "Tạp hoá Sơn" lật thành "Bún Sơn" (số lật dọc); thùng gạo (`vat/thung-gao`) bay ra, nồi nước dùng (`vat/noi-nuoc-dung`) và rổ bún (`vat/ro-bun`) bay vào thế chỗ theo cung.
- **85.1s** (“Xây một lần”) — Chip "dùng lại cho mọi loại cửa hàng" hiện; ba biểu tượng cửa hàng khác (cà phê, hiệu thuốc, quần áo) nhỏ xếp hàng dưới, cùng dùng bộ khung.

### Đoạn 5: Framework là cái khung đã đóng gói sẵn

_Bố cục_: giữa khung: hộp lớn "BỘ KHUNG CỬA HÀNG" (thẻ HTML) chứa quầy thu ngân, kho, sổ kế toán; ba hộp nhỏ bên dưới: React, Zustand, Prisma.

- **88.8s** (“Trong thế giới lập trình”) — Hộp lớn "BỘ KHUNG CỬA HÀNG" hiện giữa khung (spring-pop), bên trong ba biểu tượng nhỏ.
- **91.9s** (“React”) — Hộp nhỏ thứ nhất rơi xuống, nhãn "React" (chữ đen).
- **93.0s** (“Zustand”) — Hộp nhỏ thứ hai "Zustand".
- **94.1s** (“Prisma”) — Hộp nhỏ thứ ba "Prisma"; ba hộp nằm cạnh nhau (2 giây dừng).
- **95.9s** (“Người ta gọi chúng”) — Chữ "framework / thư viện" gạch dưới nhẹ.
- **104.4s** (“Có cái đóng gói sẵn cách dựng giao diện”) — Hộp thứ nhất (React) sáng với biểu tượng cửa sổ giao diện.
- **107.1s** (“cách nhớ và chia sẻ dữ liệu”) — Hộp thứ hai (Zustand) sáng với biểu tượng cuốn sổ; chữ "FRAMEWORK = BỘ KHUNG ĐÓNG GÓI SẴN" hiện trên hộp lớn.
- **110.2s** (“làm việc với database”) — Hộp thứ ba (Prisma) sáng với biểu tượng database (2 giây dừng).
- **112.9s** (“Giống như ông Sơn dùng lại”) — Hộp lớn chuyển sang "Tiệm bún" rồi sang "Sản phẩm mới" mà khung giữ nguyên (1,5 giây dừng).
- **122.0s** (“Và bên trong mỗi bộ khung”) — Hộp lớn mở nắp, ánh sáng hiện lên.
- **124.3s** (“Vẫn là biến”) — Năm viên gạch bay vào trong hộp lần lượt, nằm cạnh nhau.
- **130.9s** (“mỗi framework mới”) — Ba hộp nhỏ cũng mở nắp, trong mỗi hộp là năm viên gạch cùng thứ tự (2,5 giây dừng).

### Đoạn 6: Tư duy kiến trúc sư

_Bố cục_: Ông Sơn (`ong-son/goc`) đứng cạnh sơ đồ tiệm, bút đỏ (SVG) vạch; ba câu hỏi bên phải; ba viên gạch đầu tương ứng.

- **136.3s** (“Thợ”) — Ông Sơn trượt vào cạnh sơ đồ tiệm; hai chip "Thợ code" và "Kiến trúc sư" hiện.
- **138.8s** (“Kiến trúc sư hỏi ba câu”) — Chip "Kiến trúc sư" sáng, ba câu hỏi hiện lần lượt bên phải: "Thứ này là gì?", "Ai làm việc gì?", "Thông tin nằm ở đâu?".
- **140.2s** (“thứ này là gì”) — Câu 1 sáng (bút đỏ gạch dưới).
- **142.0s** (“ai làm việc gì”) — Câu 2 sáng.
- **143.4s** (“thông tin nằm ở đâu”) — Câu 3 sáng; ba câu hiện đủ (2 giây dừng).
- **145.4s** (“Ba câu này khớp”) — Ba mũi tên cong từ ba câu hỏi xuống ba viên gạch BIẾN, HÀM, DATABASE.
- **149.3s** (“là cái nhãn”) — Câu 1 ↔ BIẾN sáng.
- **151.6s** (“là người làm một việc”) — Câu 2 ↔ HÀM sáng.
- **154.2s** (“là cuốn sổ kế toán”) — Câu 3 ↔ DATABASE sáng.
- **156.4s** (“Câu đầu tiên chính là”) — Câu 1 phóng lớn; chữ "ĐẶT TÊN" hiện cạnh.
- **161.2s** (“Ai trượt bài này”) — Dấu X đỏ nhỏ hiện trên "các bài sau" (2 giây dừng).

### Đoạn 7: Quay lại đoạn code, khép vòng hook và thử thách

_Bố cục_: cửa sổ code 13 dòng giống Cảnh 0, tô màu năm viên gạch; sau đó số "20.000.000đ" chuyển "triệu đô"; cuối cùng Ông Sơn nhìn camera và ba câu hỏi.

- **164.3s** (“Bây giờ, hãy quay lại”) — Cửa sổ code từ Cảnh 0 hiện lại giữa khung (cắt, cùng vị trí).
- **167.5s** (“Dòng”) — `tong_tien = 0` sáng vàng (BIẾN) với chip "biến".
- **171.7s** (“Tinh tien”) — `def tinh_tien(...)` sáng xanh dương (HÀM) với chip "hàm".
- **175.6s** (“Hoi ke toan”) — `hoi_ke_toan(...)` sáng tím (DATABASE) với chip "database".
- **182.3s** (“vòng tròn hỏi đi hỏi lại”) — Dòng `if` sáng lục lam rồi dòng `while` sáng hồng (giọng đọc: if rồi while); mọi phần đã tô màu (3 giây dừng).
- **185.3s** (“Bạn vừa đọc được”) — Cả đoạn code sáng đồng thời với năm màu; chữ "Bạn vừa đọc được một đoạn code" hiện dưới.
- **188.5s** (“Năm viên gạch, xếp lại”) — Năm viên gạch hiện bên dưới cửa sổ code, mỗi viên tương ứng một màu (2 giây dừng).
- **192.1s** (“Đầu video tôi hứa”) — Cửa sổ code thu nhỏ sang trái; số "20.000.000đ" (đen, nhắc Cảnh 1) hiện lại bên phải.
- **199.4s** (“bắt đầu từ 20 triệu”) — Số "20.000.000đ" nổi bật, rồi từng chip (nhãn, người làm một việc, sổ) hiện dưới.
- **206.5s** (“Khác nhau ở quy mô”) — "20.000.000đ" chuyển thành "triệu đô" (số lật), thanh "quy mô" dài ra, thanh "tư duy" giữ nguyên (1,5 giây dừng).
- **209.7s** (“Thử thách cho bạn”) — Ông Sơn (`ong-son/goc`) nhìn thẳng camera giữa khung; ba câu hỏi hiện lại bên phải.
- **215.9s** (“trả lời ba câu hỏi”) — Chip "Viết xuống phần bình luận" hiện (chữ đen) cạnh ba câu hỏi.

### Chốt: Đời không như mơ

_Bố cục_: nền ngoại thất tiệm tối dần thành đêm; cuốn sổ (`vat/so`) với dòng giá bị sửa; tên trộm bịt mặt (`ten-trom/goc`) rón rén cầm bút; Ông Sơn (`ong-son/ngac-nhien`); cuối đoạn kệ gạch mở rộng thêm bốn ô mờ (BẢO VỆ, GIAO DIỆN, CHI NHÁNH QUA MẠNG, XỬ LÝ LỖI) và chữ AUTHENTICATION.

- **221.3s** (“Nhưng đời không như mơ”) — Cảnh ngoại thất tiệm đông khách, ánh sáng ấm; chữ "Nhưng đời không như mơ" mờ đi, nền chuyển dần sang tối xanh.
- **222.8s** (“Một buổi sáng”) — Cắt sang cuốn sổ kế toán (`vat/so`) mở trên bàn, bảng giá nước mắm "45.000đ" (xanh dương đậm); Ông Sơn (`ong-son/ngac-nhien`) trượt vào xem.
- **227.7s** (“sửa thành”) — Nét bút đỏ gạch ngang "45.000đ" và hiện "1.000đ" đỏ đậm kèm dấu X; ô giá nháy đỏ.
- **229.2s** (“Cả đêm”) — Chuyển sang đêm: tên trộm bịt mặt (`ten-trom/goc`) rón rén lướt qua từ trái sang phải, tay cầm bút; chai nước mắm lần lượt bay theo cung ra cửa.
- **231.2s** (“trong im lặng”) — Bộ đếm "−60 chai" (đỏ) chạy xuống; chip "im lặng" mờ.
- **232.0s** (“Tiệm suýt phá sản”) — Thanh lãi tụt về 0, chữ "Lãi: 0đ" (đỏ đậm) kèm dấu X; Ông Sơn (`ong-son/ngac-nhien`) ôm đầu.
- **234.0s** (“Ai đã mở”) — Dấu hỏi lớn trên cuốn sổ; bóng đen của tên trộm hiện mờ phía sau sổ.
- **235.8s** (“làm sao một cái tiệm”) — Hai nhân vật cạnh nhau cùng đưa tay tới cuốn sổ: Chị Hạnh (`chi-hanh/goc`) và tên trộm; chip "ai là ai?" hiện giữa hai người.
- **239.4s** (“kẻ lạ”) — Vòng đỏ khoanh tên trộm, chip "kẻ lạ" hiện; Chị Hạnh có dấu tích xanh.
- **240.7s** (“Câu trả lời nằm ở”) — Cảnh sạch về nền trắng ngà; kệ gạch năm viên ở góc trên trái mở rộng thêm bốn ô mờ: BẢO VỆ, GIAO DIỆN, CHI NHÁNH QUA MẠNG, XỬ LÝ LỖI (chỉ là hình, lời dẫn không liệt kê).
- **242.9s** (“authentication”) — Ô BẢO VỆ sáng lên (đậm, bóng nhẹ), chữ "AUTHENTICATION" 96 px hiện giữa khung; giữ hình tới hết video.

