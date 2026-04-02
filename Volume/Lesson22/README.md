# Làm việc với tệp tin
## Giới thiệu
Bài học này sẽ giới thiệu về các kiến thức cơ bản khi làm việc với tệp tin trong Python. Tệp tin là một phần quan trọng trong việc lưu trữ và đọc dữ liệu trong các chương trình máy tính. Python cung cấp nhiều chức năng và phương thức để làm việc với tệp tin, giúp bạn có thể dễ dàng đọc, viết và xử lý dữ liệu từ tệp tin.

## Lý thuyết
Để làm việc với tệp tin trong Python, bạn cần hiểu về các khái niệm sau:
- **Mở tệp tin**: Trước khi đọc hoặc viết vào một tệp tin, bạn cần mở nó bằng hàm `open()`. Hàm này trả về một đối tượng tệp tin, bạn có thể sử dụng đối tượng này để đọc hoặc viết vào tệp tin.
- **Phương thức đọc**: Để đọc dữ liệu từ một tệp tin, bạn có thể sử dụng các phương thức như `read()`, `readline()`, `readlines()`.
- **Phương thức viết**: Để viết dữ liệu vào một tệp tin, bạn có thể sử dụng các phương thức như `write()`, `writelines()`.
- **Đóng tệp tin**: Sau khi hoàn thành việc đọc hoặc viết vào tệp tin, bạn nên đóng tệp tin bằng phương thức `close()` để giải phóng tài nguyên.

## Ví dụ
Dưới đây là một ví dụ đơn giản về việc đọc và viết vào một tệp tin:
```python
# Mở tệp tin để viết
f = open("test.txt", "w")
# Viết vào tệp tin
f.write("Xin chào, thế giới!")
# Đóng tệp tin
f.close()

# Mở tệp tin để đọc
f = open("test.txt", "r")
# Đọc từ tệp tin
print(f.read())
# Đóng tệp tin
f.close()
```
Ví dụ trên sẽ tạo một tệp tin mới có tên "test.txt" và viết vào đó dòng chữ "Xin chào, thế giới!". Sau đó, nó sẽ mở lại tệp tin và đọc nội dung, in ra màn hình.

## Bài tập
Bài tập này sẽ yêu cầu bạn thực hiện các nhiệm vụ sau:
- Tạo một tệp tin mới có tên "bai_tap.txt".
- Viết vào tệp tin dòng chữ "Đây là bài tập về tệp tin".
- Đọc nội dung từ tệp tin và in ra màn hình.
- Thêm một dòng chữ mới vào tệp tin.
- Đọc lại nội dung từ tệp tin và in ra màn hình.
Hãy sử dụng kiến thức đã học trong bài này để hoàn thành bài tập. Chúc bạn thành công!