# Làm quen với thư viện Matplotlib
## Giới thiệu
Thư viện Matplotlib là một trong những thư viện phổ biến nhất trong Python, được sử dụng để tạo ra các loại biểu đồ, đồ thị khác nhau. Nó cung cấp một cách đơn giản và hiệu quả để trực quan hóa dữ liệu, giúp người dùng dễ dàng hiểu và phân tích dữ liệu. Trong bài này, chúng ta sẽ tìm hiểu cách sử dụng thư viện Matplotlib để tạo ra các loại biểu đồ cơ bản.

## Lý thuyết
Matplotlib cung cấp nhiều loại biểu đồ khác nhau, bao gồm biểu đồ đường, biểu đồ cột, biểu đồ tròn, biểu đồ phân tán,... Mỗi loại biểu đồ có thể được tùy chỉnh để phù hợp với nhu cầu của người dùng. Để sử dụng Matplotlib, chúng ta cần nhập thư viện vào chương trình Python của mình bằng lệnh `import matplotlib.pyplot as plt`. Sau đó, chúng ta có thể sử dụng các hàm trong thư viện để tạo ra biểu đồ. Ví dụ, để tạo ra một biểu đồ đường, chúng ta có thể sử dụng hàm `plt.plot()`.

## Ví dụ
Dưới đây là một ví dụ về cách sử dụng Matplotlib để tạo ra một biểu đồ đường:
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Biểu đồ đường')
plt.show()
```
Kết quả sẽ là một biểu đồ đường với trục x và trục y được ghi chú rõ ràng. Chúng ta cũng có thể tạo ra các loại biểu đồ khác nhau bằng cách sử dụng các hàm khác nhau trong thư viện Matplotlib. Ví dụ, để tạo ra một biểu đồ cột, chúng ta có thể sử dụng hàm `plt.bar()`.

## Bài tập
Để thực hành sử dụng thư viện Matplotlib, hãy thử tạo ra các loại biểu đồ khác nhau sau:
- Biểu đồ cột với dữ liệu x = [1, 2, 3, 4, 5] và y = [2, 4, 6, 8, 10]
- Biểu đồ tròn với dữ liệu x = [10, 20, 30, 40] và y = [10, 20, 30, 40]
- Biểu đồ phân tán với dữ liệu x = [1, 2, 3, 4, 5] và y = [2, 4, 6, 8, 10]
Hãy thử nghiệm với các loại biểu đồ khác nhau và tùy chỉnh chúng để phù hợp với nhu cầu của bạn.