"""
Bài học: Python 37 - Làm Quen Với Biến Và Kiểu Dữ Liệu

Mục tiêu:
- Hiểu khái niệm biến trong Python.
- Biết các kiểu dữ liệu cơ bản: int, float, str, bool.
- Biết cách khai báo và sử dụng biến.
- Thực hành với các ví dụ và bài tập nhỏ.
"""

def main():
    # =========== 1. KHÁI NIỆM BIẾN ===========
    # Biến là một tên gọi để lưu trữ dữ liệu trong bộ nhớ.
    # Trong Python, bạn không cần khai báo kiểu dữ liệu trước khi dùng.
    
    # Ví dụ 1: Sử dụng biến để lưu thông tin cá nhân
    ten = "Nguyen Van A"      # Kiểu chuỗi (str)
    tuoi = 20                 # Kiểu số nguyên (int)
    chieu_cao = 1.75          # Kiểu số thực (float)
    la_sinh_vien = True       # Kiểu luận lý (bool)

    print("=== Ví dụ 1: Thông tin cá nhân ===")
    print("Họ tên:", ten)
    print("Tuổi:", tuoi)
    print("Chiều cao:", chieu_cao, "m")
    print("Là sinh viên:", la_sinh_vien)

    # =========== 2. KIỂM TRA KIỂU DỮ LIỆU ===========
    # Hàm type() giúp kiểm tra kiểu dữ liệu của biến
    print("\n=== Kiểm tra kiểu dữ liệu ===")
    print("Kiểu của 'ten':", type(ten))
    print("Kiểu của 'tuoi':", type(tuoi))
    print("Kiểu của 'chieu_cao':", type(chieu_cao))
    print("Kiểu của 'la_sinh_vien':", type(la_sinh_vien))

    # =========== 3. CÁC KIỂU DỮ LIỆU CƠ BẢN ===========
    # - int: số nguyên (vd: 5, -10, 100)
    # - float: số thực (vd: 3.14, -0.5, 2.0)
    # - str: chuỗi ký tự, đặt trong "" hoặc ''
    # - bool: giá trị True hoặc False

    # Ví dụ 2: Tính toán với biến
    print("\n=== Ví dụ 2: Tính toán với biến ===")
    a = 15
    b = 4
    tong = a + b
    hieu = a - b
    tich = a * b
    thuong = a / b  # Kết quả là float
    chia_nguyen = a // b  # Chia lấy phần nguyên
    du = a % b      # Chia lấy dư

    print(f"{a} + {b} = {tong}")
    print(f"{a} - {b} = {hieu}")
    print(f"{a} * {b} = {tich}")
    print(f"{a} / {b} = {thuong} (kiểu {type(thuong)})")
    print(f"{a} // {b} = {chia_nguyen}")
    print(f"{a} % {b} = {du}")

    # =========== 4. ÉP KIỂU DỮ LIỆU ===========
    # Có thể chuyển đổi giữa các kiểu dữ liệu bằng hàm: int(), float(), str()
    print("\n=== Ép kiểu dữ liệu ===")
    so_str = "123"           # chuỗi
    so_int = int(so_str)     # chuyển thành số nguyên
    so_float = float(so_int) # chuyển thành số thực
    print("Chuyển '123' -> int:", so_int, type(so_int))
    print("Chuyển 123 -> float:", so_float, type(so_float))

    # =========== 5. BÀI TẬP NHỎ ===========
    # Yêu cầu người dùng nhập thông tin và xử lý
    print("\n=== Bài tập nhỏ: Tính tuổi sau 5 năm ===")
    try:
        ten_nguoi_dung = input("Nhập tên của bạn: ")
        tuoi_hien_tai = int(input("Nhập tuổi hiện tại: "))
        tuoi_sau_5_nam = tuoi_hien_tai + 5
        print(f"Xin chào {ten_nguoi_dung}! Sau 5 năm nữa, bạn sẽ {tuoi_sau_5_nam} tuổi.")
    except ValueError:
        print("Lỗi: Vui lòng nhập tuổi là một số hợp lệ!")

    # =========== 6. GHI NHỚ ===========
    # - Tên biến nên có nghĩa, ví dụ: ten, diem_toan, so_luong
    # - Python phân biệt chữ hoa/chữ thường: Ten ≠ ten
    # - Không dùng từ khóa của Python làm tên biến (như: if, for, while,...)

    print("\nChúc mừng bạn đã hoàn thành bài học về Biến và Kiểu Dữ Liệu!")

# Gọi hàm chính
if __name__ == "__main__":
    main()
```

---

### 💡 Hướng dẫn sử dụng:
1. Lưu đoạn code trên vào file: `bien_va_kieu_du_lieu.py`
2. Chạy bằng lệnh: `python bien_va_kieu_du_lieu.py`
3. Nhập thông tin khi được yêu cầu để hoàn thành bài tập.

---

### ✅ Mục tiêu đạt được sau bài học:
- Hiểu và sử dụng được biến.
- Nhận biết 4 kiểu dữ liệu cơ bản.
- Biết cách ép kiểu và tính toán đơn giản.
- Áp dụng vào bài tập thực tế.