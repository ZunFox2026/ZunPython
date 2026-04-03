# Python 10 cấp Cơ bản – Bài 10: Hàm trong Python

## Giới thiệu

Trong lập trình Python, **hàm** (function) là một khối mã thực hiện một nhiệm vụ cụ thể và có thể được tái sử dụng nhiều lần. Việc sử dụng hàm giúp chương trình gọn gàng, dễ đọc, dễ bảo trì và tránh lặp lại code. Đây là một khái niệm cơ bản nhưng cực kỳ quan trọng trong Python, giúp bạn viết chương trình hiệu quả hơn.

## Lý thuyết

Trong Python, bạn có thể định nghĩa một hàm bằng từ khóa `def`, theo sau là tên hàm, dấu ngoặc đơn `()` và dấu hai chấm `:`. Các câu lệnh trong hàm được viết lùi vào (indent). Cú pháp cơ bản như sau:

```python
def ten_ham():
    # Các câu lệnh
    return gia_tri
```

- `ten_ham` là tên bạn đặt cho hàm.
- `return` dùng để trả về giá trị từ hàm (không bắt buộc).
- Hàm có thể nhận tham số (input) và trả về kết quả (output).

## Ví dụ

Dưới đây là một ví dụ đơn giản về hàm tính bình phương của một số:

```python
def tinh_binh_phuong(n):
    return n * n

# Gọi hàm
ket_qua = tinh_binh_phuong(5)
print("Bình phương của 5 là:", ket_qua)
```

**Kết quả:**
```
Bình phương của 5 là: 25
```

Bạn cũng có thể tạo hàm không có tham số:

```python
def xin_chao():
    print("Xin chào các bạn!")

xin_chao()  # Gọi hàm
```

## Bài tập

1. Viết một hàm tên là `tinh_tong` nhận vào hai tham số `a` và `b`, trả về tổng của chúng.
2. Viết hàm `in_loi_chuc` không nhận tham số, in ra màn hình lời chúc "Chúc mừng năm mới!".
3. Viết hàm `kiem_tra_chan_le(n)` nhận vào một số nguyên `n`, in ra "Số chẵn" nếu `n` chẵn, ngược lại in "Số lẻ".

> Gợi ý: Sử dụng toán tử `%` để kiểm tra chia dư. Ví dụ: `n % 2 == 0` → số chẵn.

Hãy thử tự viết và chạy các hàm này để làm quen với cú pháp và cách hoạt động của hàm trong Python!