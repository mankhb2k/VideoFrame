# Lời thoại đầy đủ cho TTS

## Cảnh 0: Hook (0:00 đến 0:40)

Bạn mở một file code, và chỉ muốn dùng đúng một hàm. Nhưng hàm đó nằm trong class cha. Class cha lại kế thừa class ông. Class ông lại kế thừa thêm một class nữa. Đến tầng thứ năm, bạn bắt đầu tự hỏi: mình đang đọc code, hay đang đọc gia phả?

Lập trình viên Joe Armstrong, cha đẻ của ngôn ngữ Erlang, từng nói về chuyện này rất hay. Bạn muốn một quả chuối, nhưng thứ bạn nhận được là một con khỉ đang cầm quả chuối, và cả khu rừng xung quanh nó.

Trong video này, mình sẽ so sánh hai cách tổ chức code. OOP, với ví dụ bằng TypeScript. Và POP, tức là Protocol-Oriented Programming, với ví dụ bằng Swift. Cuối video, bạn sẽ có bảy luật để viết TypeScript theo tư duy POP, giúp ứng dụng dễ mở rộng hơn.

## Cảnh 1: OOP trong TypeScript (0:40 đến 2:40)

OOP, hay lập trình hướng đối tượng, xoay quanh một ý tưởng: gói dữ liệu và hành vi vào cùng một chỗ, gọi là class. Bốn khái niệm bạn hay nghe là đóng gói, trừu tượng, kế thừa và đa hình.

Đóng gói nghĩa là giấu trạng thái bên trong, chỉ mở ra những hàm cần thiết. Hãy nhìn vào ví dụ. Class Animal có một thuộc tính riêng tư tên là energy, bên ngoài không thể chạm vào. Chỉ có hàm eat mới được phép tăng năng lượng.

Kế thừa nghĩa là class con tái sử dụng code của class cha. Class Bird kế thừa Animal, nên chim tự động biết ăn. Thêm vào đó, nó có hàm fly để bay. Rồi Sparrow, chim sẻ, kế thừa Bird, và thế là chim sẻ vừa ăn được vừa bay được, mà bạn không phải viết lại gì cả. Đây chính là thứ khiến OOP hấp dẫn: viết một lần, dùng ở mọi nơi.

Còn đa hình thì sao? Đa hình cho phép bạn gọi cùng một hàm trên nhiều kiểu khác nhau. Trong TypeScript, abstract class Shape buộc mọi class con phải tự cài đặt hàm area. Circle tính diện tích theo bán kính. Bạn tạo một mảng các Shape, rồi gọi area cho từng phần tử, mà không cần biết đó là hình gì.

Trong nhiều thập niên, OOP thắng lớn vì đây là cách rất tự nhiên để mô hình hóa thế giới thật, nhất là trong những đội nhóm lớn. Và TypeScript càng tiếp thêm động lực: từ khóa class có sẵn từ ES 2015, cùng với extends, abstract và private. Dùng được ngay. Cho đến khi yêu cầu bắt đầu thay đổi.

## Cảnh 2: Khi kế thừa bắt đầu hỏng (2:40 đến 4:00)

Rồi sếp báo: thêm chim cánh cụt. Chim cánh cụt là một loài chim, nên bạn cho nó kế thừa Bird. Nhưng Bird có hàm fly. Còn chim cánh cụt thì không biết bay.

Bạn có hai lựa chọn xấu. Một là cho hàm fly của Penguin ném ra một lỗi. Hai là tách lại cả cây kế thừa. Cách thứ nhất phá vỡ nguyên tắc thay thế Liskov: ở bất cứ chỗ nào dùng được Bird, thì Penguin cũng phải dùng được. Vậy mà khi một hàm gọi fly cho cả đàn chim, chương trình nổ ngay khi gặp chim cánh cụt.

Chưa hết. Tuần sau, sếp muốn thêm một chiếc máy bay không người lái, tên là Drone. Nó biết bay, nhưng không phải động vật. Nó không thể kế thừa Bird, vì nó đâu phải chim. Mà TypeScript chỉ cho phép kế thừa một class duy nhất. Vậy là bạn copy logic bay sang một chỗ khác. Từ giờ, có hai bản sao cần sửa cùng lúc, và sớm muộn gì cũng có một bản bị quên.

