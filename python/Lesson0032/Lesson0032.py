# Khởi tạo màn hình
import turtle

# Tạo một màn hình mới
man_hinh = turtle.Screen()

# Đặt tiêu đề cho màn hình
man_hinh.title("Làm quen với thư viện Turtle")

# Tạo một con rùa
rua = turtle.Turtle()

# Di chuyển con rùa đến vị trí (0, 0)
rua.penup()
rua.goto(0, 0)
rua.pendown()

# Vẽ hình vuông
# Comment: phương thức forward di chuyển con rùa về phía trước một khoảng cách nhất định
# Comment: phương thức right quay con rùa sang phải một góc nhất định
for _ in range(4):
    rua.forward(100)  # di chuyển 100 đơn vị
    rua.right(90)     # quay 90 độ sang phải

# Vẽ hình tròn
# Comment: phương thức circle vẽ một hình tròn với bán kính nhất định
rua.penup()
rua.goto(0, -100)
rua.pendown()
rua.circle(50)       # vẽ hình tròn với bán kính 50

# Vẽ hình ngôi sao
# Comment: phương thức forward và right được sử dụng để vẽ hình ngôi sao
rua.penup()
rua.goto(0, 100)
rua.pendown()
for _ in range(5):
    rua.forward(100)
    rua.right(144)

# Giữ màn hình mở cho đến khi người dùng đóng lại
turtle.done()