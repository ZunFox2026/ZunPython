# Tạo hình nền động
## Giới thiệu
Bài học này sẽ hướng dẫn bạn cách tạo hình nền động bằng CSS. Hình nền động là một kỹ thuật giúp tạo ra hiệu ứng chuyển động trên hình nền của trang web, giúp tăng thêm sự thu hút và thú vị cho người dùng. Với CSS, bạn có thể dễ dàng tạo ra các hiệu ứng hình nền động mà không cần sử dụng đến JavaScript.

## Lý thuyết
Để tạo hình nền động, bạn cần sử dụng thuộc tính `background` và `animation` trong CSS. Thuộc tính `background` giúp bạn thiết lập hình nền cho trang web, trong khi thuộc tính `animation` giúp tạo ra hiệu ứng chuyển động. Bạn có thể sử dụng các giá trị như `linear-gradient`, `radial-gradient` để tạo ra các hình nền động.

Ví dụ:
```css
body {
  background: linear-gradient(to right, #f00, #0f0, #00f);
  background-size: 1000px 1000px;
  animation: move 10s ease infinite;
}

@keyframes move {
  0% {
    background-position: 0% 0%;
  }
  100% {
    background-position: 100% 100%;
  }
}
```
Trong ví dụ trên, chúng ta tạo ra một hình nền động bằng cách sử dụng `linear-gradient` và `animation`. Thuộc tính `background-size` giúp chúng ta thiết lập kích thước của hình nền, trong khi thuộc tính `animation` giúp tạo ra hiệu ứng chuyển động.

## Ví dụ
Một ví dụ khác về tạo hình nền động là sử dụng `radial-gradient` để tạo ra một hiệu ứng hình nền động dạng tròn.

Ví dụ:
```css
body {
  background: radial-gradient(at 50% 50%, #f00, #0f0, #00f);
  background-size: 1000px 1000px;
  animation: move 10s ease infinite;
}

@keyframes move {
  0% {
    background-position: 0% 0%;
  }
  100% {
    background-position: 100% 100%;
  }
}
```
Trong ví dụ này, chúng ta sử dụng `radial-gradient` để tạo ra một hình nền động dạng tròn.

## Bài tập
Bài tập cho bạn là tạo ra một hình nền động bằng cách sử dụng `linear-gradient` và `animation`. Hãy thử nghiệm với các giá trị khác nhau của thuộc tính `background` và `animation` để tạo ra các hiệu ứng hình nền động khác nhau.

Một số gợi ý:

* Thử sử dụng `repeating-linear-gradient` để tạo ra một hình nền động dạng lưới.
* Thử sử dụng `repeating-radial-gradient` để tạo ra một hình nền động dạng tròn lặp lại.
* Thử thay đổi giá trị của thuộc tính `background-size` và `animation` để tạo ra các hiệu ứng hình nền động khác nhau.