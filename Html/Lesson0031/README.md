# Tạo hiệu ứng loading
## Giới thiệu
Hiệu ứng loading là một phần quan trọng trong thiết kế web, giúp người dùng biết rằng trang web đang tải dữ liệu hoặc thực hiện một hành động nào đó. Trong bài này, chúng ta sẽ tìm hiểu cách tạo hiệu ứng loading cơ bản bằng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng loading, chúng ta có thể sử dụng các kỹ thuật sau:
- Sử dụng ảnh động (gif) hoặc video để tạo hiệu ứng loading.
- Sử dụng CSS để tạo hiệu ứng động, chẳng hạn như chuyển động, thay đổi kích thước, màu sắc.
- Sử dụng JavaScript để kiểm soát hiệu ứng loading, chẳng hạn như hiển thị hoặc ẩn hiệu ứng loading khi trang web tải xong.

Ví dụ về tạo hiệu ứng loading bằng CSS:
```html
<div class="loading">
  <div class="loading-circle"></div>
</div>
```
```css
.loading {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.loading-circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: 5px solid #ccc;
  border-top: 5px solid #666;
  animation: rotate 1s linear infinite;
}

@keyframes rotate {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
```
## Ví dụ
Chúng ta có thể tạo hiệu ứng loading đơn giản bằng cách sử dụng CSS như sau:
```html
<div class="loading-example">
  <div class="loading-example-circle"></div>
</div>
```
```css
.loading-example {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.loading-example-circle {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  border: 3px solid #ccc;
  border-top: 3px solid #666;
  animation: rotate-example 1s linear infinite;
}

@keyframes rotate-example {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
```
## Bài tập
Bài tập: Tạo hiệu ứng loading bằng cách sử dụng ảnh động (gif) và CSS. Yêu cầu:
- Tạo một trang web có một nút tải dữ liệu.
- Khi người dùng click vào nút, hiển thị hiệu ứng loading.
- Sau 2 giây, ẩn hiệu ứng loading và hiển thị thông báo "Dữ liệu đã được tải xong".
- Sử dụng CSS để tạo hiệu ứng động cho nút tải dữ liệu.
- Sử dụng JavaScript để kiểm soát hiệu ứng loading và hiển thị thông báo.