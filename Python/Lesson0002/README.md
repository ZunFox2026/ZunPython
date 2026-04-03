# Bài 2: Cấu Trúc Điều Khiển và Hàm Đơn Giản trong Python

## Giới thiệu

Trong lập trình, việc kiểm soát luồng thực thi của chương trình là yếu tố quan trọng giúp chương trình hoạt động linh hoạt theo các điều kiện khác nhau. Bài học này sẽ giới thiệu về các **cấu trúc điều khiển** như `if`, `elif`, `else` và cách viết **hàm đơn giản** bằng từ khóa `def` trong Python. Đây là nền tảng cơ bản để xây dựng các chương trình phức tạp hơn sau này.

---

## Lý thuyết

Python sử dụng các cấu trúc điều khiển để quyết định hướng đi của chương trình dựa trên điều kiện. Câu lệnh điều kiện phổ biến nhất là `if-elif-else`:

- `if`: Kiểm tra điều kiện đầu tiên.
- `elif`: Kiểm tra các điều kiện bổ sung (nếu có).
- `else`: Thực hiện khi tất cả điều kiện trên đều sai.

Ngoài ra, Python cho phép định nghĩa **hàm** bằng từ khóa `def`, giúp tái sử dụng mã một cách hiệu quả. Cú pháp cơ bản:

```python
def ten_ham(tham_so):
    # nội dung hàm
    return ket_qua
```

---

## Ví dụ

Dưới đây là ví dụ kết hợp cấu trúc điều khiển và hàm:

```python
def kiem_tra_so(n):
    if n > 0:
        return "Số dương"
    elif n < 0:
        return "Số âm"
    else:
        return "Số bằng 0"

# Gọi hàm
print(kiem_tra_so(5))   # Kết quả: Số dương
print(kiem_tra_so(-3))  # Kết quả: Số âm
print(kiem_tra_so(0))   # Kết quả: Số bằng 0
```

---

## Bài tập

1. Viết hàm `kiem_tra_chan_le(n)` nhận một số nguyên và trả về `"Chẵn"` nếu số đó chia hết cho 2, ngược lại trả về `"Lẻ"`.
2. Viết chương trình dùng cấu trúc `if-elif-else` để xếp loại học lực theo điểm trung bình:
   - Nếu điểm >= 8: "Giỏi"
   - Nếu điểm >= 6.5: "Khá"
   - Nếu điểm >= 5: "Trung bình"
   - Ngược lại: "Yếu"

> Gợi ý: Tạo hàm và kiểm tra với các giá trị khác nhau để đảm bảo chương trình hoạt động đúng.