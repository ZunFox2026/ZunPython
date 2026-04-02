# Media Query
Bài học này sẽ giới thiệu về Media Query, một tính năng quan trọng trong CSS giúp chúng ta tạo ra các trang web đáp ứng (responsive) trên nhiều thiết bị và kích thước màn hình khác nhau.

## Giới thiệu
Media Query là một kỹ thuật trong CSS cho phép chúng ta áp dụng các kiểu dáng (styles) khác nhau dựa trên các điều kiện cụ thể của thiết bị hoặc môi trường mà trang web đang được hiển thị. Điều này giúp chúng ta tạo ra các trang web có thể thích nghi với nhiều loại thiết bị, từ điện thoại di động đến máy tính bảng, laptop và thậm chí là máy tính để bàn. Với Media Query, chúng ta có thể kiểm soát cách thức hiển thị của trang web trên các thiết bị có kích thước màn hình, độ phân giải, hướng hiển thị (landscape hoặc portrait) khác nhau.

## Lý thuyết
Để sử dụng Media Query, chúng ta cần sử dụng cú pháp `@media` trong CSS. Cú pháp cơ bản của Media Query như sau:
```css
@media (điều kiện) {
  /* Các kiểu dáng CSS sẽ được áp dụng khi điều kiện được đáp ứng */
}
```
Trong đó, `điều kiện` có thể là một trong nhiều loại điều kiện khác nhau, chẳng hạn như `max-width`, `min-width`, `max-height`, `min-height`, `orientation`, v.v. Ví dụ:
```css
@media (max-width: 768px) {
  /* Các kiểu dáng CSS sẽ được áp dụng khi chiều rộng màn hình không vượt quá 768px */
  body {
    font-size: 16px;
  }
}
```
Điều này có nghĩa là khi chiều rộng màn hình không vượt quá 768px (ví dụ như trên điện thoại di động hoặc máy tính bảng), font-size của toàn bộ trang web sẽ được thiết lập là 16px.

## Ví dụ
Dưới đây là ví dụ về việc sử dụng Media Query để tạo ra một trang web đáp ứng:
```css
/* Kiểu dáng mặc định cho trang web */
body {
  font-size: 18px;
  background-color: #f2f2f2;
}

/* Áp dụng kiểu dáng cho màn hình có chiều rộng không vượt quá 768px */
@media (max-width: 768px) {
  body {
    font-size: 16px;
    background-color: #ccc;
  }
}

/* Áp dụng kiểu dáng cho màn hình có chiều rộng không vượt quá 480px */
@media (max-width: 480px) {
  body {
    font-size: 14px;
    background-color: #aaa;
  }
}
```
Trong ví dụ này, chúng ta có ba kiểu dáng khác nhau cho trang web dựa trên chiều rộng màn hình: mặc định (18px và #f2f2f2), cho màn hình có chiều rộng không vượt quá 768px (16px và #ccc), và cho màn hình có chiều rộng không vượt quá 480px (14px và #aaa).

## Bài tập
Bài tập này yêu cầu bạn tạo ra một trang web đơn giản có thể thích nghi với nhiều loại thiết bị. Yêu cầu cụ thể như sau:
- Tạo một trang web có tiêu đề, đoạn văn và nút bấm.
- Sử dụng Media Query để áp dụng các kiểu dáng khác nhau cho trang web dựa trên chiều rộng màn hình:
  - Đối với màn hình có chiều rộng không vượt quá 768px, thiết lập font-size của tiêu đề là 20px và đoạn văn là 16px.
  - Đối với màn hình có chiều rộng không vượt quá 480px, thiết lập font-size của tiêu đề là 18px và đoạn văn là 14px.
- Thử nghiệm trang web của bạn trên các thiết bị khác nhau hoặc sử dụng công cụ phát triển của trình duyệt để xem kết quả.