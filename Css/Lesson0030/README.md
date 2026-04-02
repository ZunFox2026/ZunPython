# Tìm hiểu về Media Queries
## Giới thiệu
Media Queries là một tính năng mạnh mẽ trong CSS cho phép chúng ta áp dụng các phong cách khác nhau dựa trên các điều kiện cụ thể như chiều rộng màn hình, thiết bị, hướng màn hình, v.v. Điều này giúp chúng ta tạo ra các trang web và ứng dụng có khả năng thích ứng với nhiều loại thiết bị và kích thước màn hình khác nhau.

## Lý thuyết
Media Queries sử dụng cú pháp `@media` để xác định các điều kiện. Sau đó, chúng ta có thể áp dụng các phong cách CSS bên trong khối `@media`. Ví dụ, để áp dụng phong cách cho màn hình có chiều rộng tối đa 768px, chúng ta có thể sử dụng:
```css
@media (max-width: 768px) {
  /* CSS styles ở đây */
  body {
    background-color: lightblue;
  }
}
```
Trong ví dụ trên, khi chiều rộng màn hình nhỏ hơn hoặc bằng 768px, nền của trang web sẽ chuyển sang màu xanh nhạt.

## Ví dụ
Một ví dụ thực tế về việc sử dụng Media Queries là tạo ra một menu di động. Chúng ta có thể ẩn menu khi ở trên máy tính bảng hoặc điện thoại và chỉ hiển thị khi người dùng nhấn vào nút menu. Ví dụ:
```css
@media (max-width: 992px) {
  .menu {
    display: none;
  }
  .menu-toggle {
    display: block;
  }
}
```
Trong ví dụ này, khi chiều rộng màn hình nhỏ hơn hoặc bằng 992px, menu sẽ bị ẩn và nút menu toggle sẽ được hiển thị.

## Bài tập
Bài tập cho bạn là tạo một trang web đơn giản có chứa một phần tiêu đề, một phần nội dung và một phần chân trang. Sử dụng Media Queries để khi chiều rộng màn hình nhỏ hơn 768px, phần tiêu đề và chân trang sẽ có màu nền khác, và phần nội dung sẽ có chiều rộng tối đa 90% so với chiều rộng màn hình. Thử nghiệm với các giá trị khác nhau và quan sát sự thay đổi trên trang web của bạn. Đây là một cơ hội tuyệt vời để bạn thực hành và nắm vững kỹ năng sử dụng Media Queries trong thiết kế web.