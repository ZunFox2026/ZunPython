# Bài học Python số 18 - Cấp độ Trung cấp

## Chủ đề: Xử lý ngoại lệ (Exception Handling) và sử dụng `try-except-finally`

Trong lập trình, không phải lúc nào mọi thứ cũng diễn ra như mong đợi. Dữ liệu đầu vào có thể sai định dạng, file có thể không tồn tại, hoặc kết nối mạng có thể bị gián đoạn. Nếu không xử lý những tình huống này, chương trình sẽ bị sập (crash).

Bài học này sẽ giúp bạn học cách xử lý các lỗi (ngoại lệ) trong Python một cách chuyên nghiệp bằng câu lệnh `try-except-finally`, từ đó xây dựng các chương trình ổn định và thân thiện với người dùng hơn.

---

### 1. Mục tiêu bài học

Sau bài học này, bạn sẽ có thể:
- Hiểu được khái niệm ngoại lệ (exception) trong Python.
- Sử dụng `try`, `except`, `else`, và `finally` để xử lý lỗi.
- Xử lý nhiều loại ngoại lệ khác nhau.
- Tự viết và phát sinh ngoại lệ khi cần.
- Viết chương trình an toàn và dễ bảo trì hơn.

---

### 2. Lý thuyết chi tiết

#### Khái niệm ngoại lệ (Exception)

Ngoại lệ là các lỗi xảy ra trong quá trình thực thi chương trình, ví dụ như chia cho 0, truy cập chỉ số vượt ngoài danh sách, hoặc mở một file không tồn tại.

Python cung cấp cơ chế `try-except` để bắt và xử lý các lỗi này.

#### Cú pháp cơ bản

```python
try:
    # Các câu lệnh có thể gây lỗi
    pass
except LoaiLoi1:
    # Xử lý lỗi loại 1
    pass
except LoaiLoi2:
    # Xử lý lỗi loại 2
    pass
else:
    # Chạy nếu không có lỗi
    pass
finally:
    # Luôn chạy, bất kể có lỗi hay không
    pass
```

#### Một số loại ngoại lệ phổ biến

- `ValueError`: Khi giá trị không hợp lệ (ví dụ: chuyển "abc" thành số).
- `TypeError`: Khi kiểu dữ liệu không phù hợp.
- `IndexError`: Khi truy cập chỉ số vượt ngoài danh sách.
- `KeyError`: Khi truy cập khóa không tồn tại trong từ điển.
- `FileNotFoundError`: Khi cố mở file không tồn tại.
- `ZeroDivisionError`: Khi chia một số cho 0.

#### Ví dụ đơn giản

```python
try:
    x = int(input("Nhập một số: "))
    print(10 / x)
except ZeroDivisionError:
    print("Không thể chia cho 0!")
except ValueError:
    print("Bạn phải nhập một số!")
```

---

### 3. Ví dụ minh họa

**Ví dụ 1:** Đọc file dữ liệu điểm số học sinh và tính trung bình

**Ví dụ 2:** Xử lý đầu vào người dùng khi đăng ký tuổi

**Ví dụ 3:** Tính toán an toàn với danh sách điểm

---

### 4. Bài tập thực hành

1. Viết hàm `chia_hai_so(a, b)` trả về kết quả a/b, xử lý lỗi chia cho 0 và nhập sai kiểu.
2. Viết chương trình đọc file `diem.txt`, xử lý trường hợp file không tồn tại.
3. Viết hàm `tim_phan_tu(danh_sach, chi_so)` truy cập phần tử tại chỉ số, xử lý lỗi chỉ số vượt quá.
4. Viết chương trình nhập tên và tuổi, đảm bảo tuổi là số nguyên dương.
5. Viết hàm `tinh_can_bac_hai(x)` với điều kiện x >= 0, phát sinh lỗi nếu x < 0.

---

### 5. Tổng kết

Xử lý ngoại lệ là kỹ năng thiết yếu khi lập trình. Nó giúp chương trình hoạt động ổn định, tránh crash và cung cấp thông tin hữu ích cho người dùng. Hãy luôn suy nghĩ về các tình huống lỗi có thể xảy ra và xử lý chúng một cách hợp lý.

Sử dụng `try-except-finally` một cách linh hoạt để:
- Bắt các lỗi cụ thể.
- Cung cấp thông báo lỗi rõ ràng.
- Giải phóng tài nguyên trong khối `finally`.
- Không bỏ qua lỗi nếu không cần thiết (tránh `except:` không rõ loại).

Hãy luyện tập nhiều để trở thành lập trình viên Python vững vàng hơn!