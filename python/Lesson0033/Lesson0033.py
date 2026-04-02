# Import thư viện Turtle
import turtle

# Tạo một màn hình mới
man_hinh = turtle.Screen()

# Đặt tiêu đề cho màn hình
man_hinh.title("Làm quen với thư viện Turtle")

# Tạo một con rùa mới
rua = turtle.Turtle()

# Đặt tốc độ di chuyển của rùa
rua.speed(1)  # 1 là tốc độ chậm nhất, 10 là tốc độ nhanh nhất

# Di chuyển rùa đi 100 đơn vị
rua.forward(100)

# Quay rùa sang phải 90 độ
rua.right(90)

# Di chuyển rùa đi 100 đơn vị
rua.forward(100)

# Quay rùa sang trái 90 độ
rua.left(90)

# Viết văn bản lên màn hình
rua.write("Xin chào, thế giới!", align="center", font=("Arial", 24, "bold"))

# Giữ màn hình mở cho đến khi người dùng nhấn nút
man_hinh.mainloop()