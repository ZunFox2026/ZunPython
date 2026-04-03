# Python 25 Cấp Cơ Bản

## Giới thiệu

Chào mừng bạn đến với bài học thứ 25 trong chuỗi "Python 25 Cấp Cơ Bản" – hành trình giúp người mới bắt đầu làm quen và làm chủ ngôn ngữ lập trình Python một cách dễ dàng. Bài học này tập trung vào khái niệm **Hàm trong Python**, một trong những nền tảng quan trọng giúp mã nguồn của bạn trở nên gọn gàng, dễ đọc và có thể tái sử dụng. Khi hiểu rõ về hàm, bạn sẽ viết code chuyên nghiệp hơn và giải quyết vấn đề hiệu quả hơn.

## Lý thuyết

Hàm (function) là khối lệnh thực hiện một nhiệm vụ cụ thể và có thể được gọi để sử dụng nhiều lần trong chương trình. Trong Python, bạn định nghĩa hàm bằng từ khóa `def`, theo sau là tên hàm và dấu ngoặc đơn `()`. Các tham số (nếu có) được đặt trong ngoặc, và khối lệnh nằm sau dấu hai chấm `:` phải được thụt lề đúng cách.

Cú pháp cơ bản:
```python
def ten_ham(tham_so):
    # Khối lệnh
    return gia_tri
```

Hàm có thể trả về giá trị bằng lệnh `return`. Nếu không có `return`, hàm sẽ trả về `None` mặc định.

## Ví dụ

Dưới đây là ví dụ về một hàm tính tổng hai số:

```python
def tinh_tong(a, b):
    return a + b

# Gọi hàm
ket_qua = tinh_tong(5, 3)
print("Tổng là:", ket_qua)  # Output: Tổng là: 8
```

Hàm `tinh_tong` nhận hai tham số `a` và `b`, rồi trả về tổng của chúng. Việc sử dụng hàm giúp ta không cần viết lại phép cộng mỗi lần cần tính.

## Bài tập

1. Viết hàm `tinh_dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong)` trả về diện tích hình chữ nhật.
2. Viết hàm `kiem_tra_chan_le(so)` in ra "Chẵn" nếu số chẵn, "Lẻ" nếu số lẻ.
3. Viết hàm `tinh_giai_thua(n)` tính và trả về giai thừa của số nguyên dương `n`.

Hãy thử tự viết code và chạy thử các hàm này để nắm vững kiến thức!