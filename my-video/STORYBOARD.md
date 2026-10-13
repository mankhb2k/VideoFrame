---
format: 1920x1080
duration: 522s
message: "Đừng bỏ OOP, hãy bỏ thói quen kế thừa mặc định: bắt đầu từ khả năng, không phải từ dòng dõi."
arc: Hook → OOP hấp dẫn → Kế thừa hỏng → POP giải cùng bài toán → So sánh → Vì sao hợp kiến trúc hiện đại → Bảy luật → Chốt
audience: dev web/mobile đã biết TypeScript cơ bản
mode: collaborative
---

Giọng đọc: `vi-vn-advisor-2` (Gemini TTS). Mốc dưới đây tính từ độ dài giọng đọc thật (`assets/audio/moc-canh.json`); mỗi cảnh có 0,3 giây lặng ở đầu và khoảng 0,3 giây ở cuối để chuyển cảnh. Mốc nhỏ trong cảnh (`t=`) là ước tính theo tỉ lệ ký tự, sẽ chỉnh lại bằng mốc từng từ sau khi transcribe.

## Frame 1 — Hook: con khỉ và quả chuối

- scene: Quả chuối trên nền tối bị kéo dần ra, hiện con khỉ rồi cả khu rừng node xám; câu của Joe Armstrong gõ từng từ; OOP vs POP.
- start: 0s
- duration: 45s
- voice: 0.3s → 44.7s
- transition_in: cut
- status: animated
- blueprint: zoom-out-workspace-reveal
- blueprint_phu: typewriter-reveal (câu trích dẫn), comparison-split (OOP vs POP)
- composition_id: scene-1
- cues: canh0_hook
- assets: khi-cam-chuoi.png, chuoi.png, khi.png
- src: compositions/frames/01-hook.html
- rules: discrete-text-sequence, spring-pop-entrance, ambient-glow-bloom
- voiceover: "Bạn mở một file code, và chỉ muốn dùng đúng một hàm... Joe Armstrong... Trong video này, mình sẽ so sánh hai cách tổ chức code. OOP... và POP..."

Ba nhịp:

1. t=0–13: một quả chuối nằm giữa màn tối. Camera lùi ra (zoom-out dừng dần), hiện con khỉ đang cầm nó, rồi hiện cả khu rừng là các node xám nối nhau, khớp câu "class cha, class ông, tầng thứ năm".
2. t=13–29: trích dẫn của Joe Armstrong gõ từng từ (typewriter) với tên tác giả bên dưới. Từ "con khỉ" và "khu rừng" sáng hổ phách đúng lúc được đọc.
3. t=29–45: chữ "OOP" (hổ phách) trượt vào từ trái, "POP" (xanh ngọc) từ phải, "vs" ở giữa; phụ đề "Protocol-Oriented Programming". Nói rõ POP không phải lập trình thủ tục.

## Frame 2 — OOP trong TypeScript

- scene: Bốn ô khái niệm hiện lần lượt, code gõ dần bên trái, cây Animal → Bird → Sparrow mọc nhánh xanh lá bên phải.
- start: 45s
- duration: 77.2s
- voice: 45.3s → 121.9s
- transition_in: crossfade
- status: animated
- blueprint: grid-card-assemble
- blueprint_phu: prompt-type-submit-generate (code gõ)
- composition_id: scene-2
- cues: canh1_oop-typescript
- assets: chim-se.png
- src: compositions/frames/02-oop.html
- rules: svg-path-draw, waterfall-entry, svg-icon-enrichment, asr-keyword-glow
- voiceover: "OOP, lập trình hướng đối tượng, xoay quanh một ý tưởng... Đa hình thì sao?... Ba thập niên đầu, OOP thắng lớn..."

1. t=0–22: bốn ô vuông Đóng gói, Trừu tượng, Kế thừa, Đa hình hiện lần lượt, mỗi ô một icon nhỏ.
2. t=22–48: ô thu nhỏ về góc; code `Animal`/`Bird`/`Sparrow` gõ bên trái (6 dòng một lần), cây kế thừa mọc từng nhánh bên phải, màu xanh lá. `code-highlight` sáng dòng `#energy` khi nói "đóng gói", dòng `extends` khi nói "kế thừa".
3. t=48–77: code đổi sang `abstract class Shape`/`Circle`, tiếng gõ nhẹ; hiện mũi tên đa hình từ `Shape[]` tới các kiểu con. Chốt bằng chữ "mọi thứ đang ổn" (xanh).

## Frame 3 — Khi kế thừa bắt đầu hỏng

