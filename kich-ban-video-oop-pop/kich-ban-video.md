# Kịch bản video: OOP (TypeScript) vs POP (Swift)

13/10/2026

## Tổng quan

Video nên dài khoảng 10 phút (9:45–10:15 tùy tốc độ đọc), đủ để có code thật ở cả hai ngôn ngữ mà không bị loãng. Giọng đọc tiếng Việt, thuật ngữ giữ tiếng Anh. Đối tượng: dev web/mobile đã biết TypeScript cơ bản, chưa chắc biết Swift.

**Thông điệp một câu:** vấn đề không nằm ở OOP mà ở thói quen kế thừa; hãy bắt đầu từ khả năng (protocol/interface) thay vì từ dòng dõi (class cha).

| Phần | Nội dung | Thời gian | Độ dài |
| --- | --- | --- | --- |
| 0 | Hook: con khỉ và quả chuối | 0:00–0:40 | 40 giây |
| 1 | OOP trong TypeScript | 0:40–2:40 | 2 phút |
| 2 | Khi kế thừa bắt đầu hỏng | 2:40–4:00 | 1 phút 20 giây |
| 3 | POP trong Swift | 4:00–6:00 | 2 phút |
| 4 | So sánh trực diện | 6:00–7:15 | 1 phút 15 giây |
| 5 | Vì sao POP hợp kiến trúc hiện đại | 7:15–8:15 | 1 phút |
| 6 | Bảy luật TypeScript theo tư duy POP | 8:15–9:45 | 1 phút 30 giây |
| 7 | Chốt và kêu gọi hành động | 9:45–10:15 | 30 giây |

Ghi chú nội dung: "POP" trong video này là *Protocol-Oriented Programming*, không phải lập trình thủ tục; nói rõ điều này ở giây thứ 30 để khán giả khỏi nhầm.

## Phần 0 — Hook (0:00–0:40)

Mục tiêu: trong 40 giây, khán giả thấy đúng nỗi đau của mình: chỉ muốn một tính năng nhưng phải kéo theo cả cây kế thừa.

**Lời thoại:**

> Bạn mở một file code và chỉ muốn dùng đúng một hàm `play()`. Nhưng hàm đó nằm trong class cha. Class cha lại kế thừa class ông. Class ông lại kế thừa… bạn đếm đến tầng thứ năm thì thôi.
>
> Lập trình viên Joe Armstrong, cha đẻ ngôn ngữ Erlang, từng nói: "Bạn muốn quả chuối, nhưng nhận được con khỉ đang cầm quả chuối, và cả khu rừng xung quanh nó."
>
> Video này so sánh hai cách tổ chức code: OOP với ví dụ TypeScript, và POP, tức Protocol-Oriented Programming, với ví dụ Swift. Cuối video, bạn sẽ có bảy luật để viết TypeScript theo tư duy POP, giúp ứng dụng dễ mở rộng hơn.

**Hình ảnh:**

1. 0:00–0:12: một quả chuối ở giữa màn hình tối. Chuối bị kéo dần ra, hiện con khỉ cầm nó, rồi hiện cả khu rừng (các node xám nối nhau).
2. 0:12–0:25: trích dẫn của Joe Armstrong gõ chữ từng từ một (hiệu ứng typewriter), phía dưới ghi tên tác giả.
3. 0:25–0:40: logo "OOP" bên trái, "POP" bên phải, chữ "vs" ở giữa. Phụ đề: "Protocol-Oriented Programming".

## Phần 1 — OOP trong TypeScript (0:40–2:40)

Mục tiêu: giải thích OOP công bằng, nó giải quyết được gì và vì sao nó hấp dẫn lúc đầu. Khán giả phải thấy OOP "có lý" trước khi thấy nó hỏng.

**Lời thoại (0:40–1:30):**

