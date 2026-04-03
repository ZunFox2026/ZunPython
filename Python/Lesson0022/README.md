# Python 22 Cấp Cơ Bản

## Giới thiệu

Bài học "Python 22 Cấp Cơ Bản" là bài thứ 22 trong chuỗi bài học Python dành cho người mới bắt đầu. Mục tiêu của bài học này là giúp người học hiểu và vận dụng kiến thức về **vòng lặp `while`** trong Python – một cấu trúc điều khiển quan trọng dùng để lặp lại một khối lệnh khi điều kiện còn đúng. Vòng lặp `while` rất hữu ích khi số lần lặp chưa được xác định trước, ví dụ như khi chờ người dùng nhập dữ liệu hợp lệ hoặc xử lý dữ liệu cho đến khi đạt điều kiện dừng.

## Lý thuyết

Vòng lặp `while` trong Python kiểm tra một điều kiện trước mỗi lần lặp. Nếu điều kiện đúng (`True`), các câu lệnh bên trong vòng lặp sẽ được thực hiện. Quá trình này tiếp tục cho đến khi điều kiện trở thành sai (`False`).

Cú pháp cơ bản:
```python
while điều_kiện:
    # Các câu lệnh lặp lại
```

Lưu ý: Cần đảm bảo rằng điều kiện trong `while` sẽ trở thành `False` tại một thời điểm nào đó để tránh **vòng lặp vô hạn**.

## Ví dụ

Dưới đây là một ví dụ đơn giản sử dụng vòng lặp `while` để in các số từ 1 đến 5:

```python
i = 1
while i <= 5:
    print(i)
    i += 1  # Tăng i lên 1 sau mỗi lần lặp
```

**Kết quả in ra màn hình:**
```
1
2
3
4
5
```

Trong ví dụ trên, biến `i` được khởi tạo bằng 1. Mỗi lần lặp, chương trình kiểm tra `i <= 5`. Sau khi in giá trị của `i`, biến này được tăng lên 1. Khi `i` vượt quá 5, điều kiện sai và vòng lặp dừng.

## Bài tập

1. Viết chương trình sử dụng vòng lặp `while` để tính tổng các số từ 1 đến 10.
2. Nhập một số nguyên dương từ người dùng. Dùng vòng lặp `while` để in ra các số chẵn từ 0 đến số đó.
3. Viết chương trình yêu cầu người dùng nhập "yes" hoặc "no". Tiếp tục hỏi cho đến khi họ nhập đúng một trong hai lựa chọn.

👉 Gợi ý: Sử dụng `input()` để nhận dữ liệu và kiểm tra điều kiện trong `while`.