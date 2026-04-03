# Bài học Python số 38: Xử lý ngoại lệ (Exception Handling) - Cấp độ Trung cấp

## Mục tiêu bài học
- Hiểu khái niệm ngoại lệ (exception) trong Python và tại sao cần xử lý chúng.
- Biết cách sử dụng khối `try`, `except`, `else`, và `finally` để kiểm soát lỗi chương trình.
- Áp dụng xử lý ngoại lệ vào các tình huống thực tế như đọc file, nhập liệu người dùng, phép chia, v.v.
- Viết code an toàn, tránh crash chương trình do lỗi không mong muốn.

## Lý thuyết chi tiết

Trong quá trình chạy chương trình, có thể xảy ra các lỗi không mong muốn như: chia cho 0, truy cập chỉ số ngoài danh sách, mở file không tồn tại, v.v. Những lỗi này gọi là **ngoại lệ (exception)**. Nếu không xử lý, chương trình sẽ dừng đột ngột.

Python cung cấp cơ chế `try-except` để bắt và xử lý các ngoại lệ, giúp chương trình tiếp tục chạy hoặc thông báo lỗi một cách thân thiện.

### Cú pháp cơ bản:
```python
try:
    # Đoạn code có thể gây lỗi
    pass
except LoaiException:
    # Xử lý nếu xảy ra lỗi thuộc loại này
    pass
else:
    # Chạy nếu KHÔNG có lỗi
    pass
finally:
    # Luôn chạy, dù có lỗi hay không
    pass
```

### Một số ngoại lệ phổ biến:
- `ZeroDivisionError`: chia cho 0
- `ValueError`: giá trị không hợp lệ (vd: chuyển "abc" thành số)
- `FileNotFoundError`: file không tồn tại
- `IndexError`: truy cập chỉ số vượt quá danh sách
- `KeyError`: truy cập khóa không tồn tại trong từ điển

### Ví dụ đơn giản:
```python
try:
    x = int(input("Nhập số: "))
    print(10 / x)
except ZeroDivisionError:
    print("Không được chia cho 0!")
except ValueError:
    print("Vui lòng nhập số hợp lệ!")
```

## Ví dụ minh họa

### Ví dụ 1: Đọc file an toàn
Chương trình đọc nội dung file, nhưng xử lý nếu file không tồn tại.

### Ví dụ 2: Nhập số nguyên an toàn
Hàm yêu cầu người dùng nhập số nguyên, lặp lại nếu nhập sai.

### Ví dụ 3: Tính điểm trung bình học sinh
Xử lý khi danh sách điểm rỗng hoặc có điểm không hợp lệ.

## Bài tập thực hành
1. Viết hàm chia hai số, xử lý lỗi chia cho 0 và nhập sai kiểu dữ liệu.
2. Viết chương trình đọc file văn bản và đếm số dòng, xử lý nếu file không tồn tại.
3. Viết hàm tìm phần tử lớn nhất trong danh sách, xử lý khi danh sách rỗng hoặc chứa phần tử không phải số.
4. Tạo chương trình đăng nhập đơn giản với số lần thử giới hạn, xử lý lỗi nhập sai định dạng.
5. Viết hàm chuyển chuỗi thành danh sách số, xử lý lỗi định dạng.

## Tổng kết
Xử lý ngoại lệ là kỹ năng quan trọng giúp chương trình của bạn **ổn định**, **chuyên nghiệp**, và **dễ bảo trì**. Thay vì để chương trình sập, bạn có thể bắt lỗi, thông báo rõ ràng, và đưa ra hướng xử lý phù hợp. Hãy luôn suy nghĩ về các trường hợp lỗi có thể xảy ra khi viết code, và sử dụng `try-except` một cách hợp lý.

> ✅ **Lưu ý**: Không nên dùng `except:` không có loại ngoại lệ cụ thể vì có thể che giấu lỗi quan trọng. Luôn bắt cụ thể từng loại lỗi nếu có thể.