# Import thư viện matplotlib
import matplotlib.pyplot as plt

# Tạo dữ liệu mẫu
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo hình vẽ
plt.figure()

# Thêm tiêu đề cho hình vẽ
plt.title('Đồ thị hàm số y = x^2')

# Thêm nhãn cho trục x và y
plt.xlabel('x')
plt.ylabel('y')

# Vẽ đồ thị
plt.plot(x, y)

# Hiển thị lưới
plt.grid(True)

# Hiển thị đồ thị
plt.show()