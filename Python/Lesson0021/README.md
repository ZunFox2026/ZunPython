# Bài học 21: Xử lý Ngoại lệ (Exception Handling) trong Python

## Mục tiêu bài học
- Hiểu được khái niệm ngoại lệ (exception) và tại sao cần xử lý chúng.
- Biết cách sử dụng khối `try`, `except`, `else`, và `finally`.
- Áp dụng xử lý ngoại lệ trong các tình huống thực tế như đọc file, nhập liệu người dùng, tính toán số học.
- Viết code an toàn, tránh crash chương trình do lỗi không mong muốn.

## Lý thuyết chi tiết

### 1. Ngoại lệ là gì?
Ngoại lệ (exception) là các lỗi xảy ra trong quá trình thực thi chương trình. Khác với lỗi cú pháp, ngoại lệ xảy ra khi chương trình đang chạy, ví dụ như chia cho 0, truy cập chỉ số ngoài danh sách, hoặc mở một file không tồn tại.

Python cung cấp cơ chế `try-except` để xử lý các ngoại lệ này, giúp chương trình không bị dừng đột ngột.

### 2. Cú pháp cơ bản
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
    # Luôn luôn chạy, dù có lỗi hay không
    pass
```

### 3. Một số ngoại lệ thường gặp
- `ZeroDivisionError`: chia cho 0
- `ValueError`: giá trị không hợp lệ (ví dụ: chuyển "abc" thành số)
- `IndexError`: truy cập chỉ số ngoài danh sách
- `FileNotFoundError`: file không tồn tại
- `TypeError`: kiểu dữ liệu không phù hợp

### 4. Bắt nhiều ngoại lệ
Bạn có thể bắt nhiều loại ngoại lệ khác nhau bằng cách dùng nhiều khối `except`.

## Ví dụ minh họa

### Ví dụ 1: Xử lý chia cho 0
```python
try:
    a = int(input("Nhập số bị chia: "))
    b = int(input("Nhập số chia: "))
    ket_qua = a / b
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")
else:
    print(f"Kết quả: {ket_qua}")
finally:
    print("Chương trình kết thúc.")
```

### Ví dụ 2: Đọc file an toàn
```python
try:
    with open("data.txt", "r", encoding="utf-8") as f:
        noi_dung = f.read()
        print(noi_dung)
except FileNotFoundError:
    print("Lỗi: File 'data.txt' không tồn tại.")
except PermissionError:
    print("Lỗi: Không có quyền truy cập file.")
else:
    print("Đọc file thành công.")
finally:
    print("Hoàn tất thao tác đọc file.")
```

### Ví dụ 3: Xử lý nhập liệu người dùng
```python
def nhap_tuoi():
    while True:
        try:
            tuoi = int(input("Nhập tuổi của bạn: "))
            if tuoi < 0:
                raise ValueError("Tuổi không thể âm.")
            break
        except ValueError as e:
            print(f"Lỗi: {e}. Vui lòng nhập lại.")
    print(f"Tuổi của bạn là: {tuoi}")
```

## Bài tập thực hành
1. Viết hàm `chia_hai_so(a, b)` trả về kết quả chia `a` cho `b`. Xử lý các trường hợp `b = 0` và đầu vào không phải số.
2. Viết chương trình đọc một file số nguyên, mỗi dòng một số, tính trung bình các số đó. Xử lý các lỗi như file không tồn tại, dòng không phải số.
3. Viết hàm `tinh_can_bac_hai(x)` tính căn bậc hai của `x`. Nếu `x < 0`, báo lỗi hợp lý.
4. Viết chương trình cho phép người dùng nhập danh sách tên (ngăn cách bởi dấu phẩy), sau đó in ngẫu nhiên một tên. Xử lý trường hợp người dùng không nhập gì.
5. Viết hàm `doc_danh_sach_tu_file(filename)` đọc danh sách từ file, mỗi dòng là một phần tử. Xử lý lỗi file không tồn tại và file rỗng.

## Tổng kết
Xử lý ngoại lệ là kỹ năng quan trọng giúp chương trình của bạn trở nên **ổn định** và **dễ sử dụng hơn**. Bằng cách sử dụng `try-except-else-finally`, bạn có thể:
- Ngăn chương trình sập khi gặp lỗi.
- Cung cấp thông báo lỗi rõ ràng cho người dùng.
- Dọn dẹp tài nguyên (file, kết nối, v.v.) trong khối `finally`.

Hãy luôn cân nhắc: **Không nên bỏ qua mọi lỗi**, mà nên xử lý đúng cách hoặc ghi log để dễ dàng gỡ lỗi sau này.