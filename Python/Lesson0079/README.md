# Bài học Python nâng cao số 79: Lập trình phản xạ (Reflection) và sử dụng `inspect` module

## Mục tiêu bài học
- Hiểu được khái niệm lập trình phản xạ (reflection) trong Python.
- Biết cách sử dụng module `inspect` để khám phá cấu trúc mã nguồn tại thời điểm chạy.
- Ứng dụng `inspect` để ghi log thông tin hàm, kiểm tra tham số, tự động tạo tài liệu, và gỡ lỗi nâng cao.
- Phát triển các công cụ hỗ trợ lập trình như validator, decorator thông minh, hoặc framework nhỏ.

## Lý thuyết chi tiết

### 1. Lập trình phản xạ (Reflection) là gì?
Lập trình phản xạ là khả năng của một chương trình trong việc tự kiểm tra, phân tích và thay đổi cấu trúc hoặc hành vi của chính nó trong lúc chạy. Python hỗ trợ phản xạ rất mạnh mẽ nhờ vào bản chất "object mọi thứ".

Ví dụ:
- Kiểm tra kiểu dữ liệu của một biến bằng `type()`.
- Lấy danh sách thuộc tính của một đối tượng bằng `dir()`.
- Lấy giá trị thuộc tính bằng `getattr()`.

### 2. Module `inspect`
Module `inspect` cung cấp nhiều hàm để thu thập thông tin về các đối tượng đang chạy: hàm, lớp, phương thức, tham số, stack frame, v.v.

Một số hàm quan trọng:
- `inspect.getmembers(obj)`: Trả về danh sách các cặp (tên, giá trị) của tất cả thành viên trong đối tượng.
- `inspect.isfunction(obj)`, `inspect.isclass(obj)`: Kiểm tra loại đối tượng.
- `inspect.signature(func)`: Lấy chữ ký (signature) của hàm, bao gồm tham số, kiểu, giá trị mặc định.
- `inspect.getsource(obj)`: Lấy mã nguồn của đối tượng (nếu có sẵn).
- `inspect.stack()`: Lấy thông tin về các frame trong call stack.

### Ví dụ nhỏ:
```python
import inspect

def hello(name: str, age: int = 20):
    pass

sig = inspect.signature(hello)
for name, param in sig.parameters.items():
    print(f'{name}: {param.annotation} = {param.default}')
```

## Ví dụ minh họa

### Ví dụ 1: Tự động ghi log tham số đầu vào của hàm
Tạo decorator ghi log các tham số được truyền vào hàm bằng `inspect`.

### Ví dụ 2: Trích xuất thông tin hàm để tạo tài liệu API đơn giản
Lấy tên hàm, tham số, kiểu, giá trị mặc định để in ra mô tả API.

### Ví dụ 3: Kiểm tra loại tham số tại thời điểm chạy (Runtime type checking)
Sử dụng `inspect` để kiểm tra kiểu dữ liệu của tham số truyền vào, cảnh báo nếu không khớp với type hint.

## Bài tập thực hành
1. Viết decorator `@log_calls` ghi log tên hàm và các tham số khi được gọi.
2. Viết hàm `describe_function(func)` in ra mô tả chi tiết về một hàm (tên, tham số, kiểu, mặc định, docstring).
3. Viết decorator `@type_check` kiểm tra kiểu dữ liệu của tham số truyền vào dựa trên type hint.
4. Viết hàm `find_functions_in_module(module, min_params=2)` tìm tất cả hàm trong một module có ít nhất `min_params` tham số.
5. Viết hàm `print_call_stack()` in ra danh sách các hàm đang được gọi (tên hàm và file) từ điểm hiện tại.

## Tổng kết
Module `inspect` là một công cụ mạnh mẽ trong Python cho các tác vụ nâng cao như tự động hóa, gỡ lỗi, tạo framework, hoặc xây dựng công cụ phân tích mã nguồn. Việc sử dụng `inspect` hợp lý giúp tăng tính linh hoạt và khả năng bảo trì của hệ thống. Tuy nhiên, cần cẩn trọng vì lạm dụng có thể làm giảm hiệu năng và tăng độ phức tạp.

Học viên nên luyện tập thường xuyên với các ví dụ và bài tập để làm chủ kỹ năng này, đặc biệt khi phát triển thư viện hoặc công cụ nội bộ.