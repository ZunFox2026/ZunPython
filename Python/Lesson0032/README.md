# Bài học Python số 32: Làm việc với Decorators (Trang trí viên)

## Mục tiêu bài học
- Hiểu được khái niệm và vai trò của **decorator** trong Python.
- Biết cách tạo và sử dụng decorator đơn giản cũng như decorator có tham số.
- Áp dụng decorator vào các tình huống thực tế như: đo thời gian thực thi, xác thực, ghi log.
- Nâng cao kỹ năng viết code sạch, tái sử dụng và chuyên nghiệp hơn.

## Lý thuyết chi tiết

### 1. Decorator là gì?
Decorator là một hàm nhận vào một hàm khác và mở rộng hành vi của hàm đó mà không thay đổi nội dung của hàm đó. Đây là một tính năng mạnh mẽ của Python, thuộc về khái niệm **Higher-Order Functions**.

### 2. Cách hoạt động của decorator
- Trong Python, **hàm là đối tượng cấp một (first-class object)**, có thể được gán vào biến, truyền vào hàm khác.
- Một decorator là một hàm nhận vào một hàm (`func`) và trả về một hàm mới (thường là hàm bao bọc `wrapper`).

### 3. Cú pháp sử dụng decorator
Sử dụng ký hiệu `@ten_decorator` phía trên định nghĩa hàm.

```python
@decorator
def my_function():
    pass
```

Tương đương với:

```python
my_function = decorator(my_function)
```

### 4. Ví dụ minh họa đơn giản

```python
def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

@make_bold
def say_hello():
    return "Xin chào"
```

Kết quả: `"<b>Xin chào</b>"`

### 5. Decorator có tham số
Cần thêm một lớp hàm bao bọc bên ngoài để nhận tham số.

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
```

## Ví dụ minh họa

### Ví dụ 1: Đo thời gian thực thi hàm
Dùng để kiểm tra hiệu suất.

### Ví dụ 2: Ghi log hoạt động
Tự động ghi lại khi một hàm được gọi.

### Ví dụ 3: Xác thực truy cập
Chỉ cho phép chạy hàm nếu người dùng đã đăng nhập.

## Bài tập thực hành
1. Viết decorator `@log_calls` để in ra tên hàm và tham số khi gọi hàm.
2. Viết decorator `@retry` để thử lại hàm nếu gặp lỗi, tối đa 3 lần.
3. Viết decorator `@cache` đơn giản để lưu kết quả của hàm theo tham số.
4. Viết decorator `@timing` để in thời gian thực thi, nhưng chỉ in nếu thời gian > 1 giây.
5. Viết decorator `@ensure_positive` kiểm tra tất cả tham số là số dương.

## Tổng kết
- Decorator giúp tách biệt logic chính và logic phụ (cross-cutting concerns) như logging, caching, timing, security.
- Decorator làm code gọn gàng, dễ bảo trì và tái sử dụng.
- Có thể tạo decorator đơn giản hoặc phức tạp, có tham số hoặc không.
- Nên sử dụng `functools.wraps` để giữ nguyên thông tin hàm gốc khi cần.

Hãy luyện tập thường xuyên để thành thạo kỹ thuật này – một công cụ mạnh mẽ trong tay lập trình viên Python trung cấp trở lên.