> OOP, lập trình hướng đối tượng, xoay quanh một ý tưởng: gói dữ liệu và hành vi vào cùng một chỗ, gọi là class. Bốn khái niệm bạn hay nghe: đóng gói, trừu tượng, kế thừa và đa hình.
>
> Đóng gói nghĩa là giấu trạng thái bên trong, chỉ mở ra những hàm cần thiết. Kế thừa nghĩa là class con tái sử dụng code của class cha. Và đây là thứ khiến OOP hấp dẫn: bạn viết `eat()` một lần ở `Animal`, mọi loài đều có.

```ts
class Animal {
  #energy = 100;               // đóng gói: không truy cập từ bên ngoài
  constructor(protected name: string) {}

  eat() {
    this.#energy += 10;
    console.log(`${this.name} đang ăn`);
  }
}

class Bird extends Animal {    // kế thừa
  fly() { console.log(`${this.name} bay lên`); }
}

class Sparrow extends Bird {}
new Sparrow("Chào mào").fly();   // chạy tốt
```

**Lời thoại (1:30–2:40):**

> Đa hình thì sao? Cho phép bạn gọi cùng một hàm trên nhiều kiểu khác nhau. Trong TypeScript, `abstract class` buộc class con phải tự triển khai hàm, và bạn gọi qua kiểu cha.
>
> Ba thập niên đầu, OOP thắng lớn vì đây là cách tốt để mô hình hóa thế giới thật trong một đội nhóm lớn. Và TypeScript càng tiếp thêm động lực: từ khóa `class` có sẵn từ ES2015, `extends`, `abstract`, `private`. Dùng được ngay.

```ts
abstract class Shape {
  abstract area(): number;
}
class Circle extends Shape {
  constructor(private r: number) { super(); }
  area() { return Math.PI * this.r ** 2; }
}
const shapes: Shape[] = [new Circle(2)];
shapes.forEach(s => console.log(s.area()));   // đa hình
```

**Hình ảnh:**

1. Bốn ô vuông (Đóng gói, Trừu tượng, Kế thừa, Đa hình) hiện lần lượt, mỗi ô có icon nhỏ.
2. Code TypeScript gõ dần bên trái; bên phải cây kế thừa `Animal → Bird → Sparrow` mọc thêm từng nhánh, màu xanh lá ("mọi thứ đang ổn").
3. Highlight dòng `extends` khi nói về kế thừa và dòng `#energy` khi nói về đóng gói.

## Phần 2 — Khi kế thừa bắt đầu hỏng (2:40–4:00)

Mục tiêu: cho khán giả thấy cây kế thừa vỡ ra khi yêu cầu thay đổi, bằng hai yêu cầu rất đời thường: một con chim không biết bay và một vật thể biết bay nhưng không phải động vật.

**Lời thoại:**

> Rồi sếp báo: thêm chim cánh cụt. Chim cánh cụt là chim, nên bạn cho nó kế thừa `Bird`. Nhưng `Bird` có hàm `fly()`. Bạn có hai lựa chọn xấu: ném lỗi trong `fly()` của cánh cụt, hoặc tách lại cả cây. Cả hai đều phá vỡ nguyên tắc thay thế Liskov: ở chỗ nào dùng được `Bird`, thì `Penguin` phải dùng được, nhưng nó lại làm chương trình nổ.
>
> Chưa hết. Tuần sau sếp muốn thêm máy bay không người lái, biết bay, nhưng không phải động vật. Nó không thể kế thừa `Bird`, vì đâu phải chim. Mà TypeScript chỉ cho kế thừa một class. Bạn sẽ copy `fly()` sang chỗ khác, và từ đó bắt đầu có hai bản sao cần sửa cùng lúc.
>
> Đây chính là con khỉ và quả chuối. Bạn chỉ muốn khả năng bay, nhưng OOP bắt bạn lấy cả dòng dõi.

