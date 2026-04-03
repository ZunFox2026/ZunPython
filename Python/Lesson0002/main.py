# main.py - Bài học 2: Cấu trúc rẽ nhánh (if-else, elif)

# --- 1. Câu lệnh if cơ bản ---
# Câu lệnh if dùng để kiểm tra một điều kiện.
# Nếu điều kiện đúng (True), thì thực hiện khối lệnh bên trong.

print("--- Ví dụ 1: Kiểm tra tuổi để vào rạp chiếu phim ---")

age = 17
if age >= 18:
    print("Bạn đã đủ 18 tuổi, được xem phim người lớn.")
print("Cảm ơn bạn đã sử dụng dịch vụ!\n")

# --- 2. Câu lệnh if-else ---
# Nếu điều kiện đúng thì thực hiện khối if, nếu sai thì thực hiện khối else.

print("--- Ví dụ 2: Kiểm tra đậu/rớt dựa trên điểm số ---")

diem = 4.5
if diem >= 5:
    print(f"Bạn đạt {diem}/10 - Chúc mừng, bạn đã đậu!")
else:
    print(f"Bạn đạt {diem}/10 - Rất tiếc, bạn chưa đậu.")
print()

# --- 3. Câu lệnh if-elif-else ---
# Khi có nhiều điều kiện, dùng elif (else if) để kiểm tra lần lượt.

print("--- Ví dụ 3: Xếp loại học lực theo điểm số ---")

diem = 8.2
if diem >= 9:
    xep_loai = "Xuất sắc"
elif diem >= 8:
    xep_loai = "Giỏi"
elif diem >= 6.5:
    xep_loai = "Khá"
elif diem >= 5:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"

print(f"Với điểm {diem}, học lực của bạn là: {xep_loai}\n")

# --- 4. Điều kiện lồng nhau ---
# Có thể đặt một câu lệnh if bên trong câu lệnh if khác.

print("--- Ví dụ 4: Kiểm tra đăng nhập và quyền truy cập ---")

ten_dang_nhap = "admin"
mat_khau = "123456"

if ten_dang_nhap == "admin":
    if mat_khau == "123456":
        print("Đăng nhập thành công! Chào mừng quản trị viên.")
    else:
        print("Mật khẩu sai!")
else:
    print("Tên đăng nhập không tồn tại.")
print()

# --- 5. Các toán tử so sánh thường dùng ---
# >  : lớn hơn
# <  : nhỏ hơn
# >= : lớn hơn hoặc bằng
# <= : nhỏ hơn hoặc bằng
# == : bằng nhau
# != : khác nhau

# Ví dụ:
so = 10
if so % 2 == 0:
    print(f"{so} là số chẵn.")
else:
    print(f"{so} là số lẻ.")
