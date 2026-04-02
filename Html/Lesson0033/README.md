# Tạo hiệu ứng loading
## Giới thiệu
Tạo hiệu ứng loading là một kỹ thuật được sử dụng để thông báo cho người dùng rằng trang web hoặc ứng dụng đang trong quá trình tải dữ liệu. Hiệu ứng này giúp cải thiện trải nghiệm người dùng và tạo sự chuyên nghiệp cho trang web hoặc ứng dụng. Trong bài này, chúng ta sẽ tìm hiểu về cách tạo hiệu ứng loading cơ bản bằng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng loading, chúng ta cần sử dụng các kỹ thuật CSS như animation, transform, và opacity. Chúng ta cũng có thể sử dụng HTML để tạo cấu trúc cho hiệu ứng loading. Một số thuộc tính CSS quan trọng để tạo hiệu ứng loading bao gồm:
- `animation`: Định nghĩa một animation cho phần tử.
- `transform`: Định nghĩa một biến dạng cho phần tử.
- `opacity`: Định nghĩa độ trong suốt cho phần tử.

Ví dụ, chúng ta có thể tạo một vòng tròn loading bằng cách sử dụng HTML và CSS như sau:
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
  animation: loading 1s linear infinite;
}

@keyframes loading {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
```
## Ví dụ
Chúng ta có thể tạo nhiều loại hiệu ứng loading khác nhau bằng cách sử dụng các kỹ thuật CSS khác nhau. Ví dụ, chúng ta có thể tạo một hiệu ứng loading dạng thanh tiến trình bằng cách sử dụng HTML và CSS như sau:
```html
<div class="loading-bar">
  <div class="loading-bar-inner"></div>
</div>
```
```css
.loading-bar {
  width: 100%;
  height: 10px;
  background-color: #ccc;
}

.loading-bar-inner {
  width: 0%;
  height: 100%;
  background-color: #666;
  animation: loading-bar 2s linear infinite;
}

@keyframes loading-bar {
  0% {
    width: 0%;
  }
  100% {
    width: 100%;
  }
}
```
## Bài tập
Để rèn luyện kỹ năng tạo hiệu ứng loading, bạn có thể thử tạo các loại hiệu ứng loading khác nhau bằng cách sử dụng các kỹ thuật CSS khác nhau. Ví dụ, bạn có thể thử tạo một hiệu ứng loading dạng hình vuông, hoặc một hiệu ứng loading dạng texto. Bạn cũng có thể thử tạo một hiệu ứng loading có thể được điều khiển bằng JavaScript. Hãy thử nghiệm và tìm hiểu các kỹ thuật CSS khác nhau để tạo ra các hiệu ứng loading độc đáo và thú vị.