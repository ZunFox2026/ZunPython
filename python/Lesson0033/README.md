# Làm quen với thư viện Turtle
## Giới thiệu
Thư viện Turtle là một công cụ đồ họa đơn giản được tích hợp sẵn trong ngôn ngữ lập trình Python. Nó cho phép người dùng tạo ra các hình ảnh và hình dạng khác nhau bằng cách điều khiển một con rùa ảo di chuyển trên màn hình. Thư viện này rất phù hợp cho những người mới bắt đầu học lập trình vì nó dễ sử dụng và cung cấp một cách trực quan để học về các khái niệm lập trình.

## Lý thuyết
Thư viện Turtle cung cấp một số hàm và phương thức cơ bản để điều khiển con rùa ảo, bao gồm:
- `forward()`: Di chuyển con rùa về phía trước một khoảng cách nhất định.
- `backward()`: Di chuyển con rùa về phía sau một khoảng cách nhất định.
- `left()`: Quay con rùa sang trái một góc nhất định.
- `right()`: Quay con rùa sang phải một góc nhất định.
- `penup()`: Nâng bút lên, con rùa di chuyển mà không vẽ.
- `pendown()`: đặt bút xuống, con rùa di chuyển và vẽ.
- `color()`: Thay đổi màu sắc của bút.

Người dùng có thể kết hợp các hàm và phương thức này để tạo ra các hình dạng và hình ảnh phức tạp.

## Ví dụ
Dưới đây là một ví dụ đơn giản về việc sử dụng thư viện Turtle để vẽ một hình vuông:
```python
import turtle

# Tạo một con rùa mới
rùa = turtle.Turtle()

# Vẽ một hình vuông
for i in range(4):
    rùa.forward(100)  # Di chuyển về phía trước 100 đơn vị
    rùa.right(90)      # Quay sang phải 90 độ

# Giữ cửa sổ mở cho đến khi người dùng đóng nó
turtle.done()
```
Kết quả của đoạn mã này là một hình vuông với mỗi cạnh dài 100 đơn vị.

## Bài tập
Để làm quen với thư viện Turtle, bạn có thể thử các bài tập sau:
- Vẽ một hình tam giác bằng cách sử dụng hàm `forward()` và `left()`.
- Tạo một hình tròn bằng cách sử dụng hàm `circle()`.
- Vẽ một hình ngôi sao bằng cách sử dụng hàm `forward()` và `right()`.
- Thử thay đổi màu sắc của bút và nền của cửa sổ đồ họa.

Bằng cách thực hiện các bài tập này, bạn sẽ trở nên熟悉 hơn với thư viện Turtle và có thể tạo ra các hình ảnh và hình dạng phức tạp hơn.