# Làm quen với thư viện matplotlib
## Giới thiệu
Thư viện matplotlib là một trong những thư viện phổ biến nhất trong Python, được sử dụng để tạo ra các biểu đồ và hình ảnh. Với matplotlib, bạn có thể tạo ra các biểu đồ từ đơn giản đến phức tạp, từ biểu đồ đường đến biểu đồ 3D. Trong bài này, chúng ta sẽ tìm hiểu cách làm quen với thư viện matplotlib và cách sử dụng nó để tạo ra các biểu đồ cơ bản.

## Lý thuyết
Để bắt đầu sử dụng matplotlib, bạn cần nhập thư viện này vào chương trình của mình bằng cách sử dụng câu lệnh `import matplotlib.pyplot as plt`. Sau đó, bạn có thể sử dụng các hàm trong thư viện này để tạo ra các biểu đồ. Một số hàm cơ bản trong matplotlib bao gồm:
- `plt.plot()`: Tạo ra biểu đồ đường
- `plt.bar()`: Tạo ra biểu đồ cột
- `plt.scatter()`: Tạo ra biểu đồ điểm
- `plt.show()`: Hiển thị biểu đồ
Ngoài ra, bạn cũng có thể tùy chỉnh biểu đồ của mình bằng cách sử dụng các hàm như `plt.title()`, `plt.xlabel()`, `plt.ylabel()`,...

## Ví dụ
Dưới đây là một ví dụ về cách sử dụng matplotlib để tạo ra một biểu đồ đường cơ bản:
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
Kết quả của ví dụ này sẽ là một biểu đồ đường với tiêu đề "Biểu đồ đường", nhãn X và Y cho các trục.

## Bài tập
Để rèn luyện kỹ năng sử dụng matplotlib, bạn có thể thử các bài tập sau:
- Tạo ra một biểu đồ cột với 5 cột, mỗi cột có giá trị tương ứng là 10, 20, 30, 40, 50.
- Tạo ra một biểu đồ điểm với 10 điểm, mỗi điểm có tọa độ x và y được sinh ngẫu nhiên.
- Tạo ra một biểu đồ đường với 2 đường, mỗi đường có 5 điểm, và tùy chỉnh màu sắc và kiểu đường cho mỗi đường.