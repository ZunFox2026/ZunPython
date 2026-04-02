# Tạo hiệu ứng Scrollbar tùy chỉnh
## Giới thiệu
Trong thiết kế web, thanh cuộn (Scrollbar) là một phần quan trọng giúp người dùng di chuyển qua nội dung trên trang web. Tuy nhiên, thanh cuộn mặc định của trình duyệt thường không đẹp và không phù hợp với thiết kế của trang web. Vì vậy, việc tạo hiệu ứng Scrollbar tùy chỉnh là cần thiết để mang lại trải nghiệm người dùng tốt hơn. Trong bài này, chúng ta sẽ tìm hiểu cách tạo hiệu ứng Scrollbar tùy chỉnh bằng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng Scrollbar tùy chỉnh, chúng ta cần sử dụng các thuộc tính CSS sau:
- `::-webkit-scrollbar`: chọn phần tử thanh cuộn
- `::-webkit-scrollbar-thumb`: chọn phần tử nút cuộn
- `::-webkit-scrollbar-track`: chọn phần tử đường ray cuộn
- `::-webkit-scrollbar-button`: chọn phần tử nút cuộn lên hoặc xuống
- `::-webkit-scrollbar-corner`: chọn phần tử góc của thanh cuộn

Chúng ta cũng cần sử dụng các thuộc tính CSS khác như `width`, `height`, `background-color`, `border-radius` để tùy chỉnh hình thức của thanh cuộn.

Ví dụ:
```html
<div class="scrollbar">
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
  <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
  <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
</div>
```

```css
.scrollbar {
  width: 300px;
  height: 200px;
  overflow-y: scroll;
}

.scrollbar::-webkit-scrollbar {
  width: 10px;
}

.scrollbar::-webkit-scrollbar-thumb {
  background-color: #ccc;
  border-radius: 10px;
}

.scrollbar::-webkit-scrollbar-track {
  background-color: #eee;
}
```

## Ví dụ
Trong ví dụ trên, chúng ta đã tạo một phần tử `div` với lớp `scrollbar` và thêm nội dung vào đó. Sau đó, chúng ta sử dụng CSS để tùy chỉnh hình thức của thanh cuộn. Chúng ta đã chọn phần tử thanh cuộn, nút cuộn và đường ray cuộn, và thêm các thuộc tính CSS để thay đổi hình thức của chúng.

Kết quả là một thanh cuộn tùy chỉnh với nút cuộn màu xám và đường ray cuộn màu sáng.

## Bài tập
Bài tập cho bạn:
- Tạo một trang web với một phần tử `div` có lớp `scrollbar`
- Thêm nội dung vào phần tử `div` để tạo thanh cuộn
- Sử dụng CSS để tùy chỉnh hình thức của thanh cuộn, bao gồm:
 * Thay đổi màu sắc của nút cuộn và đường ray cuộn
 * Thay đổi kích thước của thanh cuộn
 * Thêm hiệu ứng hover cho nút cuộn
- Thử nghiệm với các thuộc tính CSS khác để tạo ra các hiệu ứng khác nhau.