# Làm quen với thư viện matplotlib
## Giới thiệu
Thư viện matplotlib là một trong những thư viện phổ biến nhất trong Python, được sử dụng để tạo ra các biểu đồ và hình ảnh. Matplotlib cung cấp một cách dễ dàng và linh hoạt để tạo ra các biểu đồ 2D và 3D, giúp người dùng có thể minh họa và phân tích dữ liệu một cách trực quan. Trong bài này, chúng ta sẽ tìm hiểu cách làm quen với thư viện matplotlib và cách sử dụng nó để tạo ra các biểu đồ cơ bản.

## Lý thuyết
Để bắt đầu sử dụng matplotlib, bạn cần phải hiểu một số khái niệm cơ bản. Đầu tiên, bạn cần phải nhập thư viện matplotlib vào chương trình của mình bằng lệnh `import matplotlib.pyplot as plt`. Sau đó, bạn có thể sử dụng các hàm khác nhau của matplotlib để tạo ra các biểu đồ. Ví dụ, bạn có thể sử dụng hàm `plt.plot()` để tạo ra một biểu đồ đường, hàm `plt.bar()` để tạo ra một biểu đồ cột, và hàm `plt.scatter()` để tạo ra một biểu đồ phân tán. Ngoài ra, bạn cũng có thể sử dụng các hàm khác như `plt.title()`, `plt.xlabel()`, `plt.ylabel()` để thêm tiêu đề, nhãn x, nhãn y cho biểu đồ.

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
Khi chạy code này, bạn sẽ thấy một biểu đồ đường với tiêu đề, nhãn x, nhãn y. Bạn cũng có thể thay đổi màu sắc, kiểu đường, kích thước biểu đồ bằng cách sử dụng các tham số khác nhau của hàm `plt.plot()`.

## Bài tập
Để thực hành sử dụng matplotlib, bạn có thể thử tạo ra các biểu đồ khác nhau bằng cách sử dụng các hàm và tham số khác nhau. Ví dụ, bạn có thể tạo ra một biểu đồ cột để so sánh giá trị của các hạng mục khác nhau, hoặc tạo ra một biểu đồ phân tán để xem mối quan hệ giữa hai biến số. Bạn cũng có thể thử thêm tiêu đề, nhãn x, nhãn y cho biểu đồ, và thay đổi màu sắc, kiểu đường, kích thước biểu đồ. Sau khi hoàn thành các bài tập này, bạn sẽ có thể sử dụng matplotlib để tạo ra các biểu đồ phức tạp và trực quan hơn.