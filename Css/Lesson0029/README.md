# Tìm hiểu về Media Queries
## Giới thiệu
Media Queries là một tính năng trong CSS giúp developer tạo ra các trang web có khả năng đáp ứng (responsive) với các thiết bị và kích thước màn hình khác nhau. Với Media Queries, bạn có thể áp dụng các kiểu dáng và bố cục khác nhau cho trang web dựa trên các điều kiện như chiều rộng màn hình, chiều cao màn hình, định hướng thiết bị (dọc hoặc ngang),... Điều này giúp cải thiện trải nghiệm người dùng trên các thiết bị di động, máy tính bảng, laptop, desktop, v.v.

## Lý thuyết
Media Queries sử dụng cú pháp `@media` trong CSS để xác định các điều kiện và áp dụng các kiểu dáng tương ứng. Các điều kiện thường được sử dụng bao gồm:
- `max-width` và `min-width`: để kiểm tra chiều rộng tối đa và tối thiểu của màn hình.
- `max-height` và `min-height`: để kiểm tra chiều cao tối đa và tối thiểu của màn hình.
- `orientation`: để kiểm tra định hướng của thiết bị (dọc hoặc ngang).

Ví dụ về sử dụng Media Queries trong CSS:
```css
@media (max-width: 768px) {
  /* Các kiểu dáng cho màn hình có chiều rộng tối đa 768px */
  body {
    font-size: 16px;
  }
}

@media (min-width: 1024px) {
  /* Các kiểu dáng cho màn hình có chiều rộng tối thiểu 1024px */
  body {
    font-size: 18px;
  }
}
```

## Ví dụ
Một ví dụ cụ thể về sử dụng Media Queries để tạo ra một trang web đáp ứng là tạo ra một bố cục khác nhau cho màn hình di động và máy tính. Ví dụ:
```css
/* Bố cục cho màn hình di động */
@media (max-width: 480px) {
  .container {
    width: 100%;
    padding: 10px;
  }
  .header {
    height: 50px;
  }
}

/* Bố cục cho màn hình máy tính */
@media (min-width: 1024px) {
  .container {
    width: 80%;
    padding: 20px;
    margin: 0 auto;
  }
  .header {
    height: 100px;
  }
}
```
Trong ví dụ này, khi chiều rộng màn hình nhỏ hơn hoặc bằng 480px (thường là kích thước của màn hình di động), trang web sẽ áp dụng bố cục cho di động. Khi chiều rộng màn hình lớn hơn hoặc bằng 1024px (thường là kích thước của màn hình máy tính), trang web sẽ áp dụng bố cục cho máy tính.

## Bài tập
Bài tập cho bạn: Tạo một trang web đơn giản có thể đáp ứng với các kích thước màn hình khác nhau. Sử dụng Media Queries để áp dụng các kiểu dáng và bố cục khác nhau dựa trên chiều rộng màn hình. Ví dụ, bạn có thể tạo ra một trang web có:
- Bố cục một cột trên màn hình di động (chiều rộng < 768px)
- Bố cục hai cột trên màn hình máy tính bảng (chiều rộng từ 768px đến 1024px)
- Bố cục ba cột trên màn hình máy tính (chiều rộng > 1024px)
Hãy thử nghiệm và xem kết quả!