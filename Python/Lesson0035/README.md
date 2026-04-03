# Python 35 Cấp Cơ Bản

## Giới thiệu

"Python 35 Cấp Cơ Bản" là bài học thứ 35 trong chuỗi bài học giúp người mới bắt đầu làm quen và làm chủ ngôn ngữ lập trình Python. Bài học này tập trung vào việc củng cố kiến thức cơ bản thông qua việc tổng hợp và vận dụng các khái niệm đã học như biến, vòng lặp, điều kiện, hàm và xử lý chuỗi. Mục tiêu của bài là giúp người học tự tin hơn khi viết các chương trình nhỏ, giải quyết bài toán thực tế một cách logic và có tổ chức.

## Lý thuyết

Trong bài học này, chúng ta sẽ ôn lại một số khái niệm trọng tâm:

- **Biến và kiểu dữ liệu**: Sử dụng biến để lưu trữ thông tin như số nguyên, số thực, chuỗi.
- **Câu điều kiện**: Dùng `if`, `elif`, `else` để thực hiện các nhánh logic.
- **Vòng lặp**: Sử dụng `for` và `while` để lặp lại các thao tác.
- **Hàm**: Tạo hàm bằng `def` để tái sử dụng mã nguồn.
- **Xử lý chuỗi**: Các thao tác như nối chuỗi, cắt chuỗi, kiểm tra chuỗi con.

Việc hiểu rõ và vận dụng linh hoạt các khái niệm này là nền tảng để học các chủ đề nâng cao hơn như làm việc với tệp, thư viện, hoặc lập trình hướng đối tượng.

## Ví dụ

Dưới đây là một ví dụ nhỏ minh họa việc sử dụng hàm và vòng lặp để in ra các số chẵn trong một danh sách:

```python
def in_so_chan(danh_sach):
    for so in danh_sach:
        if so % 2 == 0:
            print(so)

# Gọi hàm
so_nguyen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
in_so_chan(so_nguyen)
```

Kết quả:
```
2
4
6
8
10
```

## Bài tập

1. Viết hàm `dem_tu` nhận vào một chuỗi và trả về số lượng từ trong chuỗi đó.
2. Tạo một danh sách số và viết chương trình tìm số lớn nhất, nhỏ nhất bằng vòng lặp (không dùng hàm `max`, `min`).
3. Viết chương trình kiểm tra một số có phải là số nguyên tố hay không.

> Gợi ý: Sử dụng vòng lặp `for` và toán tử `%` để kiểm tra chia hết.