# Bài học Python nâng cao số 89: Lập trình phản xạ (Reflection) và sử dụng `inspect` module

## Mục tiêu bài học
- Hiểu được khái niệm **lập trình phản xạ (reflection)** trong Python.
- Biết cách sử dụng module `inspect` để khám phá cấu trúc mã nguồn tại thời điểm chạy.
- Áp dụng `inspect` để ghi log chi tiết, kiểm tra tham số hàm, và tạo các công cụ phát triển tự động.
- Phát triển các ứng dụng linh hoạt hơn nhờ khả năng tự khám phá và điều chỉnh hành vi dựa trên mã nguồn.

## Lý thuyết chi tiết

### 1. Lập trình phản xạ (Reflection) là gì?
Lập trình phản xạ là khả năng của một chương trình trong việc **tự quan sát và thay đổi cấu trúc hoặc hành vi của chính nó** trong lúc chạy. Trong Python, điều này được hỗ trợ rất mạnh mẽ nhờ vào tính chất động của ngôn ngữ.

Một số thao tác phản xạ phổ biến:
- Kiểm tra kiểu dữ liệu: `type(obj)`, `isinstance(obj, cls)`
- Liệt kê thuộc tính: `dir(obj)`
- Lấy giá trị thuộc tính: `getattr(obj, 'attr')`
- Thiết lập thuộc tính: `setattr(obj, 'attr', value)`
- Kiểm tra sự tồn tại: `hasattr(obj, 'attr')`

Tuy nhiên, module `inspect` còn đi xa hơn: nó cho phép ta khám phá **thông tin về hàm, phương thức, tham số, stack call, mã nguồn**, v.v.

### 2. Module `inspect`
Module `inspect` cung cấp nhiều hàm hữu ích để kiểm tra đối tượng tại thời điểm chạy.

Một số hàm quan trọng:
- `inspect.getmembers(obj)`: trả về danh sách các thành viên của đối tượng.
- `inspect.isfunction(obj)`, `inspect.ismethod(obj)`: kiểm tra loại đối tượng.
- `inspect.signature(func)`: trả về thông tin về tham số của hàm (kiểu, mặc định, bắt buộc...).
- `inspect.getsource(obj)`: lấy mã nguồn của hàm hoặc lớp dưới dạng chuỗi.
- `inspect.stack()`: trả về thông tin về call stack hiện tại.

#### Ví dụ nhỏ:
```python
import inspect

def hello(name, age=20):
    pass

sig = inspect.signature(hello)
for param in sig.parameters.values():
    print(param.name, param.default)
```

## Ví dụ minh họa

### Ví dụ 1: Ghi log tự động thông tin tham số hàm
Tạo một decorator sử dụng `inspect` để in ra các tham số được truyền vào hàm.

### Ví dụ 2: Kiểm tra và in mã nguồn của các hàm trong một module
Duyệt qua tất cả các hàm trong module hiện tại và in ra mã nguồn của chúng.

### Ví dụ 3: Debug call stack khi có lỗi
Tự động in ra đường đi của các lời gọi hàm khi xảy ra lỗi.

## Bài tập thực hành
1. Viết decorator `@log_calls` ghi log tên hàm và tham số (kể cả tham số keyword) khi hàm được gọi.
2. Viết hàm `print_function_sources(module)` in mã nguồn của tất cả các hàm trong một module.
3. Viết hàm `analyze_function_params(func)` in chi tiết tất cả tham số của một hàm: tên, kiểu (nếu có), giá trị mặc định.
4. Viết hàm `who_called_me()` in ra tên hàm đã gọi hàm hiện tại.
5. Tạo một decorator `@validate_types` kiểm tra kiểu dữ liệu của tham số đầu vào dựa trên type hints.

## Tổng kết
- Lập trình phản xạ giúp Python trở nên cực kỳ linh hoạt.
- Module `inspect` là công cụ mạnh để xây dựng các công cụ phát triển, debug, logging, và serialization.
- Khi sử dụng phản xạ, cần cân nhắc giữa tính linh hoạt và hiệu năng, vì các thao tác kiểm tra tại runtime có thể chậm hơn.
- Các ứng dụng thực tế: framework web (Flask, FastAPI), ORM (SQLAlchemy), công cụ test, IDE hỗ trợ.

> **Lưu ý**: Dù mạnh mẽ, phản xạ nên được dùng đúng chỗ — tránh làm mã nguồn khó hiểu hoặc giảm hiệu năng không cần thiết.