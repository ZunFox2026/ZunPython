# Bài học 8: Lỗi và Ngoại lệ (try-except)

Chào mừng bạn đến với **Bài học số 8** trong khóa học Python dành cho người mới bắt đầu! Trong bài học này, chúng ta sẽ tìm hiểu về **lỗi và ngoại lệ** trong Python, cách xử lý chúng bằng câu lệnh `try-except` để chương trình của bạn hoạt động ổn định hơn, ngay cả khi có sự cố xảy ra.

## Mục tiêu bài học

Sau bài học này, bạn sẽ có thể:
- Hiểu được sự khác biệt giữa lỗi cú pháp và ngoại lệ.
- Sử dụng câu lệnh `try-except` để bắt và xử lý ngoại lệ.
- Xử lý các loại ngoại lệ cụ thể như `ValueError`, `ZeroDivisionError`, `IndexError`, v.v.
- Viết chương trình an toàn, tránh bị sập khi người dùng nhập sai dữ liệu.

## Lý thuyết chi tiết

Trong quá trình viết chương trình, có thể xảy ra hai loại lỗi chính:

1. **Lỗi cú pháp (Syntax Error)**: Xảy ra khi bạn viết code sai cú pháp. Python sẽ không thể chạy chương trình.
   ```python
   print("Xin chào"  # Thiếu dấu ngoặc đóng
   ```

2. **Ngoại lệ (Exception)**: Xảy ra trong quá trình thực thi chương trình, dù cú pháp đúng. Ví dụ: chia cho 0, truy cập chỉ số ngoài danh sách, nhập sai kiểu dữ liệu...

Để chương trình không bị dừng đột ngột khi gặp ngoại lệ, chúng ta dùng khối `try-except`.

### Cú pháp cơ bản

```python
try:
    # Đoạn code có thể gây lỗi
    pass
except TênLỗi:
    # Xử lý lỗi
    pass
```

### Một số ngoại lệ phổ biến
- `ValueError`: Khi giá trị không hợp lệ (ví dụ: chuyển "abc" thành số).
- `ZeroDivisionError`: Chia cho 0.
- `IndexError`: Truy cập chỉ số vượt ngoài danh sách.
- `TypeError`: Kiểu dữ liệu không phù hợp.

Bạn cũng có thể bắt nhiều loại lỗi hoặc dùng `except` chung để bắt mọi lỗi.

## Ví dụ minh họa

### Ví dụ 1: Xử lý nhập số

Khi người dùng nhập chữ thay vì số, chương trình sẽ không bị sập.

```python
try:
    so = int(input("Nhập một số nguyên: "))
    print(f"Bạn đã nhập: {so}")
except ValueError:
    print("Lỗi: Bạn phải nhập một số nguyên!")
```

### Ví dụ 2: Chia hai số an toàn

Tránh lỗi chia cho 0.

```python
try:
    a = float(input("Nhập số bị chia: "))
    b = float(input("Nhập số chia: "))
    ket_qua = a / b
    print(f"Kết quả: {ket_qua}")
except ZeroDivisionError:
    print("Không thể chia cho 0!")
except ValueError:
    print("Bạn phải nhập số hợp lệ!")
```

### Ví dụ 3: Truy cập danh sách an toàn

```python
danh_sach = [10, 20, 30]
try:
    chi_so = int(input("Nhập chỉ số muốn truy cập: "))
    print(f"Giá trị tại vị trí {chi_so}: {danh_sach[chi_so]}")
except IndexError:
    print("Chỉ số vượt quá danh sách!")
except ValueError:
    print("Bạn phải nhập một số nguyên!")
```

## Bài tập thực hành

1. Viết chương trình nhập tuổi, kiểm tra nếu tuổi âm hoặc không phải số thì báo lỗi.
2. Viết chương trình tính trung bình cộng của hai số, xử lý lỗi khi người dùng nhập sai.
3. Viết chương trình truy cập phần tử trong từ điển, xử lý lỗi nếu khóa không tồn tại.
4. Viết chương trình đọc một số và tính căn bậc hai, xử lý nếu số âm.
5. Viết chương trình mô phỏng rút thăm trúng thưởng từ danh sách, xử lý khi danh sách rỗng.

## Tổng kết

- Dùng `try-except` để chương trình không bị sập khi có lỗi.
- Xử lý từng loại ngoại lệ cụ thể để thông báo rõ ràng.
- Luôn kiểm tra dữ liệu người dùng nhập vào.
- Đây là kỹ năng quan trọng để viết chương trình chuyên nghiệp và thân thiện.

Hãy thực hành nhiều để thành thạo! Chúc bạn học tốt!