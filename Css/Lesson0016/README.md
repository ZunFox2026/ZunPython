# Tìm hiểu về Media Queries
## Giới thiệu
Media Queries là một tính năng trong CSS cho phép các nhà phát triển web áp dụng các phong cách khác nhau dựa trên các điều kiện cụ thể của thiết bị hoặc trình duyệt. Điều này giúp tạo ra các trang web đáp ứng (responsive) có thể thích nghi với nhiều loại thiết bị và kích thước màn hình khác nhau. Trong bài viết này, chúng ta sẽ tìm hiểu về Media Queries, cách sử dụng chúng và một số ví dụ cơ bản.

## Lý thuyết
Media Queries thường được sử dụng để kiểm tra các thuộc tính như chiều rộng và chiều cao của màn hình, loại thiết bị (máy tính bảng, điện thoại di động, v.v.) và hướng của thiết bị (nằm ngang hoặc đứng). Cú pháp cơ bản của một Media Query là `@media`, sau đó là loại thiết bị và điều kiện. Ví dụ:
```css
@media (max-width: 768px) {
  /* CSS ở đây sẽ được áp dụng khi chiều rộng màn hình nhỏ hơn hoặc bằng 768px */
}
```
Trong ví dụ trên, bất kỳ CSS nào được viết bên trong khối `@media` sẽ chỉ được áp dụng khi chiều rộng của màn hình nhỏ hơn hoặc bằng 768px, thường là trường hợp của các thiết bị di động.

## Ví dụ
Giả sử chúng ta muốn tạo một trang web có menu di động chỉ xuất hiện trên các thiết bị di động nhỏ hơn 768px. Chúng ta có thể sử dụng Media Query như sau:
```css
.menu {
  display: none;
}

@media (max-width: 768px) {
  .menu {
    display: block;
  }
}
```
Trong ví dụ này, `.menu` sẽ chỉ được hiển thị (có `display: block`) khi chiều rộng màn hình nhỏ hơn hoặc bằng 768px.

## Bài tập
Để thực hành sử dụng Media Queries, hãy tạo một trang web đơn giản có một thanh navigation và một nội dung chính. Sau đó, sử dụng Media Query để thay đổi kích thước của thanh navigation và cách hiển thị nội dung khi chiều rộng màn hình nhỏ hơn 1024px. Ví dụ, bạn có thể biến thanh navigation thành một menu di động với các mục được hiển thị theo chiều dọc khi màn hình nhỏ. Hãy thử nghiệm với các điều kiện khác nhau và quan sát cách trang web của bạn phản ứng trên các thiết bị và kích thước màn hình khác nhau.