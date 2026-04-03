# Python 47: Lập Trình Hướng Đối Tượng Cơ Bản

## Giới thiệu

Lập trình hướng đối tượng (OOP - Object-Oriented Programming) là một phương pháp lập trình phổ biến trong Python và nhiều ngôn ngữ khác. Thay vì viết các hàm rời rạc, OOP giúp tổ chức mã nguồn thành các **đối tượng** – những thực thể kết hợp **dữ liệu (thuộc tính)** và **hành vi (phương thức)**. Bài học này giới thiệu những khái niệm cơ bản nhất của OOP trong Python: lớp (class), đối tượng (object), thuộc tính và phương thức.

## Lý thuyết

Trong OOP, **lớp (class)** là bản mẫu để tạo ra các **đối tượng (object)**. Mỗi đối tượng có thể có:

- **Thuộc tính (attributes)**: Dữ liệu mô tả đối tượng (ví dụ: tên, tuổi).
- **Phương thức (methods)**: Các hàm được định nghĩa trong lớp, mô tả hành vi của đối tượng.

Từ khóa `class` được dùng để khai báo một lớp. Phương thức đặc biệt `__init__()` được gọi khi tạo đối tượng — dùng để khởi tạo các thuộc tính.

## Ví dụ

Dưới đây là ví dụ về một lớp đơn giản `SinhVien`:

```python
class SinhVien:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def gioi_thieu(self):
        print(f"Xin chào, mình tên là {self.ten},今年 {self.tuoi} tuổi.")

# Tạo đối tượng từ lớp
sv1 = SinhVien("An", 20)
sv1.gioi_thieu()  # Kết quả: Xin chào, mình tên là An,今年 20 tuổi.
```

Trong ví dụ trên:
- `SinhVien` là lớp.
- `sv1` là một đối tượng (instance) của lớp.
- `__init__` khởi tạo thuộc tính `ten` và `tuoi`.
- `gioi_thieu()` là phương thức in thông tin sinh viên.

## Bài tập

1. Tạo một lớp `HinhChuNhat` với hai thuộc tính: `chieu_dai` và `chieu_rong`.
2. Thêm phương thức `dien_tich()` để tính diện tích hình chữ nhật.
3. Tạo một đối tượng hình chữ nhật có chiều dài 5, chiều rộng 3 và in ra diện tích của nó.

> Gợi ý: Sử dụng `__init__` để khởi tạo, và một phương thức trả về `chieu_dai * chieu_rong`.