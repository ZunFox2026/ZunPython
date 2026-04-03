# Bài học Python nâng cao số 61: Lập trình phản xạ (Reflection) và sử dụng `inspect` module

Trong bài học này, chúng ta sẽ tìm hiểu về **lập trình phản xạ (reflection)** trong Python và cách sử dụng module `inspect` — một công cụ mạnh mẽ giúp khám phá và tương tác với mã nguồn tại **thời gian chạy (runtime)**. Đây là chủ đề nâng cao, đặc biệt hữu ích khi phát triển các framework, thư viện, công cụ debug, hoặc các ứng dụng cần tính linh hoạt cao.

## 1. Mục tiêu bài học

- Hiểu được khái niệm **lập trình phản xạ** trong Python.
- Biết cách sử dụng module `inspect` để:
  - Liệt kê các thành viên của một đối tượng (hàm, lớp, biến...)
  - Lấy thông tin về tham số, ký tự docstring, stack gọi hàm.
  - Kiểm tra loại đối tượng (hàm, lớp, phương thức, v.v.)
- Ứng dụng thực tế trong tự động hóa, logging, và tạo framework.

## 2. Lý thuyết chi tiết

### 2.1. Lập trình phản xạ là gì?

**Lập trình phản xạ (Reflection)** là khả năng của một chương trình trong việc **tự quan sát và thay đổi cấu trúc, hành vi của chính nó** tại thời gian chạy.

Python hỗ trợ phản xạ rất mạnh mẽ, bao gồm các hàm như:
- `type()`, `isinstance()`
- `hasattr()`, `getattr()`, `setattr()`, `delattr()`
- `dir()`
- Và đặc biệt là module `inspect`

### 2.2. Module `inspect`

Module `inspect` cung cấp nhiều hàm để lấy thông tin chi tiết về các đối tượng Python, bao gồm:

- `inspect.getmembers(obj)`: Trả về danh sách các cặp (tên, giá trị) của các thành viên trong `obj`.
- `inspect.isfunction(obj)`, `inspect.isclass(obj)`, `inspect.ismethod(obj)`: Kiểm tra loại đối tượng.
- `inspect.signature(func)`: Lấy thông tin về tham số của hàm.
- `inspect.getdoc(obj)`: Lấy docstring của đối tượng.
- `inspect.stack()`: Lấy thông tin về ngăn xếp gọi hàm (call stack).

### 2.3. Ứng dụng thực tế

- Tự động đăng ký các lớp/hàm trong framework (như Flask, Django).
- Ghi log chi tiết về hàm được gọi.
- Tạo CLI tự động từ các hàm.
- Debug và phân tích mã nguồn tại runtime.

## 3. Ví dụ minh họa

### Ví dụ 1: Liệt kê các phương thức và thuộc tính của một lớp

Chúng ta sẽ tạo một lớp `Car` và dùng `inspect` để in ra tất cả các phương thức và thuộc tính.

### Ví dụ 2: Lấy thông tin tham số của hàm

Dùng `inspect.signature()` để phân tích cách một hàm nhận tham số.

### Ví dụ 3: Ghi log tự động tên hàm và tham số gọi

Tạo một decorator dùng `inspect` để ghi log chi tiết mỗi khi một hàm được gọi.

## 4. Bài tập thực hành

1. Viết hàm `list_functions(module)` nhận một module và in ra danh sách tất cả các hàm trong đó cùng docstring.
2. Viết hàm `analyze_class(cls)` in ra tên, các phương thức, thuộc tính, và docstring của một lớp.
3. Tạo một decorator `@trace_call` ghi lại tên hàm, tham số đầu vào và kết quả trả về vào file log.
4. Viết hàm `find_functions_with_keyword(module, keyword)` tìm tất cả các hàm trong module có chứa từ khóa trong docstring.
5. Dùng `inspect.stack()` để in ra chuỗi gọi hàm hiện tại (call stack) mỗi khi một hàm được gọi.

## 5. Tổng kết

Lập trình phản xạ và module `inspect` là những công cụ mạnh mẽ giúp Python trở nên linh hoạt và mạnh mẽ trong việc xây dựng hệ thống tự động, framework và công cụ phát triển. Việc hiểu rõ và sử dụng thành thạo `inspect` sẽ giúp bạn:

- Viết mã thông minh hơn.
- Tự động hóa các tác vụ quản lý mã nguồn.
- Xây dựng các công cụ debug, logging, và testing hiệu quả.

Hãy luyện tập kỹ các ví dụ và bài tập để nắm vững kỹ năng này!