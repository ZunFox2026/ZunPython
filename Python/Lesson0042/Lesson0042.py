"""
Bài 42: Python Cơ bản
Môn học: Lập trình Python
Tác giả: Học viên Python
Ngày: 2025

Mục tiêu:
- Ôn tập các khái niệm cơ bản trong Python
- Làm việc với biến, kiểu dữ liệu, cấu trúc điều kiện, vòng lặp, hàm và danh sách
- Áp dụng kiến thức vào bài tập thực hành nhỏ
"""

# 1. Biến và kiểu dữ liệu cơ bản
# Python tự động nhận diện kiểu dữ liệu khi gán giá trị

ten = "Nguyễn Văn A"       # Chuỗi (string)
tuoi = 20                   # Số nguyên (int)
chieu_cao = 1.75            # Số thực (float)
la_sinh_vien = True         # Boolean (True/False)

# In thông tin ra màn hình
print("Thông tin cá nhân:")
print(f"Tên: {ten}")
print(f"Tuổi: {tuoi}")
print(f"Chiều cao: {chieu_cao} m")
print(f"Là sinh viên: {la_sinh_vien}")

# 2. Cấu trúc điều kiện (if-elif-else)
print("\n--- Kiểm tra độ tuổi ---")
if tuoi < 18:
    print("Bạn chưa đủ tuổi trưởng thành.")
elif tuoi >= 18 and tuoi < 60:
    print("Bạn là người trưởng thành.")
else:
    print("Bạn là người cao tuổi.")

# Ví dụ 2: Kiểm tra số chẵn/lẻ
so = 15
if so % 2 == 0:
    print(f"{so} là số chẵn.")
else:
    print(f"{so} là số lẻ.")

# 3. Vòng lặp
print("\n--- In các số từ 1 đến 5 ---")
for i in range(1, 6):
    print(i)

# Ví dụ: Tính tổng các số từ 1 đến 10
tong = 0
for i in range(1, 11):
    tong += i
print(f"Tổng các số từ 1 đến 10 là: {tong}")

# 4. Danh sách (list) và các thao tác cơ bản
danh_sach_mon_hoc = ["Toán", "Lý", "Hóa", "Văn", "Sử"]
print(f"\nDanh sách môn học: {danh_sach_mon_hoc}")

# Thêm phần tử vào danh sách
danh_sach_mon_hoc.append("Địa")
print(f"Sau khi thêm 'Địa': {danh_sach_mon_hoc}")

# Duyệt danh sách bằng vòng lặp
print("Các môn học:")
for mon in danh_sach_mon_hoc:
    print(f" - {mon}")

# 5. Hàm trong Python
def tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa):
    """
    Hàm tính điểm trung bình của 3 môn
    Input: điểm Toán, Lý, Hóa
    Output: điểm trung bình (float)
    """
    return (diem_toan + diem_ly + diem_hoa) / 3

# Gọi hàm và in kết quả
dtb = tinh_diem_trung_binh(8.5, 7.0, 9.0)
print(f"\nĐiểm trung bình: {dtb:.2f}")

# Ví dụ 2: Hàm kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    """Kiểm tra xem một số có phải là số nguyên tố không"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"17 có phải số nguyên tố? {la_so_nguyen_to(17)}")
print(f"15 có phải số nguyên tố? {la_so_nguyen_to(15)}")

# 6. Bài tập nhỏ: Quản lý danh sách học sinh
"""
Bài tập: Viết chương trình quản lý danh sách học sinh đơn giản
- Mỗi học sinh có: tên, tuổi, điểm trung bình
- In ra học sinh có điểm cao nhất
"""

# Danh sách học sinh (dùng danh sách các từ điển)
danh_sach_hoc_sinh = [
    {"ten": "An", "tuoi": 17, "dtb": 8.5},
    {"ten": "Bình", "tuoi": 18, "dtb": 9.2},
    {"ten": "Chi", "tuoi": 17, "dtb": 7.8}
]

print("\n--- Bài tập nhỏ: Tìm học sinh có điểm cao nhất ---")
diem_cao_nhat = 0
hoc_sinh_gioi = None

for hs in danh_sach_hoc_sinh:
    if hs["dtb"] > diem_cao_nhat:
        diem_cao_nhat = hs["dtb"]
        hoc_sinh_gioi = hs

if hoc_sinh_gioi:
    print(f"Học sinh giỏi nhất: {hoc_sinh_gioi['ten']} - DTB: {hoc_sinh_gioi['dtb']}")

# 7. Kết luận
print("\n--- Hoàn thành bài 42: Python Cơ bản ---")
print("Bạn đã ôn tập các kiến thức: biến, kiểu dữ liệu, điều kiện, vòng lặp, hàm và danh sách.")


def main():
    """Hàm chính để chạy chương trình"""
    print("Chương trình bắt đầu...")
    
    # Gọi lại một vài hàm để kiểm tra
    print(f"5! = {tinh_giai_thua(5)}")
    
    # In danh sách học sinh
    print("\nDanh sách học sinh:")
    for hs in danh_sach_hoc_sinh:
        print(f"{hs['ten']} - {hs['tuoi']} tuổi - DTB: {hs['dtb']}")
    
    print("Chương trình kết thúc.")


def tinh_giai_thua(n):
    """Tính giai thừa của n"""
    if n == 0 or n == 1:
        return 1
    ket_qua = 1
    for i in range(2, n + 1):
        ket_qua *= i
    return ket_qua


# Chạy chương trình
if __name__ == "__main__":
    main()
```