# Bài học Python số 22 - Xử lý ngoại lệ (Exception Handling)

## Mục tiêu bài học
- Hiểu được khái niệm ngoại lệ (exception) trong Python.
- Biết cách sử dụng khối `try`, `except`, `else`, và `finally` để xử lý lỗi.
- Áp dụng xử lý ngoại lệ trong các tình huống thực tế như đọc file, nhập dữ liệu người dùng.
- Viết code an toàn, tránh crash chương trình do lỗi không mong muốn.

## Lý thuyết chi tiết

Trong quá trình chạy chương trình, có thể xảy ra các lỗi như chia cho 0, truy cập chỉ số ngoài danh sách, hoặc không tìm thấy file. Những lỗi này được gọi là **ngoại lệ (exception)**.

Python cung cấp cơ chế xử lý ngoại lệ bằng khối `try...except`:

- `try`: Đặt các câu lệnh có thể gây lỗi vào đây.
- `except`: Xử lý lỗi nếu xảy ra.
- `else`: Thực thi nếu không có lỗi nào xảy ra.
- `finally`: Luôn thực thi, dù có lỗi hay không.

### Cú pháp cơ bản
```python
try:
    # Code có thể gây lỗi
    pass
except LoaiException:
    # Xử lý lỗi
    pass
else:
    # Thực thi nếu không có lỗi
    pass
finally:
    # Luôn thực thi
    pass
```

### Một số ngoại lệ phổ biến
- `ZeroDivisionError`: Chia cho 0
- `ValueError`: Giá trị không hợp lệ (vd: chuyển chuỗi "abc" thành số)
- `IndexError`: Truy cập chỉ số ngoài danh sách
- `FileNotFoundError`: Không tìm thấy file

## Ví dụ minh họa

### Ví dụ 1: Xử lý chia cho 0
```python
try:
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    print(f"a / b = {a / b}")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")
```

### Ví dụ 2: Đọc file an toàn
```python
try:
    with open("data.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File không tồn tại. Vui lòng kiểm tra lại tên file.")
except PermissionError:
    print("Không có quyền truy cập file này.")
```

### Ví dụ 3: Xử lý danh sách
```python
numbers = [10, 20, 30]
try:
    index = int(input("Nhập chỉ số muốn truy cập: "))
    print(f"Giá trị tại chỉ số {index}: {numbers[index]}")
except IndexError:
    print("Lỗi: Chỉ số vượt quá kích thước danh sách!")
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên!")
```

## Bài tập thực hành
1. Viết hàm `chia_hai_so(a, b)` trả về kết quả a/b. Xử lý các lỗi có thể xảy ra.
2. Viết chương trình đọc một file số, tính trung bình các số trong file. Xử lý lỗi nếu file không tồn tại hoặc dữ liệu không hợp lệ.
3. Viết chương trình nhập 3 cạnh tam giác, kiểm tra xem có tạo thành tam giác không. Xử lý lỗi nhập liệu.
4. Viết hàm `doc_danh_sach_tu_file(filename)` đọc danh sách tên từ file (mỗi tên một dòng), trả về danh sách tên. Xử lý các lỗi có thể xảy ra.
5. Viết chương trình cho người dùng đoán số từ 1 đến 100. Xử lý lỗi khi người dùng nhập không phải số.

## Tổng kết
- Xử lý ngoại lệ giúp chương trình chạy ổn định hơn.
- Luôn dùng `try...except` khi làm việc với dữ liệu không chắc chắn (input người dùng, file, mạng).
- Có thể bắt nhiều loại ngoại lệ riêng biệt để xử lý cụ thể.
- Dùng `finally` để dọn dẹp tài nguyên (đóng file, kết nối...).
- Tránh dùng `except:` không rõ kiểu ngoại lệ vì che giấu lỗi.
