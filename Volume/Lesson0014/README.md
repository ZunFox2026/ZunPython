# Làm quen với thư viện matplotlib
## Giới thiệu
Thư viện matplotlib là một trong những thư viện phổ biến nhất trong Python, được sử dụng để tạo ra các biểu đồ và hình ảnh chất lượng cao. Nó cung cấp một cách linh hoạt và dễ dàng để tạo ra các biểu đồ khác nhau, từ biểu đồ đơn giản đến biểu đồ phức tạp. Trong bài này, chúng ta sẽ tìm hiểu cách làm quen với thư viện matplotlib và cách sử dụng nó để tạo ra các biểu đồ cơ bản.

## Lý thuyết
Để bắt đầu sử dụng matplotlib, bạn cần import thư viện này vào chương trình của mình. Bạn có thể làm điều này bằng cách sử dụng câu lệnh `import matplotlib.pyplot as plt`. Sau khi import, bạn có thể bắt đầu tạo ra các biểu đồ bằng cách sử dụng các hàm như `plt.plot()`, `plt.bar()`, `plt.pie()`, v.v. Mỗi hàm này sẽ tạo ra một loại biểu đồ khác nhau. Ví dụ, `plt.plot()` sẽ tạo ra một biểu đồ đường, trong khi `plt.bar()` sẽ tạo ra một biểu đồ cột.

Matplotlib cũng cung cấp nhiều tùy chọn để tùy chỉnh biểu đồ của bạn, như thay đổi màu sắc, thêm tiêu đề, thêm nhãn cho các trục, v.v. Bạn có thể sử dụng các hàm như `plt.title()`, `plt.xlabel()`, `plt.ylabel()` để thực hiện các việc này.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách sử dụng matplotlib để tạo ra một biểu đồ đường:
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
Kết quả sẽ là một biểu đồ đường với tiêu đề "Biểu đồ đường" và nhãn cho các trục X và Y.

## Bài tập
Bài tập này sẽ giúp bạn làm quen với thư viện matplotlib. Hãy tạo ra một biểu đồ cột với các giá trị sau:
- Nhãn cho các cột: 'A', 'B', 'C', 'D'
- Giá trị cho các cột: 10, 20, 30, 40

Hãy sử dụng các hàm như `plt.bar()` để tạo ra biểu đồ cột, và `plt.title()`, `plt.xlabel()`, `plt.ylabel()` để thêm tiêu đề và nhãn cho các trục. Kết quả sẽ là một biểu đồ cột với tiêu đề "Biểu đồ cột" và nhãn cho các trục X và Y.