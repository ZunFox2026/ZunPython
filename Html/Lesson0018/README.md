# Tạo hiệu ứng Parallax
## Giới thiệu
Hiệu ứng Parallax là một kỹ thuật thiết kế web hiện đại, tạo ra sự chuyển động của các lớp hình ảnh hoặc phần tử khi người dùng cuộn trang web. Hiệu ứng này mang lại trải nghiệm người dùng độc đáo và thú vị, giúp trang web trở nên sinh động và bắt mắt hơn. Trong bài viết này, chúng ta sẽ tìm hiểu cách tạo hiệu ứng Parallax bằng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng Parallax, chúng ta cần sử dụng thuộc tính `background-attachment` trong CSS. Thuộc tính này cho phép chúng ta gắn hình nền vào một vị trí cụ thể trên trang web, tạo ra sự chuyển động khi người dùng cuộn trang. Ngoài ra, chúng ta cũng cần sử dụng thuộc tính `background-position` để đặt hình nền tại vị trí mong muốn.

Ví dụ về sử dụng `background-attachment` và `background-position`:
```html
<div class="parallax">
  <div class="layer1"></div>
  <div class="layer2"></div>
</div>
```

```css
.parallax {
  height: 500px;
}

.layer1 {
  background-image: url('image1.jpg');
  background-attachment: fixed;
  background-position: center;
  height: 100%;
  width: 100%;
}

.layer2 {
  background-image: url('image2.jpg');
  background-attachment: scroll;
  background-position: center;
  height: 100%;
  width: 100%;
}
```
Trong ví dụ trên, lớp `layer1` sẽ được gắn vào vị trí cố định trên trang web, trong khi lớp `layer2` sẽ di chuyển khi người dùng cuộn trang.

## Ví dụ
Dưới đây là một ví dụ hoàn chỉnh về tạo hiệu ứng Parallax:
```html
<html>
<head>
  <title>Hiệu ứng Parallax</title>
  <style>
    body {
      margin: 0;
      padding: 0;
    }
    
    .parallax {
      height: 500px;
    }
    
    .layer1 {
      background-image: url('image1.jpg');
      background-attachment: fixed;
      background-position: center;
      height: 100%;
      width: 100%;
    }
    
    .layer2 {
      background-image: url('image2.jpg');
      background-attachment: scroll;
      background-position: center;
      height: 100%;
      width: 100%;
    }
  </style>
</head>
<body>
  <div class="parallax">
    <div class="layer1"></div>
    <div class="layer2"></div>
  </div>
</body>
</html>
```
Khi chạy ví dụ trên, bạn sẽ thấy hiệu ứng Parallax khi cuộn trang web.

## Bài tập
Bài tập: Tạo một trang web đơn giản với hiệu ứng Parallax, sử dụng hai lớp hình ảnh khác nhau. Lớp trên cùng sẽ được gắn vào vị trí cố định, trong khi lớp dưới cùng sẽ di chuyển khi người dùng cuộn trang. Hãy sử dụng thuộc tính `background-attachment` và `background-position` để tạo hiệu ứng này.