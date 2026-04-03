"""
Bài học Python 13: Lập Trình Cơ Bản Từ A đến Z
File: python13_basic_programming.py

Mục tiêu:
- Ôn tập các khái niệm cơ bản: biến, kiểu dữ liệu, điều kiện, vòng lặp, hàm.
- Viết chương trình nhỏ giải quyết bài toán thực tế.
- Áp dụng vào ví dụ và bài tập thực hành.
"""

# 1. Biến và kiểu dữ liệu cơ bản
# Python tự động nhận diện kiểu dữ liệu khi gán giá trị

ten = "An"              # Chuỗi (string)
tuoi = 16               # Số nguyên (int)
chieu_cao = 1.75        # Số thực (float)
la_hoc_sinh = True      # Boolean (True/False)

print("Thông tin học sinh:")
print(f"Tên: {ten}")
print(f"Tuổi: {tuoi}")
print(f"Chiều cao: {chieu_cao} m")
print(f"Là học sinh: {la_hoc_sinh}")

# 2. Câu điều kiện (if-elif-else)
def danh_gia_tuoi(tuoi):
    """Hàm đánh giá độ tuổi theo nhóm"""
    if tuoi < 13:
        return "Thiếu nhi"
    elif tuoi < 18:
        return "Vị thành niên"
    else:
        return "Người lớn"

# Ví dụ 1: Sử dụng hàm đánh giá tuổi
print("\nVí dụ 1: Đánh giá độ tuổi")
print(f"{ten} là: {danh_gia_tuoi(tuoi)}")

# Ví dụ 2: Vòng lặp for và while
print("\nVí dụ 2: In bảng cửu chương 5")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

print("\nVí dụ 3: Đếm ngược bằng while")
dem = 5
while dem > 0:
    print(f"Đếm ngược: {dem}")
    dem -= 1
print("Xuất phát!")

# 3. Danh sách (list) và xử lý dữ liệu đơn giản
diem_toan = [8, 9, 7, 10, 6, 9]

print(f"\nDanh sách điểm Toán: {diem_toan}")
print(f"Điểm cao nhất: {max(diem_toan)}")
print(f"Điểm thấp nhất: {min(diem_toan)}")
print(f"Điểm trung bình: {sum(diem_toan) / len(diem_toan):.2f}")

# 4. Hàm tính điểm trung bình và xếp loại
def xep_loai_diem(diem):
    """Xếp loại học lực theo điểm trung bình"""
    if diem >= 9.0:
        return "Xuất sắc"
    elif diem >= 8.0:
        return "Giỏi"
    elif diem >= 6.5:
        return "Khá"
    elif diim >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

# Tính điểm trung bình và xếp loại
dtb = sum(diem_toan) / len(diem_toan)
print(f"\nXếp loại học lực: {xep_loai_diem(dtb)}")

# 5. Bài tập nhỏ: Tính tổng các số chẵn từ 1 đến n
def tinh_tong_chan(n):
    """Tính tổng các số chẵn từ 1 đến n"""
    tong = 0
    for i in range(2, n + 1, 2):  # Bắt đầu từ 2, bước nhảy 2
        tong += i
    return tong

# Gọi hàm và in kết quả
n = 10
print(f"\nBài tập: Tổng các số chẵn từ 1 đến {n} là: {tinh_tong_chan(n)}")

# 6. Bài tập nâng cao nhỏ: Kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    """Kiểm tra xem n có phải số nguyên tố không"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Ví dụ kiểm tra
so_kiem_tra = 17
print(f"{so_kiem_tra} là số nguyên tố? {la_so_nguyen_to(so_kiem_tra)}")

# 7. Hàm chính (main)
def main():
    """Hàm chính chạy chương trình"""
    print("=" * 50)
    print("PYTHON 13: LẬP TRÌNH CƠ BẢN TỪ A ĐẾN Z".center(50))
    print("=" * 50)
    
    # Chạy lại một vài ví dụ
    print(f"\nChào bạn {ten}! Bạn {tuoi} tuổi và là {danh_gia_tuoi(tuoi)}.")
    print(f"Tổng chẵn đến 10: {tinh_tong_chan(10)}")
    print(f"17 là số nguyên tố? {la_so_nguyen_to(17)}")
    
    print("\nChương trình kết thúc. Cảm ơn bạn đã học!")

# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()
```

---

### 📘 Hướng dẫn sử dụng:
1. Lưu đoạn code trên vào file `python13_basic_programming.py`
2. Chạy bằng lệnh: `python python13_basic_programming.py`
3. Kết quả sẽ hiển thị các ví dụ và bài tập cơ bản.

### ✅ Bài tập nhỏ cho người học:
- Thay đổi giá trị `tuoi` và `diem_toan` để xem kết quả thay đổi ra sao.
- Viết hàm mới để đếm số lượng điểm >= 8 trong danh sách `diem_toan`.

> 💡 Gợi ý: Dùng vòng lặp và biến đếm.

Chúc bạn học tốt với Python! 🐍