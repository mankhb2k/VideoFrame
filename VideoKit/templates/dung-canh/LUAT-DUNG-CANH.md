# Luật dựng một đoạn video (dành cho người hoặc agent dựng)

Mỗi đoạn là một **sub-composition HyperFrames** viết bằng HTML/CSS và một timeline GSAP tạm dừng. Bạn chỉ viết **một file nguồn cho mỗi đoạn được giao**: `video/compositions/src/<id>.body.html`, rồi chạy `build_canh.py` để ghép thành `video/compositions/frames/<id>.html`. Không sửa `index.html`, `du-an.json`, `vk.css`, `vk.js`, file của đoạn khác, hay các ảnh.

## 1. Cấu trúc file nguồn (bắt buộc)

```html
<style>
/*VK_FONT*/
/*VK_CSS*/
#root { position: absolute; inset: 0; }
.cXdY-ten { ... }          /* class riêng: tiền tố id đoạn không dấu gạch, ví dụ c1d3- cho c1-d3 */
</style>
<div id="root" data-composition-id="c1-d3" data-width="1920" data-height="1080">
  ... nội dung ...
</div>
<script>
/*VK_JS*/
const D = 12.1;                              // thời lượng đoạn (giây), lấy từ gói
const tl = gsap.timeline({ paused: true });
... tween ...
window.__timelines["c1-d3"] = tl;            // khoá = id đoạn, đúng từng chữ
</script>
```

Ba dòng `/*VK_FONT*/`, `/*VK_CSS*/`, `/*VK_JS*/` giữ nguyên, `build_canh.py` thay bằng khai báo font và mọi thành phần trong `VideoKit/components/` (`core/vk.css`, `core/vk.js`, `ide/...`). Style gốc bằng `#root`, **không** bằng class trên phần tử gốc. Mọi `id` và class của đoạn có tiền tố riêng (`c1d3-...`) để không đụng đoạn khác. Mọi thứ nằm trong một file, không `<link>` ngoài.

Mẫu hoàn chỉnh đã kiểm tra: `video/compositions/src/c0-d1.body.html` (cửa sổ code, chữ, pop) và `c1-d1.body.html` (ảnh nền, nhân vật, đếm số, chip). Đọc cả hai trước khi viết.

## 2. Chạy và kiểm tra (làm từ thư mục `video/`)

```
python3 ../../../VideoKit/scripts/build_canh.py <id> [<id> ...]
npx hyperframes check                        # chỉ quan tâm các báo cáo thuộc đoạn của bạn (đoạn khác của agent khác có thể đang dựng dở)
npx hyperframes snapshot --at T1,T2,T3 --no-end -o <thư mục tạm>   # T = giây TUYỆT ĐỐI trong video = "bắt đầu tại" (ghi trong gói) + giây trong đoạn
```

Mở `contact-sheet.jpg` (hoặc từng `frame-*.png`) trong thư mục tạm để nhìn kết quả. Chụp ít nhất: giữa mỗi nhịp quan trọng, và 0,2 giây trước hết đoạn (trạng thái cuối). Sửa đến khi: không còn lỗi (error) cho đoạn của bạn, hình đúng bố cục trong gói, chữ không đè nhau, không tràn khung, không chạm vùng logo. Cảnh báo `content_overlap` hợp lý khi cố ý chồng lớp (ví dụ chữ trên biển) thì thêm `data-layout-allow-overlap` vào phần tử đó. Thư mục tạm dùng `/private/tmp/...` hoặc thư mục scratchpad, không để trong dự án.

## 3. Khung hình và bố cục