- scene: Cây gọn gàng hiện lại; Penguin rơi vào nhánh Bird làm nhánh đỏ và nổ; Drone bay vào bị mũi tên bật ngược; mớ spaghetti; lia ra con khỉ khổng lồ.
- start: 122.2s
- duration: 62.2s
- voice: 122.5s → 184.06s
- transition_in: crossfade
- status: animated
- blueprint: camera-journey
- blueprint_phu: overwhelm-surround (mớ rối)
- composition_id: scene-3
- cues: canh2_ke-thua-hong
- assets: chim-se.png, canh-cut.png, drone.png, khi-cam-chuoi.png
- src: compositions/frames/03-break.html
- rules: multi-phase-camera, chromatic-glitch, physics-press-reaction
- voiceover: "Rồi sếp báo: thêm chim cánh cụt... máy bay không người lái... Đây chính là con khỉ và quả chuối."

1. t=0–20: cây gọn từ Frame 2 hiện lại; Penguin rơi vào nhánh `Bird`; nhánh chuyển đỏ, `rgb-glitch-text` trên `fly()` và `camera-shake` ngắn khi đọc "ném lỗi". Code 3 dòng `Penguin extends Bird` gõ bên cạnh.
2. t=20–42: Drone bay vào, mũi tên nối tới `Bird` rồi bật ngược lại (nhãn "không phải chim"); hai bản `fly()` copy nằm cạnh nhau.
3. t=42–62: mũi tên chồng chéo, node nhích lại thành mớ rối, chữ "Ai dám sửa?"; camera lùi ra thành con khỉ khổng lồ cầm quả chuối trong khu rừng (khớp Frame 1).

## Frame 4 — POP trong Swift

- scene: Nền sáng hơn một nấc; ba khối Lego Flyable/Eater/SoundPlayer bay vào, khớp vào Sparrow, Penguin bị từ chối Flyable bằng dấu X đỏ, Drone nhận Flyable.
- start: 184.4s
- duration: 93.9s
- voice: 184.7s → 277.98s
- transition_in: crossfade
- status: animated
- blueprint: grid-card-assemble
- blueprint_phu: cursor-ui-demo (khớp và thử gắn khối)
- composition_id: scene-4
- cues: canh3_pop-swift
- assets: chim-se.png, canh-cut.png, drone.png
- src: compositions/frames/04-pop.html
- rules: theme-crossfade-morph, spring-pop-entrance, press-release-spring, physics-press-reaction
- voiceover: "Năm 2015, tại WWDC, kỹ sư Dave Abrahams... Protocol là bản cam kết hành vi... Chim cánh cụt không ký Flyable..."

1. t=0–15: nền chuyển sáng hơn (`theme-crossfade-morph`); chữ "WWDC 2015" và tên Dave Abrahams; câu khẩu hiệu "đừng bắt đầu bằng class, hãy bắt đầu bằng protocol".
2. t=15–50: ba khối Lego bay vào giữa khung; code Swift (`protocol Flyable`, `extension` mặc định) gõ dần; `Sparrow` hiện dạng thẻ phẳng, hai khối khớp vào với tiếng "cạch".
3. t=50–72: `Penguin` chỉ nhận Eater; khi gắn Flyable, khối bật ra, dấu X đỏ nhỏ và `input-feedback` rung, đúng câu "compiler chặn ngay". `Drone` nhận Flyable, không có đường nào nối tới Animal.
4. t=72–94: `release(_ things: [any Flyable])` gõ; dòng `release([Penguin()])` báo lỗi biên dịch đỏ; chốt "khả năng trước, dòng dõi sau".

## Frame 5 — So sánh trực diện

- scene: Màn hình chia đôi: bên trái mũi tên đỏ lan khi thêm SoundPlayer, bên phải một khối bay vào gắn hai kiểu; sau đó bảng so sánh bảy hàng hiện từng hàng.
- start: 278.3s
- duration: 62.9s
- voice: 278.6s → 340.92s
- transition_in: crossfade
- status: animated
- blueprint: comparison-split
- composition_id: scene-5
- cues: canh4_so-sanh
- assets: chim-se.png, canh-cut.png, drone.png
- src: compositions/frames/05-compare.html
- rules: waterfall-entry, stat-bars-and-fills, press-release-spring
- voiceover: "Giờ thử một yêu cầu mới: cho Sparrow và Drone phát được tiếng kêu... OOP hỏi: nó là cái gì? POP hỏi: nó làm được gì?"

1. t=0–35: chia đôi, vạch chia ở giữa; bên trái OOP/TypeScript mũi tên đỏ lan ra nhiều node, bên phải POP/Swift chỉ một khối `SoundPlayer` gắn vào Sparrow và Drone, các node còn lại xám yên lặng.
2. t=35–52: hai câu hỏi lớn "Nó là cái gì?" (hổ phách) và "Nó làm được gì?" (xanh ngọc) hiện đối xứng.
3. t=52–63: bảng 7 hàng hiện từng hàng (từ kịch bản), hàng "Phát hiện sai sót" nhấn đỏ/xanh. Bảng giữ tối đa 6 từ mỗi ô để đọc được trên màn hình.

## Frame 6 — Vì sao tư duy POP hợp kiến trúc hiện đại

