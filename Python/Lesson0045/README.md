# Bài học Python nâng cao số 45: Làm việc với Context Managers và Protocol `__enter__`, `__exit__`

## Mục tiêu bài học
- Hiểu rõ khái niệm context manager và tầm quan trọng của nó trong quản lý tài nguyên.
- Nắm vững cách tạo và sử dụng context manager bằng phương thức `__enter__` và `__exit__`.
- Biết cách sử dụng `contextlib` để tạo context manager đơn giản hơn.
- Ứng dụng context manager trong các tình huống thực tế như xử lý file, kết nối cơ sở dữ liệu, đo thời gian thực thi, v.v.

## Lý thuyết chi tiết

### 1. Context Manager là gì?
Context manager là một mẫu thiết kế (design pattern) trong Python giúp quản lý việc cấp phát và giải phóng tài nguyên một cách an toàn và sạch sẽ. Nó đảm bảo rằng tài nguyên luôn được giải phóng đúng cách, ngay cả khi có lỗi xảy ra.

Cú pháp phổ biến nhất của context manager là dùng với từ khóa `with`:

```python
with open('file.txt', 'r') as f:
    data = f.read()
```

Trong đoạn code trên, file sẽ tự động đóng sau khi ra khỏi khối `with`, kể cả khi có lỗi xảy ra.

### 2. Giao diện Context Manager
Một object là context manager nếu nó định nghĩa hai phương thức:
- `__enter__`: Được gọi khi bắt đầu khối `with`. Trả về giá trị gán cho biến sau `as`.
- `__exit__`: Được gọi khi kết thúc khối `with`. Xử lý việc dọn dẹp tài nguyên. Nó nhận 3 tham số: `exc_type`, `exc_value`, `traceback`. Nếu trả về `True`, ngoại lệ sẽ bị kìm nén.

### 3. Tạo Context Manager từ lớp
Bạn có thể tự tạo một context manager bằng cách định nghĩa lớp có hai phương thức `__enter__` và `__exit__`.

### 4. Tạo Context Manager bằng `@contextmanager`
Module `contextlib` cung cấp decorator `@contextmanager`, cho phép tạo context manager từ hàm sinh (generator), giúp viết ngắn gọn hơn.

## Ví dụ minh họa

### Ví dụ 1: Context Manager cho việc đo thời gian thực thi
Tạo một context manager để đo thời gian thực hiện một đoạn code.

### Ví dụ 2: Quản lý kết nối cơ sở dữ liệu giả lập
Mô phỏng việc mở và đóng kết nối CSDL một cách an toàn.

### Ví dụ 3: Context Manager dùng `@contextmanager` để tạm thời thay đổi thư mục làm việc
Sử dụng `contextlib.contextmanager` để tạo context manager thay đổi thư mục tạm thời.

## Bài tập thực hành
1. Tạo context manager để ghi log thời gian bắt đầu và kết thúc một hành động.
2. Viết context manager quản lý việc mở file JSON để đọc/ghi an toàn.
3. Tạo context manager đếm số lượng dòng được xử lý trong một file văn bản.
4. Viết context manager để tạm thời thay đổi giá trị một biến môi trường.
5. Tạo context manager xử lý ngoại lệ và ghi log nếu có lỗi xảy ra.

## Tổng kết
Context manager là công cụ mạnh mẽ để quản lý tài nguyên và đảm bảo tính an toàn khi làm việc với các tác vụ như mở file, kết nối mạng, hay thay đổi trạng thái hệ thống. Việc sử dụng `with` cùng context manager giúp code rõ ràng, dễ bảo trì và tránh được các lỗi phổ biến như quên đóng tài nguyên. Nắm vững context manager là bước quan trọng khi phát triển ứng dụng Python chuyên nghiệp.