- Khung 1920×1080, lề an toàn 96 px. **Góc phải dưới có logo tròn 132 px: không đặt gì ở x > 1700 và y > 880.**
- Nếu gói nói có kệ gạch: dải y 40–140 (x 96–860) dành cho kệ; nội dung chính đặt dưới y = 150. Kệ tạo bằng `vk.keGach` (xem `components/core/vk.js`), `co` = số viên có sẵn; viên gạch mới của đoạn chốt cảnh dùng `vk.gachLon` (rơi lớn giữa khung rồi bay lên đúng ô trên kệ).
- Mỗi nhịp có **một tiêu điểm**. Chữ chính ≥ 56 px, chú thích ≥ 28 px, code ≥ 30 px. Tối đa 6 dòng code trong một cửa sổ (trừ đoạn code đầu và cuối video).
- Màu: nền `var(--nen)` (đã có sẵn trên `index.html`), chữ `var(--muc)`; giá liệt kê `.th-gia` (xanh dương đậm), giá bán và tổng `.th-gia-ban`/`.th-tong` (xanh lá đậm), sai hoặc cảnh báo `.th-canh-bao` (đỏ đậm); cam `var(--cam)` chỉ để tô nền, không làm chữ. Màu khái niệm: BIẾN vàng, HÀM xanh dương, DATABASE tím, IF/ELSE lục lam, VÒNG LẶP hồng (`--bien`, `--ham`, `--db`, `--re`, `--lap`; chữ dùng bản `-dam`, nền thẻ bản `-nhat`). Lỗi và đúng luôn kèm biểu tượng (dấu X, dấu tích), không chỉ dựa vào màu.
- Vật thể giao diện thường: viền mảnh, bóng mềm (lớp `.th-vat`, `.vk-the`, `.vk-chip`, `.vk-bubble`). Không bóng cứng, không viền dày. Code luôn trong `.th-cuaso` (3 chấm macOS) với `.vk-code` và mỗi dòng một `<span class="vk-dong">`; từ khoá tô bằng `<span class="k-bien">` v.v.
- Chữ: chỉ dùng `Be Vietnam Pro` (chữ thường) và `JetBrains Mono` (code); mọi font đã khai báo sẵn. Không dùng font khác.
- **Không hiển thị câu lời dẫn thành chữ.** Chỉ chữ khoá, nhãn, số, tên khái niệm, mã code. Lời dẫn trong gói chỉ để căn nhịp.

## 4. Nhân vật và đạo cụ (ảnh PNG nền trong)

- Danh sách và vùng nhìn thấy của từng ảnh: `storyboard/ANH-KICH-THUOC.md`. Đường dẫn trong code: `assets/images/<id>.png` (ví dụ `assets/images/ong-son/goc.png`).
- Tất cả vuông 1024 px (nền 1536×864, phủ toàn khung 1920×1080 bằng `width:1920px;height:1080px`). Nhân vật cao khoảng 98% ảnh, đứng sát đáy. `vk.nv(parent, {src, size, cx, base})` đặt ảnh vuông `size` px, tâm ngang tại `cx`, **đáy ảnh** tại `base` (bóng elip dưới chân tự tạo; `bong:false` để tắt). Hàm trả về phần tử ảnh để bạn tween (`img._bong` là bóng).
- **Cỡ nhân vật chuẩn** (giá trị `size` khi đứng cùng nhau; một mình có thể phóng tới 1,25 lần, nhưng người cùng khung phải cùng hệ số). **Ông Sơn luôn cao hơn Cô Lan một chút**: Ông Sơn 670, Cô Lan 610, Anh Tâm 630, Chị Hạnh 610, Anh Hùng 640, Bình 585, Bà Tư 545, Thanh niên 650. Ảnh nửa thân (`quay-thu-ngan`) có đầu to hơn dáng đứng ở cùng `size`: dùng `size` nhỏ hơn dáng đứng khoảng 10% (ví dụ Cô Lan sau quầy 550 khi Ông Sơn đứng cạnh 640). Ảnh nhóm `chi-hanh/ban-ke-toan` dùng `size` 900 đến 1100 và đặt đáy ảnh sát đáy khung.
- Đạo cụ (`vat/...`) vuông 1024; vật chiếm khoảng 80% ảnh. Chữ trên đạo cụ trơn (bao, thùng, chai, sổ) là nhãn HTML đặt đè lên vùng nhãn trống (căn bằng thử và chụp lại).
- Một người chuyển dáng (ví dụ `goc` → `ngac-nhien`): đặt hai ảnh chồng đúng một chỗ, ảnh sau `opacity:0`, đổi bằng `tl.set` hoặc crossfade 0,15 giây tại đúng thời điểm.

## 5. Chuyển động (bắt buộc xác định, seek được hai chiều)

