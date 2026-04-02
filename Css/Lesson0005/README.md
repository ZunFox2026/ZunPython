# Tìm hiểu về Outline
## Giới thiệu
Outline là một thuộc tính trong CSS giúp tạo ra một đường viền xung quanh một phần tử HTML. Đường viền này khác với border ở chỗ nó không chiếm thêm không gian và không ảnh hưởng đến kích thước của phần tử. Outline thường được sử dụng để tạo ra hiệu ứng nhấn hoặc để chỉ ra phần tử đang được tập trung.

## Lý thuyết
Để sử dụng outline, bạn có thể thêm thuộc tính `outline` vào phần tử mong muốn. Thuộc tính này có thể nhận một hoặc nhiều giá trị, bao gồm:
- `outline-width`: Chiều rộng của đường viền
- `outline-style`: Kiểu của đường viền (solid, dashed, dotted, v.v.)
- `outline-color`: Màu sắc của đường viền

Ví dụ:
```css
.example {
  outline: 2px solid #000;
}
```
Trong ví dụ trên, phần tử có class `example` sẽ có một đường viền đen rắn với chiều rộng 2 pixel.

## Ví dụ
Khi bạn muốn tạo ra một hiệu ứng nhấn cho một nút bấm, bạn có thể sử dụng outline như sau:
```css
.button {
  background-color: #fff;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
}

.button:focus {
  outline: 2px solid #007bff;
}
```
Trong ví dụ này, khi nút bấm được tập trung (focus), nó sẽ có một đường viền xanh với chiều rộng 2 pixel.

## Bài tập
Bài tập: Tạo một phần tử div có chiều rộng và chiều cao là 100 pixel, nền màu xám, và có một đường viền màu đen rắn với chiều rộng 1 pixel khi được di chuột qua (hover).
```css
.div-hover {
  width: 100px;
  height: 100px;
  background-color: #ccc;
}

.div-hover:hover {
  outline: 1px solid #000;
}
```
Bằng cách sử dụng thuộc tính outline, bạn có thể dễ dàng tạo ra các hiệu ứng nhấn hoặc chỉ ra phần tử đang được tập trung mà không cần phải lo lắng về việc chiếm thêm không gian. Hãy thử nghiệm với các giá trị và kiểu khác nhau của thuộc tính outline để tạo ra các hiệu ứng độc đáo cho trang web của bạn.