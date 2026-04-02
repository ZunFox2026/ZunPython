# Import thư viện Matplotlib
import matplotlib.pyplot as plt

# Tạo dữ liệu mẫu
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo biểu đồ đường
plt.plot(x, y)

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ đường')

# Thêm nhãn cho trục x và trục y
plt.xlabel('Trục x')
plt.ylabel('Trục y')

# Hiển thị lưới
plt.grid(True)

# Hiển thị biểu đồ
plt.show()

# Tạo dữ liệu mẫu
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo biểu đồ cột
plt.bar(x, y)

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ cột')

# Thêm nhãn cho trục x và trục y
plt.xlabel('Trục x')
plt.ylabel('Trục y')

# Hiển thị lưới
plt.grid(True)

# Hiển thị biểu đồ
plt.show()

# Tạo dữ liệu mẫu
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo biểu đồ tròn
plt.pie(y, labels=x, autopct='%1.1f%%')

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ tròn')

# Hiển thị biểu đồ
plt.show()