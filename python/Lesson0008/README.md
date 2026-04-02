# Làm việc với tệp
Làm việc với tệp là một kỹ năng quan trọng trong lập trình Python, cho phép bạn lưu trữ và đọc dữ liệu từ các tệp tin. Trong bài này, chúng ta sẽ tìm hiểu về các cách đọc và ghi dữ liệu vào tệp tin.

## Giới thiệu
Trong Python, bạn có thể làm việc với các loại tệp tin khác nhau như tệp tin văn bản (.txt), tệp tin CSV (.csv), tệp tin JSON (.json),... Để làm việc với tệp tin, bạn cần mở tệp tin đó bằng hàm `open()`. Hàm này sẽ trả về một đối tượng tệp tin mà bạn có thể sử dụng để đọc hoặc ghi dữ liệu.

## Lý thuyết
Để mở một tệp tin, bạn cần sử dụng hàm `open()` với hai tham số: đường dẫn đến tệp tin và chế độ mở tệp tin. Có ba chế độ mở tệp tin chính:
- `r`: Mở tệp tin để đọc.
- `w`: Mở tệp tin để ghi. Nếu tệp tin đã tồn tại, nội dung của tệp tin sẽ bị xóa. Nếu tệp tin không tồn tại, một tệp tin mới sẽ được tạo.
- `a`: Mở tệp tin để thêm nội dung. Nếu tệp tin đã tồn tại, nội dung mới sẽ được thêm vào cuối tệp tin. Nếu tệp tin không tồn tại, một tệp tin mới sẽ được tạo.

Bạn cũng có thể sử dụng các chế độ mở tệp tin khác như `r+`, `w+`, `a+`,... để thực hiện các hành động đọc và ghi phức tạp hơn.

## Ví dụ
Dưới đây là một ví dụ minh họa cách mở và ghi dữ liệu vào một tệp tin:
```python
# Mở tệp tin để ghi
f = open('example.txt', 'w')

# Ghi dữ liệu vào tệp tin
f.write('Xin chào, thế giới!')

# Đóng tệp tin
f.close()
```
Sau khi chạy đoạn code trên, một tệp tin mới có tên `example.txt` sẽ được tạo với nội dung `Xin chào, thế giới!`.

Để đọc dữ liệu từ tệp tin, bạn có thể sử dụng hàm `read()`:
```python
# Mở tệp tin để đọc
f = open('example.txt', 'r')

# Đọc dữ liệu từ tệp tin
data = f.read()

# Đóng tệp tin
f.close()

# In dữ liệu
print(data)
```
Khi chạy đoạn code trên, nội dung của tệp tin `example.txt` sẽ được in ra màn hình.

## Bài tập
Bài tập 1: Tạo một tệp tin mới có tên `hello.txt` và ghi nội dung `Xin chào, thế giới!` vào tệp tin đó.
Bài tập 2: Đọc nội dung của tệp tin `hello.txt` và in ra màn hình.
Bài tập 3: Tạo một tệp tin mới có tên `numbers.txt` và ghi các số từ 1 đến 10 vào tệp tin đó, mỗi số trên một dòng.
Bài tập 4: Đọc nội dung của tệp tin `numbers.txt` và tính tổng của các số trong tệp tin.