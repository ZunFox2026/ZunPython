# Bài 28: Làm việc với thư viện matplotlib

# Thư viện matplotlib được sử dụng để tạo các biểu đồ và hình ảnh
import matplotlib.pyplot as plt

# Tạo dữ liệu mẫu
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo biểu đồ đường thẳng
plt.plot(x, y)

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ đường thẳng')

# Thêm nhãn cho các trục
plt.xlabel('Trục x')
plt.ylabel('Trục y')

# Hiển thị lưới
plt.grid(True)

# Hiển thị biểu đồ
plt.show()

# Tạo biểu đồ cột
plt.bar(x, y)

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ cột')

# Thêm nhãn cho các trục
plt.xlabel('Trục x')
plt.ylabel('Trục y')

# Hiển thị lưới
plt.grid(True)

# Hiển thị biểu đồ
plt.show()

# Tạo biểu đồ tròn
plt.pie(y)

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ tròn')

# Hiển thị biểu đồ
plt.show()