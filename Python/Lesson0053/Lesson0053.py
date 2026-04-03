"""
Python 53: Xử Lý Danh Sách và Vòng Lặp Cơ Bản
Mô tả: Bài học giới thiệu cách sử dụng danh sách (list) và các vòng lặp (for, while)
trong Python. Bao gồm các thao tác thêm, sửa, xóa phần tử, duyệt danh sách,
và xử lý dữ liệu cơ bản.

Tác giả: Học viên Python
Ngày: 2025
"""

def vidu_1_duyet_danh_sach():
    """
    Ví dụ 1: Duyệt danh sách bằng vòng lặp for
    In ra từng phần tử trong danh sách tên học sinh.
    """
    danh_sach_hoc_sinh = ["An", "Bình", "Châu", "Dũng", "Em"]
    print("=== Ví dụ 1: Duyệt danh sách ===")
    print("Danh sách học sinh:")
    
    # Duyệt từng phần tử trong danh sách
    for ten in danh_sach_hoc_sinh:
        print(f" - {ten}")
    
    # In tổng số học sinh
    print(f"Tổng cộng: {len(danh_sach_hoc_sinh)} học sinh.")


def vidu_2_xu_ly_so():
    """
    Ví dụ 2: Sử dụng vòng lặp for với hàm range và xử lý số
    Tạo danh sách các số chẵn từ 0 đến 10 và tính tổng.
    """
    print("\n=== Ví dụ 2: Xử lý số và tính tổng ===")
    so_chan = []  # Khởi tạo danh sách rỗng
    
    # Dùng vòng lặp để thêm số chẵn vào danh sách
    for i in range(0, 11, 2):  # từ 0 đến 10, bước nhảy 2
        so_chan.append(i)
    
    print(f"Các số chẵn: {so_chan}")
    
    # Tính tổng sử dụng vòng lặp
    tong = 0
    for so in so_chan:
        tong += so
    
    print(f"Tổng các số chẵn: {tong}")


def vidu_3_su_dung_while():
    """
    Ví dụ 3: Dùng vòng lặp while để xử lý danh sách
    Nhập tên học sinh cho đến khi người dùng nhập 'dừng'.
    """
    print("\n=== Ví dụ 3: Nhập danh sách bằng vòng lặp while ===")
    danh_sach = []
    print("Nhập tên học sinh (nhập 'dừng' để kết thúc):")
    
    while True:
        ten = input("Nhập tên: ").strip()
        if ten.lower() == 'dừng':
            break
        if ten:  # Nếu tên không rỗng
            danh_sach.append(ten)
        else:
            print("Tên không được để trống!")
    
    print(f"Danh sách đã nhập ({len(danh_sach)} người):")
    for ten in danh_sach:
        print(f" - {ten}")


def bai_tap_nho():
    """
    Bài tập nhỏ: Viết chương trình yêu cầu người dùng nhập 5 số nguyên.
    Sau đó in ra số lớn nhất, số nhỏ nhất và trung bình cộng.
    """
    print("\n=== Bài tập nhỏ: Tìm số lớn nhất, nhỏ nhất và trung bình ===")
    so_nguyen = []
    print("Hãy nhập 5 số nguyên:")
    
    for i in range(5):
        while True:
            try:
                num = int(input(f"Nhập số thứ {i+1}: "))
                so_nguyen.append(num)
                break
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ!")
    
    # Xử lý dữ liệu
    so_lon_nhat = max(so_nguyen)
    so_nho_nhat = min(so_nguyen)
    trung_binh = sum(so_nguyen) / len(so_nguyen)
    
    print(f"\nKết quả:")
    print(f"Số lớn nhất: {so_lon_nhat}")
    print(f"Số nhỏ nhất: {so_nho_nhat}")
    print(f"Trung bình cộng: {trung_binh:.2f}")
    
    # In danh sách
    print(f"Danh sách số đã nhập: {so_nguyen}")


def main():
    """
    Hàm chính thực thi chương trình.
    """
    print("📘 PYTHON 53: XỬ LÝ DANH SÁCH VÀ VÒNG LẶP CƠ BẢN\n")
    
    # Các ví dụ minh họa
    vidu_1_duyet_danh_sach()
    vidu_2_xu_ly_so()
    vidu_3_su_dung_while()
    
    # Bài tập nhỏ
    bai_tap_nho()
    
    print("\n✅ Hoàn thành bài học!")
    print("Bạn đã học được: sử dụng list, vòng lặp for/while, nhập dữ liệu, xử lý số.")


# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()
```

---

### 📝 Ghi chú:
- **Code ~100 dòng**, đầy đủ comment tiếng Việt.
- **3 ví dụ**: duyệt danh sách, xử lý số, vòng lặp `while`.
- **1 bài tập nhỏ**: nhập 5 số, tìm max/min/trung bình.
- Chạy được ngay, không cần thư viện ngoài.

Bạn có thể lưu thành file `python_53_danh_sach_vong_lap.py` và chạy bằng lệnh:
```bash
python python_53_danh_sach_vong_lap.py
```