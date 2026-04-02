# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng trong lập trình, cho phép bạn lưu trữ và truy xuất dữ liệu từ các tệp tin khác nhau. Trong bài này, chúng ta sẽ tìm hiểu cách làm việc với tệp tin trong Python, bao gồm việc đọc và ghi tệp tin.

## Lý thuyết
Trong Python, bạn có thể làm việc với tệp tin bằng cách sử dụng hàm `open()`. Hàm này sẽ mở tệp tin và trả về một đối tượng tệp tin, cho phép bạn đọc và ghi dữ liệu vào tệp tin. Có nhiều chế độ mở tệp tin khác nhau, bao gồm:
- `r`: Mở tệp tin để đọc.
- `w`: Mở tệp tin để ghi, nếu tệp tin đã tồn tại thì sẽ bị xóa.
- `a`: Mở tệp tin để ghi, nếu tệp tin đã tồn tại thì sẽ được附 thêm vào cuối tệp tin.
- `r+`: Mở tệp tin để đọc và ghi.
Bạn cũng có thể chỉ định kiểu tệp tin bằng cách thêm `t` cho tệp tin văn bản hoặc `b` cho tệp tin nhị phân vào chế độ mở tệp tin.

## Ví dụ
Ví dụ về việc đọc và ghi tệp tin:
```python
# Mở tệp tin để đọc
f = open('example.txt', 'r')
# Đọc nội dung tệp tin
content = f.read()
print(content)
# Đóng tệp tin
f.close()

# Mở tệp tin để ghi
f = open('example.txt', 'w')
# Ghi nội dung vào tệp tin
f.write('Xin chào, thế giới!')
# Đóng tệp tin
f.close()
```
Lưu ý rằng sau khi mở tệp tin, bạn cần đóng tệp tin lại bằng cách gọi phương thức `close()` để giải phóng tài nguyên.

## Bài tập
Bài tập 1: Tạo một tệp tin văn bản có tên là `hello.txt` và ghi nội dung `Xin chào, thế giới!` vào tệp tin đó.
Bài tập 2: Đọc nội dung của tệp tin `hello.txt` và in ra màn hình.
Bài tập 3: Tạo một tệp tin nhị phân có tên là `image.jpg` và ghi một hình ảnh vào tệp tin đó.
Bài tập 4: Đọc nội dung của tệp tin `image.jpg` và lưu vào một tệp tin khác có tên là `image_copy.jpg`.