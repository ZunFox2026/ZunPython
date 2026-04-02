# Làm quen với thư viện matplotlib
## Giới thiệu
Thư viện matplotlib là một trong những thư viện phổ biến nhất trong Python, được sử dụng để tạo ra các biểu đồ và hình ảnh chất lượng cao. Nó cung cấp một giải pháp mạnh mẽ và linh hoạt để tạo ra các biểu đồ 2D và 3D, từ các biểu đồ đơn giản như biểu đồ đường, biểu đồ cột đến các biểu đồ phức tạp hơn như biểu đồ phân tán, biểu đồsurface.

Matplotlib được thiết kế để tương tác với các thư viện khác trong Python như NumPy, SciPy và Pandas, giúp cho việc phân tích và trực quan hóa dữ liệu trở nên dễ dàng hơn. Trong bài này, chúng ta sẽ tìm hiểu cách làm quen với thư viện matplotlib và cách sử dụng nó để tạo ra các biểu đồ cơ bản.

## Lý thuyết
Để bắt đầu sử dụng matplotlib, bạn cần hiểu một số khái niệm cơ bản về cách nó hoạt động. Matplotlib sử dụng một hệ thống lưới để tạo ra các biểu đồ, với các trục x, y và z được định nghĩa bởi người dùng. Các biểu đồ được tạo ra bằng cách sử dụng các hàm như plot(), scatter(), bar(), v.v.

Một số khái niệm quan trọng khác trong matplotlib bao gồm:

* Figure: Đây là cửa sổ chính chứa biểu đồ
* Axes: Đây là khu vực chứa biểu đồ, có thể có nhiều axes trong một figure
* Plot: Đây là biểu đồ được tạo ra bằng cách sử dụng các hàm như plot(), scatter(), v.v.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách sử dụng matplotlib để tạo ra một biểu đồ đường:
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Biểu đồ đường')
plt.show()
```
Đây là ví dụ về cách tạo ra một biểu đồ cột:
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.bar(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Biểu đồ cột')
plt.show()
```
## Bài tập
Để thực hành sử dụng matplotlib, bạn có thể thực hiện các bài tập sau:

* Tạo ra một biểu đồ phân tán với 2 biến ngẫu nhiên
* Tạo ra một biểu đồ đường với 2 hàm số khác nhau
* Tạo ra một biểu đồ cột với dữ liệu thực tế

Hãy nhớ rằng, việc thực hành là chìa khóa để trở thành thành thạo trong sử dụng matplotlib. Bạn có thể tìm kiếm các tài liệu và ví dụ khác trên internet để giúp bạn hiểu rõ hơn về cách sử dụng matplotlib.