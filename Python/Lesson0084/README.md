# Bài học Python nâng cao số 84: Lập trình phản xạ (Reflection) và sử dụng `inspect` module

## Mục tiêu bài học
- Hiểu được khái niệm lập trình phản xạ (reflection) trong Python.
- Biết cách sử dụng module `inspect` để kiểm tra, phân tích các thành phần mã nguồn như hàm, lớp, biến, tham số…
- Ứng dụng `inspect` để xây dựng các công cụ gỡ lỗi, kiểm tra mã, hoặc tạo meta-programming (lập trình tạo mã).
- Nâng cao khả năng viết mã linh hoạt và tự động hóa.

## Lý thuyết chi tiết

### 1. Lập trình phản xạ là gì?

Lập trình phản xạ (reflection) là khả năng của một chương trình trong việc **tự quan sát và thao tác chính nó** tại thời điểm chạy (runtime). Trong Python, điều này có nghĩa là bạn có thể:
- Kiểm tra các đối tượng (hàm, lớp, module…)
- Lấy thông tin về tham số, thuộc tính, phương thức
- Gọi phương thức hoặc truy cập thuộc tính một cách động

Python hỗ trợ phản xạ rất mạnh, nhờ vào các hàm như `getattr()`, `hasattr()`, `type()`, `dir()`, và đặc biệt là module `inspect`.

### 2. Module `inspect`

Module `inspect` cung cấp các công cụ để lấy thông tin chi tiết về các đối tượng Python. Một số hàm quan trọng:

- `inspect.getmembers(obj)`: Trả về danh sách các thành viên (thuộc tính, phương thức) của đối tượng.
- `inspect.isfunction(obj)`, `inspect.isclass(obj)`: Kiểm tra loại đối tượng.
- `inspect.signature(func)`: Lấy chữ ký của hàm (tham số, kiểu, giá trị mặc định).
- `inspect.getsource(obj)`: Lấy mã nguồn của đối tượng (nếu có).
- `inspect.stack()`: Lấy thông tin về các hàm đang gọi (gọi stack).

### 3. Ứng dụng thực tế
- Tự động tạo tài liệu (doc generation)
- Gỡ lỗi nâng cao
- Viết framework hoặc thư viện hỗ trợ kiểm tra và phân tích mã
- Tạo decorator thông minh

## Ví dụ minh họa

Xem file `main.py` để chạy các ví dụ:

1. **Kiểm tra các thành viên của một lớp**
2. **Lấy chữ ký hàm và phân tích tham số**
3. **In mã nguồn của một hàm**

## Bài tập thực hành

Xem file `exercises.py` để làm bài tập. Sau đó kiểm tra lời giải trong `solutions.py`.

## Tổng kết

Module `inspect` là một công cụ mạnh mẽ trong tay lập trình viên Python nâng cao. Việc hiểu và sử dụng tốt lập trình phản xạ giúp bạn:
- Viết mã linh hoạt hơn
- Tự động hóa các tác vụ kiểm tra và gỡ lỗi
- Xây dựng các thư viện, công cụ phát triển

Tuy nhiên, cần cẩn trọng khi dùng vì mã phản xạ có thể khó đọc và gây rủi ro bảo mật nếu không kiểm soát tốt.

Hãy luyện tập thường xuyên để thành thạo kỹ năng này!