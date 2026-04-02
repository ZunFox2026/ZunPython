# Làm quen với thư viện matplotlib
## Giới thiệu
Thư viện matplotlib là một trong những thư viện phổ biến nhất của Python, được sử dụng để tạo ra các biểu đồ và hình ảnh. Nó cung cấp một cách thức dễ dàng và linh hoạt để tạo ra các biểu đồ 2D và 3D, từ các biểu đồ đơn giản như biểu đồ đường, biểu đồ cột, đến các biểu đồ phức tạp hơn như biểu đồ phân tán, biểu đồ bề mặt.

Matplotlib được thiết kế để hoạt động với các mảng và danh sách dữ liệu, giúp cho việc tạo ra các biểu đồ trở nên dễ dàng và hiệu quả. Ngoài ra, thư viện này cũng cung cấp nhiều tính năng tùy chỉnh, cho phép người dùng điều chỉnh màu sắc, kích thước, font chữ và nhiều yếu tố khác của biểu đồ.

## Lý thuyết
Để sử dụng matplotlib, trước tiên bạn cần phải nhập thư viện này vào chương trình của mình bằng câu lệnh `import matplotlib.pyplot as plt`. Sau đó, bạn có thể sử dụng các hàm và phương thức của matplotlib để tạo ra các biểu đồ.

Một số hàm cơ bản của matplotlib bao gồm:
- `plt.plot()`: Tạo ra biểu đồ đường.
- `plt.bar()`: Tạo ra biểu đồ cột.
- `plt.scatter()`: Tạo ra biểu đồ phân tán.
- `plt.show()`: Hiển thị biểu đồ.

Ngoài ra, bạn cũng có thể tùy chỉnh biểu đồ bằng cách sử dụng các tham số như `label`, `title`, `xlabel`, `ylabel`,...

## Ví dụ
Dưới đây là một ví dụ đơn giản về việc sử dụng matplotlib để tạo ra biểu đồ đường:
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title('Biểu đồ đường')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
```
Kết quả sẽ là một biểu đồ đường với tiêu đề "Biểu đồ đường" và hai trục X, Y.

## Bài tập
Để giúp bạn nắm vững hơn về thư viện matplotlib, dưới đây là một số bài tập bạn có thể thử:
- Tạo ra một biểu đồ cột với 5 cột, mỗi cột có giá trị tương ứng là 10, 20, 30, 40, 50.
- Tạo ra một biểu đồ phân tán với 10 điểm, mỗi điểm có tọa độ x, y ngẫu nhiên.
- Tạo ra một biểu đồ đường với 2 đường, mỗi đường có màu sắc khác nhau.

Hy vọng qua các ví dụ và bài tập trên, bạn đã có một cái nhìn tổng quan về thư viện matplotlib và cách sử dụng nó để tạo ra các biểu đồ.