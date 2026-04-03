# Python 28 Cấp Cơ Bản

## Giới thiệu

"Python 28 Cấp Cơ Bản" là bài học thứ 28 trong chuỗi các bài học giúp người mới bắt đầu làm quen và nắm vững những kiến thức nền tảng về ngôn ngữ lập trình Python. Bài học này tập trung vào chủ đề **xử lý lỗi (Exception Handling)** – một kỹ năng quan trọng giúp chương trình hoạt động ổn định hơn khi gặp các tình huống bất ngờ như nhập liệu sai, lỗi chia cho 0, hoặc truy cập tệp không tồn tại. Việc xử lý lỗi đúng cách giúp chương trình không bị sập và cung cấp thông báo rõ ràng cho người dùng.

## Lý thuyết

Trong Python, lỗi được chia thành hai loại chính: **lỗi cú pháp (syntax errors)** và **lỗi ngoại lệ (exceptions)**. Lỗi ngoại lệ xảy ra trong quá trình thực thi chương trình, ví dụ như `ZeroDivisionError`, `ValueError`, hay `FileNotFoundError`. Để xử lý các lỗi này, Python cung cấp khối lệnh `try-except`:

- `try`: Chứa đoạn mã có thể gây lỗi.
- `except`: Xử lý lỗi nếu xảy ra.
- `else`: Thực thi nếu không có lỗi.
- `finally`: Luôn thực thi, dù có lỗi hay không.

## Ví dụ

Dưới đây là ví dụ minh họa cách sử dụng `try-except` để xử lý lỗi chia cho 0:

```python
try:
    num1 = int(input("Nhập số thứ nhất: "))
    num2 = int(input("Nhập số thứ hai: "))
    result = num1 / num2
except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
else:
    print(f"Kết quả: {result}")
finally:
    print("Chương trình kết thúc.")
```

## Bài tập

1. Viết chương trình yêu cầu người dùng nhập tuổi. Sử dụng `try-except` để đảm bảo giá trị nhập vào là số nguyên dương. Nếu không, in ra thông báo lỗi.
2. Mở một tệp văn bản để đọc. Xử lý trường hợp tệp không tồn tại bằng `FileNotFoundError`.
3. Viết hàm tính căn bậc hai của một số. Xử lý lỗi khi số âm bằng `try-except`.