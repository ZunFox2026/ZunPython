# Bài học Python nâng cao số 50: Lập trình phản xạ (Reflection) và sử dụng `inspect` module

## Mục tiêu bài học
- Hiểu được khái niệm **lập trình phản xạ (reflection)** trong Python.
- Biết cách sử dụng module `inspect` để khám phá cấu trúc code tại thời điểm chạy.
- Ứng dụng `inspect` để tự động hóa các tác vụ như ghi log, kiểm tra tham số, hoặc tạo tài liệu tự động.
- Nâng cao khả năng viết code linh hoạt và tự điều chỉnh hành vi dựa trên cấu trúc nội tại của chương trình.

## Lý thuyết chi tiết

### 1. Lập trình phản xạ (Reflection) là gì?
Lập trình phản xạ là khả năng của một chương trình trong việc **tự quan sát và thao tác chính nó** trong lúc chạy. Trong Python, điều này có nghĩa là bạn có thể:
- Kiểm tra các đối tượng (hàm, lớp, module)
- Lấy thông tin về tham số, thuộc tính, phương thức
- Gọi hàm hoặc truy cập thuộc tính một cách động

Python hỗ trợ reflection rất mạnh nhờ vào bản chất động (dynamic) của ngôn ngữ.

### 2. Module `inspect`
Module `inspect` là công cụ mạnh mẽ để thực hiện reflection. Nó cung cấp nhiều hàm hữu ích:

- `inspect.getmembers(obj)`: Lấy danh sách các thành viên của đối tượng.
- `inspect.isfunction(obj)`, `inspect.ismethod(obj)`, `inspect.isclass(obj)`: Kiểm tra loại đối tượng.
- `inspect.signature(func)`: Lấy chữ ký (tham số) của hàm.
- `inspect.getsource(obj)`: Lấy mã nguồn của đối tượng (nếu có).
- `inspect.stack()`: Lấy thông tin về ngăn xếp gọi hàm (call stack).

### Ví dụ cơ bản
```python
import inspect

def hello(name, age=20):
    """Chào một người"""
    print(f"Xin chào {name}, {age} tuổi.")

# Lấy thông tin về hàm
sig = inspect.signature(hello)
print(sig)  # (name, age=20)

for name, param in sig.parameters.items():
    print(f"Tham số: {name}, mặc định: {param.default}")
```

## Ví dụ minh họa

### Ví dụ 1: Tạo decorator ghi log tự động với thông tin tham số
Sử dụng `inspect.signature` để ghi log tham số đầu vào của hàm.

### Ví dụ 2: Kiểm tra và in ra tất cả phương thức của một lớp
Dùng `inspect.getmembers` và `inspect.ismethod` để liệt kê các phương thức.

### Ví dụ 3: Trích xuất mã nguồn và tài liệu của các hàm trong module
Tự động sinh tài liệu bằng cách đọc `__doc__` và `inspect.getsource()`.

## Bài tập thực hành
1. Viết hàm `print_caller_info()` in ra tên hàm đang gọi nó và tên hàm gọi hàm đó.
2. Viết decorator `@log_calls` ghi log tên hàm và các tham số được truyền vào.
3. Viết hàm `explore_module(module)` in ra tất cả hàm và lớp trong một module kèm mô tả.
4. Viết hàm `validate_types` kiểm tra kiểu tham số dựa trên type hints.
5. Viết hàm `find_functions_with_docstring(module)` tìm tất cả hàm có docstring trong một module.

## Tổng kết
Lập trình phản xạ và module `inspect` giúp chúng ta viết code thông minh hơn, tự động hơn. Đây là kỹ năng quan trọng khi phát triển framework, thư viện, công cụ kiểm thử, hoặc hệ thống logging và monitoring. Tuy nhiên, cần sử dụng cẩn trọng vì có thể làm code khó hiểu nếu lạm dụng.

Hãy luyện tập để thành thạo `inspect` — một trong những vũ khí mạnh nhất của lập trình viên Python nâng cao!
