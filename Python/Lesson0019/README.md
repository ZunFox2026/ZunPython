# Bài học 19: Xử lý ngoại lệ và thiết kế chương trình bền vững

## Mục tiêu bài học
- Hiểu khái niệm ngoại lệ (exception) và tầm quan trọng của việc xử lý lỗi trong lập trình.
- Biết cách sử dụng khối `try`, `except`, `else`, và `finally` để kiểm soát lỗi.
- Áp dụng xử lý ngoại lệ vào các tình huống thực tế như đọc file, nhập liệu người dùng, tính toán an toàn.
- Xây dựng chương trình Python ổn định, ít bị sập do lỗi không mong muốn.

## Lý thuyết chi tiết

Trong quá trình chạy chương trình, có thể xảy ra các tình huống bất ngờ như: chia cho 0, truy cập phần tử ngoài danh sách, mở file không tồn tại... Những tình huống này gọi là **ngoại lệ (exception)**.

Python cung cấp cơ chế `try...except` để bắt và xử lý các ngoại lệ, giúp chương trình không bị dừng đột ngột.

### Cú pháp cơ bản:
```python
try:
    # Đoạn code có thể gây lỗi
    pass
except LoaiException:
    # Xử lý lỗi nếu xảy ra
    pass
else:
    # Chạy nếu không có lỗi
    pass
finally:
    # Luôn chạy, bất kể có lỗi hay không
    pass
```

### Các loại ngoại lệ phổ biến:
- `ZeroDivisionError`: chia cho 0
- `ValueError`: giá trị không hợp lệ (vd: chuyển "abc" thành số)
- `IndexError`: truy cập chỉ số ngoài danh sách
- `FileNotFoundError`: file không tồn tại
- `TypeError`: sai kiểu dữ liệu

### Ví dụ nhỏ:
```python
try:
    x = int(input("Nhập một số: "))
    print(10 / x)
except ZeroDivisionError:
    print("Không thể chia cho 0!")
except ValueError:
    print("Bạn phải nhập số!")
```

## Ví dụ minh họa

### Ví dụ 1: Đọc file an toàn
Chương trình đọc nội dung file, xử lý trường hợp file không tồn tại.

### Ví dụ 2: Tính trung bình điểm số
Nhập danh sách điểm, xử lý lỗi khi nhập sai định dạng hoặc danh sách rỗng.

### Ví dụ 3: Mô phỏng rút tiền tại ATM
Kiểm tra số dư, xử lý các lỗi như nhập sai số tiền, số tiền âm, không đủ tiền.

## Bài tập thực hành
1. Viết hàm chia hai số, xử lý các lỗi có thể xảy ra.
2. Viết chương trình nhập tuổi, yêu cầu tuổi phải là số nguyên dương.
3. Đọc file dữ liệu và đếm số dòng, xử lý nếu file không tồn tại.
4. Viết hàm tìm phần tử lớn nhất trong danh sách, xử lý danh sách rỗng.
5. Tạo chương trình tính chỉ số BMI, xử lý lỗi đầu vào.

## Tổng kết
Xử lý ngoại lệ là kỹ năng quan trọng giúp chương trình trở nên chuyên nghiệp và ổn định hơn. Việc sử dụng `try...except` đúng cách giúp bạn kiểm soát lỗi, cung cấp thông báo rõ ràng và tiếp tục chương trình khi có thể. Hãy luôn suy nghĩ về các trường hợp lỗi trong thiết kế chương trình.