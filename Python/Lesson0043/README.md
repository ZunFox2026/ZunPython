# Python 43: Xử Lý Danh Sách và Vòng Lặp

## Giới thiệu

Trong lập trình Python, danh sách (list) và vòng lặp là hai khái niệm cơ bản nhưng cực kỳ quan trọng. Danh sách giúp lưu trữ nhiều giá trị trong một biến duy nhất, còn vòng lặp cho phép thực hiện lặp lại một đoạn mã nhiều lần. Kết hợp hai công cụ này, bạn có thể xử lý dữ liệu một cách hiệu quả và linh hoạt. Bài học này sẽ giúp bạn nắm vững cách sử dụng danh sách cùng các vòng lặp `for` và `while` trong Python.

## Lý thuyết

- **Danh sách (List)**: Là cấu trúc dữ liệu lưu trữ nhiều phần tử theo thứ tự, có thể thay đổi (mutable). Khai báo bằng dấu ngoặc vuông `[]`.
- **Vòng lặp `for`**: Duyệt qua từng phần tử trong danh sách.
- **Vòng lặp `while`**: Lặp khi điều kiện còn đúng, thường dùng khi cần kiểm soát chỉ số.
- Các thao tác phổ biến: thêm phần tử (`append()`), truy cập phần tử theo chỉ số, duyệt danh sách.

## Ví dụ

Dưới đây là ví dụ minh họa cách sử dụng danh sách và vòng lặp để in từng phần tử:

```python
# Tạo danh sách các số
numbers = [3, 7, 1, 9, 4]

# Duyệt danh sách bằng vòng lặp for
print("Các số trong danh sách:")
for num in numbers:
    print(num)

# Duyệt bằng vòng lặp while
print("\nSử dụng while:")
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
```

**Kết quả:**
```
Các số trong danh sách:
3
7
1
9
4

Sử dụng while:
3
7
1
9
4
```

## Bài tập

1. Tạo danh sách chứa tên của 5 người bạn, sau đó in ra màn hình bằng vòng lặp `for`.
2. Viết chương trình tính tổng các số trong danh sách `[2, 4, 6, 8, 10]` sử dụng vòng lặp `while`.
3. Thêm phần tử "Python" vào cuối danh sách `['Học', 'lập', 'trình']` rồi in toàn bộ danh sách.

> Gợi ý: Dùng `append()` để thêm phần tử, `len()` để kiểm tra độ dài danh sách.