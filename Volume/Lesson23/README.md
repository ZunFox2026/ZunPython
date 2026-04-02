# Làm quen với thư viện matplotlib
## Giới thiệu
Thư viện matplotlib là một trong những thư viện phổ biến nhất trong Python, được sử dụng để tạo ra các biểu đồ và hình ảnh chất lượng cao. Nó cung cấp một cách dễ dàng và linh hoạt để tạo ra các biểu đồ 2D và 3D, từ các biểu đồ đơn giản như biểu đồ đường và biểu đồ cột, đến các biểu đồ phức tạp hơn như biểu đồ phân tán và biểu đồ mặt. Trong bài này, chúng ta sẽ tìm hiểu cách làm quen với thư viện matplotlib và cách sử dụng nó để tạo ra các biểu đồ cơ bản.

## Lý thuyết
Trước khi bắt đầu sử dụng matplotlib, chúng ta cần hiểu một số khái niệm cơ bản. Thư viện matplotlib bao gồm các thành phần chính sau:
- **Figure**: Đây là khu vực chứa biểu đồ, tương tự như một tờ giấy.
- **Axes**: Đây là khu vực chứa các trục tọa độ và biểu đồ.
- **Plot**: Đây là biểu đồ thực tế, được tạo ra bằng cách sử dụng các hàm plot khác nhau.
Để tạo ra một biểu đồ, chúng ta cần thực hiện các bước sau:
1. Import thư viện matplotlib vào chương trình.
2. Tạo ra một figure và axes bằng cách sử dụng hàm `subplots()`.
3. Sử dụng các hàm plot khác nhau để tạo ra biểu đồ.
4. hiển thị biểu đồ bằng cách sử dụng hàm `show()`.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách sử dụng matplotlib để tạo ra một biểu đồ đường:
```python
import matplotlib.pyplot as plt

# Tạo ra một figure và axes
fig, ax = plt.subplots()

# Tạo ra một biểu đồ đường
ax.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])

# Hiển thị biểu đồ
plt.show()
```
Kết quả sẽ là một biểu đồ đường đơn giản với các điểm dữ liệu được kết nối bằng các đoạn thẳng.

## Bài tập
Để củng cố kiến thức, hãy thực hiện các bài tập sau:
1. Tạo ra một biểu đồ cột với các giá trị [10, 20, 30, 40, 50] trên trục x và [100, 200, 300, 400, 500] trên trục y.
2. Tạo ra một biểu đồ phân tán với các giá trị [1, 2, 3, 4, 5] trên trục x và [2, 4, 6, 8, 10] trên trục y.
3. Tạo ra một biểu đồ mặt với các giá trị [1, 2, 3, 4, 5] trên trục x và [1, 2, 3, 4, 5] trên trục y, và các giá trị [10, 20, 30, 40, 50] trên trục z.
Hãy sử dụng các hàm plot khác nhau của matplotlib để tạo ra các biểu đồ này.