# Tính nhất quán trong thiết kế
## Giới thiệu
Tính nhất quán trong thiết kế là yếu tố quan trọng quyết định sự thành công của một dự án thiết kế. Nhất quán giúp tạo ra sự đồng bộ và thống nhất trong giao diện, giúp người dùng dễ dàng sử dụng và nhận diện thương hiệu. Trong bài viết này, chúng ta sẽ tìm hiểu về tính nhất quán trong thiết kế, lý thuyết và ví dụ minh họa.

## Lý thuyết
Tính nhất quán trong thiết kế bao gồm nhiều yếu tố như màu sắc, phông chữ, kích thước, khoảng cách,... Để tạo ra tính nhất quán, chúng ta cần định nghĩa rõ ràng các yếu tố này và sử dụng chúng một cách thống nhất trong toàn bộ dự án. Ví dụ, nếu chúng ta chọn màu sắc chính là xanh biển, chúng ta nên sử dụng màu này cho tất cả các nút bấm, tiêu đề, và các yếu tố khác. Chúng ta cũng nên chọn một phông chữ duy nhất và sử dụng nó cho tất cả các văn bản.

Ví dụ về CSS minh họa tính nhất quán:
```css
body {
  font-family: Arial, sans-serif;
  color: #333;
}

h1, h2, h3 {
  color: #007bff;
}

button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
```
Trong ví dụ trên, chúng ta định nghĩa phông chữ và màu sắc cho toàn bộ trang web, và sử dụng màu xanh biển (#007bff) cho các tiêu đề và nút bấm.

## Ví dụ
Một ví dụ khác về tính nhất quán trong thiết kế là sử dụng khoảng cách và padding một cách thống nhất. Ví dụ, nếu chúng ta đặt khoảng cách giữa các phần tử là 20px, chúng ta nên sử dụng khoảng cách này cho tất cả các phần tử.

Ví dụ về CSS minh họa tính nhất quán về khoảng cách:
```css
.container {
  padding: 20px;
  margin: 20px;
}

.item {
  padding: 10px;
  margin: 10px;
}
```
Trong ví dụ trên, chúng ta định nghĩa khoảng cách và padding cho các phần tử container và item, và sử dụng chúng một cách thống nhất trong toàn bộ dự án.

## Bài tập
Bài tập cho bạn là tạo ra một trang web đơn giản với tính nhất quán trong thiết kế. Bạn cần định nghĩa các yếu tố như màu sắc, phông chữ, kích thước, khoảng cách,... và sử dụng chúng một cách thống nhất trong toàn bộ dự án. Bạn có thể sử dụng CSS để định nghĩa các yếu tố này và áp dụng chúng cho các phần tử trên trang web.

Một số gợi ý cho bài tập:

* Định nghĩa màu sắc chính và sử dụng nó cho các tiêu đề và nút bấm
* Chọn một phông chữ duy nhất và sử dụng nó cho tất cả các văn bản
* Sử dụng khoảng cách và padding một cách thống nhất cho các phần tử
* Tạo ra một trang web với ít nhất 3 phần tử khác nhau (tiêu đề, văn bản, nút bấm,...) và áp dụng tính nhất quán trong thiết kế cho chúng.