# Tạo hiệu ứng Parallax
## Giới thiệu
Hiệu ứng Parallax là một kỹ thuật được sử dụng trong thiết kế web để tạo ra một trải nghiệm người dùng thú vị và hấp dẫn. Hiệu ứng này cho phép các phần tử trên trang web di chuyển với tốc độ khác nhau khi người dùng cuộn chuột, tạo ra một cảm giác về chiều sâu và không gian. Trong bài học này, chúng ta sẽ tìm hiểu cách tạo hiệu ứng Parallax bằng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng Parallax, chúng ta cần sử dụng thuộc tính `background-attachment` trong CSS. Thuộc tính này cho phép chúng ta gắn một hình nền vào một phần tử và quyết định cách hình nền đó sẽ di chuyển khi người dùng cuộn chuột. Giá trị `fixed` của thuộc tính `background-attachment` sẽ giữ hình nền tại một vị trí cố định, trong khi giá trị `scroll` sẽ di chuyển hình nền cùng với phần tử khi người dùng cuộn chuột.

Ví dụ về cách sử dụng thuộc tính `background-attachment`:
```html
<div class="parallax">
  <div class="parallax-layer" style="background-image: url('layer1.jpg'); background-attachment: fixed;"></div>
  <div class="parallax-layer" style="background-image: url('layer2.jpg'); background-attachment: scroll;"></div>
</div>
```
```css
.parallax {
  height: 100vh;
  overflow-y: scroll;
}

.parallax-layer {
  height: 100vh;
  background-size: cover;
  background-position: center;
}
```
Trong ví dụ trên, lớp `parallax-layer` đầu tiên sẽ giữ hình nền cố định khi người dùng cuộn chuột, trong khi lớp thứ hai sẽ di chuyển cùng với phần tử.

## Ví dụ
Dưới đây là một ví dụ hoàn chỉnh về cách tạo hiệu ứng Parallax:
```html
<html>
<head>
  <style>
    .parallax {
      height: 100vh;
      overflow-y: scroll;
    }

    .parallax-layer {
      height: 100vh;
      background-size: cover;
      background-position: center;
    }

    .layer1 {
      background-image: url('layer1.jpg');
      background-attachment: fixed;
    }

    .layer2 {
      background-image: url('layer2.jpg');
      background-attachment: scroll;
    }
  </style>
</head>
<body>
  <div class="parallax">
    <div class="parallax-layer layer1"></div>
    <div class="parallax-layer layer2"></div>
  </div>
</body>
</html>
```
Trong ví dụ này, chúng ta có hai lớp `parallax-layer` với hình nền khác nhau. Lớp đầu tiên sẽ giữ hình nền cố định, trong khi lớp thứ hai sẽ di chuyển cùng với phần tử khi người dùng cuộn chuột.

## Bài tập
Để thực hành tạo hiệu ứng Parallax, hãy thực hiện các bước sau:
- Tạo một trang web mới với một phần tử `div` có lớp `parallax`.
- Thêm hai lớp `parallax-layer` vào trong phần tử `parallax`.
- Gán hình nền cho từng lớp `parallax-layer` bằng thuộc tính `background-image`.
- Sử dụng thuộc tính `background-attachment` để quyết định cách hình nền sẽ di chuyển khi người dùng cuộn chuột.
- Thử nghiệm với các giá trị khác nhau của thuộc tính `background-attachment` để tạo ra hiệu ứng Parallax thú vị.