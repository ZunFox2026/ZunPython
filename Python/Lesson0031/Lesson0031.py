"""
Python 31 cấp Cơ bản - Bài học tổng hợp
Tác giả: Học viên Python
Mô tả: Chương trình giới thiệu 31 khái niệm cơ bản trong Python thông qua ví dụ và bài tập nhỏ.
"""

# 1. In ra màn hình
print("Chào mừng bạn đến với Python 31 cấp Cơ bản!")

# 2. Biến và kiểu dữ liệu
ten = "An"           # chuỗi
tuoi = 15            # số nguyên
chieu_cao = 1.65     # số thực
la_hoc_sinh = True   # boolean

# 3-6. Các kiểu dữ liệu cơ bản: int, float, str, bool
print(f"Tên: {ten} (kiểu {type(ten)})")
print(f"Tuổi: {tuoi} (kiểu {type(tuoi)})")
print(f"Chiều cao: {chieu_cao} (kiểu {type(chieu_cao)})")
print(f"Là học sinh: {la_hoc_sinh} (kiểu {type(la_hoc_sinh)})")

# 7. Nhập dữ liệu từ người dùng
# ten_moi = input("Nhập tên của bạn: ")

# 8. Câu lệnh điều kiện if
if tuoi >= 18:
    print("Bạn đã đủ tuổi trưởng thành.")
else:
    print("Bạn chưa đủ tuổi trưởng thành.")

# 9. Câu lệnh elif
diem = 85
if diem >= 90:
    xep_loai = "Xuất sắc"
elif diem >= 80:
    xep_loai = "Giỏi"
elif diem >= 70:
    xep_loai = "Khá"
else:
    xep_loai = "Trung bình"
print(f"Xếp loại học lực: {xep_loai}")

# 10-11. Vòng lặp for và while
print("In số từ 1 đến 5 bằng for:")
for i in range(1, 6):
    print(i, end=" ")
print()

dem = 1
print("In số từ 1 đến 5 bằng while:")
while dem <= 5:
    print(dem, end=" ")
    dem += 1
print()

# 12. Danh sách (list)
danh_sach_lop = ["Mai", "Lan", "Hùng"]
# 13. Thêm phần tử vào danh sách
danh_sach_lop.append("Cúc")
# 14. Truy cập phần tử
print("Học sinh đầu tiên:", danh_sach_lop[0])
# 15. Duyệt danh sách
for hoc_sinh in danh_sach_lop:
    print(f"Xin chào {hoc_sinh}!")

# 16. Tuple - bộ dữ liệu không thay đổi
toa_do = (10, 20)
# 17. Truy cập phần tử tuple
print("Tọa độ X:", toa_do[0])

# 18. Từ điển (dictionary)
thong_tin_hoc_sinh = {
    "ten": "Bình",
    "tuoi": 16,
    "lop": "10A1"
}
# 19. Truy cập giá trị trong từ điển
print(f"Học sinh: {thong_tin_hoc_sinh['ten']}, Lớp: {thong_tin_hoc_sinh['lop']}")

# 20. Hàm đơn giản
def tinh_tong(a, b):
    """Hàm tính tổng hai số"""
    return a + b

# 21. Gọi hàm
ket_qua = tinh_tong(10, 20)
print(f"Tổng của 10 và 20 là: {ket_qua}")

# 22. Hàm với tham số mặc định
def xin_chao(ten, loi_chao="Chào bạn"):
    print(f"{loi_chao}, {ten}!")

xin_chao("Minh")
xin_chao("Hoa", "Xin chào")

# 23. Xử lý ngoại lệ (try-except)
try:
    tuoi_ng = int(input("Nhập tuổi của bạn (số nguyên): "))
    print(f"Tuổi của bạn là: {tuoi_ng}")
except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")

# 24-25. Mở và ghi file
try:
    with open("hello.txt", "w", encoding="utf-8") as f:
        f.write("Xin chào từ Python!\n")
        f.write("Đây là file văn bản đầu tiên.")
    print("Đã ghi file thành công.")
except Exception as e:
    print(f"Lỗi khi ghi file: {e}")

# 26-27. Đọc file
try:
    with open("hello.txt", "r", encoding="utf-8") as f:
        noi_dung = f.read()
        print("Nội dung file:")
        print(noi_dung)
except FileNotFoundError:
    print("Không tìm thấy file để đọc.")

# 28. Import module
import math
print(f"Căn bậc 2 của 16 là: {math.sqrt(16)}")

# 29. Định nghĩa lớp (class)
class HocSinh:
    def __init__(self, ten, lop):
        self.ten = ten
        self.lop = lop

    def gioi_thieu(self):
        return f"Tôi tên là {self.ten}, học lớp {self.lop}."

# 30. Tạo đối tượng
hs1 = HocSinh("Nam", "9B")
print(hs1.gioi_thieu())

# 31. Sử dụng list comprehension
so_chan = [x for x in range(10) if x % 2 == 0]
print("Các số chẵn từ 0 đến 9:", so_chan)


# --- Ví dụ minh họa ---
# Ví dụ 1: Tính điểm trung bình
print("\n=== VÍ DỤ 1: Tính điểm trung bình ===")
diem_toan = 8
diem_van = 7.5
diem_anh = 9
dtb = (diem_toan + diem_van + diem_anh) / 3
print(f"Điểm trung bình: {dtb:.2f}")

# Ví dụ 2: Kiểm tra số nguyên tố
print("\n=== VÍ DỤ 2: Kiểm tra số nguyên tố ===")
n = 17
la_nguyen_to = True
if n < 2:
    la_nguyen_to = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            la_nguyen_to = False
            break
print(f"{n} là số nguyên tố: {la_nguyen_to}")


# --- Bài tập nhỏ ---
"""
Bài tập: Viết chương trình nhập vào một danh sách số nguyên,
sau đó in ra:
- Tổng các số
- Số lớn nhất
- Các số lẻ
"""
print("\n=== BÀI TẬP NHỎ ===")
try:
    day_so = input("Nhập các số nguyên, cách nhau bởi dấu phẩy: ")
    danh_sach = [int(x.strip()) for x in day_so.split(",")]
    
    tong = sum(danh_sach)
    lon_nhat = max(danh_sach)
    so_le = [x for x in danh_sach if x % 2 == 1]
    
    print(f"Tổng: {tong}")
    print(f"Số lớn nhất: {lon_nhat}")
    print(f"Các số lẻ: {so_le}")
except Exception as e:
    print(f"Lỗi nhập liệu: {e}")


def main():
    print("\n--- Chương trình kết thúc ---")
    print("Bạn đã hoàn thành bài học Python 31 cấp Cơ bản!")


if __name__ == "__main__":
    main()
```