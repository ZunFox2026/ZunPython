# Tìm hiểu về Shadow
## Giới thiệu
Trong thiết kế web, Shadow (bóng) là một hiệu ứng quan trọng giúp tạo ra độ sâu và chiều cao cho các элемент trên trang web. Nó giúp thu hút sự chú ý của người dùng và tạo ra một giao diện người dùng đẹp mắt. Trong bài viết này, chúng ta sẽ tìm hiểu về Shadow trong CSS và cách sử dụng nó để tạo ra các hiệu ứng bóng khác nhau.

## Lý thuyết
Shadow trong CSS được tạo ra bằng cách sử dụng thuộc tính `box-shadow`. Thuộc tính này có thể nhận một hoặc nhiều giá trị, mỗi giá trị bao gồm các thông số sau:
- `offset-x`: khoảng cách giữa bóng và phần tử theo trục x
- `offset-y`: khoảng cách giữa bóng và phần tử theo trục y
- `blur-radius`: bán kính mờ của bóng
- `spread-radius`: bán kính lan tỏa của bóng
- `color`: màu của bóng

Ví dụ:
```css
.box {
  box-shadow: 10px 10px 5px rgba(0, 0, 0, 0.2);
}
```
Trong ví dụ trên, bóng sẽ được tạo ra với khoảng cách 10px theo trục x và y, bán kính mờ 5px, và màu đen với độ trong suốt 0.2.

## Ví dụ
Để minh họa cách sử dụng Shadow, hãy xem xét ví dụ sau:
```css
.card {
  width: 200px;
  height: 100px;
  background-color: #f0f0f0;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  padding: 20px;
}
```
Trong ví dụ này, chúng ta tạo ra một thẻ `.card` với bóng mờ xung quanh, tạo ra một hiệu ứng đẹp mắt và hiện đại.

## Bài tập
Để thực hành sử dụng Shadow, hãy thực hiện các bài tập sau:
- Tạo ra một phần tử div với bóng mờ màu xám xung quanh.
- Tạo ra một nút bấm với bóng mờ màu xanh đậm khi di chuột qua.
- Tạo ra một hình ảnh với bóng mờ màu đen khi di chuột qua.

Bằng cách thực hành và thử nghiệm với các giá trị khác nhau của thuộc tính `box-shadow`, bạn có thể tạo ra các hiệu ứng bóng đa dạng và đẹp mắt cho trang web của mình.