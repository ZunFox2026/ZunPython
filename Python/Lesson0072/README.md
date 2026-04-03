# Bài học Python số 72: Lập trình phản xạ (Reflection) và sử dụng `inspect` module

## Mục tiêu bài học
- Hiểu được khái niệm **lập trình phản xạ (reflection)** trong Python.
- Biết cách sử dụng module `inspect` để truy xuất thông tin về các đối tượng, hàm, lớp, tham số, stack...
- Áp dụng phản xạ để xây dựng các công cụ phát triển, ghi log, kiểm thử tự động hoặc framework.
- Làm chủ các kỹ thuật nâng cao như kiểm tra tham số hàm, đọc docstring, duyệt thành viên lớp, và xác định nơi gọi hàm.

## Lý thuyết chi tiết

### 1. Lập trình phản xạ là gì?
Lập trình phản xạ (reflection) là khả năng của một chương trình trong việc tự kiểm tra, phân tích và thay đổi cấu trúc hoặc hành vi của chính nó trong lúc chạy (runtime). Python hỗ trợ phản xạ rất mạnh mẽ nhờ vào bản chất động của ngôn ngữ.

Các hàm phản xạ cơ bản trong Python:
- `type(obj)`: trả về kiểu của đối tượng.
- `isinstance(obj, cls)`: kiểm tra đối tượng có phải là thể hiện của lớp hay không.
- `hasattr(obj, 'attr')`, `getattr(obj, 'attr')`, `setattr(obj, 'attr', value)`: kiểm tra, lấy, gán thuộc tính.
- `dir(obj)`: liệt kê các thuộc tính và phương thức của đối tượng.

Tuy nhiên, để làm việc sâu hơn (ví dụ: xem tham số hàm, docstring, dòng mã, stack), ta cần dùng module `inspect`.

### 2. Module `inspect`
Module `inspect` cung cấp các hàm để lấy thông tin chi tiết về các đối tượng Python như hàm, lớp, phương thức, frame, module...

Một số hàm quan trọng:
- `inspect.getmembers(obj, predicate=None)`: trả về danh sách các cặp (tên, giá trị) của các thành viên trong `obj`.
- `inspect.isfunction(obj)`, `inspect.isclass(obj)`, `inspect.ismethod(obj)`: kiểm tra loại đối tượng.
- `inspect.getdoc(obj)`: lấy docstring của đối tượng.
- `inspect.getsource(obj)`: lấy mã nguồn của đối tượng (nếu có).
- `inspect.signature(obj)`: trả về đối tượng `Signature` mô tả tham số của hàm.
- `inspect.currentframe()`, `inspect.stack()`: xem call stack hiện tại.

### 3. Ứng dụng thực tế
- Tự động tạo tài liệu (documentation).
- Xây dựng decorator thông minh.
- Ghi log chi tiết về các hàm được gọi.
- Framework kiểm thử tự động phát hiện test case.
- Xây dựng CLI tự động từ các hàm.

## Ví dụ minh họa

### Ví dụ 1: Kiểm tra và in thông tin về một hàm
Chúng ta sẽ viết một hàm in ra chi tiết về một hàm bất kỳ: tên, tham số, kiểu tham số, giá trị mặc định, và docstring.

### Ví dụ 2: Tự động phát hiện và chạy các hàm test
Tạo một module với các hàm bắt đầu bằng `test_`, sau đó dùng `inspect` để tìm và thực thi chúng.

### Ví dụ 3: Ghi log ai đã gọi một hàm
Dùng `inspect.stack()` để xem hàm được gọi từ đâu — hữu ích trong debug.

## Bài tập thực hành
1. Viết hàm `print_class_info(cls)` in ra tất cả phương thức và thuộc tính của một lớp.
2. Viết decorator `@log_call` ghi lại tên hàm, tham số đầu vào và nơi gọi khi hàm được thực thi.
3. Viết hàm `find_functions_by_doc_keyword(module, keyword)` tìm tất cả hàm trong một module có từ khóa trong docstring.
4. Tạo một hàm `validate_types(func)` decorator kiểm tra kiểu tham số dựa trên type hints.
5. Viết hàm `get_caller_info()` trả về tên hàm và số dòng nơi gọi đến nó.

## Tổng kết
Lập trình phản xạ và module `inspect` là công cụ mạnh mẽ giúp Python trở thành ngôn ngữ linh hoạt trong phát triển framework, công cụ debug và tự động hóa. Việc hiểu và sử dụng thành thạo `inspect` giúp bạn viết code thông minh hơn, giảm lặp lại, tăng tính tự động và hỗ trợ debug hiệu quả. Tuy nhiên, cần cẩn trọng vì phản xạ có thể làm giảm hiệu năng và làm code khó đọc nếu lạm dụng.