```ts
class Penguin extends Bird {
  fly() { throw new Error("Chim cánh cụt không bay được!"); }  // vỡ Liskov
}

function release(birds: Bird[]) {
  birds.forEach(b => b.fly());   // nổ khi gặp Penguin
}

class Drone {                    // không thể extends Bird
  fly() { /* copy-paste lại logic bay */ }
}
```

**Hình ảnh:**

1. Cây kế thừa gọn gàng ở Phần 1 hiện lại. Chim cánh cụt rơi vào nhánh `Bird`, nhánh đó chuyển đỏ, tiếng báo lỗi vang lên.
2. Drone bay vào màn hình, nối một mũi tên tới `Bird`, mũi tên bật ngược lại ("không phải chim").
3. Các mũi tên chồng chéo, các node nhích lại gần nhau thành một mớ rối (spaghetti), chữ "Ai dám sửa?" hiện lên.
4. Lia ra xa: một con khỉ khổng lồ cầm quả chuối, cả khu rừng phía sau.

## Phần 3 — POP trong Swift (4:00–6:00)

Mục tiêu: giải cùng bài toán Chim cánh cụt và Drone bằng protocol, để khán giả thấy khác biệt ngay trên cùng ví dụ. Dùng đúng ba nhân vật cũ để dễ so sánh.

**Lời thoại (4:00–5:00):**

> Năm 2015, tại WWDC, kỹ sư Dave Abrahams của Apple giới thiệu Protocol-Oriented Programming trong Swift, với một khẩu hiệu: đừng bắt đầu bằng class, hãy bắt đầu bằng protocol.
>
> Protocol là bản cam kết hành vi. Thay vì hỏi "con này thuộc dòng dõi nào", ta hỏi "con này làm được gì". Ai bay được thì ký vào `Flyable`. Ai ăn được thì ký vào `Eater`. Và nhờ `extension`, protocol có thể kèm sẵn cách làm mặc định, nên không phải viết lại ở từng nơi.

```swift
protocol Flyable { func fly() }
protocol Eater   { func eat() }

extension Flyable {                  // hành vi mặc định
    func fly() { print("Đang bay") }
}

struct Sparrow: Flyable, Eater {     // ghép khả năng như ghép Lego
    func eat() { print("Chim sẻ ăn") }
}
struct Penguin: Eater {              // đơn giản là không ký Flyable
    func eat() { print("Cánh cụt ăn") }
}
struct Drone: Flyable {}             // không cần là động vật
```

**Lời thoại (5:00–6:00):**

> Chim cánh cụt không ký `Flyable`, nên không bao giờ bị gọi `fly()`. Compiler sẽ chặn ngay từ lúc build, không đợi đến lúc chạy mới nổ. Drone ký `Flyable` mà không cần dính dáng gì tới `Animal`.
>
> Bạn cũng để ý: ở đây mọi thứ là `struct`, kiểu giá trị, không có cây thừa kế nào. Một kiểu có thể ký nhiều protocol cùng lúc, điều mà kế thừa class đơn không làm được. Và Swift vẫn có class khi bạn cần, POP chỉ đổi thứ tự ưu tiên: khả năng trước, dòng dõi sau.

```swift
func release(_ things: [any Flyable]) {
    things.forEach { $0.fly() }
}
release([Sparrow(), Drone()])   // OK
release([Penguin()])            // Lỗi biên dịch: Penguin không phải Flyable
```

**Hình ảnh:**

1. Màn hình sạch lại, nền sáng hơn Phần 2. Ba khối Lego mang nhãn `Flyable`, `Eater`, `SoundPlayer` bay vào giữa khung.
2. `Sparrow` hiện ra dưới dạng một thẻ phẳng; hai khối Lego (Flyable, Eater) khớp vào thẻ với tiếng "cạch".
3. `Penguin` chỉ nhận khối Eater. Khi thử gắn Flyable, khối bật ra kèm biểu tượng chữ X đỏ nhỏ, đúng lúc đọc câu "compiler chặn ngay".
4. `Drone` hiện ra bên cạnh, nhận khối Flyable, không có đường nào nối tới Animal.

