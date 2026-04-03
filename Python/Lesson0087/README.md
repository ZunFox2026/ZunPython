# Bài học Python nâng cao số 87: Lập trình phản xạ (Reflection) và sử dụng `inspect`

## Mục tiêu bài học
- Hiểu được khái niệm lập trình phản xạ (reflection) trong Python.
- Sử dụng module `inspect` để kiểm tra các đối tượng, hàm, lớp, tham số và stack.
- Áp dụng phản xạ để xây dựng các công cụ gỡ lỗi, ghi log tự động, hoặc framework nhỏ.
- Nâng cao khả năng thiết kế hệ thống linh hoạt, tự động phát hiện và xử lý code.

## Lý thuyết chi tiết

### 1. Lập trình phản xạ (Reflection) là gì?
Lập trình phản xạ là khả năng của một chương trình trong việc tự kiểm tra, phân tích và thay đổi cấu trúc hoặc hành vi của chính nó trong lúc chạy. Python hỗ trợ phản xạ rất mạnh mẽ nhờ vào bản chất động của ngôn ngữ.

Một số thao tác phản xạ phổ biến:
- Kiểm tra kiểu dữ liệu: `type()`, `isinstance()`
- Liệt kê thuộc tính: `dir()`
- Lấy giá trị thuộc tính: `getattr()`, `setattr()`, `hasattr()`
- Kiểm tra mã nguồn: `inspect.getsource()`
- Phân tích stack gọi hàm: `inspect.stack()`

### 2. Module `inspect`
Module `inspect` cung cấp nhiều hàm tiện ích để lấy thông tin về các đối tượng đang chạy.

#### Một số hàm quan trọng:
- `inspect.isfunction(obj)`: Kiểm tra đối tượng có phải là hàm không.
- `inspect.isclass(obj)`: Kiểm tra có phải là lớp.
- `inspect.getmembers(obj, predicate=None)`: Lấy danh sách các thành viên (thuộc tính, phương thức) của đối tượng.
- `inspect.signature(func)`: Trả về thông tin về tham số của hàm.
- `inspect.getsource(obj)`: Lấy mã nguồn của hàm hoặc lớp.
- `inspect.stack()`: Trả về thông tin về các frame đang chạy (hữu ích để debug).

### Ví dụ minh họa
Xem các ví dụ trong `main.py`.

## Bài tập thực hành
Hoàn thành các bài tập trong `exercises.py` và kiểm tra bằng `solutions.py`.

## Tổng kết
Lập trình phản xạ và sử dụng `inspect` giúp chúng ta viết code thông minh hơn, tự động hóa việc kiểm tra, ghi log, hoặc xây dựng các framework. Tuy nhiên, cần sử dụng cẩn trọng vì có thể làm code khó đọc hoặc gây lỗi nếu không kiểm soát tốt.

Phản xạ là công cụ mạnh, phù hợp với các dự án lớn, hệ thống tự động, hoặc công cụ phát triển.
