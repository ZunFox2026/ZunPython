# Bài học Python Nâng cao 44: Lập trình phản xạ (Reflection) và sử dụng `inspect`

## Mục tiêu bài học
- Hiểu khái niệm lập trình phản xạ (reflection) trong Python.
- Sử dụng module `inspect` để truy vấn thông tin về các đối tượng, hàm, lớp, và stack.
- Áp dụng phản xạ để viết mã linh hoạt, tự động phát hiện và xử lý các thành phần trong chương trình.
- Biết cách debug và ghi log thông minh bằng cách trích xuất thông tin từ ngữ cảnh thực thi.

## Lý thuyết chi tiết

**Lập trình phản xạ (Reflection)** là khả năng của một chương trình trong việc tự kiểm tra, phân tích và thay đổi cấu trúc hoặc hành vi của chính nó trong lúc chạy. Python hỗ trợ rất mạnh lập trình phản xạ nhờ vào bản chất động của ngôn ngữ.

Module `inspect` trong Python cung cấp các hàm mạnh mẽ để lấy thông tin về các đối tượng như: hàm, lớp, phương thức, module, stack frame...

### Một số hàm quan trọng trong `inspect`:

- `inspect.getmembers(obj)`: Trả về danh sách các thành viên (thuộc tính, phương thức) của đối tượng.
- `inspect.isfunction(obj)`, `inspect.isclass(obj)`, `inspect.ismethod(obj)`: Kiểm tra loại đối tượng.
- `inspect.getsource(obj)`: Lấy mã nguồn của đối tượng (nếu có).
- `inspect.getfile(obj)`: Trả về đường dẫn file chứa đối tượng.
- `inspect.stack()`: Trả về thông tin về các frame trong stack gọi hàm.
- `inspect.signature(obj)`: Trả về thông tin về tham số của hàm.

### Ví dụ đơn giản:

```python
import inspect

def hello(name):
    return f"Xin chào {name}!"

# Lấy chữ ký hàm
sig = inspect.signature(hello)
print(sig)  # (name)

# Lấy danh sách tham số
for param in sig.parameters.values():
    print(param.name, param.kind)
```

## Ví dụ minh họa

### Ví dụ 1: Tự động ghi log tên hàm và tham số
Viết một decorator dùng `inspect` để ghi log tự động tên hàm và các tham số đầu vào.

### Ví dụ 2: Liệt kê tất cả các hàm trong một module
Duyệt qua một module và in ra danh sách các hàm cùng mã nguồn của chúng.

### Ví dụ 3: Gỡ lỗi bằng thông tin stack
Tự động in ra tên hàm, file và dòng lệnh đang thực thi khi có lỗi.

## Bài tập thực hành
1. Viết hàm `print_class_info(cls)` in ra tất cả phương thức và thuộc tính của một lớp.
2. Viết decorator `@debug_call` ghi log khi một hàm được gọi, bao gồm tên hàm, tham số và giá trị trả về.
3. Viết hàm `find_functions_by_name(module, name)` tìm tất cả các hàm trong một module có tên chứa chuỗi `name`.
4. Viết hàm `get_caller_info()` trả về tên hàm và số dòng của hàm gọi nó.
5. Tạo một công cụ kiểm tra nhanh mã nguồn: hàm `show_source_if_available(obj)` in mã nguồn nếu có, nếu không thì báo.

## Tổng kết
Lập trình phản xạ và module `inspect` là công cụ mạnh mẽ giúp chúng ta viết mã linh hoạt, tự động và thông minh hơn. Khi kết hợp với decorator, logging, hay các framework tự động hóa, `inspect` giúp giảm đáng kể lượng mã lặp lại và tăng khả năng bảo trì. Tuy nhiên, cần sử dụng cẩn trọng vì có thể làm giảm hiệu năng và làm mã khó hiểu nếu lạm dụng.

Hãy luyện tập các bài tập để thành thạo kỹ năng này – đây là nền tảng cho nhiều thư viện lớn như Flask, Django, hay các công cụ testing và mocking.