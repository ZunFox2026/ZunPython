# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một phần quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ các tệp tin. Trong bài này, chúng ta sẽ tìm hiểu về các cách làm việc với tệp tin trong Python, bao gồm cả việc đọc và ghi dữ liệu.

## Lý thuyết
Trong Python, bạn có thể làm việc với tệp tin bằng cách sử dụng hàm `open()`. Hàm này sẽ trả về một đối tượng tệp tin, cho phép bạn thực hiện các hoạt động như đọc, ghi, thêm vào tệp tin. Có hai chế độ chính khi làm việc với tệp tin: chế độ đọc (`'r'`) và chế độ ghi (`'w'`). Ngoài ra, bạn cũng có thể sử dụng chế độ thêm vào (`'a'`) để thêm dữ liệu vào cuối tệp tin.

Khi bạn mở một tệp tin, bạn cần phải nhớ đóng nó lại khi không còn sử dụng để tránh lãng phí tài nguyên. Bạn có thể đóng tệp tin bằng cách sử dụng phương thức `close()`. Tuy nhiên, một cách tốt hơn là sử dụng câu lệnh `with`, nó sẽ tự động đóng tệp tin khi bạn không còn sử dụng.

## Ví dụ
Dưới đây là một số ví dụ về làm việc với tệp tin trong Python:

*   Đọc dữ liệu từ tệp tin:
    ```python
with open('ten_tep.txt', 'r') as f:
    noi_dung = f.read()
    print(noi_dung)
```
*   Ghi dữ liệu vào tệp tin:
    ```python
with open('ten_tep.txt', 'w') as f:
    f.write('Day la noi dung moi')
```
*   Thêm dữ liệu vào tệp tin:
    ```python
with open('ten_tep.txt', 'a') as f:
    f.write(' Them noi dung moi')
```

## Bài tập
Bài tập dưới đây sẽ giúp bạn thực hành làm việc với tệp tin trong Python:

*   Tạo một tệp tin mới có tên `gioi_thieu.txt` và ghi vào đó một đoạn văn bản giới thiệu về bản thân.
*   Đọc và in ra nội dung của tệp tin `gioi_thieu.txt`.
*   Thêm vào cuối tệp tin `gioi_thieu.txt` một đoạn văn bản mới.
*   Tạo một chương trình cho phép người dùng nhập vào tên tệp tin và nội dung, sau đó ghi nội dung vào tệp tin đó.