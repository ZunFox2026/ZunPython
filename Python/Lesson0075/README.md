# Bài học Python nâng cao số 75: Làm việc với Context Managers và `__enter__`, `__exit__`

## Mục tiêu bài học
- Hiểu rõ khái niệm **Context Manager** trong Python.
- Biết cách sử dụng `with` để quản lý tài nguyên một cách an toàn.
- Thực hiện tạo **Context Manager** tùy chỉnh bằng cách sử dụng phương thức `__enter__` và `__exit__`.
- Áp dụng Context Manager trong các tình huống thực tế như xử lý file, kết nối cơ sở dữ liệu, đo thời gian thực thi, v.v.

## Lý thuyết chi tiết

### 1. Context Manager là gì?
Context Manager (trình quản lý ngữ cảnh) là một khái niệm trong Python cho phép bạn **thiết lập và dọn dẹp tài nguyên một cách tự động** trong một khối code nhất định, thường thông qua câu lệnh `with`.

Cú pháp phổ biến:
```python
with open('file.txt', 'r') as f:
    data = f.read()
# File tự động đóng sau khi ra khỏi khối `with`
```

### 2. Nguyên lý hoạt động
Một đối tượng trở thành Context Manager nếu nó định nghĩa hai phương thức đặc biệt:
- `__enter__(self)`: được gọi khi bắt đầu khối `with`, trả về giá trị gán cho biến sau `as`.
- `__exit__(self, exc_type, exc_value, traceback)`: được gọi khi thoát khối `with`, cho dù có lỗi hay không.

Trong đó:
- `exc_type`: loại ngoại lệ (nếu có), nếu không có thì là `None`.
- `exc_value`: giá trị ngoại lệ.
- `traceback`: đối tượng traceback (dấu vết lỗi).

Nếu `__exit__` trả về `True`, ngoại lệ sẽ bị **ngăn chặn** (không ném ra ngoài). Nếu trả về `False` hoặc `None`, ngoại lệ sẽ được ném tiếp.

### 3. Tạo Context Manager tùy chỉnh
Bạn có thể tạo class có `__enter__` và `__exit__` để trở thành Context Manager.

Ví dụ đơn giản:
```python
class MyContext:
    def __enter__(self):
        print("Bắt đầu context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Kết thúc context")
        if exc_type is not None:
            print(f"Có lỗi xảy ra: {exc_value}")
        return False  # Không ngăn lỗi
```

## Ví dụ minh họa

### Ví dụ 1: Đo thời gian thực thi
Tạo Context Manager để đo thời gian thực hiện một đoạn code.

### Ví dụ 2: Quản lý kết nối cơ sở dữ liệu giả lập
Tạo một Context Manager mô phỏng việc mở và đóng kết nối CSDL.

### Ví dụ 3: Ghi log tự động khi bắt đầu và kết thúc
Tạo Context Manager ghi log khi vào và ra khỏi khối lệnh.

## Bài tập thực hành
1. Viết Context Manager để tạm thời thay đổi thư mục làm việc.
2. Viết Context Manager để đếm số lượng dòng trong file khi đọc.
3. Viết Context Manager để bắt lỗi và ghi log, nhưng không ngắt chương trình.
4. Viết Context Manager quản lý bộ nhớ đệm (cache) trong một khối lệnh.
5. Viết Context Manager in ra thông báo khi có ngoại lệ, nhưng cho phép chương trình tiếp tục.

## Tổng kết
Context Manager là một công cụ mạnh mẽ để quản lý tài nguyên trong Python một cách sạch sẽ và an toàn. Việc sử dụng `with` giúp tránh rò rỉ tài nguyên (như file mở không đóng, kết nối mạng không giải phóng). Ngoài việc sử dụng các Context Manager có sẵn như `open()`, bạn có thể tự tạo ra các Context Manager tùy chỉnh để phục vụ nhu cầu riêng, từ đo hiệu năng đến quản lý trạng thái.

Kiến thức này rất quan trọng khi làm việc với hệ thống, xử lý tài nguyên, hoặc xây dựng thư viện. Hãy luyện tập nhiều để thuần thục kỹ năng này!