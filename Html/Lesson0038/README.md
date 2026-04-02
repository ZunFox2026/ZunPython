## Giới thiệu
Tạo hiệu ứng loading là một kỹ thuật được sử dụng trong thiết kế web để tạo ra một trải nghiệm người dùng tốt hơn. Khi người dùng chờ đợi một trang web hoặc một phần của trang web được tải, hiệu ứng loading sẽ giúp họ biết rằng trang web đang trong quá trình tải và sẽ sớm sẵn sàng. Trong bài này, chúng ta sẽ tìm hiểu về cách tạo hiệu ứng loading bằng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng loading, chúng ta sẽ sử dụng kết hợp giữa HTML và CSS. HTML sẽ được sử dụng để tạo cấu trúc của hiệu ứng loading, trong khi CSS sẽ được sử dụng để tạo kiểu và hoạt ảnh cho hiệu ứng. Chúng ta sẽ sử dụng các thuộc tính CSS như `animation`, `keyframes` để tạo ra hiệu ứng loading.

Ví dụ về cấu trúc HTML cho hiệu ứng loading:
```html
<div class="loading">
  <div class="loading-bar"></div>
</div>
```
Ví dụ về CSS cho hiệu ứng loading:
```css
.loading {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.loading-bar {
  width: 50px;
  height: 50px;
  border: 8px solid #ccc;
  border-top: 8px solid #333;
  border-radius: 50%;
  animation: rotate 2s linear infinite;
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
Trong ví dụ trên, chúng ta đã tạo một hiệu ứng loading với một thanh tròn đang quay.

## Ví dụ
Dưới đây là ví dụ về cách sử dụng hiệu ứng loading trong một trang web:
```html
<html>
<head>
  <title>Hiệu ứng loading</title>
  <style>
    .loading {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }

    .loading-bar {
      width: 50px;
      height: 50px;
      border: 8px solid #ccc;
      border-top: 8px solid #333;
      border-radius: 50%;
      animation: rotate 2s linear infinite;
    }

    @keyframes rotate {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }
  </style>
</head>
<body>
  <div class="loading">
    <div class="loading-bar"></div>
  </div>
</body>
</html>
```
Khi chạy ví dụ trên, bạn sẽ thấy một hiệu ứng loading với một thanh tròn đang quay.

## Bài tập
Bài tập cho bạn là tạo một hiệu ứng loading với một hình dạng khác, chẳng hạn như một hình vuông hoặc một hình tam giác. Bạn cũng có thể thêm màu sắc và kiểu dáng khác nhau cho hiệu ứng loading. Hãy thử nghiệm và tạo ra một hiệu ứng loading độc đáo và thú vị.