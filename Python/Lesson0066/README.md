# Bài học Python Nâng cao - Bài 66: Lập trình phản xạ (Reflection) và sử dụng `inspect` để phân tích code tại runtime

Trong bài học này, chúng ta sẽ tìm hiểu về **lập trình phản xạ (reflection)** trong Python — một kỹ thuật nâng cao cho phép chương trình tự kiểm tra, phân tích và thay đổi cấu trúc hoặc hành vi của chính nó trong lúc chạy (runtime). Đây là một chủ đề quan trọng khi làm việc với các framework như Flask, Django, hoặc khi xây dựng các công cụ phân tích, debug, hoặc kiểm thử tự động.

Chúng ta sẽ tập trung vào module `inspect` — một công cụ mạnh mẽ trong thư viện chuẩn của Python để truy vấn thông tin về các đối tượng như hàm, lớp, phương thức, tham số, và thậm chí là mã nguồn.

---

## 1. Mục tiêu bài học

- Hiểu được khái niệm **lập trình phản xạ (reflection)** trong Python.
- Biết sử dụng module `inspect` để lấy thông tin về các đối tượng trong chương trình.
- Ứng dụng `inspect` để:
  - Liệt kê các phương thức và thuộc tính của một lớp.
  - Trích xuất thông tin tham số của hàm (tên, kiểu, giá trị mặc định).
  - Đọc mã nguồn của hàm hoặc lớp.
  - Kiểm tra ngăn xếp gọi hàm (call stack).
- Xây dựng các công cụ tự động kiểm tra hoặc ghi log thông minh.

---

## 2. Lý thuyết chi tiết

### 2.1. Lập trình phản xạ là gì?

**Lập trình phản xạ** (Reflection) là khả năng của một chương trình để tự quan sát, phân tích và thay đổi cấu trúc hoặc hành vi của chính nó trong lúc thực thi. Trong Python, điều này được hỗ trợ mạnh mẽ nhờ vào tính chất **mọi thứ đều là đối tượng**.

Ví dụ:
- Một hàm là một đối tượng → có thể kiểm tra tham số, tên, mã nguồn.
- Một lớp là một đối tượng → có thể xem các phương thức, thuộc tính.

### 2.2. Module `inspect`

Module `inspect` cung cấp nhiều hàm hữu ích để kiểm tra các đối tượng tại runtime.

Một số hàm phổ biến:

| Hàm | Mô tả |
|------|------|
| `inspect.getmembers(obj)` | Lấy danh sách các thành viên (thuộc tính, phương thức) của đối tượng |
| `inspect.isfunction(obj)` | Kiểm tra xem có phải là hàm |
| `inspect.ismethod(obj)` | Kiểm tra có phải là phương thức |
| `inspect.isclass(obj)` | Kiểm tra có phải là lớp |
| `inspect.signature(func)` | Lấy chữ ký (tham số) của hàm |
| `inspect.getsource(obj)` | Lấy mã nguồn của hàm/lớp dưới dạng chuỗi |
| `inspect.stack()` | Lấy thông tin ngăn xếp gọi hàm |

### 2.3. Ví dụ nhỏ minh họa

```python
import inspect

def hello(name: str, age: int = 20):
    return f"Xin chào {name}, {age} tuổi."

# Lấy chữ ký hàm
sig = inspect.signature(hello)
for param in sig.parameters.values():
    print(param.name, param.annotation, param.default)
```

Output:
```
name <class 'str'> <class 'inspect._empty'>
age <class 'int'> 20
```

---

## 3. Ví dụ minh họa

### Ví dụ 1: Liệt kê tất cả phương thức của một lớp

Tạo một lớp `Calculator` và dùng `inspect` để in ra tất cả các phương thức công khai.

### Ví dụ 2: Trích xuất thông tin tham số hàm để tạo tài liệu tự động

Viết hàm `describe_function(func)` trả về mô tả chi tiết về tham số của một hàm.

### Ví dụ 3: Ghi log tự động tên hàm và tham số khi gọi

Sử dụng `inspect.stack()` để ghi log tên hàm đang gọi và tham số truyền vào — hữu ích khi debug.

---

## 4. Bài tập thực hành

1. Viết hàm `list_public_methods(cls)` nhận vào một lớp và in ra danh sách các phương thức công khai (không bắt đầu bằng `_`).
2. Viết hàm `get_function_defaults(func)` trả về một từ điển chứa tên tham số và giá trị mặc định của hàm.
3. Viết hàm `debug_caller()` in ra tên hàm gọi nó và tên file thực thi.
4. Viết hàm `print_class_source(cls)` in ra mã nguồn của một lớp (nếu có thể).
5. Viết decorator `@log_call` sử dụng `inspect` để in ra tên hàm và các tham số khi gọi.

---

## 5. Tổng kết

Lập trình phản xạ với module `inspect` mở ra khả năng mạnh mẽ để:
- Tự động sinh tài liệu.
- Gỡ lỗi và theo dõi chương trình.
- Xây dựng framework và công cụ kiểm thử.
- Phân tích cấu trúc mã nguồn mà không cần đọc file.

Tuy nhiên, nên sử dụng cẩn trọng vì:
- Code có thể trở nên khó hiểu.
- Phụ thuộc vào cấu trúc nội bộ.
- Hiệu năng có thể giảm nếu dùng quá nhiều.

Hiểu rõ `inspect` sẽ giúp bạn trở thành lập trình viên Python chuyên sâu, có thể đọc và xây dựng các hệ thống lớn một cách thông minh.