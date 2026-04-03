# Bài học Python số 12: Xử lý ngoại lệ và cấu trúc try-except

## Mục tiêu bài học
- Hiểu được khái niệm ngoại lệ (exception) trong Python.
- Biết cách sử dụng khối `try-except` để bắt và xử lý lỗi.
- Xử lý nhiều loại ngoại lệ khác nhau.
- Sử dụng các khối `else` và `finally` để quản lý luồng chương trình hiệu quả.
- Áp dụng xử lý ngoại lệ vào các tình huống thực tế như đọc file, nhập liệu người dùng.

## Lý thuyết chi tiết

Trong quá trình chạy chương trình, có thể xảy ra các lỗi không mong muốn như chia cho 0, truy cập chỉ số ngoài danh sách, hoặc mở một file không tồn tại. Những lỗi này được gọi là **ngoại lệ (exception)**. Nếu không được xử lý, chương trình sẽ dừng lại và hiện lỗi.

Python cung cấp cơ chế `try-except` để bắt và xử lý các ngoại lệ, giúp chương trình tiếp tục chạy thay vì sập.

### Cấu trúc cơ bản
```python
try:
    # Đoạn code có thể gây lỗi
    pass
except LoaiException:
    # Xử lý lỗi nếu xảy ra
    pass
```

### Các khối bổ sung
- `else`: chạy nếu không có lỗi xảy ra trong `try`.
- `finally`: luôn chạy, bất kể có lỗi hay không.

### Một số ngoại lệ phổ biến
- `ZeroDivisionError`: chia cho 0.
- `ValueError`: giá trị không hợp lệ (vd: chuyển "abc" thành số).
- `IndexError`: truy cập chỉ số ngoài danh sách.
- `FileNotFoundError`: không tìm thấy file.

### Ví dụ cơ bản
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
```

## Ví dụ minh họa

### Ví dụ 1: Xử lý người dùng nhập sai kiểu dữ liệu
Khi yêu cầu người dùng nhập số, nếu họ nhập chữ, chương trình sẽ báo lỗi. Ta dùng `try-except` để xử lý.

### Ví dụ 2: Đọc file an toàn
Khi mở file, nếu file không tồn tại, chương trình sẽ lỗi. Dùng `try-except` để thông báo thay vì crash.

### Ví dụ 3: Xử lý nhiều loại lỗi cùng lúc
Chương trình tính chia hai số, xử lý cả lỗi chia 0 và lỗi nhập không phải số.

## Bài tập thực hành
1. Viết hàm nhập số nguyên từ người dùng, yêu cầu nhập lại nếu sai.
2. Viết chương trình đọc file và đếm số dòng, xử lý nếu file không tồn tại.
3. Viết hàm tính căn bậc hai, xử lý khi số âm.
4. Xử lý lỗi khi truy cập phần tử danh sách.
5. Kết hợp `try-except-else-finally` trong một chương trình nhỏ.

## Tổng kết
Xử lý ngoại lệ là kỹ năng quan trọng giúp chương trình ổn định và thân thiện hơn. Sử dụng `try-except` hợp lý giúp bắt lỗi và hướng dẫn người dùng, tránh crash chương trình. Luôn nhớ dùng `finally` cho các thao tác dọn dẹp như đóng file, kết nối cơ sở dữ liệu.