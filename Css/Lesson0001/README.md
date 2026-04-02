# Tìm hiểu về Units trong CSS
## Giới thiệu
 Units trong CSS (Cascading Style Sheets) là đơn vị đo lường được sử dụng để xác định kích thước của các phần tử trên trang web. Việc hiểu và sử dụng Units một cách chính xác là rất quan trọng để tạo ra các trang web có giao diện đẹp, đồng bộ và phù hợp với nhiều loại thiết bị khác nhau. Trong bài này, chúng ta sẽ tìm hiểu về các loại Units cơ bản trong CSS và cách sử dụng chúng.

## Lý thuyết
Trong CSS, có nhiều loại Units khác nhau, bao gồm cả đơn vị tuyệt đối và đơn vị tương đối. Các đơn vị tuyệt đối phổ biến bao gồm `px` (pixel), `cm` (centimét), `mm` (milimét), `in` (inch), `pt` (point) và `pc` (pica). Trong khi đó, các đơn vị tương đối bao gồm `%` (phần trăm), `em`, `rem`, `vw` (view width) và `vh` (view height).

- `px` là đơn vị cơ bản nhất và được sử dụng rộng rãi nhất, thường được sử dụng để đặt kích thước cho các phần tử.
- `cm`, `mm`, `in`, `pt`, `pc` thường được sử dụng trong in ấn.
- `%` thường được sử dụng để xác định kích thước của các phần tử dựa trên kích thước của phần tử cha.
- `em` và `rem` được sử dụng để xác định kích thước phông chữ.
- `vw` và `vh` được sử dụng để xác định kích thước của các phần tử dựa trên kích thước của cửa sổ trình duyệt.

Ví dụ về việc sử dụng các đơn vị tuyệt đối:
```css
div {
  width: 500px;
  height: 200px;
  font-size: 16px;
}
```

## Ví dụ
Giả sử chúng ta muốn tạo một hộp có kích thước là 50% so với chiều rộng của trang web và chiều cao là 300 pixel. Chúng ta có thể sử dụng các đơn vị tương đối và tuyệt đối như sau:

```css
.box {
  width: 50vw;
  height: 300px;
  background-color: #f2f2f2;
  padding: 20px;
  font-size: 1.5em;
}
```

Trong ví dụ trên, `50vw` xác định chiều rộng của hộp là 50% chiều rộng của cửa sổ trình duyệt, `300px` xác định chiều cao là 300 pixel, `20px` là khoảng cách giữa nội dung và biên giới của hộp, và `1.5em` xác định kích thước phông chữ là 1.5 lần so với kích thước phông chữ mặc định.

## Bài tập
Để rèn luyện kỹ năng sử dụng Units trong CSS, hãy thực hành bằng cách tạo các phần tử có kích thước khác nhau sử dụng các đơn vị tuyệt đối và tương đối. Ví dụ:

- Tạo một đoạn văn bản có kích thước phông chữ là 18 pixel và màu xanh dương.
- Tạo một hình chữ nhật có kích thước 200x100 pixel, màu nền là màu đỏ và có độ đệm là 10 pixel.
- Tạo một hộp có chiều rộng là 30% so với chiều rộng của trang web và chiều cao là 250 pixel.

Hãy nhớ sử dụng các đơn vị khác nhau để tạo ra các hiệu ứng khác nhau và quan sát cách chúng ảnh hưởng đến giao diện của trang web.