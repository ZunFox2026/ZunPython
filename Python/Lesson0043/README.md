# Bài học Python Nâng cao 43: Lập trình phản xạ (Reflection) và sử dụng `inspect` module

Trong bài học này, chúng ta sẽ tìm hiểu về **lập trình phản xạ (reflection)** trong Python — một kỹ năng nâng cao giúp chương trình có thể tự phân tích, kiểm tra và thay đổi cấu trúc hoặc hành vi của chính nó trong lúc chạy. Đây là nền tảng cho nhiều công cụ như framework web (Flask, Django), thư viện kiểm thử (pytest), hay công cụ tự động hóa.

Chúng ta sẽ tập trung vào module `inspect` — một công cụ mạnh mẽ để kiểm tra các đối tượng trong Python như hàm, lớp, phương thức, tham số, và thậm chí là mã nguồn.

---

## Mục tiêu bài học

Sau bài học này, bạn sẽ có thể:

1. Hiểu được khái niệm **lập trình phản xạ** trong Python.
2. Sử dụng module `inspect` để:
   - Kiểm tra thông tin hàm và lớp.
   - Lấy danh sách tham số, mặc định, kiểu dữ liệu.
   - Truy xuất mã nguồn của một hàm.
   - Xác định loại đối tượng (hàm, lớp, phương thức, v.v.).
3. Ứng dụng `inspect` vào thực tế như xây dựng decorator thông minh, hệ thống ghi log, hoặc validate đầu vào tự động.

---

## Lý thuyết chi tiết

### 1. Lập trình phản xạ là gì?

Lập trình phản xạ (reflection) là khả năng của một chương trình để tự kiểm tra, phân tích, hoặc thay đổi cấu trúc và hành vi của chính nó trong lúc chạy. Trong Python, điều này được hỗ trợ rất mạnh mẽ nhờ vào tính chất **đối tượng bậc nhất (first-class objects)** của mọi thứ (hàm, lớp, biến, v.v.).

Ví dụ:

- `type(obj)` — kiểm tra kiểu của đối tượng.
- `dir(obj)` — liệt kê các thuộc tính và phương thức của đối tượng.
- `hasattr(obj, 'name')`, `getattr(obj, 'name')` — kiểm tra và lấy thuộc tính.
- `callable(obj)` — kiểm tra xem có phải là hàm không.

Tuy nhiên, để làm việc sâu hơn (ví dụ: biết tên tham số, giá trị mặc định, kiểu dữ liệu, hoặc mã nguồn), ta cần đến module `inspect`.

### 2. Module `inspect`

Module `inspect` cung cấp nhiều hàm hữu ích để kiểm tra các đối tượng trong Python.

#### Một số hàm quan trọng:

- `inspect.getmembers(obj)`: Trả về danh sách các cặp (tên, giá trị) của tất cả các thành viên trong `obj`.
- `inspect.isfunction(obj)`, `inspect.isclass(obj)`, `inspect.ismethod(obj)`: Kiểm tra loại đối tượng.
- `inspect.signature(func)`: Trả về chữ ký (signature) của hàm — bao gồm tham số, mặc định, và kiểu.
- `inspect.getsource(obj)`: Trả về mã nguồn của đối tượng dưới dạng chuỗi (nếu có).
- `inspect.getdoc(obj)`: Trả về docstring của đối tượng.

#### Ví dụ nhỏ:

```python
import inspect

def hello(name: str, age: int = 20):
    """Chào một người"""
    print(f"Xin chào {name}, {age} tuổi.")

sig = inspect.signature(hello)
for name, param in sig.parameters.items():
    print(f"Tham số: {name}, Kiểu: {param.annotation}, Mặc định: {param.default}")
```

Kết quả:

```
Tham số: name, Kiểu: <class 'str'>, Mặc định: <class 'inspect._empty'>
Tham số: age, Kiểu: <class 'int'>, Mặc định: 20
```

---

## Ví dụ minh họa

### Ví dụ 1: Trích xuất thông tin hàm để tự động validate tham số

Chúng ta sẽ tạo một decorator sử dụng `inspect` để kiểm tra kiểu dữ liệu của tham số đầu vào.

### Ví dụ 2: Tạo hệ thống in ra mã nguồn của các hàm trong một module

In ra mã nguồn của từng hàm để gỡ lỗi hoặc tài liệu hóa.

### Ví dụ 3: Tự động ghi log hành vi của các phương thức trong một lớp

Sử dụng `inspect` để biết tên phương thức và tham số, từ đó ghi log chi tiết.

---

## Bài tập thực hành

1. Viết hàm `list_functions(module)` nhận một module và in ra danh sách các hàm cùng với số lượng tham số.
2. Viết decorator `@log_calls` ghi log mỗi lần một hàm được gọi, hiển thị tên hàm và các tham số truyền vào.
3. Viết hàm `get_class_methods(cls)` trả về danh sách các phương thức của một lớp, kèm theo docstring (nếu có).
4. Viết hàm `validate_annotations(func, *args, **kwargs)` kiểm tra xem các đối số truyền vào có khớp với kiểu dữ liệu trong annotation không.

---

## Tổng kết

- Lập trình phản xạ giúp Python trở nên linh hoạt và mạnh mẽ.
- Module `inspect` là công cụ không thể thiếu cho các hệ thống tự động, framework, hoặc công cụ phát triển.
- Biết cách sử dụng `inspect.signature`, `getsource`, `isfunction`, v.v. giúp bạn viết code thông minh hơn.
- Các ứng dụng thực tế bao gồm: validation tự động, logging, serialization, và API tự động.

> ✅ Hãy thực hành các bài tập để nắm vững kỹ năng này!
