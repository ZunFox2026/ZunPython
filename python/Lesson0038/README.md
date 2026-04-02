# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng trong lập trình Python. Trong phần này, chúng ta sẽ tìm hiểu cách đọc, ghi và thực hiện các thao tác khác trên tệp tin. Bài học này sẽ giúp bạn hiểu rõ cách sử dụng tệp tin trong chương trình Python của mình.

## Lý thuyết
Trong Python, chúng ta có thể làm việc với tệp tin bằng cách sử dụng các hàm và phương thức có sẵn. Để mở một tệp tin, chúng ta sử dụng hàm `open()`. Hàm này trả về một đối tượng tệp tin, chúng ta có thể sử dụng đối tượng này để đọc hoặc ghi dữ liệu vào tệp tin. Có hai chế độ mở tệp tin là `r` (đọc) và `w` (ghi). Nếu tệp tin không tồn tại và chúng ta mở nó ở chế độ `w`, Python sẽ tạo một tệp tin mới.

Để đọc dữ liệu từ tệp tin, chúng ta có thể sử dụng phương thức `read()`. Phương thức này trả về một chuỗi chứa toàn bộ nội dung của tệp tin. Để ghi dữ liệu vào tệp tin, chúng ta có thể sử dụng phương thức `write()`.

## Ví dụ
Dưới đây là ví dụ minh họa cách đọc và ghi dữ liệu vào tệp tin:
```python
# Mở tệp tin ở chế độ đọc
f = open("example.txt", "r")
# Đọc nội dung của tệp tin
content = f.read()
print(content)
# Đóng tệp tin
f.close()

# Mở tệp tin ở chế độ ghi
f = open("example.txt", "w")
# Ghi dữ liệu vào tệp tin
f.write("Hello, World!")
# Đóng tệp tin
f.close()
```
Trong ví dụ trên, chúng ta mở tệp tin `example.txt` ở chế độ đọc, đọc nội dung của tệp tin và in nó ra màn hình. Sau đó, chúng ta mở tệp tin lại ở chế độ ghi, ghi dữ liệu vào tệp tin và đóng tệp tin.

## Bài tập
Bài tập này yêu cầu bạn tạo một chương trình Python để quản lý danh sách sinh viên. Chương trình sẽ cho phép người dùng thêm, xóa và xem danh sách sinh viên. Dữ liệu sẽ được lưu trữ trong một tệp tin tên là `students.txt`.

Yêu cầu:

* Tạo một hàm để thêm sinh viên vào danh sách.
* Tạo một hàm để xóa sinh viên khỏi danh sách.
* Tạo một hàm để xem danh sách sinh viên.
* Sử dụng tệp tin `students.txt` để lưu trữ dữ liệu.

Gợi ý: Sử dụng các phương thức `read()`, `write()` và `close()` để làm việc với tệp tin.