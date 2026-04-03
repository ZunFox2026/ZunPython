"""
Bài học: Python 6 cấp cơ bản (Cấp 1 đến Cấp 6)
Mục tiêu: Giới thiệu 6 cấp độ cơ bản trong học Python qua ví dụ và bài tập nhỏ.

Cấp 1: In dữ liệu
Cấp 2: Biến và kiểu dữ liệu
Cấp 3: Câu điều kiện (if/else)
Cấp 4: Vòng lặp (for/while)
Cấp 5: Hàm (def)
Cấp 6: Danh sách (list) và xử lý dữ liệu đơn giản
"""

def main():
    # Cấp 1: In dữ liệu ra màn hình
    print("=== Cấp 1: In dữ liệu ===")
    print("Chào mừng bạn đến với Python 6 cấp cơ bản!")

    # Cấp 2: Biến và kiểu dữ liệu
    print("\n=== Cấp 2: Biến và kiểu dữ liệu ===")
    ten = "An"           # chuỗi
    tuoi = 12            # số nguyên
    chieu_cao = 1.55     # số thập phân
    dat_hoc_bong = True  # kiểu boolean

    print(f"Tên: {ten}")
    print(f"Tuổi: {tuoi}")
    print(f"Chiều cao: {chieu_cao} mét")
    print(f"Đạt học bổng: {dat_hoc_bong}")

    # Cấp 3: Câu điều kiện (if/else)
    print("\n=== Cấp 3: Câu điều kiện ===")
    if tuoi >= 12:
        print(f"{ten} đủ tuổi tham gia câu lạc bộ lập trình.")
    else:
        print(f"{ten} chưa đủ tuổi tham gia câu lạc bộ.")

    # Ví dụ thêm
    diem = 85
    if diem >= 90:
        xep_loai = "Xuất sắc"
    elif diem >= 75:
        xep_loai = "Khá"
    else:
        xep_loai = "Trung bình"
    print(f"Điểm: {diem} -> Xếp loại: {xep_loai}")

    # Cấp 4: Vòng lặp
    print("\n=== Cấp 4: Vòng lặp ===")
    print("In số từ 1 đến 5:")
    for i in range(1, 6):
        print(f"Số: {i}")

    # Ví dụ while: đếm ngược
    print("Đếm ngược từ 3:")
    dem = 3
    while dem > 0:
        print(dem)
        dem -= 1
    print("Hết giờ!")

    # Cấp 5: Hàm (def)
    print("\n=== Cấp 5: Hàm ===")

    def chao_ten(ten):
        """Hàm chào một người theo tên"""
        return f"Xin chào {ten}! Rất vui được gặp bạn."

    def tinh_tong(a, b):
        """Hàm tính tổng hai số"""
        return a + b

    # Gọi hàm
    print(chao_ten("Bình"))
    print(f"Tổng của 5 và 7 là: {tinh_tong(5, 7)}")

    # Cấp 6: Danh sách và xử lý dữ liệu
    print("\n=== Cấp 6: Danh sách (list) ===")
    diem_so = [8, 9, 7, 10, 6]
    print(f"Danh sách điểm: {diem_so}")

    # Tính trung bình
    trung_binh = sum(diem_so) / len(diem_so)
    print(f"Điểm trung bình: {trung_binh:.1f}")

    # Thêm điểm mới
    diem_so.append(9)
    print(f"Sau khi thêm điểm: {diem_so}")

    # Duyệt danh sách
    print("Các điểm số:")
    for diem in diem_so:
        print(f"- {diem}")

    # Bài tập nhỏ
    print("\n=== Bài tập nhỏ ===")
    """
    Bài tập: Viết chương trình nhập tên và 3 điểm số của học sinh.
    In ra tên, điểm cao nhất, điểm thấp nhất và điểm trung bình.
    """
    print("Bài tập: Nhập thông tin học sinh và xử lý điểm số")
    # Dữ liệu mẫu thay vì nhập từ người dùng để đơn giản
    ten_hoc_sinh = "Lan"
    diem_bai = [8, 7, 9]

    diem_cao_nhat = max(diem_bai)
    diem_thap_nhat = min(diem_bai)
    trung_binh_bai = sum(diem_bai) / len(diem_bai)

    print(f"Học sinh: {ten_hoc_sinh}")
    print(f"Điểm: {diem_bai}")
    print(f"Điểm cao nhất: {diem_cao_nhat}")
    print(f"Điểm thấp nhất: {diem_thap_nhat}")
    print(f"Điểm trung bình: {trung_binh_bai:.1f}")

    print("\nChúc mừng bạn đã hoàn thành Python 6 cấp cơ bản!")


# Gọi hàm chính
if __name__ == "__main__":
    main()
```