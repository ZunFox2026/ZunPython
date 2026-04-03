# Bài học Python Trung cấp - Bài 11: Xử lý ngoại lệ và thiết kế chương trình bền bỉ

## Mục tiêu bài học
- Hiểu rõ khái niệm ngoại lệ (exception) và vai trò của nó trong lập trình.
- Biết cách sử dụng khối `try`, `except`, `else`, và `finally` để xử lý lỗi.
- Áp dụng xử lý ngoại lệ vào các tình huống thực tế như đọc file, nhập liệu người dùng, tính toán an toàn.
- Thiết kế chương trình có khả năng phục hồi lỗi và thông báo rõ ràng.

## Nội dung lý thuyết

Trong quá trình chạy chương trình, có thể xảy ra các lỗi không mong muốn như chia cho 0, truy cập chỉ số ngoài danh sách, hoặc không tìm thấy file. Những lỗi này được gọi là **ngoại lệ** (exception).

Python cung cấp cơ chế xử lý ngoại lệ bằng khối `try...except` để bắt và xử lý các lỗi, giúp chương trình không bị sập và có thể tiếp tục chạy.

### Cú pháp cơ bản
```python
try:
    # Đoạn code có thể gây lỗi
    code_here()
except LoaiLoi:
    # Xử lý lỗi nếu xảy ra
    handle_error()
```

### Các khối mở rộng
- `else`: chạy nếu không có lỗi xảy ra trong `try`.
- `finally`: luôn chạy, dù có lỗi hay không, thường dùng để dọn dẹp tài nguyên.

### Một số ngoại lệ phổ biến
- `ValueError`: giá trị không hợp lệ (ví dụ: chuyển "abc" thành số).
- `TypeError`: kiểu dữ liệu không phù hợp.
- `IndexError`: truy cập chỉ số ngoài danh sách.
- `KeyError`: truy cập key không tồn tại trong từ điển.
- `FileNotFoundError`: không tìm thấy file.

## Ví dụ minh họa
Xem file `main.py` để chạy các ví dụ.

## Bài tập thực hành
Hãy hoàn thành các bài tập trong file `exercises.py` và kiểm tra với `solutions.py`.

## Tổng kết
Xử lý ngoại lệ là kỹ năng quan trọng giúp chương trình trở nên **ổn định** và **dễ bảo trì**. Việc bắt lỗi đúng cách không chỉ tránh crash mà còn giúp người dùng hiểu được vấn đề. Hãy luôn suy nghĩ về các trường hợp lỗi khi viết code!
