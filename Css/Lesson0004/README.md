# Tìm hiểu về thuộc tính Overflow
## Giới thiệu
Trong thiết kế web, chúng ta thường gặp phải tình huống mà nội dung của một phần tử vượt quá kích thước của nó. Để giải quyết vấn đề này, thuộc tính `overflow` được sử dụng. Thuộc tính `overflow` cho phép chúng ta kiểm soát cách hiển thị nội dung khi nó vượt quá kích thước của phần tử chứa nó. Trong bài viết này, chúng ta sẽ tìm hiểu về thuộc tính `overflow` và cách sử dụng nó trong CSS.

## Lý thuyết
Thuộc tính `overflow` có 4 giá trị chính: `visible`, `hidden`, `scroll`, và `auto`. Mỗi giá trị sẽ quyết định cách nội dung vượt quá sẽ được hiển thị.
- `visible`: Đây là giá trị mặc định của thuộc tính `overflow`. Khi sử dụng `visible`, nội dung vượt quá sẽ được hiển thị ra ngoài phần tử chứa nó.
- `hidden`: Giá trị `hidden` sẽ ẩn đi nội dung vượt quá, và người dùng sẽ không thể xem nội dung đó.
- `scroll`: Giá trị `scroll` sẽ hiển thị thanh cuộn cho phép người dùng cuộn để xem nội dung vượt quá.
- `auto`: Giá trị `auto` sẽ tự động thêm thanh cuộn nếu nội dung vượt quá kích thước của phần tử chứa nó.

Ví dụ về sử dụng thuộc tính `overflow` trong CSS:
```css
.div-1 {
  width: 200px;
  height: 100px;
  overflow: hidden;
}

.div-2 {
  width: 200px;
  height: 100px;
  overflow: scroll;
}

.div-3 {
  width: 200px;
  height: 100px;
  overflow: auto;
}
```

## Ví dụ
Để minh họa rõ hơn về cách sử dụng thuộc tính `overflow`, hãy xem xét ví dụ sau:
Giả sử chúng ta có một phần tử `div` với chiều rộng và chiều cao cố định, và chúng ta muốn kiểm soát cách nội dung vượt quá sẽ được hiển thị.
```css
#example {
  width: 300px;
  height: 200px;
  background-color: #f2f2f2;
  padding: 20px;
  overflow: auto;
}
```
Nội dung của phần tử `#example` sẽ được hiển thị với thanh cuộn nếu nội dung vượt quá kích thước của nó.

## Bài tập
Bài tập này sẽ giúp bạn thực hành sử dụng thuộc tính `overflow` trong thiết kế web.
Yêu cầu:
- Tạo một trang web đơn giản với một phần tử `div` có chiều rộng và chiều cao cố định.
- Thêm nội dung vào phần tử `div` để nó vượt quá kích thước của phần tử chứa nó.
- Sử dụng thuộc tính `overflow` để kiểm soát cách nội dung vượt quá sẽ được hiển thị.
- Thử nghiệm với các giá trị khác nhau của thuộc tính `overflow` (visible, hidden, scroll, auto) để xem sự khác biệt.