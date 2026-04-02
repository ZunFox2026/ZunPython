"""
Bài 42: Python Cơ bản
Mô tả: Chương trình tổng hợp các kiến thức nền tảng của Python
bao gồm: biến, điều kiện, vòng lặp, hàm, danh sách và từ điển.
"""

def kiem_tra_so_nguyen_to(n):
    """Kiểm tra xem một số nguyên có phải là số nguyên tố không."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tinh_tong_danh_sach(danh_sach):
    """Tính tổng các phần tử kiểu số trong danh sách."""
    tong = 0
    for so in danh_sach:
        tong += so
    return tong

def main():
    # 1. Biến và kiểu dữ liệu cơ bản
    tieu_de = "Bài 42: Python Cơ bản"
    phien_ban = 3.11
    print(f"=== {tieu_de} ===")
    print(f"Phiên bản Python khuyến nghị: {phien_ban}\n")

    # 2. Cấu trúc điều kiện (if - elif - else)
    diem_thi = 85
    if diem_thi >= 90:
        xep_loai = "Xuất sắc"
    elif diem_thi >= 80:
        xep_loai = "Giỏi"
    elif diem_thi >= 70:
        xep_loai = "Khá"
    elif diem_thi >= 50:
        xep_loai = "Trung bình"
    else:
        xep_loai = "Yếu"
    print(f"1. Điểm số: {diem_thi} -> Xếp loại: {xep_loai}")

    # 3. Vòng lặp for và while
    print("\n2. Duyệt dãy số (for loop):")
    for i in range(1, 6):
        print(f"   - Số {i}")

    dem = 3
    print("\n3. Đếm ngược (while loop):")
    while dem > 0:
        print(f"   - {dem}...")
        dem -= 1
    print("   - Bắt đầu!")

    # 4. Xử lý danh sách (List) và List Comprehension
    danh_sach_so = [12, 7, 19, 4, 25, 8, 13]
    print(f"\n4. Danh sách ban đầu: {danh_sach_so}")
    tong = tinh_tong_danh_sach(danh_sach_so)
    print(f"   Tổng các phần tử: {tong}")

    # Lọc số nguyên tố bằng List Comprehension
    so_nguyen_to = [so for so in danh_sach_so if kiem_tra_so_nguyen_to(so)]
    print(f"   Số nguyên tố tìm được: {so_nguyen_to}")

    # 5. Làm việc với từ điển (Dictionary)
    print("\n5. Thông tin sinh viên:")
    sinh_vien = {
        "ho_ten": "Trần Thị B",
        "ma_sv": "SV001",
        "diem_toan": 8.5,
        "diem_ly": 7.0,
        "diem_hoa": 9.0
    }
    for khoa, gia_tri in sinh_vien.items():
        print(f"   {khoa}: {gia_tri}")
    diem_tb = (sinh_vien["diem_toan"] + sinh_vien["diem_ly"] + sinh_vien["diem_hoa"]) / 3
    print(f"   Điểm trung bình: {diem_tb:.2f}")

    print("\n=== Hoàn thành Bài 42 ===")

if __name__ == "__main__":
    main()