- Timeline duy nhất, `paused: true`, đăng ký ở `window.__timelines["<id>"]`. Không `Math.random`, không `Date.now`, không `repeat: -1`, không CSS `transition`/`animation`, không tween `width`/`height`/`top`/`left` (dùng `x`, `y`, `scale`, `rotation`, `opacity`, `clip-path`, `backgroundColor`, `strokeDashoffset`).
- Luôn dùng `fromTo` (hoặc các hàm `vk.*`) cho tween vào, để trạng thái đầu rõ ràng. Phần tử xuất hiện dần cho `opacity:0` bằng `fromTo`, **không** `display:none` hay `visibility:hidden` làm trạng thái đầu.
- Không đặt CSS `transform` (ví dụ `translate(-50%,-50%)` để căn giữa) lên phần tử mà GSAP cũng tween `x/y/scale/rotation`: GSAP ghi đè. Căn giữa bằng `left`/`top` cộng `margin`, hoặc bọc phần tử trong một div căn giữa.
- Mỗi nhịp trong gói ghi một thời điểm (giây tính từ **đầu đoạn**). Tween bắt đầu **đúng hoặc ngay trước** thời điểm đó (tối đa sớm 0,15 giây), không để mọi thứ hiện ở giây 0 (không "nạp trước"). Phần tử mới đến lúc nào hiện lúc đó. Hết đoạn giữ nguyên hình, **không** hiệu ứng thoát ở cuối (đoạn sau cắt thẳng vào).
- Khoảng "dừng" trong gói nghĩa là giữ hình tĩnh để người xem đọc: không thêm chuyển động khác (con trỏ nhấp nháy hoặc thở nhẹ ≤ 2% được phép).
- Vật đi giữa hai chỗ: `vk.cung` (bay theo cung, `cao` âm là vồng lên), kết thúc bằng `vk.nay`. Số tăng dần: `vk.dem`. Chữ hiện: `vk.vao`/`vk.pop`. Đường vẽ dần: phần tử `<path pathLength="1" class="vk-net">` rồi `vk.ve`. Sáng dòng code: `vk.sangDong`. Gõ chữ: `vk.go`.
- Hiệu ứng nhịp (sfx) do bước khác lo; bạn **không** gắn `<audio>` và không phát âm thanh.

## 6. Chất lượng

- Nhìn ảnh chụp như một người xem: chữ có đọc được trong 1 giây không, có chỗ nào đè, lệch, tràn, hay trống trải bất thường không. Ưu tiên bố cục rõ, cân đối, nhiều khoảng thở hơn là nhồi nhiều thứ.
- Làm đúng từng nhịp trong gói, không bỏ nhịp nào, không thêm nhân vật hay ý mới. Nếu một nhịp không thể làm đúng (thiếu ảnh, mâu thuẫn), làm phương án gần nhất và ghi rõ trong báo cáo cuối.
- File nguồn đặt chú thích ngắn cho từng nhịp (`// 4,3s: ...`) như hai file mẫu.

## 7. Báo cáo cuối (ngắn)

Với mỗi đoạn: đã dựng xong hay chưa, kết quả `check` cho đoạn đó, các ảnh đã chụp và đã nhìn, các chỗ làm khác gói (nếu có) và vì sao.

## 8. Cửa sổ soạn code kiểu VS Code (`vk.ide`)

Mọi cảnh có code demo dùng `vk.ide` (thành phần ở `VideoKit/components/ide/`, `build_canh.py` tự nối vào; mở `components/ide/demo.html` bằng trình duyệt để xem thử). Có thanh tiêu đề 3 chấm macOS, tab tên file, số dòng, tô màu cú pháp Python theo VS Code Dark+, caret khi gõ, thanh trạng thái và terminal. API viết bằng tiếng Anh.

```js
const ide = vk.ide(root, { x: 160, y: 80, width: 1600, file: "notes.py", terminal: 240, code: ['name = "Son"', "capital = 20000000"] });
let t = ide.type(tl, { from: 1, to: 2, t: 3.0, cps: 30 });   // gõ dần dòng 1..2, trả về giây kết thúc
ide.show(tl, 3, 4, 8.0);                                      // hiện luôn dòng 3..4
ide.hide(tl, 1, 4, 12.0);                                     // ẩn dòng 1..4 để dùng lại cửa sổ cho bước sau
ide.highlight(tl, 2, tOn, tOff);                              // tô sáng dòng khi lời dẫn nói tới
ide.run(tl, t + 0.4, { command: "python notes.py", output: ["Name: Son", "Capital: 20000000"] });
```

Cỡ chữ theo số dòng (`level: "auto"` mặc định): `large` 1 đến 6 dòng (40), `normal` 7 đến 9 (32), `small` 10 đến 14 (26). Trên 14 dòng thì chia màn bằng `show` và `hide`. Cửa sổ tự cao vừa số dòng; đặt `height` rồi `fit: true` để giữ khung và thu nhỏ cỡ chữ. Mức `small` luôn nên dùng `highlight` theo lời dẫn. Tuỳ chọn khác: `lang: "text"`, `title`, `tabLabel`, `languageName`, `statusBar: false`. Mốc `t` đi qua `vkWarp` như mọi tween khác.
