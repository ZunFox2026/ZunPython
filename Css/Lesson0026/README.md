# Tìm hiểu về Media Queries
## Giới thiệu
Media Queries là một tính năng trong CSS cho phép bạn áp dụng các phong cách khác nhau cho trang web dựa trên các điều kiện nhất định, chẳng hạn như kích thước màn hình, hướng màn hình, loại thiết bị, v.v. Điều này giúp bạn có thể tạo ra một trang web đáp ứng được trên nhiều loại thiết bị và kích thước màn hình khác nhau.

## Lý thuyết
Media Queries sử dụng cú pháp `@media` để định nghĩa các điều kiện cho việc áp dụng phong cách. Cú pháp cơ bản của Media Queries là `@media loại thiết bị và (điều kiện) { phong cách }`. Loại thiết bị có thể là `all`, `screen`, `print`, v.v. Điều kiện thường được sử dụng là `width`, `height`, `orientation`, v.v.

Ví dụ:
```css
@media screen and (max-width: 768px) {
  body {
    background-color: #f2f2f2;
  }
}
```
Trong ví dụ trên, phong cách sẽ được áp dụng cho trang web khi nó được hiển thị trên màn hình có chiều rộng tối đa là 768px.

## Ví dụ
Media Queries có thể được sử dụng để tạo ra một trang web đáp ứng được trên nhiều loại thiết bị. Ví dụ, bạn có thể sử dụng Media Queries để thay đổi kích thước font chữ, chiều rộng của các phần tử, v.v. dựa trên kích thước màn hình.

Ví dụ:
```css
@media screen and (max-width: 480px) {
  h1 {
    font-size: 24px;
  }
}

@media screen and (min-width: 481px) and (max-width: 768px) {
  h1 {
    font-size: 36px;
  }
}

@media screen and (min-width: 769px) {
  h1 {
    font-size: 48px;
  }
}
```
Trong ví dụ trên, kích thước font chữ của thẻ `h1` sẽ được thay đổi dựa trên kích thước màn hình.

## Bài tập
Bài tập này yêu cầu bạn tạo ra một trang web đơn giản có thể đáp ứng được trên nhiều loại thiết bị. Sử dụng Media Queries để thay đổi kích thước font chữ, chiều rộng của các phần tử, v.v. dựa trên kích thước màn hình.

Yêu cầu:
- Tạo ra một trang web có tiêu đề, đoạn văn và hình ảnh.
- Sử dụng Media Queries để thay đổi kích thước font chữ của tiêu đề và đoạn văn dựa trên kích thước màn hình.
- Sử dụng Media Queries để thay đổi chiều rộng của hình ảnh dựa trên kích thước màn hình.
- Kiểm tra trang web trên nhiều loại thiết bị và kích thước màn hình khác nhau để đảm bảo rằng nó đáp ứng được trên nhiều loại thiết bị.