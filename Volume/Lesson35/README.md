# Làm việc với tệp hình ảnh
## Giới thiệu
Trong lập trình Python, việc làm việc với tệp hình ảnh là một kỹ năng quan trọng và thường được sử dụng trong nhiều lĩnh vực khác nhau như xử lý hình ảnh, trí tuệ nhân tạo, và phát triển ứng dụng. Bài viết này sẽ hướng dẫn bạn cách làm việc với tệp hình ảnh bằng ngôn ngữ lập trình Python.

## Lý thuyết
Để làm việc với tệp hình ảnh trong Python, bạn có thể sử dụng thư viện Pillow (Python Imaging Library). Thư viện này cung cấp nhiều chức năng để đọc, viết, và xử lý hình ảnh. Bạn có thể cài đặt thư viện Pillow bằng cách chạy lệnh `pip install pillow` trong terminal.

Một số chức năng quan trọng của thư viện Pillow bao gồm:
- Mở và hiển thị hình ảnh
- Chuyển đổi định dạng hình ảnh
- Xử lý hình ảnh (cắt,resize, thêm chữ,...)
- Lưu hình ảnh

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách mở và hiển thị hình ảnh bằng thư viện Pillow:
```python
from PIL import Image

# Mở hình ảnh
img = Image.open('image.jpg')

# Hiển thị hình ảnh
img.show()
```
Trong ví dụ trên, chúng ta mở hình ảnh có tên `image.jpg` và hiển thị nó trên màn hình.

Một ví dụ khác về cách cắt hình ảnh:
```python
from PIL import Image

# Mở hình ảnh
img = Image.open('image.jpg')

# Cắt hình ảnh
img_crop = img.crop((100, 100, 300, 300))

# Hiển thị hình ảnh cắt
img_crop.show()
```
Trong ví dụ này, chúng ta cắt hình ảnh tại vùng có tọa độ (100, 100) đến (300, 300) và hiển thị hình ảnh cắt.

## Bài tập
Bài tập 1: Viết một chương trình Python để mở và hiển thị hình ảnh có tên `image.jpg`.

Bài tập 2: Viết một chương trình Python để cắt hình ảnh có tên `image.jpg` tại vùng có tọa độ (100, 100) đến (300, 300) và hiển thị hình ảnh cắt.

Bài tập 3: Viết một chương trình Python để chuyển đổi hình ảnh có tên `image.jpg` từ định dạng JPEG sang PNG.

Bài tập 4: Viết một chương trình Python để thêm chữ "Hello World" vào hình ảnh có tên `image.jpg` tại tọa độ (100, 100).

Bài tập 5: Viết một chương trình Python để xử lý hình ảnh có tên `image.jpg` bằng cách áp dụng các bộ lọc khác nhau (ví dụ: bộ lọc grayscale, bộ lọc blur,...).