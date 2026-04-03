"""
Bài 55: Python Cơ Bản
Tác giả: Học viên
Mô tả: Giới thiệu các khái niệm cơ bản trong Python như biến, kiểu dữ liệu, 
câu điều kiện, vòng lặp, hàm và danh sách. Mỗi phần có ví dụ minh họa và bài tập nhỏ.
"""

# 1. Biến và kiểu dữ liệu cơ bản
# Python hỗ trợ nhiều kiểu dữ liệu: int, float, str, bool

so_nguyen = 10          # kiểu int
so_thuc = 3.14          # kiểu float
chuoi = "Xin chào"      # kiểu str
dung_sai = True         # kiểu bool

# In các giá trị ra màn hình
print("Biến và kiểu dữ liệu:")
print(f"Số nguyên: {so_nguyen}")
print(f"Số thực: {so_thuc}")
print(f"Chuỗi: {chuoi}")
print(f"Boolean: {dung_sai}")

# 2. Câu điều kiện (if, elif, else)
tuoi = 18
print("\nCâu điều kiện:")
if tuoi < 13:
    print("Bạn là trẻ em.")
elif tuoi < 18:
    print("Bạn là vị thành niên.")
else:
    print("Bạn là người lớn.")

# Ví dụ 2: Kiểm tra số chẵn/lẻ
so = 7
if so % 2 == 0:
    print(f"{so} là số chẵn.")
else:
    print(f"{so} là số lẻ.")

# 3. Vòng lặp
# Vòng lặp for
print("\nVòng lặp for:")
danh_sach = ["Táo", "Cam", "Chuối"]
for phan_tu in danh_sach:
    print(f"Trái cây: {phan_tu}")

# Vòng lặp while
print("\nVòng lặp while:")
dem = 0
while dem < 3:
    print(f"Lần lặp thứ {dem + 1}")
    dem += 1

# 4. Hàm trong Python
# Hàm là khối lệnh có thể tái sử dụng
def tinh_tong(a, b):
    """
    Hàm tính tổng hai số
    Trả về tổng của a và b
    """
    return a + b

def in_chuoi_lap_lai(chuoi, so_lan):
    """
    Hàm in một chuỗi nhiều lần
    """
    for i in range(so_lan):
        print(f"Lần {i+1}: {chuoi}")

# Gọi hàm
print("\nHàm:")
ket_qua = tinh_tong(5, 7)
print(f"Tổng của 5 và 7 là: {ket_qua}")

in_chuoi_lap_lai("Hello", 3)

# 5. Danh sách (list)
print("\nDanh sách:")
danh_sach_so = [1, 2, 3, 4, 5]
danh_sach_so.append(6)  # Thêm phần tử
print(f"Danh sách sau khi thêm: {danh_sach_so}")
print(f"Phần tử đầu tiên: {danh_sach_so[0]}")
print(f"Độ dài danh sách: {len(danh_sach_so)}")

# Duyệt danh sách với chỉ số
for i, gia_tri in enumerate(danh_sach_so):
    print(f"Vị trí {i}: {gia_tri}")

# 6. Bài tập nhỏ
"""
Bài tập: Viết hàm kiểm tra số nguyên tố
Hướng dẫn: Số nguyên tố là số lớn hơn 1 và chỉ chia hết cho 1 và chính nó.
Yêu cầu: Viết hàm `kiem_tra_nguyen_to(n)` trả về True nếu n là số nguyên tố, ngược lại trả về False.
"""

def kiem_tra_nguyen_to(n):
    """
    Kiểm tra xem n có phải là số nguyên tố không
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Kiểm thử hàm
print("\nBài tập - Kiểm tra số nguyên tố:")
so_kiem_tra = [2, 3, 4, 17, 25, 29]
for so in so_kiem_tra:
    if kiem_tra_nguyen_to(so):
        print(f"{so} là số nguyên tố.")
    else:
        print(f"{so} không phải số nguyên tố.")

# Gọi hàm main (mặc dù Python không yêu cầu, nhưng để đúng yêu cầu đề bài)
def main():
    print("Chương trình Python Cơ Bản - Bài 55")
    # Gọi lại các phần ở trên nếu cần
    # (Ở đây ta đã chạy trực tiếp, nhưng main() vẫn được định nghĩa)

if __name__ == "__main__":
    main()
```

---

**Giải thích ngắn:**
- Code giới thiệu các khái niệm cơ bản: biến, kiểu dữ liệu, điều kiện, vòng lặp, hàm, danh sách.
- Có 2 ví dụ rõ ràng cho mỗi phần.
- Bài tập nhỏ: kiểm tra số nguyên tố – ứng dụng vòng lặp và điều kiện.
- Dài khoảng 100 dòng, đầy đủ comment tiếng Việt, phù hợp cho người mới học.