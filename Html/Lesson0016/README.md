# Tạo hiệu ứng hình ảnh
## Giới thiệu
Trong thiết kế web, hiệu ứng hình ảnh là một phần quan trọng giúp thu hút người dùng và tạo ấn tượng về giao diện trang web. Với HTML và CSS, chúng ta có thể tạo ra nhiều hiệu ứng hình ảnh khác nhau, từ đơn giản đến phức tạp. Bài viết này sẽ giới thiệu về cách tạo hiệu ứng hình ảnh cơ bản bằng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng hình ảnh, chúng ta thường sử dụng các thuộc tính CSS như `opacity`, `filter`, `transform`, `transition`. Các thuộc tính này cho phép chúng ta điều chỉnh độ trong suốt, màu sắc, kích thước và vị trí của hình ảnh.

Ví dụ, chúng ta có thể sử dụng thuộc tính `opacity` để tạo hiệu ứng mờ cho hình ảnh:
```html
<img src="image.jpg" style="opacity: 0.5;">
```
Hoặc sử dụng thuộc tính `filter` để tạo hiệu ứng màu sắc cho hình ảnh:
```html
<img src="image.jpg" style="filter: grayscale(100%);">
```
Chúng ta cũng có thể sử dụng thuộc tính `transform` để tạo hiệu ứng xoay, lật cho hình ảnh:
```html
<img src="image.jpg" style="transform: rotate(45deg);">
```
Cuối cùng, chúng ta có thể sử dụng thuộc tính `transition` để tạo hiệu ứng chuyển đổi mượt mà cho hình ảnh:
```html
<img src="image.jpg" style="transition: all 0.5s ease-in-out;">
```
## Ví dụ
Dưới đây là một ví dụ về tạo hiệu ứng hình ảnh bằng HTML và CSS:
```html
<!DOCTYPE html>
<html>
<head>
	<title>Tạo hiệu ứng hình ảnh</title>
	<style>
		.image {
			width: 500px;
			height: 300px;
			opacity: 0.5;
			filter: grayscale(100%);
			transform: rotate(10deg);
			transition: all 0.5s ease-in-out;
		}
		
		.image:hover {
			opacity: 1;
			filter: none;
			transform: rotate(0deg);
		}
	</style>
</head>
<body>
	<img src="image.jpg" class="image">
</body>
</html>
```
Trong ví dụ này, chúng ta tạo một hình ảnh với hiệu ứng mờ, màu sắc grayscale và xoay nhẹ. Khi người dùng di chuột qua hình ảnh, hiệu ứng sẽ chuyển đổi thành hình ảnh rõ ràng, màu sắc bình thường và không xoay.

## Bài tập
Bài tập cho bạn là tạo một trang web với hiệu ứng hình ảnh sau:
- Tạo một hình ảnh với hiệu ứng mờ và màu sắc grayscale.
- Khi người dùng di chuột qua hình ảnh, hiệu ứng sẽ chuyển đổi thành hình ảnh rõ ràng và màu sắc bình thường.
- Thêm hiệu ứng chuyển đổi mượt mà cho hình ảnh.
- Tạo một nút bấm để người dùng có thể tải hình ảnh về máy tính.

Hãy sử dụng các thuộc tính CSS đã học trong bài này để tạo hiệu ứng hình ảnh như yêu cầu. Chúc bạn thành công!