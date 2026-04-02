# Bài 22: Làm việc với tệp tin
## Giới thiệu
Trong chương trình này, chúng ta sẽ tìm hiểu về cách làm việc với tệp tin trong Python. Tệp tin là một phần quan trọng trong việc lưu trữ và xử lý dữ liệu. Python cung cấp nhiều chức năng để làm việc với tệp tin, bao gồm đọc, viết, và chỉnh sửa.

## Lý thuyết
Để làm việc với tệp tin trong Python, bạn cần sử dụng hàm `open()`. Hàm này sẽ mở một tệp tin và trả về một đối tượng tệp tin. Đối tượng này có nhiều phương thức khác nhau để đọc, viết, và chỉnh sửa tệp tin.

Có ba chế độ mở tệp tin chính:
- `r`: Chế độ đọc. Mặc định, tệp tin sẽ được mở ở chế độ này.
- `w`: Chế độ viết. Nếu tệp tin đã tồn tại, nội dung sẽ bị xóa. Nếu không, một tệp tin mới sẽ được tạo.
- `a`: Chế độ thêm. Dữ liệu sẽ được thêm vào cuối tệp tin.

Ví dụ, để mở một tệp tin có tên `example.txt` ở chế độ đọc, bạn có thể sử dụng lệnh sau:
```
file = open("example.txt", "r")
```
Sau khi mở tệp tin, bạn có thể đọc nội dung của nó bằng phương thức `read()`. Để viết dữ liệu vào tệp tin, bạn có thể sử dụng phương thức `write()`.

## Ví dụ
Dưới đây là một ví dụ về cách đọc và viết tệp tin:
```python
# Mở tệp tin ở chế độ viết
file = open("example.txt", "w")

# Viết dữ liệu vào tệp tin
file.write("Xin chào, thế giới!")

# Đóng tệp tin
file.close()

# Mở tệp tin ở chế độ đọc
file = open("example.txt", "r")

# Đọc nội dung của tệp tin
content = file.read()

# In nội dung của tệp tin
print(content)

# Đóng tệp tin
file.close()
```
Kết quả của chương trình trên sẽ là:
```
Xin chào, thế giới!
```
## Bài tập
Bài tập này yêu cầu bạn tạo một chương trình để quản lý danh sách sinh viên. Chương trình sẽ cho phép người dùng thêm, xóa, và hiển thị thông tin của sinh viên.

Yêu cầu:
- Tạo một tệp tin có tên `sinh_vien.txt` để lưu trữ thông tin của sinh viên.
- Viết một hàm để thêm thông tin của sinh viên vào tệp tin.
- Viết một hàm để xóa thông tin của sinh viên khỏi tệp tin.
- Viết một hàm để hiển thị thông tin của tất cả sinh viên.

Lưu ý: Thông tin của sinh viên sẽ được lưu trữ dưới dạng `Tên;Địa chỉ;Số điện thoại`. Ví dụ: `Nguyễn Văn A;Hà Nội;0901234567`