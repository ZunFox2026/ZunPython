# Tạo hiệu ứng tương tác
## Giới thiệu
Trong thiết kế web, việc tạo ra các hiệu ứng tương tác là rất quan trọng để thu hút người dùng và tạo ra trải nghiệm người dùng tốt hơn. Hiệu ứng tương tác có thể là thay đổi màu sắc, kích thước, hình dạng,... của các phần tử trên trang web khi người dùng tương tác với chúng. Trong bài này, chúng ta sẽ tìm hiểu cách tạo ra các hiệu ứng tương tác bằng HTML và CSS.

## Lý thuyết
Để tạo ra hiệu ứng tương tác, chúng ta có thể sử dụng các thuộc tính CSS như `:hover`, `:active`, `:focus`,... Những thuộc tính này cho phép chúng ta định nghĩa các kiểu dáng khác nhau cho các phần tử khi người dùng tương tác với chúng. Ví dụ, chúng ta có thể sử dụng `:hover` để thay đổi màu sắc của một nút bấm khi người dùng di chuột qua nó.
```html
<button class="nut-bam">Nhấp vào đây</button>
```
```css
.nut-bam {
  background-color: #ccc;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.nut-bam:hover {
  background-color: #aaa;
}
```
Trong ví dụ trên, chúng ta đã định nghĩa một nút bấm với lớp `nut-bam`. Khi người dùng di chuột qua nút bấm, lớp `:hover` sẽ được kích hoạt và thay đổi màu sắc của nút bấm.

## Ví dụ
Chúng ta có thể tạo ra nhiều hiệu ứng tương tác khác nhau bằng cách kết hợp các thuộc tính CSS và các thuộc tính khác. Ví dụ, chúng ta có thể tạo ra một hiệu ứng tương tác cho một hình ảnh khi người dùng di chuột qua nó.
```html
<img class="hinh-anh" src="hinh-anh.jpg" alt="Hình ảnh">
```
```css
.hinh-anh {
  width: 300px;
  height: 200px;
  border: 1px solid #ccc;
  border-radius: 10px;
  transition: all 0.5s ease-in-out;
}

.hinh-anh:hover {
  transform: scale(1.1);
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}
```
Trong ví dụ trên, chúng ta đã định nghĩa một hình ảnh với lớp `hinh-anh`. Khi người dùng di chuột qua hình ảnh, lớp `:hover` sẽ được kích hoạt và thay đổi kích thước và tạo bóng cho hình ảnh.

## Bài tập
Bài tập này yêu cầu bạn tạo ra một trang web đơn giản với một nút bấm và một hình ảnh. Khi người dùng di chuột qua nút bấm, màu sắc của nút bấm sẽ thay đổi. Khi người dùng di chuột qua hình ảnh, kích thước và bóng của hình ảnh sẽ thay đổi. Hãy sử dụng các thuộc tính CSS như `:hover`, `:active`, `:focus`,... để tạo ra các hiệu ứng tương tác.