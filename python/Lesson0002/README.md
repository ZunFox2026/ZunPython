# Làm quen với thư viện matplotlib
## Giới thiệu
matplotlib là một thư viện đồ họa nổi tiếng của Python, được sử dụng rộng rãi trong việc tạo ra các biểu đồ, đồ thị và hình ảnh. Thư viện này cung cấp một giải pháp mạnh mẽ và linh hoạt cho việc tạo ra các hình ảnh đồ họa, từ các biểu đồ đơn giản đến các hình ảnh phức tạp. Trong bài này, chúng ta sẽ tìm hiểu về cách sử dụng matplotlib để tạo ra các biểu đồ và đồ thị.

## Lý thuyết
matplotlib cung cấp một số lượng lớn các công cụ và tính năng để tạo ra các biểu đồ và đồ thị. Một số tính năng chính của matplotlib bao gồm:
* Tạo ra các biểu đồ 2D và 3D
* Tạo ra các đồ thị với nhiều loại biểu đồ khác nhau, chẳng hạn như biểu đồ cột, biểu đồ tròn, biểu đồ đường thẳng
* Tùy chỉnh màu sắc, kích thước và kiểu dáng của biểu đồ
* Thêm tiêu đề, nhãn và chú thích vào biểu đồ
* Lưu biểu đồ vào file hình ảnh

Để sử dụng matplotlib, chúng ta cần nhập thư viện này vào chương trình Python của mình bằng cách sử dụng lệnh `import matplotlib.pyplot as plt`. Sau đó, chúng ta có thể sử dụng các hàm và tính năng của matplotlib để tạo ra các biểu đồ và đồ thị.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách sử dụng matplotlib để tạo ra một biểu đồ cột:
```python
import matplotlib.pyplot as plt

# Dữ liệu
danh_sach = [10, 20, 30, 40, 50]

# Tạo biểu đồ
plt.bar(range(len(danh_sach)), danh_sach)

# Thêm tiêu đề và nhãn
plt.title('Biểu đồ cột')
plt.xlabel('X')
plt.ylabel('Y')

# Hiển thị biểu đồ
plt.show()
```
Kết quả của ví dụ này sẽ là một biểu đồ cột đơn giản với tiêu đề, nhãn và dữ liệu được hiển thị.

## Bài tập
Bài tập này yêu cầu bạn tạo ra một biểu đồ tròn với các dữ liệu sau:
* Dữ liệu: `[25, 30, 20, 15, 10]`
* Tiêu đề: `Biểu đồ tròn`
* Nhãn: `Dữ liệu`
* Màu sắc: `['red', 'green', 'blue', 'yellow', 'purple']`
* Lưu biểu đồ vào file hình ảnh với tên `bieu_do_tron.png`

Hãy sử dụng các tính năng và công cụ của matplotlib để hoàn thành bài tập này.