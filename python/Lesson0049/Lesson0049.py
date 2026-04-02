# Nhập thư viện matplotlib
import matplotlib.pyplot as plt

# Tạo dữ liệu cho biểu đồ
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo biểu đồ đường
plt.plot(x, y)

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ đường')

# Thêm nhãn cho trục x và trục y
plt.xlabel('Trục x')
plt.ylabel('Trục y')

# Hiển thị biểu đồ
plt.show()

# Tạo dữ liệu cho biểu đồ cột
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo biểu đồ cột
plt.bar(x, y)

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ cột')

# Thêm nhãn cho trục x và trục y
plt.xlabel('Trục x')
plt.ylabel('Trục y')

# Hiển thị biểu đồ
plt.show()

# Tạo dữ liệu cho biểu đồ tròn
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [15, 30, 45, 10, 10]

# Tạo biểu đồ tròn
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ tròn')

# Hiển thị biểu đồ
plt.show()