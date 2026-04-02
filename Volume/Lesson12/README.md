# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng trong lập trình. Tệp tin là nơi lưu trữ dữ liệu của chương trình, và việc đọc, ghi, và xử lý tệp tin là một phần không thể thiếu của nhiều ứng dụng. Trong bài này, chúng ta sẽ tìm hiểu về cách làm việc với tệp tin trong Python.

## Lý thuyết
Python cung cấp nhiều cách để làm việc với tệp tin, bao gồm đọc, ghi, và xử lý tệp tin. Có hai loại tệp tin chính: tệp tin văn bản (text file) và tệp tin nhị phân (binary file). Tệp tin văn bản là loại tệp tin chứa dữ liệu dưới dạng văn bản, trong khi tệp tin nhị phân chứa dữ liệu dưới dạng nhị phân.

Để đọc một tệp tin trong Python, chúng ta có thể sử dụng hàm `open()` và chỉ định chế độ đọc (`'r'` cho đọc, `'w'` cho ghi, `'a'` cho thêm vào cuối tệp). Sau khi mở tệp tin, chúng ta có thể sử dụng phương thức `read()` để đọc nội dung của tệp tin.

Ví dụ, để đọc một tệp tin văn bản có tên `example.txt`, chúng ta có thể sử dụng đoạn code sau:
```python
f = open('example.txt', 'r')
noidung = f.read()
print(noidung)
f.close()
```
Tương tự, để ghi một tệp tin, chúng ta có thể sử dụng hàm `open()` với chế độ ghi (`'w'`) và phương thức `write()` để ghi nội dung vào tệp tin.

## Ví dụ
Giả sử chúng ta có một tệp tin văn bản có tên `example.txt` chứa nội dung sau:
```
Xin chào thế giới!
Đây là một ví dụ về tệp tin văn bản.
```
Chúng ta có thể sử dụng đoạn code sau để đọc và in nội dung của tệp tin:
```python
f = open('example.txt', 'r')
noidung = f.read()
print(noidung)
f.close()
```
Kết quả sẽ là:
```
Xin chào thế giới!
Đây là một ví dụ về tệp tin văn bản.
```
Chúng ta cũng có thể sử dụng đoạn code sau để ghi một nội dung mới vào tệp tin:
```python
f = open('example.txt', 'w')
f.write('Nội dung mới!')
f.close()
```
Sau khi chạy đoạn code này, nội dung của tệp tin `example.txt` sẽ được thay thế bằng `Nội dung mới!`.

## Bài tập
Bài tập 1: Tạo một tệp tin văn bản có tên `hello.txt` và chứa nội dung `Xin chào thế giới!`.
Bài tập 2: Đọc và in nội dung của tệp tin `hello.txt`.
Bài tập 3: Ghi một nội dung mới vào tệp tin `hello.txt`.
Bài tập 4: Tạo một chương trình Python để đọc và xử lý nội dung của một tệp tin văn bản. Chương trình nên có thể đọc nội dung của tệp tin, tìm kiếm một từ khóa, và in ra kết quả.