## Phần 4 — So sánh trực diện (6:00–7:15)

Mục tiêu: đặt hai cách tiếp cận cạnh nhau bằng cùng một yêu cầu thay đổi, để khán giả tự thấy chi phí khác nhau thay vì chỉ nghe kết luận.

**Lời thoại:**

> Giờ thử một yêu cầu mới: cho Sparrow và Drone phát được tiếng kêu. Với cây kế thừa, SoundPlayer không thể nằm ở Animal vì Drone không phải động vật, nên bạn hoặc copy code, hoặc đổi cả cây. Với protocol, bạn thêm một khối `SoundPlayer`, rồi ký vào hai kiểu cần dùng. Không ai khác bị động chạm.
>
> Điểm khác biệt lớn nhất không nằm ở cú pháp, mà ở câu hỏi đầu tiên. OOP hỏi: "nó là cái gì?". POP hỏi: "nó làm được gì?".

**Hình ảnh:** màn hình chia đôi. Bên trái (OOP/TypeScript) mũi tên đỏ lan ra nhiều node khi thêm `SoundPlayer`; bên phải (POP/Swift) chỉ một khối mới bay vào và gắn vào hai kiểu, mọi thứ còn lại giữ màu xám yên lặng. Sau đó hiện bảng dưới đây, từng hàng một.

| Tiêu chí | OOP kế thừa (TypeScript) | POP (Swift) |
| --- | --- | --- |
| Câu hỏi đầu tiên | Nó là cái gì? (is-a) | Nó làm được gì? (can-do) |
| Cách tái sử dụng | Thừa hưởng từ class cha | Ghép các protocol, kèm extension mặc định |
| Thêm khả năng mới | Sửa cây hoặc copy code | Thêm protocol mới, ký vào kiểu cần dùng |
| Một kiểu có nhiều vai | Chỉ một class cha | Ký nhiều protocol cùng lúc |
| Phát hiện sai sót | Dễ gặp lỗi lúc chạy (như `Penguin.fly()`) | Compiler chặn từ lúc build |
| Mức độ ràng buộc | Con phụ thuộc cha chặt chẽ | Mỗi kiểu độc lập, chỉ chung hợp đồng |
| Hình dạng code theo thời gian | Cây sâu dần, càng làm càng rối | Phẳng, thêm bề ngang chứ không thêm chiều sâu |

## Phần 5 — Vì sao tư duy POP hợp kiến trúc hiện đại (7:15–8:15)

Mục tiêu: nâng ví dụ Chim và Drone lên thành bài học kiến trúc, đồng thời giữ giọng công bằng để video không bị "bên nào cũng tốt" hoặc "OOP là cái sai".

**Lời thoại:**

> Vì sao tư duy này hợp với hệ thống hiện đại? Bốn lý do.
>
> Một: mở rộng theo chiều ngang. Thêm khả năng là thêm một khối, không sửa code cũ. Đây là nguyên tắc Open/Closed. Hai: dễ test, vì bạn thay thế một protocol bằng bản giả mà không cần dựng cả cây phụ thuộc. Ba: nhiều nhóm làm song song, vì protocol là hợp đồng giữa các module, mỗi bên chỉ cần biết hợp đồng. Bốn: đổi công nghệ dễ, vì tầng trên chỉ phụ thuộc vào giao diện, không phụ thuộc vào cái cụ thể đằng sau.
>
> Nhưng đừng vội vứt OOP. Khi mô hình thật sự là "là một" và cây chỉ sâu một hai tầng, như các lớp View trong UI toolkit hay thực thể trong game engine, kế thừa vẫn hoạt động tốt. Và protocol cũng có thể bị lạm dụng: trừu tượng hóa mọi thứ khi chưa cần cũng là một mớ rối khác.

**Quy tắc ngón tay cái (hiện lên cuối phần):**

