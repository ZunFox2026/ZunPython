# Tạo hiệu ứng Parallax
## Giới thiệu
Hiệu ứng Parallax là một kỹ thuật được sử dụng trong thiết kế web để tạo ra một trải nghiệm người dùng thú vị và hấp dẫn. Nó cho phép các lớp nền và các phần tử khác di chuyển với tốc độ khác nhau khi người dùng cuộn trang, tạo ra một hiệu ứng sâu và thú vị. Trong bài này, chúng ta sẽ tìm hiểu về cách tạo hiệu ứng Parallax sử dụng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng Parallax, chúng ta cần sử dụng thuộc tính `background-attachment` trong CSS. Thuộc tính này cho phép chúng ta đặt một hình nền cố định hoặc di chuyển cùng với nội dung của trang. Ngoài ra, chúng ta cũng cần sử dụng thuộc tính `background-size` để đặt kích thước của hình nền và thuộc tính `background-position` để đặt vị trí của hình nền.

Ví dụ, chúng ta có thể tạo một lớp nền với hiệu ứng Parallax như sau:
```html
<div class="nen"></div>
```
```css
.nen {
  background-image: url('nen.jpg');
  background-attachment: fixed;
  background-size: cover;
  background-position: center;
  height: 100vh;
  width: 100vw;
}
```
Trong ví dụ trên, lớp nền có hiệu ứng Parallax sẽ di chuyển cùng với nội dung của trang khi người dùng cuộn.

## Ví dụ
Chúng ta có thể tạo một trang web với hiệu ứng Parallax như sau:
```html
<div class="nen"></div>
<div class="noi-dung">
  <h1>Tạo hiệu ứng Parallax</h1>
  <p>Hiệu ứng Parallax là một kỹ thuật được sử dụng trong thiết kế web để tạo ra một trải nghiệm người dùng thú vị và hấp dẫn.</p>
</div>
```
```css
.nen {
  background-image: url('nen.jpg');
  background-attachment: fixed;
  background-size: cover;
  background-position: center;
  height: 100vh;
  width: 100vw;
  position: absolute;
  top: 0;
  left: 0;
}

.noi-dung {
  position: relative;
  z-index: 1;
  padding: 20px;
}
```
Trong ví dụ trên, lớp nền có hiệu ứng Parallax sẽ di chuyển cùng với nội dung của trang khi người dùng cuộn, tạo ra một hiệu ứng sâu và thú vị.

## Bài tập
Bài tập của bạn là tạo một trang web với hiệu ứng Parallax sử dụng HTML và CSS. Bạn cần tạo một lớp nền với hiệu ứng Parallax và một lớp nội dung với văn bản và hình ảnh. Bạn cũng cần sử dụng thuộc tính `background-attachment` và `background-size` để đặt hình nền và kích thước của hình nền. Hãy thử nghiệm với các thuộc tính khác nhau để tạo ra một hiệu ứng Parallax thú vị và hấp dẫn.