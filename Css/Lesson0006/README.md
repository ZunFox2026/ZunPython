# Tạo hình dạng hình học với CSS
## Giới thiệu
Tạo hình dạng hình học với CSS là một kỹ thuật cơ bản trong thiết kế web, giúp bạn tạo ra các hình dạng khác nhau như hình tròn, hình vuông, hình chữ nhật, hình tam giác, v.v. Trong bài này, chúng ta sẽ tìm hiểu cách tạo hình dạng hình học với CSS và các ví dụ minh họa.

## Lý thuyết
Để tạo hình dạng hình học với CSS, bạn có thể sử dụng các thuộc tính sau:
- `width` và `height` để định nghĩa kích thước của hình dạng.
- `border-radius` để tạo hình tròn hoặc hình elip.
- `transform` để xoay, lật hoặc thay đổi hình dạng.
- `clip-path` để cắt hình dạng thành các hình dạng khác nhau.

Ví dụ, bạn có thể tạo một hình tròn bằng cách sử dụng thuộc tính `border-radius` như sau:
```css
.hinh-tron {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background-color: #f00;
}
```
## Ví dụ
Dưới đây là một số ví dụ minh họa cách tạo hình dạng hình học với CSS:
- Tạo hình vuông:
```css
.hinh-vuong {
  width: 100px;
  height: 100px;
  background-color: #0f0;
}
```
- Tạo hình chữ nhật:
```css
.hinh-chu-nhat {
  width: 200px;
  height: 100px;
  background-color: #00f;
}
```
- Tạo hình tam giác:
```css
.hinh-tam-giac {
  width: 0;
  height: 0;
  border-left: 50px solid transparent;
  border-right: 50px solid transparent;
  border-bottom: 100px solid #ff0;
}
```
## Bài tập
Bài tập cho bạn:
- Tạo một hình dạng hình học với CSS để thể hiện một chiếc ô tô, bao gồm các hình dạng như hình chữ nhật, hình tròn, hình tam giác.
- Sử dụng thuộc tính `transform` để tạo hiệu ứng xoay hoặc lật cho hình dạng.
- Sử dụng thuộc tính `clip-path` để cắt hình dạng thành các hình dạng khác nhau.
- Tạo một trang web đơn giản để展示 các hình dạng hình học mà bạn đã tạo.