# Nhập thư viện matplotlib
import matplotlib.pyplot as plt

# Tạo dữ liệu mẫu
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo đồ thị
plt.plot(x, y)

# Thêm tiêu đề cho đồ thị
plt.title('Đồ thị hàm số y = x^2')

# Thêm nhãn cho trục x và trục y
plt.xlabel('x')
plt.ylabel('y')

# Hiển thị lưới
plt.grid(True)

# Hiển thị đồ thị
plt.show()

# Tạo đồ thị với nhiều dữ liệu
x1 = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
x2 = [1, 2, 3, 4, 5]
y2 = [2, 5, 10, 17, 26]

# Tạo đồ thị
plt.plot(x1, y1, label='y = x^2')
plt.plot(x2, y2, label='y = x^2 + 1')

# Thêm tiêu đề cho đồ thị
plt.title('Đồ thị hàm số')

# Thêm nhãn cho trục x và trục y
plt.xlabel('x')
plt.ylabel('y')

# Hiển thị lưới
plt.grid(True)

# Hiển thị chú thích
plt.legend()

# Hiển thị đồ thị
plt.show()

# Tạo đồ thị hình tròn
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# Tạo đồ thị
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Hiển thị tiêu đề
plt.title('Đồ thị hình tròn')

# Hiển thị đồ thị
plt.show()