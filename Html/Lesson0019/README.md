# Tạo hiệu ứng Loading
## Giới thiệu
Trong quá trình phát triển website, việc tạo hiệu ứng loading là một bước quan trọng để cải thiện trải nghiệm người dùng. Hiệu ứng loading giúp người dùng biết rằng trang web đang tải dữ liệu và chờ đợi thông tin. Trong bài này, chúng ta sẽ tìm hiểu cách tạo hiệu ứng loading cơ bản bằng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng loading, chúng ta cần sử dụng các kỹ thuật sau:
- Tạo một phần tử chứa hiệu ứng loading bằng HTML.
- Sử dụng CSS để tạo kiểu và hiệu ứng cho phần tử này.
- Sử dụng thuộc tính `animation` trong CSS để tạo hiệu ứng động.
- Sử dụng thuộc tính `keyframes` để định nghĩa các khung hình của hiệu ứng.

Ví dụ về HTML và CSS cơ bản:
```html
<div class="loading"></div>
```
```css
.loading {
  width: 50px;
  height: 50px;
  border: 5px solid #ccc;
  border-top: 5px solid #333;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
```
Đây là một ví dụ cơ bản về hiệu ứng loading quay tròn.

## Ví dụ
Chúng ta có thể tạo nhiều loại hiệu ứng loading khác nhau bằng cách thay đổi các thuộc tính trong CSS. Ví dụ, chúng ta có thể tạo hiệu ứng loading tăng dần:
```html
<div class="loading-bar"></div>
```
```css
.loading-bar {
  width: 100px;
  height: 10px;
  background-color: #ccc;
  animation: increase 2s linear infinite;
}

@keyframes increase {
  0% {
    width: 0;
  }
  100% {
    width: 100px;
  }
}
```
Hoặc tạo hiệu ứng loading pulse:
```html
<div class="loading-pulse"></div>
```
```css
.loading-pulse {
  width: 50px;
  height: 50px;
  background-color: #ccc;
  border-radius: 50%;
  animation: pulse 1s linear infinite;
}

@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}
```
Các ví dụ trên chỉ là một số cách cơ bản để tạo hiệu ứng loading. Chúng ta có thể tạo nhiều hiệu ứng khác nhau bằng cách sử dụng các thuộc tính và kỹ thuật khác nhau trong CSS.

## Bài tập
Bài tập cho bạn là tạo một hiệu ứng loading mới bằng cách sử dụng các kỹ thuật trên. Hãy thử tạo hiệu ứng loading theo ý tưởng của mình, ví dụ như hiệu ứng loading xoay, hiệu ứng loading tăng dần, hoặc hiệu ứng loading pulse. Sử dụng các thuộc tính và kỹ thuật trong CSS để tạo hiệu ứng động và đẹp mắt. Sau khi hoàn thành, hãy chia sẻ kết quả của mình với mọi người để học hỏi và cải thiện kỹ năng.