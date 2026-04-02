# Làm việc với tệp
Đây là bài 7, cấp Cơ bản, giúp bạn hiểu rõ về cách làm việc với tệp trong Python.

## Giới thiệu
Trong lập trình, việc làm việc với tệp là một phần quan trọng. Tệp cho phép chúng ta lưu trữ và đọc dữ liệu một cách linh hoạt. Python cung cấp nhiều cách để tương tác với tệp, từ việc đọc và ghi tệp văn bản đến việc truy cập tệp nhị phân. Trong bài này, chúng ta sẽ tìm hiểu về cách làm việc với tệp trong Python.

## Lý thuyết
Để làm việc với tệp trong Python, bạn cần sử dụng hàm `open()`. Hàm này trả về một đối tượng tệp, cho phép bạn thực hiện các hoạt động như đọc và ghi tệp. Có nhiều chế độ mở tệp, bao gồm:
- `r`: Mở tệp để đọc.
- `w`: Mở tệp để ghi, nếu tệp không tồn tại thì sẽ được tạo.
- `a`: Mở tệp để thêm nội dung vào cuối tệp.
- `r+`: Mở tệp để đọc và ghi.
- `b`: Mở tệp ở chế độ nhị phân.

Khi làm việc với tệp, bạn cần nhớ đóng tệp sau khi sử dụng bằng phương thức `close()`. Tuy nhiên, để tránh phải nhớ đóng tệp, bạn có thể sử dụng lệnh `with`, nó sẽ tự động đóng tệp khi bạn kết thúc khối lệnh.

Ví dụ về mở và đóng tệp:
```python
file = open('example.txt', 'r')
# Đọc hoặc ghi tệp
file.close()
```
Hoặc sử dụng lệnh `with`:
```python
with open('example.txt', 'r') as file:
    # Đọc hoặc ghi tệp
```

## Ví dụ
Dưới đây là ví dụ về việc đọc và ghi tệp:
```python
# Tạo một tệp mới và ghi nội dung vào đó
with open('example.txt', 'w') as file:
    file.write('Xin chào, thế giới!')

# Đọc nội dung từ tệp
with open('example.txt', 'r') as file:
    print(file.read())
```
Kết quả sẽ là: `Xin chào, thế giới!`

## Bài tập
Bài tập 1: Tạo một tệp văn bản mới tên là `my_file.txt` và ghi dòng chữ "Tôi đang học Python" vào đó.
Bài tập 2: Đọc nội dung từ tệp `my_file.txt` và in nó ra màn hình.
Bài tập 3: Thêm nội dung vào cuối tệp `my_file.txt` bằng cách sử dụng chế độ mở tệp `a`.