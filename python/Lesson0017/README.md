# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một phần quan trọng trong lập trình, cho phép chúng ta lưu trữ và truy xuất dữ liệu từ các tệp tin. Trong bài này, chúng ta sẽ tìm hiểu về cách làm việc với tệp trong Python, bao gồm việc đọc và ghi dữ liệu vào tệp.

## Lý thuyết
Để làm việc với tệp trong Python, chúng ta cần sử dụng các hàm và phương thức sau:
- `open()`: Hàm này dùng để mở một tệp tin và trả về một đối tượng tệp.
- `read()`: Phương thức này dùng để đọc nội dung của tệp.
- `write()`: Phương thức này dùng để ghi nội dung vào tệp.
- `close()`: Phương thức này dùng để đóng tệp sau khi sử dụng.

Chúng ta cũng cần biết về các chế độ mở tệp, bao gồm:
- `r`: Mở tệp để đọc.
- `w`: Mở tệp để ghi, nếu tệp đã tồn tại thì nội dung sẽ bị xóa.
- `a`: Mở tệp để ghi, nếu tệp đã tồn tại thì nội dung sẽ được thêm vào cuối tệp.
- `x`: Mở tệp để tạo mới, nếu tệp đã tồn tại thì sẽ báo lỗi.

Ví dụ, để mở một tệp tin tên `example.txt` để đọc, chúng ta sử dụng câu lệnh sau:
```
file = open('example.txt', 'r')
```

## Ví dụ
Dưới đây là một số ví dụ minh họa cách làm việc với tệp trong Python:

- Đọc nội dung của tệp:
```python
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()
```

- Ghi nội dung vào tệp:
```python
file = open('example.txt', 'w')
file.write('Xin chào thế giới!')
file.close()
```

- Thêm nội dung vào cuối tệp:
```python
file = open('example.txt', 'a')
file.write('\nĐây là dòng thứ hai.')
file.close()
```

## Bài tập
Để luyện tập kỹ năng làm việc với tệp, bạn có thể thực hiện các bài tập sau:
- Tạo một tệp tin tên `hello.txt` và ghi nội dung "Xin chào thế giới!" vào tệp.
- Đọc nội dung của tệp `hello.txt` và in ra màn hình.
- Thêm nội dung "Đây là dòng thứ hai." vào cuối tệp `hello.txt`.
- Tạo một tệp tin tên `numbers.txt` và ghi các số từ 1 đến 10 vào tệp, mỗi số trên một dòng.
- Đọc nội dung của tệp `numbers.txt` và in ra màn hình.