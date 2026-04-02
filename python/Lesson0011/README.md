# Làm việc với file
## Giới thiệu
Làm việc với file là một kỹ năng quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ các file. Trong bài này, chúng ta sẽ tìm hiểu về cách làm việc với file trong Python, bao gồm cả việc đọc và ghi file.

## Lý thuyết
Trong Python, bạn có thể làm việc với file bằng cách sử dụng các hàm và phương thức sau:
- `open()`: Hàm này được sử dụng để mở một file. Nó trả về một đối tượng file mà bạn có thể sử dụng để đọc hoặc ghi dữ liệu.
- `read()`: Phương thức này được sử dụng để đọc dữ liệu từ một file.
- `write()`: Phương thức này được sử dụng để ghi dữ liệu vào một file.
- `close()`: Phương thức này được sử dụng để đóng một file.

Có nhiều chế độ mở file khác nhau, bao gồm:
- `r`: Mở file để đọc.
- `w`: Mở file để ghi. Nếu file đã tồn tại, nội dung của nó sẽ bị xóa.
- `a`: Mở file để ghi. Nếu file đã tồn tại, dữ liệu mới sẽ được thêm vào cuối file.
- `r+`: Mở file để đọc và ghi.

## Ví dụ
Dưới đây là một ví dụ về cách đọc và ghi file:
```python
# Mở file để ghi
file = open("example.txt", "w")
file.write("Xin chào, thế giới!")
file.close()

# Mở file để đọc
file = open("example.txt", "r")
nội_dung = file.read()
print(nội_dung)
file.close()
```
Trong ví dụ này, chúng ta mở một file có tên `example.txt` để ghi, sau đó viết nội dung `"Xin chào, thế giới!"` vào file. Sau đó, chúng ta mở file để đọc và in nội dung của nó ra màn hình.

## Bài tập
Bài tập này yêu cầu bạn thực hiện các bước sau:
- Tạo một file có tên `bai_tap.txt`.
- Viết một chương trình để ghi nội dung `"Tôi đang học lập trình Python"` vào file `bai_tap.txt`.
- Đọc nội dung của file `bai_tap.txt` và in nó ra màn hình.
- Thêm nội dung `"Tôi đang học về file"` vào cuối file `bai_tap.txt`.
- Đọc lại nội dung của file `bai_tap.txt` và in nó ra màn hình.

Hãy thử thực hiện bài tập này để rèn luyện kỹ năng làm việc với file trong Python!