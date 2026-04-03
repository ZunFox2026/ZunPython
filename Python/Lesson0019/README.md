# Python 19: Xử Lý Danh Sách và Vòng Lặp

## Giới thiệu

Trong lập trình Python, danh sách (list) và vòng lặp (loop) là hai khái niệm cơ bản nhưng cực kỳ quan trọng. Danh sách giúp lưu trữ nhiều giá trị trong một biến duy nhất, còn vòng lặp giúp thực hiện lặp lại một khối lệnh nhiều lần một cách hiệu quả. Bài học này sẽ giúp bạn làm quen với cách xử lý danh sách bằng các vòng lặp phổ biến như `for` và `while`, từ đó xây dựng nền tảng vững chắc cho các chương trình Python sau này.

## Lý thuyết

- **Danh sách (List)**: Là cấu trúc dữ liệu cho phép lưu trữ nhiều phần tử, có thể thay đổi (mutable), và giữ nguyên thứ tự. Khai báo bằng dấu ngoặc vuông `[]`.
- **Vòng lặp `for`**: Duyệt qua từng phần tử trong danh sách một cách tự động.
- **Vòng lặp `while`**: Lặp theo điều kiện, thường dùng khi cần kiểm soát chỉ số (index) của danh sách.
- Các thao tác phổ biến: thêm phần tử (`append()`), truy cập phần tử theo chỉ số, và duyệt danh sách.

## Ví dụ

```python
# Khai báo danh sách
so = [1, 2, 3, 4, 5]

# Duyệt danh sách bằng vòng lặp for
print("Các số trong danh sách:")
for x in so:
    print(x)

# Duyệt bằng chỉ số với range và len
print("Duyệt theo chỉ số:")
for i in range(len(so)):
    print(f"Phần tử thứ {i}: {so[i]}")

# Dùng while để in các phần tử
print("Duyệt bằng while:")
i = 0
while i < len(so):
    print(so[i])
    i += 1
```

## Bài tập

1. Tạo danh sách chứa tên 5 bạn trong lớp, sau đó in ra từng tên bằng vòng lặp `for`.
2. Viết chương trình tính tổng các số trong danh sách `[10, 20, 30, 40, 50]` sử dụng vòng lặp `while`.
3. Nhập vào một danh sách số nguyên từ bàn phím (dừng khi nhập 0), sau đó in danh sách ra màn hình.

> Gợi ý: Dùng `list.append()` để thêm phần tử và `while True` kết hợp `break` để dừng nhập.