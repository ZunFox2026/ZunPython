# Bài 24: Python Cơ bản

## Giới thiệu

Python là một ngôn ngữ lập trình phổ biến nhờ cú pháp đơn giản, dễ đọc và khả năng ứng dụng rộng rãi trong nhiều lĩnh vực như phát triển web, phân tích dữ liệu, trí tuệ nhân tạo, và tự động hóa. Bài học này sẽ cung cấp những kiến thức cơ bản về Python, giúp người mới bắt đầu làm quen với cú pháp, cấu trúc và cách viết chương trình đơn giản.

## Lý thuyết

Python là ngôn ngữ thông dịch, chạy theo trình tự từ trên xuống dưới. Một số đặc điểm chính:

- **Biến**: Không cần khai báo kiểu dữ liệu, ví dụ: `ten = "Python"`.
- **Kiểu dữ liệu phổ biến**: `int`, `float`, `str`, `bool`, `list`, `dict`.
- **Câu điều kiện**: Sử dụng `if`, `elif`, `else` với thụt lề để xác định khối lệnh.
- **Vòng lặp**: Có `for` và `while`.
- **Hàm**: Được định nghĩa bằng từ khóa `def`.

Python sử dụng **thụt lề (indentation)** thay cho dấu ngoặc để phân tách khối lệnh, vì vậy việc căn chỉnh code là rất quan trọng.

## Ví dụ

Dưới đây là một chương trình Python đơn giản kiểm tra số chẵn/lẻ:

```python
# Nhập số từ người dùng
so = int(input("Nhập một số nguyên: "))

# Kiểm tra chẵn hay lẻ
if so % 2 == 0:
    print(f"{so} là số chẵn.")
else:
    print(f"{so} là số lẻ.")
```

Chương trình này sử dụng:
- `input()` để nhận dữ liệu.
- `int()` để chuyển đổi sang số nguyên.
- Toán tử `%` để lấy phần dư.
- Câu lệnh `if-else` để rẽ nhánh chương trình.

## Bài tập

1. Viết chương trình tính tổng các số từ 1 đến n (với n được nhập từ bàn phím).
2. Viết hàm `tinh_diem_tb(toan, ly, hoa)` nhận 3 điểm số và trả về điểm trung bình.
3. Nhập tên người dùng và in ra lời chào: "Xin chào, [tên]!".

> Gợi ý: Sử dụng vòng lặp `for` và hàm `sum()` để giải bài 1; sử dụng `def` để định nghĩa hàm ở bài 2.