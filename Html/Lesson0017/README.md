# Tạo hiệu ứng Scrollbar tùy chỉnh
## Giới thiệu
Trong thiết kế web, thanh cuộn (Scrollbar) là một phần quan trọng giúp người dùng điều hướng và xem nội dung trên trang web. Tuy nhiên, thanh cuộn mặc định có thể không phù hợp với thiết kế của trang web. Vì vậy, tạo hiệu ứng Scrollbar tùy chỉnh là một kỹ thuật quan trọng giúp tăng trải nghiệm người dùng và tính thẩm mỹ cho trang web. Bài viết này sẽ hướng dẫn cách tạo hiệu ứng Scrollbar tùy chỉnh bằng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng Scrollbar tùy chỉnh, chúng ta cần sử dụng các thuộc tính CSS sau:
- `::-webkit-scrollbar`: chọn phần tử thanh cuộn
- `::-webkit-scrollbar-track`: chọn phần đường dẫn của thanh cuộn
- `::-webkit-scrollbar-thumb`: chọn phần tay cầm của thanh cuộn
- `::-webkit-scrollbar-button`: chọn phần nút bấm của thanh cuộn
- `::-webkit-scrollbar-corner`: chọn phần góc của thanh cuộn
- `::-webkit-resizer`: chọn phần thay đổi kích thước của thanh cuộn

Ví dụ:
```html
<div class="scrollbar">
  <!-- Nội dung -->
</div>
```
```css
.scrollbar {
  height: 300px;
  overflow-y: auto;
}

.scrollbar::-webkit-scrollbar {
  width: 10px;
}

.scrollbar::-webkit-scrollbar-track {
  background-color: #f5f5f5;
}

.scrollbar::-webkit-scrollbar-thumb {
  background-color: #ccc;
  border-radius: 5px;
}

.scrollbar::-webkit-scrollbar-thumb:hover {
  background-color: #aaa;
}
```
## Ví dụ
Tạo một trang web đơn giản với một khu vực nội dung có thanh cuộn tùy chỉnh:
```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .content {
      height: 300px;
      overflow-y: auto;
      width: 500px;
      background-color: #f0f0f0;
      padding: 20px;
    }

    .content::-webkit-scrollbar {
      width: 10px;
    }

    .content::-webkit-scrollbar-track {
      background-color: #f5f5f5;
    }

    .content::-webkit-scrollbar-thumb {
      background-color: #ccc;
      border-radius: 5px;
    }

    .content::-webkit-scrollbar-thumb:hover {
      background-color: #aaa;
    }
  </style>
</head>
<body>
  <div class="content">
    <!-- Nội dung -->
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
  </div>
</body>
</html>
```
## Bài tập
Tạo một trang web với một khu vực nội dung có thanh cuộn tùy chỉnh. Khu vực nội dung có chiều rộng là 800px, chiều cao là 600px. Thanh cuộn có chiều rộng là 15px, màu nền là #f0f0f0, màu tay cầm là #999. Khi di chuột qua tay cầm, màu tay cầm sẽ đổi thành #666. Hãy viết mã HTML và CSS để tạo trang web này.