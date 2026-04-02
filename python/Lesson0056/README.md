# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng trong lập trình. Trong bài này, chúng ta sẽ tìm hiểu về cách đọc và ghi tệp tin trong Python. Đây là một chủ đề cơ bản nhưng rất quan trọng, vì nó cho phép chúng ta lưu trữ và xử lý dữ liệu một cách hiệu quả.

## Lý thuyết
Trong Python, chúng ta có thể làm việc với tệp tin bằng cách sử dụng các hàm và phương thức sau:
- `open()`: Hàm này được sử dụng để mở một tệp tin. Nó trả về một đối tượng tệp tin, mà chúng ta có thể sử dụng để đọc hoặc ghi dữ liệu.
- `read()`: Phương thức này được sử dụng để đọc dữ liệu từ một tệp tin.
- `write()`: Phương thức này được sử dụng để ghi dữ liệu vào một tệp tin.
- `close()`: Phương thức này được sử dụng để đóng một tệp tin sau khi chúng ta đã xong việc với nó.

Chúng ta cũng cần phải chỉ định chế độ mở tệp tin, chẳng hạn như `'r'` để đọc, `'w'` để ghi, hoặc `'a'` để thêm dữ liệu vào cuối tệp tin.

## Ví dụ
Dưới đây là một ví dụ về cách đọc và ghi tệp tin trong Python:
```
# Mở tệp tin để đọc
f = open('example.txt', 'r')
# Đọc dữ liệu từ tệp tin
data = f.read()
# In dữ liệu
print(data)
# Đóng tệp tin
f.close()

# Mở tệp tin để ghi
f = open('example.txt', 'w')
# Ghi dữ liệu vào tệp tin
f.write('Xin chào, thế giới!')
# Đóng tệp tin
f.close()
```
Trong ví dụ này, chúng ta mở tệp tin `example.txt` để đọc, đọc dữ liệu từ tệp tin, in dữ liệu, và đóng tệp tin. Sau đó, chúng ta mở tệp tin lại để ghi, ghi dữ liệu vào tệp tin, và đóng tệp tin.

## Bài tập
Bài tập này yêu cầu bạn thực hiện các bước sau:
- Tạo một tệp tin mới có tên là `bai_tap.txt`.
- Mở tệp tin `bai_tap.txt` để ghi và thêm dòng chữ "Xin chào, thế giới!" vào tệp tin.
- Mở tệp tin `bai_tap.txt` để đọc và in dữ liệu từ tệp tin.
- Thêm một dòng chữ mới vào tệp tin `bai_tap.txt` với nội dung "Tôi đang học Python!".
- Đóng tệp tin `bai_tap.txt` sau khi hoàn thành tất cả các bước trên.

Với bài tập này, bạn sẽ được thực hành cách đọc và ghi tệp tin trong Python, cũng như cách thêm dữ liệu vào một tệp tin đã tồn tại.