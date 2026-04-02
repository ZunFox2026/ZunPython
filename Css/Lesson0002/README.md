# Tìm hiểu về thuộc tính Overflow
## Giới thiệu
Thuộc tính `overflow` là một trong những thuộc tính quan trọng trong CSS, giúp chúng ta kiểm soát cách hiển thị nội dung vượt quá kích thước của một phần tử. Khi một phần tử có chiều cao hoặc chiều rộng cố định, nhưng nội dung bên trong lại quá lớn, thuộc tính `overflow` sẽ quyết định cách xử lý phần nội dung vượt quá. Trong bài này, chúng ta sẽ tìm hiểu về thuộc tính `overflow` và cách sử dụng nó trong thiết kế web.

## Lý thuyết
Thuộc tính `overflow` có thể nhận các giá trị sau:
- `visible`: Đây là giá trị mặc định, cho phép nội dung vượt quá kích thước của phần tử được hiển thị ra ngoài.
- `hidden`: Nội dung vượt quá kích thước của phần tử sẽ bị ẩn đi.
- `scroll`: Thêm thanh cuộn vào phần tử, cho phép người dùng cuộn lên xuống để xem nội dung vượt quá.
- `auto`: Tương tự như `scroll`, nhưng thanh cuộn chỉ xuất hiện khi có nội dung vượt quá kích thước của phần tử.
Ví dụ về sử dụng thuộc tính `overflow`:
```css
.example {
  width: 200px;
  height: 100px;
  overflow: scroll;
}
```
Trong ví dụ trên, phần tử có lớp `example` sẽ có chiều rộng là 200px, chiều cao là 100px, và thêm thanh cuộn nếu nội dung vượt quá kích thước này.

## Ví dụ
Để minh họa rõ hơn về cách sử dụng thuộc tính `overflow`, hãy xem xét ví dụ sau:
```css
.box {
  width: 300px;
  height: 200px;
  border: 1px solid black;
  overflow: auto;
}

.content {
  width: 350px;
  height: 250px;
  background-color: lightblue;
}
```
```html
<div class="box">
  <div class="content"></div>
</div>
```
Trong ví dụ này, phần tử `.box` có kích thước cố định và thuộc tính `overflow` được thiết lập là `auto`. Phần tử `.content` bên trong có kích thước lớn hơn `.box`. Khi chạy ví dụ này, bạn sẽ thấy thanh cuộn xuất hiện trong phần tử `.box` để người dùng có thể xem toàn bộ nội dung của phần tử `.content`.

## Bài tập
Bài tập tiếp theo là tạo một trang web đơn giản với một hộp có chiều rộng và chiều cao cố định, và thêm nội dung văn bản vào hộp này. Sử dụng thuộc tính `overflow` để kiểm soát cách hiển thị nội dung khi nó vượt quá kích thước của hộp. Hãy thử nghiệm với các giá trị khác nhau của thuộc tính `overflow` như `visible`, `hidden`, `scroll`, và `auto` để xem sự khác biệt.