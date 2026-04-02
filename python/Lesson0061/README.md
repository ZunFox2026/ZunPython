# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ các tệp tin. Trong bài này, chúng ta sẽ tìm hiểu cách làm việc với tệp tin trong Python, bao gồm cả việc đọc và ghi dữ liệu vào tệp tin.

## Lý thuyết
Để làm việc với tệp tin trong Python, bạn cần sử dụng hàm `open()` để mở tệp tin. Hàm này trả về một đối tượng tệp tin, cho phép bạn đọc và ghi dữ liệu vào tệp tin. Có hai chế độ mở tệp tin: chế độ đọc (`'r'`) và chế độ ghi (`'w'`). Nếu tệp tin không tồn tại, chế độ ghi sẽ tạo một tệp tin mới. Nếu tệp tin đã tồn tại, chế độ ghi sẽ xóa nội dung cũ và thay thế bằng nội dung mới.

Ngoài ra, bạn cũng cần biết về các phương thức của đối tượng tệp tin, bao gồm:
- `read()`: đọc nội dung của tệp tin
- `write()`: ghi nội dung vào tệp tin
- `close()`: đóng tệp tin

Ví dụ, để mở một tệp tin tên `example.txt` ở chế độ đọc, bạn có thể sử dụng lệnh `file = open('example.txt', 'r')`.

## Ví dụ
Dưới đây là một ví dụ minh họa cách làm việc với tệp tin:
```python
# Mở tệp tin ở chế độ đọc
file = open('example.txt', 'r')
# Đọc nội dung của tệp tin
content = file.read()
print(content)
# Đóng tệp tin
file.close()
```
Để ghi nội dung vào tệp tin, bạn có thể sử dụng chế độ ghi:
```python
# Mở tệp tin ở chế độ ghi
file = open('example.txt', 'w')
# Ghi nội dung vào tệp tin
file.write('Xin chào, thế giới!')
# Đóng tệp tin
file.close()
```
Lưu ý rằng khi sử dụng chế độ ghi, nếu tệp tin đã tồn tại, nội dung cũ sẽ bị xóa.

## Bài tập
Bài tập này yêu cầu bạn thực hiện các bước sau:
1. Tạo một tệp tin tên `hello.txt` và ghi nội dung `"Xin chào, thế giới!"` vào tệp tin đó.
2. Đọc nội dung của tệp tin `hello.txt` và in ra màn hình.
3. Thêm nội dung `"Đây là một bài tập về tệp tin."` vào cuối tệp tin `hello.txt`.
4. Đọc lại nội dung của tệp tin `hello.txt` và in ra màn hình.

Khi hoàn thành bài tập, bạn sẽ có thể làm việc với tệp tin trong Python và hiểu rõ về các chế độ mở tệp tin cũng như các phương thức của đối tượng tệp tin.