# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng trong lập trình. Trong bài này, chúng ta sẽ tìm hiểu về cách đọc và ghi tệp tin trong Python. Đây là một kỹ năng cơ bản nhưng rất cần thiết khi bạn muốn lưu trữ hoặc đọc dữ liệu từ tệp tin.

## Lý thuyết
Trong Python, bạn có thể làm việc với tệp tin bằng cách sử dụng hàm `open()`. Hàm này sẽ mở tệp tin và trả về một đối tượng tệp tin. Bạn có thể sử dụng đối tượng này để đọc hoặc ghi dữ liệu vào tệp tin. Có nhiều mode khi mở tệp tin, bao gồm:
- `r`: Mở tệp tin để đọc. Đây là mode mặc định.
- `w`: Mở tệp tin để ghi. Nếu tệp tin đã tồn tại, nội dung sẽ bị xóa.
- `a`: Mở tệp tin để ghi thêm. Nếu tệp tin đã tồn tại, nội dung mới sẽ được thêm vào cuối tệp tin.
- `x`: Mở tệp tin để tạo mới. Nếu tệp tin đã tồn tại, sẽ xuất hiện lỗi.
- `b`: Mở tệp tin dưới dạng binary.
- `t`: Mở tệp tin dưới dạng text. Đây là mode mặc định.
- `+`: Mở tệp tin để đọc và ghi.

Ví dụ, để mở tệp tin `test.txt` để đọc, bạn có thể sử dụng lệnh `open("test.txt", "r")`.

## Ví dụ
Dưới đây là một số ví dụ về cách làm việc với tệp tin trong Python:
```python
# Mở tệp tin để đọc
f = open("test.txt", "r")
content = f.read()
print(content)
f.close()

# Mở tệp tin để ghi
f = open("test.txt", "w")
f.write("Xin chào!")
f.close()

# Mở tệp tin để ghi thêm
f = open("test.txt", "a")
f.write(" Đây là nội dung mới.")
f.close()
```
Lưu ý rằng khi bạn mở tệp tin, bạn cần phải đóng nó lại sau khi sử dụng bằng cách gọi hàm `close()`.

## Bài tập
Bài tập này sẽ giúp bạn thực hành kỹ năng làm việc với tệp tin. Hãy thực hiện các yêu cầu sau:
- Tạo một tệp tin mới có tên là `test.txt`.
- Viết một chương trình để đọc nội dung của tệp tin `test.txt` và in nó ra màn hình.
- Viết một chương trình để ghi nội dung "Xin chào!" vào tệp tin `test.txt`.
- Viết một chương trình để ghi thêm nội dung " Đây là nội dung mới." vào tệp tin `test.txt`.
- Đọc lại nội dung của tệp tin `test.txt` và in nó ra màn hình.
Khi bạn hoàn thành bài tập này, bạn sẽ có một hiểu biết cơ bản về cách làm việc với tệp tin trong Python.