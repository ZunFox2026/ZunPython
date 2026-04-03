"""
Python 60 Cấp Độ Cơ Bản - Hành Trình Từ Con Số 0 Đến Lập Trình Viên
File: basics_level1.py
Mục tiêu: Giới thiệu các khái niệm cơ bản của Python: biến, kiểu dữ liệu, nhập xuất, biểu thức, câu điều kiện.
"""

def main():
    # === 1. Biến và Kiểu Dữ Liệu Cơ Bản ===
    # Trong Python, bạn không cần khai báo kiểu dữ liệu
    ten = "An"              # Chuỗi (string)
    tuoi = 16               # Số nguyên (int)
    chieu_cao = 1.75        # Số thực (float)
    la_hoc_sinh = True      # Boolean (True/False)

    # In thông tin ra màn hình
    print("=== THÔNG TIN CÁ NHÂN ===")
    print(f"Họ tên: {ten}")
    print(f"Tuổi: {tuoi}")
    print(f"Chiều cao: {chieu_cao} m")
    print(f"Là học sinh: {la_hoc_sinh}")

    # === 2. Nhập Dữ Liệu Từ Người Dùng ===
    print("\n=== NHẬP THÔNG TIN ===")
    ten_nguoi_dung = input("Nhập tên của bạn: ")
    tuoi_nguoi_dung = int(input("Nhập tuổi của bạn: "))  # Chuyển sang số nguyên

    # === 3. Biểu Thức và Toán Tử ===
    nam_sinh = 2024 - tuoi_nguoi_dung
    print(f"Xin chào {ten_nguoi_dung}, bạn sinh năm {nam_sinh}.")

    # === 4. Câu Lệnh Điều Kiện (if-else) ===
    print("\n=== KIỂM TRA ĐỘ TUỔI ===")
    if tuoi_nguoi_dung >= 18:
        print("Bạn đã đủ tuổi trưởng thành.")
    else:
        print("Bạn chưa đủ tuổi trưởng thành.")

    # Ví dụ 2: Kiểm tra số chẵn/lẻ
    so = int(input("\nNhập một số nguyên: "))
    if so % 2 == 0:
        print(f"{so} là số chẵn.")
    else:
        print(f"{so} là số lẻ.")

    # Ví dụ 3: Tính điểm trung bình và xếp loại
    print("\n=== XẾP LOẠI HỌC LỰC ===")
    toan = float(input("Điểm Toán: "))
    ly = float(input("Điểm Lý: "))
    hoa = float(input("Điểm Hóa: "))

    diem_tb = (toan + ly + hoa) / 3
    print(f"Điểm trung bình: {diem_tb:.2f}")

    if diem_tb >= 8.0:
        print("Xếp loại: Giỏi")
    elif diem_tb >= 6.5:
        print("Xếp loại: Khá")
    elif diem_tb >= 5.0:
        print("Xếp loại: Trung bình")
    else:
        print("Xếp loại: Yếu")

    # === Bài Tập Nhỏ ===
    print("\n=== BÀI TẬP NHỎ ===")
    print("1. Viết chương trình nhập bán kính hình tròn, tính và in diện tích (S = π * r²).")
    print("2. Nhập một số nguyên, kiểm tra xem số đó có chia hết cho cả 3 và 5 không.")
    print("3. Nhập điểm thi, in ra 'Đậu' nếu điểm >= 5, ngược lại in 'Rớt'.")

    # Gợi ý giải bài 1:
    # import math
    # r = float(input("Bán kính: "))
    # s = math.pi * r ** 2
    # print(f"Diện tích: {s:.2f}")

# Gọi hàm chính
if __name__ == "__main__":
    main()

# Kết thúc chương trình
# Hành trình 60 cấp độ sẽ tiếp tục với vòng lặp, hàm, danh sách, file,...
```

---

📌 **Ghi chú:**
- File này nằm ở cấp độ 1: Làm quen với cú pháp cơ bản.
- Dài khoảng 100 dòng, có comment tiếng Việt.
- 3 ví dụ minh họa: kiểm tra tuổi, chẵn/lẻ, xếp loại học lực.
- 3 bài tập nhỏ kèm gợi ý để người học tự thực hành.

👉 **Tiếp theo:** Cấp độ 2 sẽ học về vòng lặp (`for`, `while`) và hàm (`def`).