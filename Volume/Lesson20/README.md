# Làm quen với thư viện Matplotlib
## Giới thiệu
Matplotlib là một thư viện vẽ đồ họa dữ liệu mạnh mẽ và phổ biến trong ngôn ngữ lập trình Python. Nó cung cấp các công cụ để tạo ra nhiều loại biểu đồ, từ biểu đồ đơn giản như đồ thị đường, đồ thị cột, đến biểu đồ phức tạp như biểu đồ 3D, biểu đồ phân tán. Matplotlib được sử dụng rộng rãi trong nhiều lĩnh vực như khoa học, kỹ thuật, tài chính, và giáo dục.

## Lý thuyết
Để sử dụng Matplotlib, bạn cần hiểu về các thành phần cơ bản của nó. Một số khái niệm quan trọng bao gồm:
- **Figure**: Là toàn bộ cửa sổ chứa đồ họa.
- **Axes**: Là khu vực chứa đồ họa thực sự, có thể có nhiều Axes trong một Figure.
- **Plot**: Là đồ họa được vẽ trên Axes, có thể là đường, cột, điểm, v.v.

Matplotlib cung cấp nhiều hàm để tạo ra các loại biểu đồ khác nhau, chẳng hạn như `plot()` cho đồ thị đường, `bar()` cho đồ thị cột, và `scatter()` cho biểu đồ phân tán. Bạn cũng có thể tùy chỉnh biểu đồ bằng cách thêm tiêu đề, nhãn cho trục, và chú thích.

## Ví dụ
Dưới đây là một ví dụ đơn giản về việc sử dụng Matplotlib để vẽ một đồ thị đường:
```python
import matplotlib.pyplot as plt

# Dữ liệu
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo biểu đồ
plt.plot(x, y)

# Thêm tiêu đề và nhãn cho trục
plt.title('Đồ thị đường')
plt.xlabel('X')
plt.ylabel('Y')

# Hiển thị biểu đồ
plt.show()
```
Kết quả sẽ là một đồ thị đường đơn giản với dữ liệu từ `x` và `y`.

## Bài tập
Để làm quen với Matplotlib, hãy thử thực hiện các bài tập sau:
1. Vẽ một biểu đồ cột với dữ liệu `[10, 20, 30, 40, 50]` trên trục Y và `[1, 2, 3, 4, 5]` trên trục X.
2. Tạo một biểu đồ phân tán với dữ liệu `x = [1, 2, 3, 4, 5]` và `y = [2, 4, 6, 8, 10]`.
3. Thêm tiêu đề, nhãn cho trục, và chú thích cho mỗi biểu đồ.

Bằng cách hoàn thành các bài tập này, bạn sẽ có một cái nhìn tổng quan về cách sử dụng Matplotlib và có thể bắt đầu tạo ra các biểu đồ phức tạp hơn cho dự án của mình.