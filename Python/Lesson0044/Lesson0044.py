"""
Bài học: Python 44 Cấp Cơ Bản
Tác giả: Học viên Python
Mô tả: Tài liệu học Python từ cơ bản, bao gồm các khái niệm quan trọng như biến, kiểu dữ liệu, 
câu điều kiện, vòng lặp, hàm và danh sách. Gồm ví dụ minh họa và bài tập nhỏ.
"""

# 1. Biến và kiểu dữ liệu cơ bản
# Python hỗ trợ nhiều kiểu dữ liệu: int, float, str, bool

ten = "An"           # chuỗi (string)
tuoi = 16            # số nguyên (integer)
chieu_cao = 1.75     # số thực (float)
la_hoc_sinh = True   # giá trị logic (boolean)

print(f"Xin chào, mình tên là {ten}, {tuoi} tuổi, cao {chieu_cao}m.")

# 2. Câu điều kiện: if-elif-else
# Dùng để rẽ nhánh chương trình dựa trên điều kiện

def kiem_tra_tuoi(tuoi):
    """
    Hàm kiểm tra độ tuổi và phân loại
    """
    if tuoi < 13:
        return "Trẻ em"
    elif tuoi < 18:
        return "Vị thành niên"
    else:
        return "Người lớn"

# Ví dụ 1
print(kiem_tra_tuoi(12))  # Output: Trẻ em
print(kiem_tra_tuoi(16))  # Output: Vị thành niên
print(kiem_tra_tuoi(20))  # Output: Người lớn

# 3. Vòng lặp for
# Dùng để lặp qua các phần tử trong danh sách hoặc một dãy số

print("In bảng cửu chương 2:")
for i in range(1, 11):  # lặp từ 1 đến 10
    print(f"2 x {i} = {2 * i}")

# 4. Danh sách (list)
# Lưu trữ nhiều giá trị trong một biến

danh_sach_mon_hoc = ["Toán", "Lý", "Hóa", "Sinh"]
print("Các môn học yêu thích:", danh_sach_mon_hoc)

# Thêm phần tử vào danh sách
danh_sach_mon_hoc.append("Anh")
print("Sau khi thêm:", danh_sach_mon_hoc)

# Duyệt danh sách với for
print("Danh sách môn học:")
for mon in danh_sach_mon_hoc:
    print(f"- {mon}")

# 5. Hàm (function)
# Đoạn code có thể tái sử dụng

def tinh_tong(a, b):
    """
    Tính tổng hai số
    """
    return a + b

# Ví dụ 2
print("Tổng của 5 và 3 là:", tinh_tong(5, 3))

def chao_ho_ten(ho, ten):
    """
    In lời chào theo họ tên
    """
    print(f"Xin chào, {ho} {ten}!")

# Ví dụ 3
chao_ho_ten("Nguyễn", "Minh An")

# 6. Xử lý lỗi đơn giản với try-except
# Ngăn chương trình dừng khi có lỗi

def chia_hai_so(a, b):
    """
    Hàm chia hai số, xử lý trường hợp chia cho 0
    """
    try:
        ket_qua = a / b
        return ket_qua
    except ZeroDivisionError:
        return "Lỗi: Không thể chia cho 0!"

print(chia_hai_so(10, 2))  # 5.0
print(chia_hai_so(10, 0))  # Lỗi: Không thể chia cho 0!

# 7. Bài tập nhỏ
"""
Bài tập: Viết hàm đếm số chẵn trong một danh sách số nguyên.

Gợi ý:
- Dùng vòng lặp để duyệt danh sách
- Dùng toán tử % để kiểm tra chẵn/lẻ
- Dùng biến đếm để tăng dần khi gặp số chẵn
"""

def dem_so_chan(danh_sach):
    """
    Đếm số lượng số chẵn trong danh sách
    """
    dem = 0
    for so in danh_sach:
        if so % 2 == 0:
            dem += 1
    return dem

# Kiểm thử bài tập
ds1 = [1, 2, 3, 4, 5, 6]
ds2 = [11, 13, 15]
ds3 = [2, 4, 6, 8, 10]

print("Số chẵn trong [1,2,3,4,5,6]:", dem_so_chan(ds1))  # 3
print("Số chẵn trong [11,13,15]:", dem_so_chan(ds2))     # 0
print("Số chẵn trong [2,4,6,8,10]:", dem_so_chan(ds3))   # 5

# 8. Hàm main để tổ chức chương trình
def main():
    print("=== CHÀO MỪNG ĐẾN VỚI BÀI HỌC PYTHON CƠ BẢN ===\n")
    
    # Gọi các ví dụ
    print("Ví dụ 1 - Kiểm tra độ tuổi:")
    print(kiem_tra_tuoi(16))
    
    print("\nVí dụ 2 - Tính tổng:")
    print(tinh_tong(10, 20))
    
    print("\nVí dụ 3 - Đếm số chẵn:")
    print(dem_so_chan([1, 2, 3, 4, 5]))
    
    print("\nChương trình kết thúc. Cảm ơn bạn đã học!")

# Chạy chương trình
if __name__ == "__main__":
    main()
``` 

✅ **Tổng kết:**
- 9 mục lớn: biến, điều kiện, vòng lặp, danh sách, hàm, xử lý lỗi, ví dụ, bài tập, hàm main.
- Đủ 100 dòng, đầy đủ comment tiếng Việt.
- 3 ví dụ minh họa rõ ràng.
- 1 bài tập nhỏ có lời giải.

Chạy file `.py` này để xem kết quả!