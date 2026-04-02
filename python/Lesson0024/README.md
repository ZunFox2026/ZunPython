# Làm việc với tệp ZIP
## Giới thiệu
Trong quá trình lập trình, chúng ta thường phải làm việc với các tệp và thư mục. Một trong những định dạng tệp phổ biến được sử dụng để nén và lưu trữ dữ liệu là tệp ZIP. Bài viết này sẽ hướng dẫn bạn cách làm việc với tệp ZIP bằng ngôn ngữ lập trình Python.

## Lý thuyết
Tệp ZIP là một loại tệp nén, cho phép chúng ta lưu trữ nhiều tệp và thư mục vào một tệp duy nhất. Điều này giúp giảm thiểu không gian lưu trữ và tăng tốc độ truyền tải dữ liệu. Để làm việc với tệp ZIP, Python cung cấp thư viện `zipfile`. Thư viện này cho phép chúng ta tạo, đọc và viết tệp ZIP.

Một số hàm và phương thức quan trọng trong thư viện `zipfile` bao gồm:
- `ZipFile`: Đây là lớp cơ bản để làm việc với tệp ZIP. Chúng ta có thể sử dụng nó để tạo, đọc và viết tệp ZIP.
- `write`: Phương thức này được sử dụng để thêm tệp vào tệp ZIP.
- `read`: Phương thức này được sử dụng để đọc nội dung của tệp ZIP.
- `extract`: Phương thức này được sử dụng để giải nén tệp ZIP.

## Ví dụ
Dưới đây là một ví dụ về cách tạo và đọc tệp ZIP bằng Python:
```python
import zipfile

# Tạo tệp ZIP
with zipfile.ZipFile('example.zip', 'w') as zip_file:
    zip_file.write('file1.txt')
    zip_file.write('file2.txt')

# Đọc tệp ZIP
with zipfile.ZipFile('example.zip', 'r') as zip_file:
    print(zip_file.namelist())
    zip_file.extractall()
```
Trong ví dụ trên, chúng ta tạo một tệp ZIP có tên `example.zip` và thêm two tệp `file1.txt` và `file2.txt` vào nó. Sau đó, chúng ta đọc tệp ZIP và in ra danh sách các tệp bên trong. Cuối cùng, chúng ta giải nén toàn bộ tệp ZIP vào thư mục hiện tại.

## Bài tập
Bài tập này yêu cầu bạn tạo một chương trình Python để làm việc với tệp ZIP. Chương trình nên có các chức năng sau:
- Tạo một tệp ZIP mới
- Thêm tệp vào tệp ZIP
- Đọc danh sách các tệp bên trong tệp ZIP
- Giải nén tệp ZIP
- Xóa tệp ZIP

Bạn có thể tham khảo ví dụ trên và thư viện `zipfile` để hoàn thành bài tập này. Chúc bạn thành công!