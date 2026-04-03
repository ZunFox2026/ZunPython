"""
Bài học: Python 45 Cấp Cơ Bản - Bài số 1
Tác giả: Học viên Python
Mô tả: Giới thiệu các khái niệm cơ bản trong Python:
- Biến và kiểu dữ liệu
- Câu lệnh điều kiện
- Vòng lặp
- Hàm đơn giản
- Xử lý chuỗi
"""

# 1. Biến và kiểu dữ liệu cơ bản
# Python tự động nhận diện kiểu dữ liệu khi gán giá trị

ten = "Alice"           # Chuỗi (string)
tuoi = 25               # Số nguyên (int)
chieu_cao = 1.68        # Số thực (float)
la_sinh_vien = True     # Boolean (True/False)

# In thông tin ra màn hình
print("=== Thông tin cá nhân ===")
print(f"Tên: {ten}")
print(f"Tuổi: {tuoi}")
print(f"Chiều cao: {chieu_cao} m")
print(f"Là sinh viên: {la_sinh_vien}")

# 2. Câu lệnh điều kiện (if-elif-else)
print("\n=== Kiểm tra độ tuổi ===")
if tuoi < 18:
    print("Bạn là vị thành niên.")
elif 18 <= tuoi < 60:
    print("Bạn là người trưởng thành.")
else:
    print("Bạn là người cao tuổi.")

# Ví dụ 1: Kiểm tra số chẵn/lẻ
so = 10
if so % 2 == 0:
    print(f"{so} là số chẵn.")
else:
    print(f"{so} là số lẻ.")

# 3. Vòng lặp for
print("\n=== In các số từ 1 đến 5 ===")
for i in range(1, 6):  # range(1,6) tạo ra 1,2,3,4,5
    print(f"Số thứ {i}: {i}")

# Ví dụ 2: Duyệt qua từng ký tự trong chuỗi
print("\n=== Duyệt từng ký tự trong tên ===")
for ky_tu in ten:
    print(ky_tu)

# 4. Hàm đơn giản
def tinh_dien_tich_hcn(chieu_dai, chieu_rong):
    """
    Hàm tính diện tích hình chữ nhật
    Input: chiều dài, chiều rộng
    Output: diện tích
    """
    return chieu_dai * chieu_rong

# Gọi hàm và in kết quả
dien_tich = tinh_dien_tich_hcn(5, 3)
print(f"\n=== Tính diện tích hình chữ nhật ===")
print(f"Diện tích hình chữ nhật 5x3 là: {dien_tich}")

# 5. Xử lý chuỗi
ho_ten = "Nguyễn Văn Bình"
print(f"\n=== Xử lý chuỗi: {ho_ten} ===")
print(f"Viết hoa: {ho_ten.upper()}")
print(f"Viết thường: {ho_ten.lower()}")
print(f"Độ dài chuỗi: {len(ho_ten)} ký tự")

# Ví dụ 3: Tách chuỗi theo khoảng trắng
danh_sach_tu = ho_ten.split()
print(f"Từ trong tên: {danh_sach_tu}")

# 6. Bài tập nhỏ
"""
Bài tập: Viết chương trình kiểm tra một số có phải là số nguyên tố không.

Hướng dẫn:
- Số nguyên tố là số lớn hơn 1 và chỉ chia hết cho 1 và chính nó.
- Viết hàm kiem_tra_so_nguyen_to(n)
- Trả về True nếu là số nguyên tố, ngược lại trả về False.
"""

def kiem_tra_so_nguyen_to(n):
    """
    Kiểm tra xem n có phải là số nguyên tố không
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Kiểm thử bài tập
print("\n=== Bài tập: Kiểm tra số nguyên tố ===")
so_kiem_tra = 17
if kiem_tra_so_nguyen_to(so_kiem_tra):
    print(f"{so_kiem_tra} là số nguyên tố.")
else:
    print(f"{so_kiem_tra} không phải là số nguyên tố.")

# Thử thêm một số ví dụ
print("Các số nguyên tố từ 1 đến 10:")
for num in range(1, 11):
    if kiem_tra_so_nguyen_to(num):
        print(num, end=" ")
print()  # Xuống dòng

# 7. Kết thúc chương trình
print("\nChúc mừng bạn đã hoàn thành bài học Python cơ bản đầu tiên!")

# Hàm main để chạy chương trình
def main():
    # Gọi các phần đã viết ở trên
    # (Các lệnh in và xử lý đã chạy từ trên xuống)
    pass  # Vì các lệnh đã thực thi khi import

if __name__ == "__main__":
    main()
```

---

**Tổng kết:**
- Code dài khoảng 100 dòng, đầy đủ comment tiếng Việt.
- Có 3 ví dụ minh họa: chẵn/lẻ, duyệt chuỗi, tính diện tích.
- Có 1 bài tập nhỏ: kiểm tra số nguyên tố.
- Sử dụng thuần Python cơ bản, không cần thư viện ngoài.