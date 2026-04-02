# Tạo hiệu ứng loading
## Giới thiệu
Hiệu ứng loading là một phần quan trọng trong việc tạo ra trải nghiệm người dùng tốt trên website. Khi người dùng yêu cầu tải một trang hoặc một phần nội dung, hiệu ứng loading giúp họ hiểu rằng website đang xử lý yêu cầu của họ. Trong bài này, chúng ta sẽ tìm hiểu cách tạo hiệu ứng loading đơn giản bằng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng loading, chúng ta có thể sử dụng các thuộc tính CSS như `animation`, `keyframes` để tạo ra các hiệu ứng chuyển động. Chúng ta cũng có thể sử dụng HTML để tạo ra cấu trúc cơ bản của hiệu ứng loading.

Ví dụ, chúng ta có thể sử dụng mã HTML sau để tạo ra một vòng tròn loading:
```html
<div class="loading">
  <div class="loading-circle"></div>
</div>
```
Và sử dụng mã CSS sau để tạo ra hiệu ứng loading:
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
  border-top-color: #666;
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
Dưới đây là một ví dụ cụ thể về cách tạo hiệu ứng loading bằng HTML và CSS:
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
  border-top-color: #666;
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
Khi chạy mã này, chúng ta sẽ thấy một vòng tròn loading xuất hiện ở giữa màn hình.

## Bài tập
Bài tập cho bạn là tạo một hiệu ứng loading khác nhau bằng cách thay đổi mã CSS. Ví dụ, bạn có thể tạo một hiệu ứng loading hình vuông, hoặc một hiệu ứng loading hình elip. Hãy thử nghiệm và tìm ra cách tạo ra hiệu ứng loading mà bạn muốn.

Ngoài ra, bạn cũng có thể thử thêm các hiệu ứng khác vào hiệu ứng loading, như hiệu ứng bóng hoặc hiệu ứng ánh sáng. Hãy sử dụng các thuộc tính CSS như `box-shadow` hoặc `linear-gradient` để tạo ra các hiệu ứng này.