# Bài học Python nâng cao số 76: Lập trình phản xạ (Reflection) và sử dụng `inspect` module

Trong bài học này, chúng ta sẽ tìm hiểu về **lập trình phản xạ (reflection)** trong Python — một kỹ thuật nâng cao cho phép chương trình tự kiểm tra, phân tích và thay đổi cấu trúc hoặc hành vi của chính nó trong lúc chạy. Đây là một chủ đề quan trọng khi làm việc với các framework như Django, Flask, hay khi phát triển công cụ kiểm thử, serialization, hoặc các decorator mạnh mẽ.

Chúng ta sẽ tập trung vào module `inspect` — một công cụ mạnh mẽ trong thư viện chuẩn của Python để thu thập thông tin về các đối tượng đang chạy.

## 1. Mục tiêu bài học

- Hiểu khái niệm **lập trình phản xạ** trong Python.
- Sử dụng được module `inspect` để:
  - Lấy thông tin về hàm, lớp, phương thức.
  - Kiểm tra tham số, giá trị mặc định, kiểu dữ liệu.
  - Đọc docstring và dòng mã nguồn.
- Áp dụng vào các tình huống thực tế như ghi log tự động, kiểm thử, và xây dựng framework nhỏ.

## 2. Lý thuyết chi tiết

### 2.1. Lập trình phản xạ là gì?

Lập trình phản xạ (reflection) là khả năng của một chương trình để **tự quan sát và thay đổi cấu trúc hoặc hành vi của chính nó** trong lúc thực thi. Trong Python, điều này được hỗ trợ mạnh mẽ nhờ vào tính chất động của ngôn ngữ.

Các thao tác phản xạ phổ biến:
- Kiểm tra kiểu dữ liệu (`isinstance`, `type`).
- Lấy danh sách thuộc tính (`dir()`).
- Kiểm tra xem đối tượng có thuộc tính nào đó (`hasattr`, `getattr`, `setattr`).
- Gọi phương thức động (`getattr(obj, 'method')()`).

### 2.2. Module `inspect`

Module `inspect` giúp chúng ta **lấy thông tin chi tiết về các đối tượng** như hàm, lớp, module, frame, v.v.

Một số hàm quan trọng:

- `inspect.getmembers(obj)`: Trả về danh sách các cặp (tên, giá trị) của các thành viên trong đối tượng.
- `inspect.isfunction(obj)`, `inspect.isclass(obj)`: Kiểm tra loại đối tượng.
- `inspect.signature(func)`: Trả về thông tin về tham số của hàm (tham số bắt buộc, mặc định, *args, **kwargs).
- `inspect.getsource(obj)`: Lấy mã nguồn của đối tượng (nếu có).
- `inspect.getdoc(obj)`: Lấy docstring của đối tượng.
- `inspect.stack()`: Lấy thông tin về ngăn xếp gọi hàm.

### 2.3. Ví dụ cơ bản

```python
import inspect

def hello(name: str, age: int = 20):
    """Chào một người với tên và tuổi."""
    print(f"Xin chào {name}, bạn {age} tuổi.")

# Lấy chữ ký hàm
sig = inspect.signature(hello)
print(sig)  # (name: str, age: int = 20)

# Duyệt các tham số
for param in sig.parameters.values():
    print(param.name, param.annotation, param.default)
```

## 3. Ví dụ minh họa

Dưới đây là 3 ví dụ hoàn chỉnh minh họa cách sử dụng `inspect` trong thực tế.

### Ví dụ 1: Trình ghi log tự động tham số hàm

Tạo một decorator ghi log tự động các tham số đầu vào của hàm khi gọi.

### Ví dụ 2: Kiểm tra và hiển thị mã nguồn của một lớp

In ra mã nguồn của một lớp và danh sách các phương thức.

### Ví dụ 3: Framework nhỏ tự động đăng ký hàm xử lý

Xây dựng một bộ xử lý lệnh đơn giản tự động phát hiện các hàm xử lý dựa trên tên hoặc decorator.

## 4. Bài tập thực hành

1. Viết hàm `print_function_info(func)` in ra toàn bộ thông tin về một hàm: tên, docstring, tham số, kiểu dữ liệu, giá trị mặc định.
2. Viết decorator `@validate_types` kiểm tra kiểu dữ liệu tham số đầu vào dựa trên type hints.
3. Viết hàm `find_test_functions(module)` tìm tất cả các hàm trong một module có tên bắt đầu bằng `test_` và trả về danh sách tên hàm.
4. Viết hàm `list_public_methods(cls)` liệt kê tất cả phương thức công khai của một lớp (không bắt đầu bằng `_`).
5. Viết decorator `@log_call` ghi lại tên hàm, tham số, và giá trị trả về vào file log.

## 5. Tổng kết

- Lập trình phản xạ giúp Python trở nên linh hoạt và mạnh mẽ.
- Module `inspect` là công cụ không thể thiếu khi làm việc với meta-programming.
- Ứng dụng: logging, testing, serialization, framework, ORM, CLI tools.
- Cần cẩn trọng khi dùng vì có thể làm giảm hiệu suất và gây khó hiểu nếu lạm dụng.

Hãy thực hành kỹ các ví dụ và bài tập để nắm vững kỹ năng này!