- Quan hệ "là một" thật sự, ổn định, tối đa 2 tầng: kế thừa được.
- Chỉ chia sẻ một khả năng: dùng interface/protocol hoặc hàm riêng.
- Chưa có hai nơi cùng cần: đừng tạo interface sớm.

**Hình ảnh:** bốn biểu tượng lần lượt hiện lên ngữ cảnh (mũi tên mở rộng ngang, ổ khóa kiểm thử, hai nhóm nối qua một ổ cắm, đổi công tắc). Sau đó là một thẻ "Khi nào OOP vẫn ổn" với hai ví dụ (UI, game) và ba quy tắc ngón tay cái phía trên.

## Phần 6 — Bảy luật TypeScript theo tư duy POP (8:15–9:45)

Mục tiêu: biến tư duy Swift thành thói quen viết TypeScript hàng ngày. TypeScript không có protocol extension như Swift, nhưng có interface, kiểu giao, hàm thuần và kiểm tra kiểu lúc build, đủ để đi theo cùng hướng.

**Lời thoại mở đầu:**

> TypeScript không có protocol như Swift, nhưng bạn vẫn có thể nghĩ như POP. Đây là bảy luật, mỗi luật một ý.

**Luật 1. Bắt đầu từ interface, không bắt đầu từ class.** Trước khi gõ `class`, hãy hỏi "khả năng nào cần?" và đặt tên nó.

```ts
interface Flyable { fly(): void }
interface Eater   { eat(): void }
```

**Luật 2. Ghép, đừng thừa kế.** Dùng kiểu giao `&` để tạo vai trò từ nhiều khả năng. Nếu bắt buộc phải `extends`, tối đa hai tầng.

```ts
const sparrow: Flyable & Eater = {
  fly: () => console.log("Bay"),
  eat: () => console.log("Ăn"),
};
```

**Luật 3. Mỗi interface chỉ một khả năng.** Tránh interface "cái gì cũng có" bắt mọi kiểu phải làm những việc nó không làm được.

```ts
// Tránh: Penguin buộc phải có fly()
interface Animal { eat(): void; fly(): void; swim(): void }
```

**Luật 4. Hành vi mặc định đặt trong hàm, không đặt trong class cha.** Đây là bản thay thế cho protocol extension của Swift.

```ts
const flyBy = (name: string): Flyable => ({
  fly: () => console.log(`${name} bay`),
});
const drone = { ...flyBy("Drone") };
```

**Luật 5. Phụ thuộc vào interface, không phụ thuộc vào class cụ thể.** Hàm chỉ cần biết khả năng, nên thay đổi bên dưới không làm hỏng bên trên và dễ viết test.

```ts
function release(things: Flyable[]) {
  things.forEach(t => t.fly());
}
```

**Luật 6. Ưu tiên dữ liệu bất biến.** Dùng `readonly` và hàm trả về đối tượng mới, giống tinh thần `struct` của Swift, để ít trạng thái ẩn chia sẻ giữa các class.

```ts
type Battery = Readonly<{ level: number }>;
const drain = (b: Battery): Battery => ({ ...b, level: b.level - 1 });
```

**Luật 7. Để compiler bắt lỗi giúp bạn.** Bật `strict`, dùng ràng buộc kiểu để lỗi hiện lúc build thay vì lúc chạy.

```ts
const penguin: Eater = { eat: () => console.log("Ăn") };
release([penguin]);   // Lỗi: Property 'fly' is missing in type 'Eater'
```

**Hình ảnh:** mỗi luật là một thẻ dọc đánh số 1 đến 7, trái là một câu ngắn (tối đa 8 chữ), phải là đoạn code hai đến bốn dòng. Thẻ trượt vào từng cái một, mỗi thẻ ở lại khoảng 11–13 giây. Cuối cùng bảy thẻ xếp thành một checklist để người xem chụp màn hình.

