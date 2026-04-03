# Python 61: Bài 1 - Làm Quen Với Biến Và Kiểu Dữ Liệu

## Giới thiệu

Trong lập trình, **biến** là một thành phần cơ bản dùng để lưu trữ dữ liệu. Mỗi biến có một tên gọi và chứa một giá trị cụ thể thuộc một **kiểu dữ liệu** nhất định như số, chuỗi, hay giá trị đúng/sai. Việc hiểu rõ biến và kiểu dữ liệu là nền tảng để học lập trình Python hiệu quả. Bài học này sẽ giúp bạn làm quen với cách khai báo biến, các kiểu dữ liệu phổ biến và cách sử dụng chúng trong Python.

## Lý thuyết

Trong Python, bạn không cần khai báo kiểu dữ liệu khi tạo biến. Python tự động xác định kiểu dựa trên giá trị được gán. Một số kiểu dữ liệu cơ bản:

- **int**: số nguyên, ví dụ: `5`, `-3`
- **float**: số thực, ví dụ: `3.14`, `-0.5`
- **str**: chuỗi ký tự, ví dụ: `"Hello"`, `'Python'`
- **bool**: giá trị logic, chỉ nhận `True` hoặc `False`

Tên biến phải bắt đầu bằng chữ cái hoặc dấu gạch dưới, không được chứa ký tự đặc biệt (trừ `_`) và không được trùng với từ khóa của Python.

## Ví dụ

```python
# Khai báo và sử dụng biến
tuoi = 20
chieu_cao = 1.75
ten = "An"
la_sinh_vien = True

# In giá trị biến ra màn hình
print("Tên:", ten)
print("Tuổi:", tuoi)
print("Chiều cao:", chieu_cao, "m")
print("Là sinh viên:", la_sinh_vien)
```

Kết quả:
```
Tên: An
Tuổi: 20
Chiều cao: 1.75 m
Là sinh viên: True
```

## Bài tập

1. Tạo các biến lưu trữ tên, tuổi, điểm trung bình và trạng thái học sinh (đang học hay đã tốt nghiệp).
2. In các thông tin này ra màn hình theo định dạng dễ đọc.
3. Thử thay đổi giá trị của biến và chạy lại chương trình để xem kết quả thay đổi thế nào.

> Gợi ý: Sử dụng hàm `print()` và các biến kiểu `str`, `int`, `float`, `bool`.