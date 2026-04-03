# Bài học Python số 24 - Cấp độ Trung cấp

## Chủ đề: Xử lý lỗi và ngoại lệ (Exception Handling)

Trong lập trình, không phải lúc nào mọi thứ cũng diễn ra như mong đợi. Khi chương trình gặp lỗi (ví dụ: chia cho 0, truy cập file không tồn tại, nhập liệu sai định dạng...), chương trình có thể bị dừng đột ngột. Để chương trình vẫn hoạt động ổn định, chúng ta cần học cách **xử lý lỗi và ngoại lệ**.

Bài học này sẽ giúp bạn hiểu cách bắt và xử lý các lỗi trong Python bằng khối lệnh `try-except`, cũng như cách chủ động tạo và xử lý các ngoại lệ tùy chỉnh.

---

### 1. Mục tiêu bài học

Sau bài học này, học viên sẽ có thể:
- Hiểu được khái niệm ngoại lệ (exception) trong Python.
- Sử dụng khối `try-except` để bắt và xử lý lỗi.
- Xử lý nhiều loại ngoại lệ khác nhau.
- Sử dụng `else` và `finally` trong xử lý ngoại lệ.
- Tạo và ném ngoại lệ tùy chỉnh bằng `raise`.
- Viết chương trình ổn định, thân thiện với người dùng khi có lỗi xảy ra.

---

### 2. Lý thuyết chi tiết

#### a. Ngoại lệ là gì?

Ngoại lệ (Exception) là các sự kiện bất thường xảy ra trong quá trình thực thi chương trình, làm gián đoạn luồng thực thi bình thường. Ví dụ:

```python
print(10 / 0)
```

Sẽ sinh ra lỗi: `ZeroDivisionError: division by zero`.

#### b. Cú pháp try-except

Cấu trúc cơ bản:

```python
try:
    # Khối lệnh có thể gây lỗi
    pass
except LoaiLoi:
    # Xử lý lỗi cụ thể
    pass
```

Ví dụ:

```python
def chia(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0")
        return None
```

#### c. Bắt nhiều ngoại lệ

```python
try:
    x = int(input("Nhập số: "))
    print(10 / x)
except ValueError:
    print("Bạn phải nhập một số nguyên!")
except ZeroDivisionError:
    print("Không thể chia cho 0!")
```

#### d. Khối else và finally

- `else`: chạy nếu không có lỗi xảy ra.
- `finally`: luôn chạy, dù có lỗi hay không.

```python
try:
    f = open("file.txt")
except FileNotFoundError:
    print("Không tìm thấy file")
else:
    print("File đã được mở thành công")
finally:
    print("Khối finally luôn được thực thi")
```

#### e. Ném ngoại lệ (raise)

Bạn có thể chủ động ném ra một ngoại lệ:

```python
if age < 0:
    raise ValueError("Tuổi không thể âm")
```

---

### 3. Ví dụ minh họa

Xem file `main.py` để chạy các ví dụ hoàn chỉnh.

---

### 4. Bài tập thực hành

Xem file `exercises.py` để làm bài tập. Sau đó kiểm tra lời giải trong `solutions.py`.

---

### 5. Tổng kết

Xử lý ngoại lệ là kỹ năng quan trọng giúp chương trình của bạn **ổn định**, **dễ bảo trì** và **thân thiện với người dùng**. Bằng cách sử dụng `try-except-else-finally` và `raise`, bạn có thể kiểm soát luồng chương trình khi có lỗi, thay vì để chương trình sập.

Hãy luyện tập thường xuyên để thành thạo kỹ năng này!
