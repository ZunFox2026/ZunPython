## Giới thiệu
Trong bài này, chúng ta sẽ tìm hiểu về cách tạo hiệu ứng Scrollbar tùy chỉnh. Scrollbar là một phần quan trọng trong giao diện người dùng của website, giúp người dùng có thể cuộn lên xuống hoặc sang trái phải để xem nội dung. Tuy nhiên, Scrollbar mặc định của trình duyệt có thể không phù hợp với thiết kế của website. Vì vậy, chúng ta cần phải tạo hiệu ứng Scrollbar tùy chỉnh để phù hợp với nhu cầu của mình.

## Lý thuyết
Để tạo hiệu ứng Scrollbar tùy chỉnh, chúng ta cần phải sử dụng CSS. Chúng ta có thể sử dụng các thuộc tính như `scrollbar-width`, `scrollbar-color`, `scrollbar-track-color` để tùy chỉnh Scrollbar. Ngoài ra, chúng ta cũng có thể sử dụng pseudo-element `::scrollbar` để tùy chỉnh Scrollbar.

Ví dụ, chúng ta có thể sử dụng CSS như sau:
```html
<div class="container">
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
  <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
  <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
</div>
```

```css
.container {
  width: 300px;
  height: 200px;
  overflow-y: scroll;
  scrollbar-width: thin;
  scrollbar-color: #666 #fff;
}

.container::-webkit-scrollbar {
  width: 10px;
  height: 10px;
}

.container::-webkit-scrollbar-track {
  background-color: #fff;
}

.container::-webkit-scrollbar-thumb {
  background-color: #666;
  border-radius: 10px;
}
```
Trong ví dụ trên, chúng ta đã tạo một container với chiều cao và chiều rộng cố định, và thêm thuộc tính `overflow-y: scroll` để tạo Scrollbar. Chúng ta cũng đã sử dụng pseudo-element `::scrollbar` để tùy chỉnh Scrollbar.

## Ví dụ
Chúng ta có thể tạo một trang web với hiệu ứng Scrollbar tùy chỉnh như sau:
```html
<html>
<head>
  <title>Hiệu ứng Scrollbar tùy chỉnh</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }
    
    .container {
      width: 500px;
      height: 300px;
      overflow-y: scroll;
      scrollbar-width: thin;
      scrollbar-color: #666 #fff;
    }
    
    .container::-webkit-scrollbar {
      width: 10px;
      height: 10px;
    }
    
    .container::-webkit-scrollbar-track {
      background-color: #fff;
    }
    
    .container::-webkit-scrollbar-thumb {
      background-color: #666;
      border-radius: 10px;
    }
  </style>
</head>
<body>
  <div class="container">
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
    <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
    <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
    <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
    <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
  </div>
</body>
</html>
```
Trong ví dụ trên, chúng ta đã tạo một trang web với hiệu ứng Scrollbar tùy chỉnh. Khi người dùng cuộn lên xuống, Scrollbar sẽ thay đổi màu sắc và kích thước.

## Bài tập
Bài tập của bạn là tạo một trang web với hiệu ứng Scrollbar tùy chỉnh. Bạn có thể sử dụng các thuộc tính như `scrollbar-width`, `scrollbar-color`, `scrollbar-track-color` để tùy chỉnh Scrollbar. Ngoài ra, bạn cũng có thể sử dụng pseudo-element `::scrollbar` để tùy chỉnh Scrollbar.

Yêu cầu:
- Tạo một trang web với chiều cao và chiều rộng cố định.
- Thêm thuộc tính `overflow-y: scroll` để tạo Scrollbar.
- Sử dụng pseudo-element `::scrollbar` để tùy chỉnh Scrollbar.
- Thay đổi màu sắc và kích thước của Scrollbar khi người dùng cuộn lên xuống.

Khi hoàn thành bài tập