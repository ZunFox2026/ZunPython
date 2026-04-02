# Làm việc với chuỗi
## Giới thiệu
Làm việc với chuỗi là một phần quan trọng trong lập trình Python. Chuỗi là một loại dữ liệu cơ bản trong Python, được sử dụng để đại diện cho văn bản. Trong bài này, chúng ta sẽ tìm hiểu về cách tạo, thao tác và sử dụng chuỗi trong Python.

## Lý thuyết
Chuỗi trong Python được tạo bằng cách đặt văn bản giữa các dấu nháy đơn hoặc nháy kép. Ví dụ: `'Xin chào'` hoặc `"Xin chào"`. Chúng ta có thể sử dụng các phương thức và hàm khác nhau để thao tác với chuỗi, chẳng hạn như:
- `len()`: trả về độ dài của chuỗi
- `upper()`: trả về chuỗi với tất cả các ký tự được chuyển thành chữ hoa
- `lower()`: trả về chuỗi với tất cả các ký tự được chuyển thành chữ thường
- `split()`: chia chuỗi thành danh sách các từ
- `join()`: kết hợp các chuỗi thành một chuỗi duy nhất

## Ví dụ
Dưới đây là một số ví dụ minh họa cách sử dụng chuỗi trong Python:
```python
# Tạo chuỗi
chuoi = 'Xin chào'

# In độ dài của chuỗi
print(len(chuoi))  # Output: 8

# Chuyển chuỗi thành chữ hoa
print(chuoi.upper())  # Output: XIN CHÀO

# Chia chuỗi thành danh sách các từ
chuoi2 = 'Xin chào thế giới'
ds_tu = chuoi2.split()
print(ds_tu)  # Output: ['Xin', 'chào', 'thế', 'giới']

# Kết hợp các chuỗi
chuoi3 = '-'.join(ds_tu)
print(chuoi3)  # Output: Xin-chào-thế-giới
```

## Bài tập
Bài tập này yêu cầu bạn thực hiện các thao tác sau với chuỗi:
- Tạo một chuỗi mới với nội dung "Hello World"
- In độ dài của chuỗi
- Chuyển chuỗi thành chữ hoa và in ra
- Chia chuỗi thành danh sách các từ và in ra
- Kết hợp các từ trong danh sách thành một chuỗi duy nhất với dấu `-` làm ký tự ngăn cách và in ra

Hãy thử thực hiện các bước trên và chạy chương trình để xem kết quả. Nếu có bất kỳ câu hỏi nào, hãy hỏi tôi, Zunny, trợ giảng Python.