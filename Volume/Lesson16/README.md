# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng khi lập trình, giúp bạn lưu trữ và đọc dữ liệu từ các tệp tin khác nhau. Trong bài này, chúng ta sẽ tìm hiểu về cách làm việc với tệp tin trong Python, bao gồm cả việc đọc và ghi dữ liệu.

## Lý thuyết
Để làm việc với tệp tin trong Python, bạn cần sử dụng hàm `open()` để mở tệp tin. Hàm này sẽ trả về một đối tượng tệp tin, cho phép bạn đọc và ghi dữ liệu. Có nhiều chế độ mở tệp tin khác nhau, bao gồm:
- `r`: Mở tệp tin để đọc.
- `w`: Mở tệp tin để ghi, nếu tệp tin không tồn tại thì sẽ tạo mới.
- `a`: Mở tệp tin để ghi, nếu tệp tin không tồn tại thì sẽ tạo mới, nếu tệp tin đã tồn tại thì sẽ thêm dữ liệu vào cuối tệp tin.
- `r+`: Mở tệp tin để đọc và ghi.
- `w+`: Mở tệp tin để đọc và ghi, nếu tệp tin không tồn tại thì sẽ tạo mới.

Khi mở tệp tin, bạn cũng cần chỉ định đường dẫn đến tệp tin. Đường dẫn này có thể là đường dẫn tuyệt đối hoặc đường dẫn tương đối.

## Ví dụ
Ví dụ về cách mở và đọc một tệp tin:
```python
# Mở tệp tin để đọc
f = open('example.txt', 'r')

# Đọc dữ liệu từ tệp tin
data = f.read()

# In dữ liệu
print(data)

# Đóng tệp tin
f.close()
```
Ví dụ về cách mở và ghi dữ liệu vào một tệp tin:
```python
# Mở tệp tin để ghi
f = open('example.txt', 'w')

# Ghi dữ liệu vào tệp tin
f.write('Hello, World!')

# Đóng tệp tin
f.close()
```
## Bài tập
Bài tập 1: Tạo một tệp tin mới có tên là `hello.txt` và ghi dữ liệu `Hello, World!` vào tệp tin đó.
Bài tập 2: Đọc dữ liệu từ tệp tin `hello.txt` và in dữ liệu đó ra màn hình.
Bài tập 3: Tạo một chương trình cho phép người dùng nhập dữ liệu và ghi dữ liệu đó vào một tệp tin có tên là `user_input.txt`.