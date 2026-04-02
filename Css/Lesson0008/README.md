# Tìm hiểu về Accessibility trong CSS
## Giới thiệu
Khả năng tiếp cận (Accessibility) là một phần quan trọng trong thiết kế và xây dựng trang web. Nó đảm bảo rằng mọi người, bất kể khả năng hoặc tình trạng thể chất, đều có thể sử dụng và tương tác với trang web của bạn. Trong CSS, khả năng tiếp cận liên quan đến việc sử dụng các thuộc tính và kỹ thuật để cải thiện trải nghiệm người dùng cho những người có khả năng hạn chế. Bài viết này sẽ giới thiệu về khả năng tiếp cận trong CSS và cung cấp các ví dụ cơ bản.

## Lý thuyết
Khả năng tiếp cận trong CSS bao gồm nhiều khía cạnh, bao gồm:
- **Màu sắc và độ tương phản**: Sử dụng màu sắc và độ tương phản phù hợp để đảm bảo văn bản và các yếu tố khác trên trang web dễ đọc.
- **Kích thước và kiểu chữ**: Chọn kích thước và kiểu chữ phù hợp để văn bản dễ đọc.
- **Navigation và tương tác**: Thiết kế các phần tử navigation và tương tác (như nút bấm, liên kết) để dễ dàng sử dụng.
- **Phản hồi cho người dùng**: Cung cấp phản hồi rõ ràng cho người dùng khi họ tương tác với trang web.

Ví dụ về sử dụng màu sắc và độ tương phản trong CSS:
```css
body {
  background-color: #f2f2f2; /* Màu nền */
  color: #333; /* Màu văn bản */
}
```
## Ví dụ
Một ví dụ cụ thể về khả năng tiếp cận trong CSS là việc sử dụng thuộc tính `:focus` để cung cấp phản hồi视觉 khi một phần tử nhận được focus. Điều này đặc biệt hữu ích cho người dùng chỉ sử dụng bàn phím để điều hướng trang web.
```css
a:focus {
  outline: 2px solid #007bff; /* Thiết lập đường viền khi liên kết nhận được focus */
}
```
## Bài tập
Bài tập để cải thiện khả năng tiếp cận trong CSS:
- Thử nghiệm với các màu sắc và độ tương phản khác nhau trên trang web của bạn để đảm bảo rằng chúng dễ đọc.
- Sử dụng thuộc tính `:focus` và `:hover` để cung cấp phản hồi cho người dùng khi họ tương tác với các phần tử trên trang web.
- Kiểm tra trang web của bạn bằng cách sử dụng chỉ bàn phím để điều hướng và đảm bảo rằng mọi phần tử đều có thể tiếp cận được.
Bằng việc áp dụng các kỹ thuật và nguyên tắc khả năng tiếp cận, bạn có thể tạo ra trang web thân thiện và dễ sử dụng cho mọi người.