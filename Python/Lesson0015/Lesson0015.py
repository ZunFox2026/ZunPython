# Python 15 cấp Cơ bản - Bài học tổng hợp
# Dành cho người mới bắt đầu: từ biến, vòng lặp, hàm đến xử lý danh sách

def main():
    """
    Hàm chính thực hiện các ví dụ và bài tập nhỏ
    """

    # ----------------- 1. Biến và kiểu dữ liệu cơ bản -----------------
    print("=== 1. Biến và kiểu dữ liệu ===")
    ten = "An"           # Chuỗi (string)
    tuoi = 15            # Số nguyên (int)
    chieu_cao = 1.65     # Số thực (float)
    hoc_gioi = True      # Boolean (True/False)

    print(f"Tên: {ten}, Tuổi: {tuoi}, Chiều cao: {chieu_cao}m, Học giỏi: {hoc_gioi}")

    # ----------------- 2. Câu điều kiện (if-elif-else) -----------------
    print("\n=== 2. Câu điều kiện ===")
    if tuoi >= 16:
        print(f"{ten} đã đủ tuổi lái xe máy.")
    elif tuoi >= 15:
        print(f"{ten} đang chờ đủ tuổi lái xe máy.")
    else:
        print(f"{ten} chưa đủ tuổi.")

    # Ví dụ 2: Kiểm tra điểm số
    diem = 8.5
    if diem >= 9:
        xep_loai = "Xuất sắc"
    elif diem >= 8:
        xep_loai = "Giỏi"
    elif diem >= 6.5:
        xep_loai = "Khá"
    else:
        xep_loai = "Cần cố gắng"
    print(f"Điểm: {diem} → Xếp loại: {xep_loai}")

    # ----------------- 3. Vòng lặp for -----------------
    print("\n=== 3. Vòng lặp for ===")
    # In các số từ 1 đến 5
    print("In số từ 1 đến 5:")
    for i in range(1, 6):
        print(f"Số: {i}")

    # Duyệt qua danh sách môn học
    mon_hoc = ["Toán", "Văn", "Anh", "Lý"]
    print("Các môn học yêu thích:")
    for mon in mon_hoc:
        print(f" - {mon}")

    # ----------------- 4. Hàm (Function) -----------------
    print("\n=== 4. Hàm trong Python ===")

    def tinh_tong(a, b):
        """Hàm tính tổng hai số"""
        return a + b

    def chao_tan(ten, lop):
        """Hàm chào hỏi học sinh"""
        print(f"Xin chào {ten} lớp {lop}! Chúc em học tốt!")

    # Gọi hàm
    ket_qua = tinh_tong(10, 25)
    print(f"Tổng của 10 và 25 là: {ket_qua}")

    chao_tan("Bình", "8A")

    # ----------------- 5. Danh sách (List) -----------------
    print("\n=== 5. Làm việc với danh sách ===")
    diem_toan = [8, 9, 7, 10, 8.5]

    # Thêm điểm mới
    diem_toan.append(9.5)
    print(f"Điểm Toán: {diem_toan}")

    # Tính điểm trung bình
    dtb = sum(diem_toan) / len(diem_toan)
    print(f"Điểm trung bình môn Toán: {dtb:.2f}")

    # ----------------- BÀI TẬP NHỎ -----------------
    print("\n=== 📝 BÀI TẬP NHỎ ===")
    print("Bài 1: Viết chương trình nhập tên và tuổi, in ra lời chào và đánh giá độ tuổi.")
    print("Bài 2: Tạo danh sách 3 môn học, in ra môn học đầu và cuối.")
    print("Bài 3: Viết hàm tính diện tích hình chữ nhật (dài, rộng).")

    # Gợi ý bài 3
    def dien_tich_hcn(chieu_dai, chieu_rong):
        return chieu_dai * chieu_rong

    print(f"Gợi ý bài 3: Diện tích HCN 5x3 = {dien_tich_hcn(5, 3)}")

    print("\nChúc mừng bạn đã hoàn thành bài học cơ bản!")
    print("Hãy thử làm bài tập và sửa code để luyện tập nhé!")


# Gọi hàm chính
if __name__ == "__main__":
    main()


# ==================== GỢI Ý BÀI TẬP (giải thử) ====================

# Bài 1: Nhập tên và tuổi
# name = input("Nhập tên: ")
# age = int(input("Nhập tuổi: "))
# if age < 13:
#     print(f"Chào {name}, em còn nhỏ quá!")
# else:
#     print(f"Chào {name}, chúc anh/chị học tốt!")

# Bài 2: Môn học đầu và cuối
# subjects = ["Sử", "Địa", "Hoá"]
# print("Môn đầu:", subjects[0])
# print("Môn cuối:", subjects[-1])

# Bài 3: Hàm tính diện tích (đã làm ở trên)
```