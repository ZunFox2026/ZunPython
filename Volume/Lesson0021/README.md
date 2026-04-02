# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một phần quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ tệp tin. Trong bài này, chúng ta sẽ tìm hiểu về các cách làm việc với tệp tin trong Python, bao gồm mở tệp tin, đọc và ghi dữ liệu, và đóng tệp tin.

## Lý thuyết
Để làm việc với tệp tin trong Python, bạn cần sử dụng hàm `open()`. Hàm này sẽ mở tệp tin và trả về một đối tượng tệp tin, cho phép bạn đọc và ghi dữ liệu. Có hai chế độ mở tệp tin chính: `r` (đọc) và `w` (ghi). Nếu bạn mở tệp tin ở chế độ `w` và tệp tin đã tồn tại, nội dung của tệp tin sẽ bị xóa. Nếu bạn muốn thêm dữ liệu vào tệp tin mà không xóa nội dung cũ, bạn có thể sử dụng chế độ `a` (thêm).

Sau khi mở tệp tin, bạn có thể sử dụng các phương thức như `read()`, `write()`, và `close()` để đọc, ghi, và đóng tệp tin. Bạn cũng có thể sử dụng vòng lặp `for` để đọc từng dòng trong tệp tin.

## Ví dụ
Dưới đây là một ví dụ về cách mở tệp tin, đọc và ghi dữ liệu:
```
# Mở tệp tin ở chế độ đọc
f = open('example.txt', 'r')
# Đọc nội dung của tệp tin
content = f.read()
print(content)
# Đóng tệp tin
f.close()

# Mở tệp tin ở chế độ ghi
f = open('example.txt', 'w')
# Ghi dữ liệu vào tệp tin
f.write('Xin chào, thế giới!')
# Đóng tệp tin
f.close()

# Mở tệp tin ở chế độ thêm
f = open('example.txt', 'a')
# Thêm dữ liệu vào tệp tin
f.write('\nThế giới rộng lớn!')
# Đóng tệp tin
f.close()
```
Bạn cũng có thể sử dụng `with` statement để mở tệp tin, điều này sẽ tự động đóng tệp tin khi bạn xong việc:
```
with open('example.txt', 'r') as f:
    content = f.read()
    print(content)
```
## Bài tập
Bài tập 1: Tạo một tệp tin mới có tên `hello.txt` và ghi nội dung "Xin chào, thế giới!" vào tệp tin đó.

Bài tập 2: Đọc nội dung của tệp tin `hello.txt` và in ra màn hình.

Bài tập 3: Thêm nội dung "Thế giới rộng lớn!" vào tệp tin `hello.txt`.

Bài tập 4: Tạo một tệp tin mới có tên `numbers.txt` và ghi các số từ 1 đến 10 vào tệp tin đó, mỗi số trên một dòng.

Bài tập 5: Đọc nội dung của tệp tin `numbers.txt` và tính tổng của các số trong tệp tin.