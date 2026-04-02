# Nhập thư viện Matplotlib
import matplotlib.pyplot as plt

# Tạo dữ liệu mẫu
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo đồ thị
plt.plot(x, y)

# Thêm tiêu đề cho đồ thị
plt.title('Đồ thị hàm số y = x^2')

# Thêm nhãn cho trục x và trục y
plt.xlabel('Trục x')
plt.ylabel('Trục y')

# Hiển thị lưới
plt.grid(True)

# Hiển thị đồ thị
plt.show()

# Tạo dữ liệu mẫu cho biểu đồ tròn
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# Tạo biểu đồ tròn
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ tròn')

# Hiển thị biểu đồ
plt.show()

# Tạo dữ liệu mẫu cho biểu đồ cột
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo biểu đồ cột
plt.bar(x, y)

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ cột')

# Hiển thị biểu đồ
plt.show()