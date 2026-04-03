# Bài học Python số 82 - Cấp độ Nâng cao

## Chủ đề: Sử dụng và Tạo Context Managers Tự Định Nghĩa

Trong bài học này, chúng ta sẽ tìm hiểu về **Context Managers** (Trình quản lý ngữ cảnh) trong Python — một kỹ thuật mạnh mẽ để quản lý tài nguyên một cách an toàn và sạch sẽ. Chúng ta không chỉ học cách sử dụng `with` với các đối tượng có sẵn như file, mà còn học cách **tạo ra Context Manager riêng** bằng cả lớp và hàm với `contextlib`.

Context Manager giúp đảm bảo rằng tài nguyên được **khởi tạo và giải phóng đúng cách**, ngay cả khi có lỗi xảy ra. Đây là kỹ năng quan trọng khi làm việc với file, kết nối cơ sở dữ liệu, khóa (lock), hay tài nguyên tạm thời.

---

### 1. Mục tiêu bài học

- Hiểu khái niệm và lợi ích của Context Manager.
- Biết cách sử dụng `with` để làm việc với tài nguyên.
- Tạo Context Manager bằng cách triển khai lớp (class-based).
- Tạo Context Manager bằng hàm với decorator `@contextmanager`.
- Áp dụng Context Manager vào các tình huống thực tế.

### 2. Lý thuyết chi tiết

#### a) Context Manager là gì?

Context Manager là một đối tượng thực hiện giao diện quản lý ngữ cảnh, cho phép bạn thực hiện các hành động **trước khi bắt đầu** và **sau khi kết thúc** một khối lệnh. Nó được sử dụng phổ biến với câu lệnh `with`.

Cú pháp:
```python
with context_manager:
    # khối lệnh
```

Python sẽ tự động gọi:
- `__enter__()` trước khi vào khối lệnh.
- `__exit__()` sau khi ra khỏi khối lệnh, kể cả khi có lỗi.

#### b) Triển khai Context Manager bằng lớp

Một lớp trở thành Context Manager nếu nó có hai phương thức:
- `__enter__(self)`
- `__exit__(self, exc_type, exc_value, traceback)`

Ví dụ:
```python
class MyContext:
    def __enter__(self):
        print("Bắt đầu...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Kết thúc.")
        if exc_type:
            print(f"Có lỗi: {exc_value}")
        return False  # Không chặn ngoại lệ
```

#### c) Dùng `@contextmanager` từ `contextlib`

Thư viện `contextlib` cung cấp decorator `@contextmanager` để tạo Context Manager từ hàm sinh (generator).

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Bắt đầu...")
    try:
        yield "dữ liệu"
    finally:
        print("Kết thúc.")
```

Khối `try...finally` đảm bảo hành động dọn dẹp luôn được thực hiện.

### 3. Ví dụ minh họa

Xem file `main.py` để chạy các ví dụ thực tế:
- Quản lý file tạm thời.
- Đo thời gian thực thi.
- Quản lý kết nối cơ sở dữ liệu giả lập.

### 4. Bài tập thực hành

Xem file `exercises.py` để làm bài tập. Sau đó kiểm tra lời giải trong `solutions.py`.

### 5. Tổng kết

Context Manager là công cụ mạnh mẽ để viết mã an toàn, sạch sẽ và dễ bảo trì. Việc tự tạo Context Manager giúp bạn đóng gói logic quản lý tài nguyên một cách chuyên nghiệp. Dù bạn dùng lớp hay `@contextmanager`, hãy luôn đảm bảo tài nguyên được giải phóng đúng lúc.

Sử dụng `with` không chỉ là thói quen tốt — đó là **best practice** trong Python.
