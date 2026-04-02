# Tìm hiểu về Media Queries
## Giới thiệu
Media Queries là một tính năng trong CSS cho phép bạn áp dụng các phong cách khác nhau dựa trên các điều kiện cụ thể của thiết bị hoặc trình duyệt. Điều này giúp bạn tạo ra các trang web đáp ứng, có thể thích nghi với nhiều loại thiết bị và kích thước màn hình khác nhau. Với Media Queries, bạn có thể kiểm soát cách hiển thị của trang web trên desktop, laptop, tablet, smartphone, v.v.

## Lý thuyết
Media Queries sử dụng cú pháp `@media` để định nghĩa các khối phong cách sẽ được áp dụng khi đáp ứng một hoặc nhiều điều kiện nhất định. Các điều kiện này thường liên quan đến kích thước màn hình, hướng màn hình (đứng hoặc ngang), độ phân giải, v.v. Ví dụ, bạn có thể sử dụng `@media (max-width: 768px)` để áp dụng các phong cách cho các thiết bị có chiều rộng màn hình tối đa là 768 pixel, thường tương ứng với các thiết bị di động.

```css
@media (max-width: 768px) {
  body {
    font-size: 16px;
  }
}
```

Trong ví dụ trên, khi trang web được truy cập từ một thiết bị có chiều rộng màn hình tối đa là 768 pixel, kích thước font của phần tử `body` sẽ được thiết lập thành 16 pixel.

## Ví dụ
Một ví dụ khác về việc sử dụng Media Queries để thay đổi bố cục của một trang web dựa trên chiều rộng màn hình. Giả sử bạn muốn bố cục của trang web trở nên đơn giản hơn trên các thiết bị di động.

```css
/* Phong cách mặc định cho desktop */
.container {
  display: flex;
  flex-direction: row;
}

/* Thay đổi phong cách cho mobile */
@media (max-width: 480px) {
  .container {
    flex-direction: column;
  }
}
```

Trong ví dụ này, trên các thiết bị di động có chiều rộng màn hình tối đa là 480 pixel, các phần tử con trong phần tử `.container` sẽ được sắp xếp theo chiều dọc thay vì chiều ngang như trên desktop.

## Bài tập
Bài tập cho bạn: Tạo một trang web đơn giản với một phần tiêu đề và một phần nội dung. Sử dụng Media Queries để thay đổi kích thước font của tiêu đề và màu nền của trang web dựa trên chiều rộng màn hình. Cụ thể:
- Trên desktop (chiều rộng màn hình > 1024px), tiêu đề có kích thước font là 36px và màu nền là xanh lá cây.
- Trên tablet (chiều rộng màn hình từ 768px đến 1024px), tiêu đề có kích thước font là 24px và màu nền là vàng.
- Trên mobile (chiều rộng màn hình < 768px), tiêu đề có kích thước font là 18px và màu nền là đỏ.

Thử nghiệm và quan sát cách trang web của bạn thay đổi khi bạn điều chỉnh kích thước cửa sổ trình duyệt hoặc truy cập từ các thiết bị khác nhau.