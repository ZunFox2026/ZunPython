# Import thư viện turtle
import turtle

# Tạo một cửa sổ mới
window = turtle.Screen()

# Đặt tiêu đề cho cửa sổ
window.title("Làm quen với thư viện Turtle")

# Tạo một con rùa mới
my_turtle = turtle.Turtle()

# Di chuyển con rùa đến vị trí (0, 0)
my_turtle.penup()
my_turtle.goto(0, 0)
my_turtle.pendown()

# Vẽ một hình vuông
for _ in range(4):
    # Di chuyển con rùa 100 đơn vị về phía trước
    my_turtle.forward(100)
    # Quay con rùa 90 độ về phía trái
    my_turtle.left(90)

# Vẽ một hình tròn
my_turtle.penup()
my_turtle.goto(0, -50)
my_turtle.pendown()
my_turtle.circle(50)

# Vẽ một hình tam giác
my_turtle.penup()
my_turtle.goto(-100, 50)
my_turtle.pendown()
for _ in range(3):
    my_turtle.forward(100)
    my_turtle.left(120)

# Đóng cửa sổ
window.mainloop()