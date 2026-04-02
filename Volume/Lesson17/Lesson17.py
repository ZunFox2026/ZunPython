# Import thư viện Matplotlib
import matplotlib.pyplot as plt

# Tạo dữ liệu mẫu
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Vẽ đồ thị
plt.plot(x, y)

# Thêm tiêu đề cho đồ thị
plt.title('Đồ thị hàm số y = x^2')

# Thêm nhãn cho trục x và y
plt.xlabel('Trục x')
plt.ylabel('Trục y')

# Hiển thị lưới
plt.grid(True)

# Hiển thị đồ thị
plt.show()

# Vẽ đồ thị nhiều đường
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [2, 5, 8, 11, 14]

plt.plot(x, y1, label='y = x^2')
plt.plot(x, y2, label='y = x + 1')

plt.title('Đồ thị hàm số')
plt.xlabel('Trục x')
plt.ylabel('Trục y')
plt.legend()
plt.grid(True)
plt.show()

# Vẽ đồ thị hình tròn
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Đồ thị hình tròn')
plt.show()

# Vẽ đồ thị cột
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.bar(x, y)
plt.title('Đồ thị cột')
plt.xlabel('Trục x')
plt.ylabel('Trục y')
plt.show()