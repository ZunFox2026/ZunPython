# Tìm hiểu về Media Queries
## Giới thiệu
Media Queries là một tính năng trong CSS cho phép chúng ta áp dụng các kiểu dáng khác nhau dựa trên các điều kiện cụ thể của thiết bị hoặc môi trường mà trang web đang được hiển thị. Điều này giúp chúng ta tạo ra các trang web đáp ứng (responsive) và có thể thích nghi với nhiều loại thiết bị và kích thước màn hình khác nhau.

## Lý thuyết
Media Queries sử dụng câu lệnh `@media` trong CSS để xác định các điều kiện mà chúng ta muốn áp dụng các kiểu dáng cụ thể. Các điều kiện này có thể bao gồm kích thước màn hình, độ phân giải, định hướng thiết bị (đứng hoặc nằm), và nhiều yếu tố khác. Ví dụ, chúng ta có thể sử dụng Media Queries để áp dụng một kiểu dáng khác nhau cho các thiết bị di động và máy tính bảng:
```css
@media (max-width: 768px) {
  /* Kiểu dáng cho thiết bị di động và máy tính bảng */
  body {
    font-size: 16px;
  }
}
```
Trong ví dụ trên, chúng ta đang áp dụng một kiểu dáng có kích thước phông chữ là 16px cho các thiết bị có chiều rộng màn hình tối đa là 768px.

## Ví dụ
Dưới đây là một ví dụ minh họa cách sử dụng Media Queries để tạo ra một trang web đáp ứng:
```css
/* Kiểu dáng mặc định */
body {
  font-size: 18px;
  background-color: #f2f2f2;
}

/* Kiểu dáng cho thiết bị di động */
@media (max-width: 480px) {
  body {
    font-size: 14px;
    background-color: #ccc;
  }
}

/* Kiểu dáng cho máy tính bảng */
@media (min-width: 481px) and (max-width: 768px) {
  body {
    font-size: 16px;
    background-color: #aaa;
  }
}

/* Kiểu dáng cho máy tính */
@media (min-width: 769px) {
  body {
    font-size: 18px;
    background-color: #fff;
  }
}
```
Trong ví dụ này, chúng ta đang áp dụng các kiểu dáng khác nhau dựa trên kích thước màn hình của thiết bị.

## Bài tập
Bài tập này yêu cầu bạn tạo ra một trang web đơn giản có thể đáp ứng với các loại thiết bị khác nhau. Hãy tạo ra một file HTML và một file CSS, sau đó sử dụng Media Queries để áp dụng các kiểu dáng khác nhau dựa trên kích thước màn hình của thiết bị. Ví dụ, bạn có thể tạo ra một trang web có các phần tử sau:
- Tiêu đề (header)
- Nội dung (content)
- Chân trang (footer)
Hãy sử dụng Media Queries để áp dụng các kiểu dáng khác nhau cho các phần tử này dựa trên kích thước màn hình của thiết bị.