## Phần 7 — Chốt và kêu gọi hành động (9:45–10:15)

Mục tiêu: để lại một câu dễ nhớ và một việc người xem làm được ngay tuần sau.

**Lời thoại:**

> Tóm lại: đừng bỏ OOP, hãy bỏ thói quen kế thừa mặc định. Trước khi viết `class`, hãy hỏi một câu: "Mình cần khả năng gì?" Hãy bắt đầu từ khả năng, rồi mới tới dòng dõi.
>
> Việc nên làm trong tuần sau: mở dự án của bạn, tìm cây kế thừa sâu nhất, và thử tách một khả năng trong đó ra thành một `interface`. Cây kế thừa trong dự án của bạn sâu mấy tầng? Hãy viết vào phần bình luận nhé. Cảm ơn bạn đã xem video.

**Hình ảnh:**

1. Câu chốt hiện lớn giữa màn hình: "Bắt đầu từ khả năng, không phải từ dòng dõi."
2. Hai khối Lego (Flyable, Eater) lắp vào nhau lần cuối; con khỉ ở phía xa nhẹ nhàng đi khuất, quả chuối nằm gọn trong tay.
3. Hộp bình luận mô phỏng với câu hỏi "Cây kế thừa của bạn sâu mấy tầng?" kèm nút đăng ký.

## Ghi chú sản xuất (HTML/CSS/Tailwind)

Dựng toàn bộ video thành một trang HTML khung 1920×1080 với một timeline GSAP duy nhất; mỗi phần của kịch bản là một `<section>` xếp chồng, và các nhãn timeline trùng đúng mốc thời gian ở bảng đầu tài liệu.

**Mốc timeline (giây):**

```js
const tl = gsap.timeline({ paused: true });
tl.addLabel("hook", 0)
  .addLabel("oop", 40)
  .addLabel("break", 160)
  .addLabel("pop", 240)
  .addLabel("compare", 360)
  .addLabel("why", 435)
  .addLabel("rules", 495)
  .addLabel("outro", 585);
window.tl = tl;   // để công cụ ngoài tua được tới từng khung hình
```

**Bảng màu đề xuất:**

| Vai trò | Màu | Dùng cho |
| --- | --- | --- |
| Nền | `#0B1020` | toàn cảnh, tối để code nổi |
| OOP | `#F59E0B` (hổ phách) | cây kế thừa, nhãn OOP |
| POP | `#10B981` (xanh ngọc) | khối Lego, nhãn POP |
| Lỗi/rối | `#EF4444` | Penguin.fly(), mũi tên chồng chéo |
| Chữ | `#E2E8F0` | tiêu đề, lời thoại phụ |

**Quy ước dựng:**

- Thu giọng đọc trước, đo thời lượng từng đoạn, rồi mới chỉnh `duration` của animation theo giọng.
- Mỗi đoạn code hiển thị tối đa 6 dòng, font mono (JetBrains Mono), tô màu cú pháp bằng highlight.js hoặc Shiki, hiệu ứng gõ từng ký tự.
- Cùng một nhân vật (Sparrow, Penguin, Drone) giữ nguyên hình dạng và vị trí ở cả hai bên so sánh.
- Dùng màu đúng nghĩa: đỏ là lỗi, xanh là ổn, không dùng cho trang trí.

**Xuất video:** cách nhanh là quay màn hình bằng OBS rồi ghép giọng đọc trong CapCut hoặc DaVinci. Cách sắc nét và không giật là chạy Playwright: lặp từng khung hình, gọi `tl.seek(frame / 30)`, chụp ảnh, rồi ghép bằng `ffmpeg -framerate 30 -i frame_%05d.png -i voice.mp3 -c:v libx264 -pix_fmt yuv420p out.mp4`. Với 10 phút ở 30 fps cần khoảng 18.000 khung hình, nên chạy ở 1280×720 để thử trước rồi mới xuất 1080p.
