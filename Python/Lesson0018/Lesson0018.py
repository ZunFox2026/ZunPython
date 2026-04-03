# Python 18 Cấp Cơ Bản
# Bài học: Tìm hiểu các khái niệm cơ bản trong Python qua 18 cấp độ đơn giản

"""
Mục tiêu:
- Học từng bước các khái niệm cơ bản trong Python.
- Áp dụng kiến thức qua ví dụ và bài tập nhỏ.
"""

# Cấp 1: In ra màn hình
print("=== Cấp 1: In ra màn hình ===")
print("Xin chào, thế giới!")  # In chuỗi ra màn hình

# Cấp 2: Biến và kiểu dữ liệu
print("\n=== Cấp 2: Biến và kiểu dữ liệu ===")
ten = "An"           # Chuỗi (string)
tuoi = 15            # Số nguyên (int)
chieu_cao = 1.65     # Số thực (float)
la_hoc_sinh = True   # Boolean (True/False)

print(f"Tên: {ten}, Tuổi: {tuoi}, Cao: {chieu_cao}m, Là học sinh: {la_hoc_sinh}")

# Cấp 3: Nhập dữ liệu từ người dùng
print("\n=== Cấp 3: Nhập dữ liệu ===")
ho_ten = input("Nhập tên của bạn: ")
print(f"Xin chào, {ho_ten}!")

# Cấp 4: Toán tử cơ bản
print("\n=== Cấp 4: Toán tử cơ bản ===")
a = 10
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")  # Làm tròn 2 chữ số thập phân

# Cấp 5: Câu điều kiện if-else
print("\n=== Cấp 5: Câu điều kiện ===")
diem = int(input("Nhập điểm: "))
if diem >= 5:
    print("Đậu!")
else:
    print("Rớt!")

# Cấp 6: Vòng lặp for
print("\n=== Cấp 6: Vòng lặp for ===")
print("In số từ 1 đến 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

# Cấp 7: Vòng lặp while
print("\n=== Cấp 7: Vòng lặp while ===")
dem = 0
while dem < 3:
    print(f"Lần lặp: {dem + 1}")
    dem += 1

# Cấp 8: Danh sách (list)
print("\n=== Cấp 8: Danh sách ===")
danh_sach_lop = ["Nam", "Lan", "Bình", "Hoa"]
print("Danh sách lớp:", danh_sach_lop)
danh_sach_lop.append("Tùng")  # Thêm phần tử
print("Sau khi thêm Tùng:", danh_sach_lop)

# Cấp 9: Truy cập phần tử danh sách
print("\n=== Cấp 9: Truy cập phần tử ===")
print("Học sinh đầu tiên:", danh_sach_lop[0])
print("Học sinh cuối:", danh_sach_lop[-1])

# Cấp 10: Hàm đơn giản
print("\n=== Cấp 10: Hàm ===")
def xin_chao(ten):
    return f"Xin chào, {ten}!"

print(xin_chao("Minh"))

# Cấp 11: Hàm có tham số mặc định
def chao_hoi(ten, loi_chao="Xin chào"):
    return f"{loi_chao}, {ten}!"

print(chao_hoi("Lan"))
print(chao_hoi("Hùng", "Chào buổi sáng"))

# Cấp 12: Xử lý chuỗi
print("\n=== Cấp 12: Xử lý chuỗi ===")
chuoi = "  học lập trình python  "
print("Chuỗi gốc:", f"'{chuoi}'")
print("Sau khi strip():", f"'{chuoi.strip()}'")
print("In hoa:", chuoi.strip().upper())

# Cấp 13: Từ điển (dictionary)
print("\n=== Cấp 13: Từ điển ===")
hocsinh = {
    "ten": "Mai",
    "tuoi": 14,
    "lop": "8A"
}
print("Thông tin học sinh:", hocsinh)
print("Tên:", hocsinh["ten"])

# Cấp 14: Try-except (xử lý lỗi)
print("\n=== Cấp 14: Xử lý lỗi ===")
try:
    so = int(input("Nhập một số: "))
    print(f"Bình phương là: {so**2}")
except ValueError:
    print("Bạn phải nhập số!")

# Cấp 15: Đọc ghi file đơn giản
print("\n=== Cấp 15: Đọc ghi file ===")
# Ghi file
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Xin chào từ Python!\n")

# Đọc file
with open("hello.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()
    print("Nội dung file:", noi_dung)

# Cấp 16: Module và import
print("\n=== Cấp 16: Sử dụng module ===")
import random
print("Số ngẫu nhiên từ 1 đến 10:", random.randint(1, 10))

# Cấp 17: List comprehension
print("\n=== Cấp 17: List comprehension ===")
so_chan = [x for x in range(10) if x % 2 == 0]
print("Số chẵn từ 0 đến 9:", so_chan)

# Cấp 18: Tổng kết và bài tập nhỏ
print("\n=== Cấp 18: Bài tập nhỏ ===")

"""
Bài tập: Viết chương trình tính điểm trung bình của học sinh.
Yêu cầu:
- Nhập tên học sinh.
- Nhập 3 điểm toán, lý, hóa.
- Tính điểm trung bình.
- In kết quả và xếp loại:
  + >= 8.0: Giỏi
  + >= 6.5: Khá
  + >= 5.0: Trung bình
  + < 5.0: Yếu
"""

def xep_loai(diem):
    if diem >= 8.0:
        return "Giỏi"
    elif diem >= 6.5:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

# Ví dụ 1
print("Ví dụ 1:")
ten = "Ngọc"
toan, ly, hoa = 8.5, 7.0, 9.0
dtb = (toan + ly + hoa) / 3
print(f"{ten} - ĐTB: {dtb:.2f} - Xếp loại: {xep_loai(dtb)}")

# Ví dụ 2
print("Ví dụ 2:")
ten = "Minh"
toan, ly, hoa = 4.5, 5.0, 4.0
dtb = (toan + ly + hoa) / 3
print(f"{ten} - ĐTB: {dtb:.2f} - Xếp loại: {xep_loai(dtb)}")

# Bài tập cho người học
print("\n--- Bài tập cho bạn ---")
print("Hãy viết chương trình tương tự với tên và điểm của bạn!")

def main():
    print("\n=== CHƯƠNG TRÌNH TÍNH ĐIỂM TRUNG BÌNH ===")
    ten = input("Nhập tên: ")
    try:
        toan = float(input("Điểm Toán: "))
        ly = float(input("Điểm Lý: "))
        hoa = float(input("Điểm Hóa: "))
        
        dtb = (toan + ly + hoa) / 3
        print(f"\n--- KẾT QUẢ ---")
        print(f"Học sinh: {ten}")
        print(f"Điểm trung bình: {dtb:.2f}")
        print(f"Xếp loại: {xep_loai(dtb)}")
        
    except ValueError:
        print("Lỗi: Vui lòng nhập số hợp lệ!")

if __name__ == "__main__":
    main()
```

---

✅ **Tổng cộng ~100 dòng**, đầy đủ comment tiếng Việt, 2 ví dụ, 1 bài tập nhỏ.  
🎯 Phù hợp cho người mới học Python từ cơ bản đến trung cấp.  
📁 Lưu file với tên: `python_18_cap_co_ban.py`