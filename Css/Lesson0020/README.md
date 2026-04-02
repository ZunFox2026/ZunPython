# Tìm hiểu về Accessibility trong CSS
## Giới thiệu
Accessibility (khả năng tiếp cận) là một phần quan trọng trong thiết kế web, giúp đảm bảo rằng tất cả mọi người, bao gồm cả những người khuyết tật, có thể sử dụng và tiếp cận thông tin trên website một cách dễ dàng. Trong CSS, chúng ta có thể áp dụng nhiều kỹ thuật khác nhau để cải thiện khả năng tiếp cận của website. Bài viết này sẽ giới thiệu về các khái niệm cơ bản và cách áp dụng chúng trong thiết kế web.

## Lý thuyết
Khả năng tiếp cận trong CSS bao gồm nhiều方面, bao gồm:
- **Màu sắc và tương phản**: Đảm bảo rằng màu sắc và tương phản giữa văn bản và nền đủ rõ ràng để người dùng có thể đọc dễ dàng.
- **Kích thước và kiểu chữ**: Chọn kích thước và kiểu chữ phù hợp để người dùng có thể đọc rõ ràng.
- ** Navigation và tương tác**: Đảm bảo rằng người dùng có thể dễ dàng điều hướng và tương tác với các yếu tố trên website.
- **Phụ đề và mô tả ảnh**: Thêm phụ đề và mô tả cho ảnh để người dùng khiếm thị có thể hiểu nội dung.

Ví dụ về áp dụng màu sắc và tương phản trong CSS:
```css
body {
    background-color: #f2f2f2; /* Màu nền */
    color: #333; /* Màu văn bản */
}
```
## Ví dụ
Một ví dụ khác về khả năng tiếp cận trong CSS là sử dụng thuộc tính `:focus` để thay đổi màu sắc hoặc kiểu dáng của các yếu tố khi người dùng tương tác với chúng. Điều này giúp người dùng khiếm thị có thể dễ dàng nhận biết được yếu tố nào đang được tập trung.
```css
button:focus {
    outline: none; /* Loại bỏ đường viền mặc định */
    box-shadow: 0 0 0 2px #51a7e8; /* Thêm bóng đổ */
}
```
## Bài tập
Để áp dụng kiến thức về khả năng tiếp cận trong CSS, hãy thực hiện các bài tập sau:
- Tạo một trang web đơn giản với màu sắc và tương phản rõ ràng.
- Thêm phụ đề và mô tả cho các ảnh trên trang web.
- Sử dụng thuộc tính `:focus` để tạo hiệu ứng tập trung cho các nút bấm và liên kết.
Bằng cách áp dụng các kỹ thuật này, bạn có thể tạo ra một trang web thân thiện và dễ sử dụng cho tất cả mọi người. Hãy nhớ rằng khả năng tiếp cận là một phần quan trọng trong thiết kế web và nên được xem xét trong suốt quá trình phát triển dự án.