- scene: Bốn biểu tượng lần lượt (mũi tên mở ngang, ổ khóa kiểm thử, hai nhóm nối qua ổ cắm, công tắc), rồi thẻ "Khi nào OOP vẫn ổn" cùng ba quy tắc ngón tay cái.
- start: 341.2s
- duration: 63.5s
- voice: 341.5s → 404.42s
- transition_in: crossfade
- status: animated
- blueprint: grid-card-assemble
- blueprint_phu: kinetic-type-beats (ba quy tắc)
- composition_id: scene-6
- cues: canh5_kien-truc-hien-dai
- assets: (không dùng ảnh nhân vật; icon SVG tự vẽ)
- src: compositions/frames/06-why.html
- rules: svg-icon-enrichment, waterfall-entry, kinetic-beat-slam, svg-path-draw
- voiceover: "Vì sao tư duy này hợp với hệ thống hiện đại? Bốn lý do... Nhưng đừng vội vứt OOP..."

1. t=0–38: bốn lý do hiện đúng nhịp "Một, Hai, Ba, Bốn", mỗi lý do một icon vẽ nét (`svg-path-draw`) và một cụm 3 đến 4 từ: Mở rộng ngang, Dễ test, Song song, Đổi công nghệ.
2. t=38–50: bốn thẻ co về góc; thẻ "Khi nào OOP vẫn ổn" hiện với hai ví dụ nhỏ (UI toolkit, game engine); màu chuyển về hổ phách để thấy OOP vẫn có chỗ đứng.
3. t=50–63: ba quy tắc ngón tay cái đập vào từng dòng (`kinetic-beat-slam`), tối đa 8 chữ mỗi dòng.

## Frame 7 — Bảy luật TypeScript theo tư duy POP

- scene: Bảy thẻ dọc đánh số 1 đến 7 trượt vào lần lượt (câu ngắn bên trái, code 2 đến 4 dòng bên phải), cuối cùng xếp thành checklist chụp màn hình.
- start: 404.7s
- duration: 92.2s
- voice: 405.0s → 489.64s
- transition_in: crossfade
- status: animated
- blueprint: fixed-anchor-cycle
- blueprint_phu: grid-card-assemble (checklist cuối)
- composition_id: scene-7
- cues: canh6_bay-luat-typescript
- assets: chim-se.png, canh-cut.png, drone.png (nhỏ, tùy chọn)
- src: compositions/frames/07-rules.html
- rules: waterfall-entry, discrete-text-sequence, asr-keyword-glow, stat-bars-and-fills
- voiceover: "TypeScript không có protocol như Swift, nhưng bạn vẫn có thể nghĩ như POP. Đây là bảy luật..."

1. t=0–6: câu mở đầu, tiêu đề "7 luật".
2. t=6–72: mỗi luật một thẻ khoảng 9 đến 10 giây (giọng đọc tuần tự, thẻ đi theo lời; mốc chính xác sẽ lấy từ transcribe): luật 1 Bắt đầu từ interface; 2 Ghép, đừng thừa kế; 3 Mỗi interface một khả năng; 4 Hành vi mặc định trong hàm; 5 Phụ thuộc interface; 6 Ưu tiên bất biến; 7 Để compiler bắt lỗi. Code mỗi thẻ gõ từng ký tự, 2 đến 4 dòng; luật 3 hiện code "tránh" màu đỏ, luật 7 hiện lỗi `Property 'fly' is missing`.
3. t=72–85: bảy thẻ thu nhỏ xếp thành checklist, mỗi dòng một `success-check` xanh ngọc; giữ đứng yên vài giây để người xem chụp màn hình.

## Frame 8 — Chốt và kêu gọi hành động

- scene: Câu chốt lớn giữa màn hình; hai khối Lego lắp lần cuối, con khỉ đi khuất, quả chuối nằm gọn trong tay; hộp bình luận mô phỏng.
- start: 496.9s
- duration: 24.8s
- voice: 497.2s → 521.36s
- transition_in: crossfade
- status: animated
- blueprint: kinetic-type-beats
- blueprint_phu: cta-morph-press (nút đăng ký)
- composition_id: scene-8
- cues: canh7_chot
- assets: khi.png, chuoi.png
- src: compositions/frames/08-outro.html
- rules: kinetic-beat-slam
- voiceover: "Tóm lại: đừng bỏ OOP, hãy bỏ thói quen kế thừa mặc định... Cây kế thừa trong dự án của bạn sâu mấy tầng? Cảm ơn bạn đã xem video."

1. t=0–9: câu "Bắt đầu từ khả năng, không phải từ dòng dõi." hiện từng cụm (`kinetic-beat-slam`).
2. t=9–17: hai khối Lego Flyable và Eater lắp vào nhau; con khỉ nhỏ ở phía xa đi khuất, quả chuối nằm gọn trong tay (chuối đổi sang tay người, lặp motif Frame 1).
3. t=17–25: hộp bình luận mô phỏng với câu "Cây kế thừa của bạn sâu mấy tầng?" và nút đăng ký bấm xuống (`press-release-spring`); khung cuối đứng yên một nhịp rồi tắt.
