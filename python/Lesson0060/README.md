# Làm việc với thư viện matplotlib
## Giới thiệu
Thư viện matplotlib là một trong những thư viện phổ biến nhất trong Python để tạo ra các biểu đồ và hình ảnh. Nó cung cấp một cách linh hoạt và dễ dàng để tạo ra các biểu đồ 2D và 3D, từ các biểu đồ đơn giản như đồ thị đường thẳng, đồ thị cột, đến các biểu đồ phức tạp hơn như đồ thị 3D, đồ thị phân tán. Trong bài này, chúng ta sẽ tìm hiểu cách làm việc với thư viện matplotlib để tạo ra các biểu đồ và hình ảnh.

## Lý thuyết
Để bắt đầu làm việc với thư viện matplotlib, bạn cần cài đặt nó vào môi trường Python của mình. Bạn có thể làm điều này bằng cách chạy lệnh `pip install matplotlib` trong terminal. Sau khi cài đặt, bạn có thể nhập thư viện vào chương trình Python của mình bằng cách sử dụng lệnh `import matplotlib.pyplot as plt`. Thư viện matplotlib cung cấp nhiều chức năng khác nhau để tạo ra các biểu đồ, chẳng hạn như `plot()` để tạo ra đồ thị đường thẳng, `bar()` để tạo ra đồ thị cột, và `hist()` để tạo ra đồ thị phân phối.

Thư viện matplotlib cũng cung cấp nhiều tùy chọn để tùy chỉnh biểu đồ, chẳng hạn như màu sắc, kích thước, và tiêu đề. Bạn có thể sử dụng các hàm như `title()` để thêm tiêu đề cho biểu đồ, `xlabel()` và `ylabel()` để thêm nhãn cho trục x và y, và `legend()` để thêm chú thích cho biểu đồ.

## Ví dụ
Dưới đây là một ví dụ đơn giản về cách sử dụng thư viện matplotlib để tạo ra một đồ thị đường thẳng:
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title('Đồ thị đường thẳng')
plt.xlabel('Trục x')
plt.ylabel('Trục y')
plt.show()
```
Ví dụ này sẽ tạo ra một đồ thị đường thẳng với tiêu đề "Đồ thị đường thẳng" và nhãn cho trục x và y. Bạn cũng có thể thêm nhiều đường thẳng vào biểu đồ bằng cách sử dụng hàm `plot()` nhiều lần.

## Bài tập
Bài tập này yêu cầu bạn tạo ra một biểu đồ cột để thể hiện số lượng sinh viên trong mỗi lớp học. Giả sử bạn có một danh sách các lớp học và số lượng sinh viên trong mỗi lớp học như sau:
```python
lop_hoc = ['Lớp 1', 'Lớp 2', 'Lớp 3', 'Lớp 4', 'Lớp 5']
so_luong_sinh_vien = [20, 25, 30, 22, 28]
```
Yêu cầu bạn tạo ra một biểu đồ cột để thể hiện số lượng sinh viên trong mỗi lớp học, với tiêu đề "Số lượng sinh viên trong mỗi lớp học" và nhãn cho trục x và y. Bạn cũng cần thêm chú thích cho biểu đồ để chỉ ra số lượng sinh viên trong mỗi lớp học.