Cứ thế, cây kế thừa mọc thêm nhánh, các mũi tên chồng chéo lên nhau, và không ai dám sửa nữa. Đây chính là con khỉ và quả chuối. Bạn chỉ muốn khả năng bay, nhưng OOP bắt bạn lấy cả dòng dõi.

## Cảnh 3: POP trong Swift (4:00 đến 6:00)

Năm 2015, tại hội nghị WWDC, kỹ sư Dave Abrahams của Apple giới thiệu Protocol-Oriented Programming trong ngôn ngữ Swift, với một khẩu hiệu: đừng bắt đầu bằng class, hãy bắt đầu bằng protocol.

Protocol là một bản cam kết về hành vi. Thay vì hỏi con này thuộc dòng dõi nhà ai, ta hỏi con này làm được gì. Ai bay được thì ký vào Flyable. Ai ăn được thì ký vào Eater. Và nhờ extension, protocol có thể kèm sẵn cách làm mặc định, nên bạn không phải viết lại ở từng nơi.

Hãy giải lại bài toán vừa rồi. Ta có hai protocol, Flyable và Eater. Flyable có một extension, đưa sẵn hành vi bay mặc định. Sparrow là một struct, ký cả Flyable lẫn Eater, và chỉ cần tự viết hàm eat. Penguin chỉ ký Eater. Đơn giản là nó không ký Flyable, thế thôi. Còn Drone chỉ ký Flyable, và không cần dính dáng gì tới Animal.

Điều quan trọng nhất nằm ở hàm release. Hàm này nhận một mảng các phần tử Flyable, rồi gọi fly cho từng phần tử. Truyền vào Sparrow và Drone thì ổn. Còn nếu bạn truyền vào Penguin, trình biên dịch sẽ báo lỗi ngay lúc build, chứ không đợi đến khi chạy mới nổ.

Bạn cũng sẽ để ý: ở đây mọi thứ là struct, tức là kiểu giá trị, và không có cây thừa kế nào cả. Một kiểu có thể ký nhiều protocol cùng lúc, điều mà kế thừa class đơn không làm được. Swift vẫn có class khi bạn cần, POP chỉ đổi thứ tự ưu tiên: khả năng trước, dòng dõi sau.

Hãy nhớ lại câu hỏi đầu tiên. Thay vì hỏi nó là cái gì, POP hỏi: nó làm được gì?

## Cảnh 4: So sánh trực diện (6:00 đến 7:15)

Bây giờ hãy thử một yêu cầu mới: cho Sparrow và Drone phát được tiếng kêu.

Với cây kế thừa, SoundPlayer không thể nằm ở Animal, vì Drone đâu phải động vật. Bạn hoặc phải copy code, hoặc phải đổi cả cái cây. Chạm vào cây là chạm vào mọi class con, và bạn phải kiểm tra lại tất cả.

Với protocol, bạn thêm một khối mới tên là SoundPlayer, rồi ký vào đúng hai kiểu cần dùng. Không ai khác bị động chạm.

Hãy nhìn vào bảng so sánh. Câu hỏi đầu tiên: OOP hỏi nó là cái gì, POP hỏi nó làm được gì. Về cách tái sử dụng: OOP thừa hưởng từ class cha, còn POP ghép các protocol cùng extension mặc định. Một kiểu chỉ có một class cha, nhưng có thể ký nhiều protocol. Về phát hiện lỗi: kế thừa dễ nổ lúc chạy, như Penguin gọi fly, còn protocol để compiler chặn ngay từ lúc build. Và hình dạng của code theo thời gian: cây kế thừa càng sâu càng rối, còn POP mở rộng theo chiều ngang, thêm khối chứ không thêm tầng.

Khác biệt lớn nhất không nằm ở cú pháp, mà ở câu hỏi đầu tiên bạn đặt ra.

## Cảnh 5: Vì sao tư duy POP hợp kiến trúc hiện đại (7:15 đến 8:15)

