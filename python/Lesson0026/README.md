# Làm quen với thư viện matplotlib
## Giới thiệu
Thư viện matplotlib là một trong những thư viện phổ biến nhất trong Python, được sử dụng để tạo ra các biểu đồ, đồ thị và hình ảnh. Nó cung cấp một cách đơn giản và hiệu quả để trực quan hóa dữ liệu, giúp người dùng dễ dàng hiểu và phân tích dữ liệu. Trong bài này, chúng ta sẽ tìm hiểu cách làm quen với thư viện matplotlib và cách sử dụng nó để tạo ra các biểu đồ cơ bản.

## Lý thuyết
Để bắt đầu sử dụng thư viện matplotlib, bạn cần nhập nó vào chương trình Python của mình bằng lệnh `import matplotlib.pyplot as plt`. Sau đó, bạn có thể sử dụng các hàm và phương thức của matplotlib để tạo ra các biểu đồ. Một số hàm và phương thức phổ biến của matplotlib bao gồm:
- `plt.plot()`: tạo ra một biểu đồ đường thẳng
- `plt.bar()`: tạo ra một biểu đồ cột
- `plt.scatter()`: tạo ra một biểu đồ phân tán
- `plt.show()`: hiển thị biểu đồ

Ngoài ra, bạn cũng có thể tùy chỉnh biểu đồ của mình bằng cách sử dụng các tham số như `label`, `title`, `xlabel`, `ylabel`, v.v.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách sử dụng matplotlib để tạo ra một biểu đồ đường thẳng:
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title('Biểu đồ đường thẳng')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
```
Kết quả sẽ là một biểu đồ đường thẳng với tiêu đề "Biểu đồ đường thẳng" và các nhãn X, Y.

## Bài tập
Bài tập này yêu cầu bạn tạo ra một biểu đồ cột sử dụng matplotlib. Dữ liệu cho biểu đồ là:
- Năm: 2018, 2019, 2020, 2021, 2022
- Doanh thu: 100, 120, 150, 180, 200

Hãy sử dụng các hàm và phương thức của matplotlib để tạo ra biểu đồ cột và hiển thị nó. Bạn cũng có thể tùy chỉnh biểu đồ của mình bằng cách thêm tiêu đề, nhãn X, Y, v.v.