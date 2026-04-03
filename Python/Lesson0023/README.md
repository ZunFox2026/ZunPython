# Bài học Python số 23: Xử lý ngoại lệ và thiết kế chương trình chống lỗi

## Mục tiêu bài học
- Hiểu được vai trò và tầm quan trọng của việc xử lý ngoại lệ trong lập trình Python.
- Biết cách sử dụng khối `try`, `except`, `else`, `finally` để kiểm soát lỗi.
- Nắm vững cách bắt các loại ngoại lệ cụ thể và xử lý phù hợp.
- Biết cách tạo và ném ngoại lệ tùy chỉnh.
- Áp dụng xử lý ngoại lệ vào các chương trình thực tế để tăng tính ổn định.

## Lý thuyết chi tiết

### 1. Ngoại lệ (Exception) là gì?
Trong quá trình chạy chương trình, có thể xảy ra các lỗi như chia cho 0, truy cập chỉ số ngoài danh sách, mở file không tồn tại,... Những lỗi này được gọi là **ngoại lệ** (exception). Nếu không được xử lý, chương trình sẽ dừng đột ngột.

Python cung cấp cơ chế `try-except` để **bắt và xử lý** những lỗi này, giúp chương trình tiếp tục chạy thay vì sập.

### 2. Cú pháp cơ bản
```python
try:
    # Đoạn code có thể gây lỗi
    pass
except LoaiException:
    # Xử lý lỗi nếu xảy ra
    pass
else:
    # Chạy nếu KHÔNG có lỗi
    pass
finally:
    # Luôn chạy, dù có lỗi hay không
    pass
```

### 3. Một số ngoại lệ phổ biến
- `ZeroDivisionError`: Chia cho 0
- `ValueError`: Giá trị không hợp lệ (vd: chuyển "abc" thành số)
- `IndexError`: Truy cập chỉ số ngoài danh sách
- `KeyError`: Truy cập khóa không tồn tại trong từ điển
- `FileNotFoundError`: Mở file không tồn tại

### 4. Bắt nhiều ngoại lệ
Bạn có thể bắt nhiều loại lỗi riêng biệt:
```python
except ValueError:
    print("Lỗi giá trị")
except ZeroDivisionError:
    print("Không thể chia cho 0")
```

### 5. Ngoại lệ tùy chỉnh
Bạn có thể tạo lớp ngoại lệ riêng bằng cách kế thừa từ `Exception`.

## Ví dụ minh họa

Dưới đây là 3 ví dụ hoàn chỉnh minh họa cách xử lý ngoại lệ trong các tình huống thực tế.

### Ví dụ 1: Nhập số nguyên an toàn
Chương trình yêu cầu người dùng nhập một số nguyên, và xử lý trường hợp người dùng nhập sai.

### Ví dụ 2: Đọc file dữ liệu điểm số
Chương trình đọc file điểm học sinh, xử lý trường hợp file không tồn tại hoặc dữ liệu lỗi.

### Ví dụ 3: Chia hai số với ngoại lệ tùy chỉnh
Tạo lớp ngoại lệ `NegativeNumberError` để báo lỗi khi người dùng nhập số âm.

## Bài tập thực hành
1. Viết hàm nhập tuổi, yêu cầu tuổi từ 1 đến 120, xử lý ngoại lệ nếu nhập sai kiểu hoặc ngoài phạm vi.
2. Viết chương trình đọc danh sách tên từ file, xử lý nếu file không tồn tại hoặc rỗng.
3. Viết hàm tính trung bình các số trong danh sách, xử lý trường hợp danh sách rỗng hoặc có phần tử không phải số.
4. Tạo ngoại lệ tùy chỉnh `InvalidEmailError` và kiểm tra định dạng email đơn giản.
5. Viết chương trình tính chỉ số BMI, xử lý các lỗi nhập liệu.

## Tổng kết
Xử lý ngoại lệ là kỹ năng thiết yếu giúp chương trình của bạn **ổn định và thân thiện với người dùng**. Bằng cách sử dụng `try-except`, bạn có thể dự đoán và xử lý các lỗi thường gặp. Ngoài ra, việc tạo ngoại lệ tùy chỉnh giúp mã nguồn rõ ràng và dễ bảo trì hơn. Hãy luôn nghĩ đến khả năng xảy ra lỗi khi viết code và chủ động xử lý chúng!