# Python 18 Cấp Cơ Bản

## Giới thiệu

Bài học thứ 18 trong chuỗi "Python Cấp Cơ Bản" sẽ giúp bạn làm quen với khái niệm **hàm (function)** trong Python — một thành phần thiết yếu để viết code rõ ràng, dễ bảo trì và tái sử dụng. Hàm cho phép bạn đóng gói một đoạn mã thực hiện một nhiệm vụ cụ thể, sau đó gọi lại nhiều lần mà không cần viết lại.

## Lý thuyết

Hàm trong Python được định nghĩa bằng từ khóa `def`, theo sau là tên hàm và cặp dấu ngoặc đơn `()`. Các tham số (nếu có) được đặt bên trong ngoặc. Câu lệnh trong hàm được viết thụt lề so với `def`. Để trả kết quả về, ta dùng lệnh `return`.

Cú pháp cơ bản:
```python
def ten_ham(tham_so):
    # các câu lệnh
    return ket_qua
```

Hàm có thể không có tham số, không trả về giá trị (`return` không cần giá trị), hoặc có nhiều tham số.

## Ví dụ

Dưới đây là một ví dụ đơn giản về hàm tính bình phương một số:

```python
def tinh_binh_phuong(n):
    return n ** 2

# Gọi hàm
so = 5
ket_qua = tinh_binh_phuong(so)
print(f"Bình phương của {so} là {ket_qua}")
```

Kết quả:
```
Bình phương của 5 là 25
```

## Bài tập

1. Viết hàm `tinh_tong(a, b)` nhận hai số và trả về tổng của chúng.
2. Viết hàm `kiem_tra_chan_le(n)` nhận một số nguyên và in ra `"Chẵn"` nếu số đó chẵn, ngược lại in `"Lẻ"`.
3. Viết hàm `tinh_dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong)` trả về diện tích hình chữ nhật.

**Gợi ý:** Sử dụng `def` để định nghĩa hàm và `return` hoặc `print` tùy yêu cầu.

> Hãy thử viết và chạy các hàm này trong môi trường Python của bạn để hiểu rõ hơn cách chúng hoạt động!