Vậy vì sao tư duy này hợp với hệ thống hiện đại? Có bốn lý do.

Một, mở rộng theo chiều ngang. Thêm khả năng là thêm một khối, không phải sửa code cũ. Đây là nguyên tắc Open Closed: mở cho việc mở rộng, đóng với việc sửa đổi.

Hai, dễ test. Bạn thay một protocol bằng một bản giả, mà không cần dựng cả cây phụ thuộc phía sau.

Ba, nhiều nhóm làm song song. Protocol là hợp đồng giữa các module, mỗi bên chỉ cần biết hợp đồng, không cần biết bên kia làm thế nào.

Bốn, đổi công nghệ dễ hơn. Tầng trên chỉ phụ thuộc vào giao diện, chứ không phụ thuộc vào thứ cụ thể đằng sau.

Nhưng đừng vội vứt OOP. Khi mô hình thật sự là quan hệ là một, và cây chỉ sâu một hai tầng, như các lớp View trong bộ UI toolkit hay thực thể trong game engine, kế thừa vẫn hoạt động tốt. Và protocol cũng có thể bị lạm dụng: trừu tượng hóa mọi thứ khi chưa cần cũng là một mớ rối khác.

Quy tắc ngón tay cái: chỉ kế thừa khi quan hệ là một thật sự, ổn định, và không quá hai tầng. Chia sẻ một khả năng thì dùng interface hoặc hàm riêng. Và chưa có hai nơi cùng cần thì đừng tạo interface sớm.

## Cảnh 6: Bảy luật TypeScript theo tư duy POP (8:15 đến 9:45)

TypeScript không có protocol như Swift, nhưng bạn vẫn có thể nghĩ như POP. Đây là bảy luật, mỗi luật một ý.

Luật một: bắt đầu từ interface, không bắt đầu từ class. Trước khi gõ class, hãy hỏi: mình cần khả năng gì, rồi đặt tên cho nó. Ví dụ Flyable và Eater.

Luật hai: ghép, đừng thừa kế. Dùng kiểu giao để tạo vai trò từ nhiều khả năng. Một con chim sẻ vừa là Flyable vừa là Eater. Nếu bắt buộc phải extends, thì tối đa hai tầng.

Luật ba: mỗi interface chỉ một khả năng. Tránh một interface Animal cái gì cũng có, vì nó bắt chim cánh cụt phải có hàm fly.

Luật bốn: hành vi mặc định đặt trong hàm, không đặt trong class cha. Đây là bản thay thế cho protocol extension của Swift. Một hàm flyBy nhận tên và trả về một đối tượng Flyable, và bất kỳ ai cần bay thì dùng lại nó.

Luật năm: phụ thuộc vào interface, không phụ thuộc vào class cụ thể. Hàm release chỉ cần biết nó nhận một mảng Flyable. Nhờ vậy, thay đổi bên dưới không làm hỏng bên trên, và viết test rất dễ.

Luật sáu: ưu tiên dữ liệu bất biến. Dùng readonly và những hàm trả về đối tượng mới, giống tinh thần struct của Swift, để ít trạng thái ẩn bị chia sẻ giữa các class.

Luật bảy: để compiler bắt lỗi giúp bạn. Bật chế độ strict. Khi bạn truyền một Eater vào hàm cần Flyable, TypeScript báo lỗi thiếu hàm fly ngay lúc build, chứ không phải lúc chạy.

## Cảnh 7: Chốt và kêu gọi hành động (9:45 đến 10:15)

Tóm lại: đừng bỏ OOP, hãy bỏ thói quen kế thừa mặc định. Trước khi viết class, hãy hỏi một câu: mình cần khả năng gì? Hãy bắt đầu từ khả năng, rồi mới tới dòng dõi.

Việc nên làm trong tuần sau: mở dự án của bạn, tìm cây kế thừa sâu nhất, và thử tách một khả năng trong đó ra thành một interface. Cây kế thừa trong dự án của bạn sâu mấy tầng? Hãy viết vào phần bình luận nhé. Cảm ơn bạn đã xem video.
