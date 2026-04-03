# Bài học Python số 98: Lập trình phản xạ (Reflection) và sử dụng `inspect` để phân tích code động

## Mục tiêu bài học
- Hiểu được khái niệm **lập trình phản xạ (reflection)** trong Python.
- Biết cách sử dụng module `inspect` để khám phá các thành phần của chương trình như hàm, lớp, tham số, stack frame...
- Ứng dụng lập trình phản xạ để xây dựng các công cụ tự động như sinh tài liệu, kiểm tra kiểu, ghi log thông minh, hoặc framework kiểm thử.
- Nâng cao khả năng đọc hiểu và tương tác với code một cách động (dynamic).

## Lý thuyết chi tiết

### 1. Lập trình phản xạ là gì?
**Lập trình phản xạ** (reflection) là khả năng của một chương trình trong việc tự quan sát, phân tích và thay đổi cấu trúc hoặc hành vi của chính nó trong lúc chạy (runtime). Python hỗ trợ mạnh mẽ lập trình phản xạ thông qua các hàm dựng sẵn như `getattr`, `hasattr`, `setattr`, `type`, `dir`, và đặc biệt là module `inspect`.

### 2. Module `inspect`
Module `inspect` cung cấp nhiều công cụ mạnh mẽ để:
- Lấy thông tin về hàm, lớp, module, stack frame.
- Kiểm tra tham số, giá trị mặc định, annotations.
- Đọc mã nguồn của hàm hoặc lớp.
- Duyệt qua các frame đang chạy (stack).

#### Một số hàm quan trọng trong `inspect`:
- `inspect.getmembers(obj)`: Trả về danh sách các thành viên của đối tượng.
- `inspect.isfunction(obj)`, `inspect.isclass(obj)`: Kiểm tra loại đối tượng.
- `inspect.signature(func)`: Lấy chữ ký (signature) của hàm (tham số, kiểu, mặc định...).
- `inspect.getsource(obj)`: Lấy mã nguồn của đối tượng (nếu có).
- `inspect.currentframe()`: Lấy frame hiện tại — hữu ích để ghi log hoặc debug.

### 3. Ví dụ cơ bản
```python
import inspect

def hello(name: str, age: int = 20):
    return f"Xin chào {name}, {age} tuổi."

sig = inspect.signature(hello)
for name, param in sig.parameters.items():
    print(f"Tham số: {name}, Kiểu: {param.annotation}, Mặc định: {param.default}")
```

Kết quả:
```
Tham số: name, Kiểu: <class 'str'>, Mặc định: <class 'inspect._empty'>
Tham số: age, Kiểu: <class 'int'>, Mặc định: 20
```

## Ví dụ minh họa

### Ví dụ 1: Tự động sinh tài liệu từ hàm
Tạo một công cụ in ra tài liệu mô tả tất cả hàm trong một module.

### Ví dụ 2: Ghi log tự động tên hàm và tham số
Tạo decorator sử dụng `inspect` để ghi log tên hàm và tham số đầu vào.

### Ví dụ 3: Kiểm tra kiểu tham số tại runtime
Xây dựng một decorator kiểm tra kiểu dữ liệu của tham số dựa vào type hints.

## Bài tập thực hành
1. Viết hàm `print_class_info(cls)` in ra tất cả phương thức và thuộc tính của một lớp.
2. Viết decorator `@debug_calls` in ra tên hàm, tham số và giá trị trả về khi gọi hàm.
3. Viết hàm `get_caller_info()` dùng `inspect` để in ra tên hàm gọi nó và tên file.
4. Viết decorator `@require_kwargs_only` yêu cầu tất cả tham số sau khi gọi phải là keyword arguments.
5. Viết hàm `list_functions_in_module(module)` liệt kê tất cả hàm trong một module cùng số lượng tham số.

## Tổng kết
Lập trình phản xạ và module `inspect` là công cụ mạnh mẽ giúp Python trở thành ngôn ngữ linh hoạt và phù hợp để xây dựng các framework, công cụ kiểm thử, ghi log, hoặc hệ thống dependency injection. Việc hiểu rõ `inspect` giúp bạn:
- Viết code thông minh hơn, tự động tương tác với cấu trúc chương trình.
- Xây dựng các decorator và công cụ hỗ trợ phát triển.
- Debug và kiểm tra code một cách hiệu quả.

Tuy nhiên, cần sử dụng thận trọng vì lạm dụng phản xạ có thể làm code khó đọc, giảm hiệu năng và tăng rủi ro lỗi.
