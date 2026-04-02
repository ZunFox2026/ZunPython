# Làm quen với thư viện Turtle
## Giới thiệu
Thư viện Turtle là một công cụ tuyệt vời trong ngôn ngữ lập trình Python, giúp bạn tạo ra các hình ảnh và đồ họa đơn giản. Thư viện này cung cấp một cách dễ dàng và trực quan để tạo ra các hình dạng, đường cong và hình ảnh khác nhau. Trong bài viết này, chúng ta sẽ tìm hiểu cách làm quen với thư viện Turtle và cách sử dụng nó để tạo ra các hình ảnh thú vị.

## Lý thuyết
Thư viện Turtle cung cấp một số hàm và phương thức cơ bản để tạo ra các hình ảnh. Một số hàm và phương thức quan trọng bao gồm:
- `turtle.forward(distance)`: Di chuyển con trỏ về phía trước một khoảng cách nhất định.
- `turtle.backward(distance)`: Di chuyển con trỏ về phía sau một khoảng cách nhất định.
- `turtle.left(angle)`: Quay con trỏ sang trái một góc nhất định.
- `turtle.right(angle)`: Quay con trỏ sang phải một góc nhất định.
- `turtle.penup()`: Nâng bút lên, không vẽ khi di chuyển.
- `turtle.pendown()`: Đặt bút xuống, vẽ khi di chuyển.
- `turtle.color(color)`: Đặt màu cho bút vẽ.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách sử dụng thư viện Turtle để vẽ một hình vuông:
```python
import turtle

# Tạo một cửa sổ mới
window = turtle.Screen()

# Tạo một con trỏ mới
my_turtle = turtle.Turtle()

# Vẽ một hình vuông
for i in range(4):
    my_turtle.forward(100)  # Di chuyển về phía trước 100 đơn vị
    my_turtle.right(90)  # Quay sang phải 90 độ

# Đóng cửa sổ
window.mainloop()
```
Khi chạy mã này, bạn sẽ thấy một hình vuông được vẽ trên màn hình.

## Bài tập
Để thực hành sử dụng thư viện Turtle, bạn có thể thử các bài tập sau:
- Vẽ một hình tròn bằng cách sử dụng hàm `turtle.circle(radius)`.
- Vẽ một ngôi sao bằng cách sử dụng hàm `turtle.forward(distance)` và `turtle.right(angle)`.
- Tạo một hình ảnh phức tạp bằng cách kết hợp nhiều hình dạng khác nhau.
Hãy thử nghiệm và khám phá các khả năng của thư viện Turtle!