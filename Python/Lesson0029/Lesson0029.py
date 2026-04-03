"""
Bài học: Python 29 - Xử Lý Danh Sách và Vòng Lặp
Mục tiêu:
- Hiểu cách tạo và thao tác với danh sách (list)
- Sử dụng vòng lặp for và while để duyệt danh sách
- Áp dụng các phương thức phổ biến của list
- Thực hành với bài tập nhỏ
"""

def vi_du_1_duyet_danh_sach():
    """
    Ví dụ 1: Duyệt danh sách bằng vòng lặp for
    """
    print("=== Ví dụ 1: Duyệt danh sách bằng for ===")
    
    danh_sach_mon_an = ["Phở", "Bún chả", "Cơm tấm", "Bánh mì"]
    
    print("Các món ăn yêu thích:")
    for mon in danh_sach_mon_an:
        print(f"- {mon}")
    
    # Dùng enumerate để lấy cả chỉ số và giá trị
    print("\nTheo thứ tự:")
    for i, mon in enumerate(danh_sach_mon_an, start=1):
        print(f"{i}. {mon}")


def vi_du_2_xu_ly_danh_sach():
    """
    Ví dụ 2: Các thao tác phổ biến với danh sách
    """
    print("\n=== Ví dụ 2: Các thao tác với danh sách ===")
    
    diem_so = [8, 7, 9, 6, 10]
    print(f"Điểm ban đầu: {diem_so}")
    
    # Thêm phần tử
    diem_so.append(8)  # Thêm vào cuối
    print(f"Sau khi thêm 8: {diem_so}")
    
    # Chèn vào vị trí cụ thể
    diem_so.insert(1, 5)  # Chèn 5 vào vị trí thứ 1
    print(f"Sau khi chèn 5 vào vị trí 1: {diem_so}")
    
    # Xóa phần tử
    diem_so.remove(6)  # Xóa giá trị 6 đầu tiên
    print(f"Sau khi xóa điểm 6: {diem_so}")
    
    # Sắp xếp danh sách
    diem_so.sort()
    print(f"Sau khi sắp xếp: {diem_so}")
    
    # Đảo ngược danh sách
    diem_so.reverse()
    print(f"Sau khi đảo ngược: {diem_so}")
    
    # Tính tổng và trung bình
    tong = sum(diem_so)
    trung_binh = tong / len(diem_so)
    print(f"Tổng điểm: {tong}, Trung bình: {trung_binh:.2f}")


def vi_du_3_vong_lap_while():
    """
    Ví dụ 3: Duyệt danh sách bằng while
    """
    print("\n=== Ví dụ 3: Duyệt bằng vòng lặp while ===")
    
    danh_sach_nhi_phan = [1, 0, 1, 1, 0, 0, 1]
    print(f"Dãy nhị phân: {danh_sach_nhi_phan}")
    
    i = 0
    tong = 0
    while i < len(danh_sach_nhi_phan):
        tong += danh_sach_nhi_phan[i]
        i += 1
    
    print(f"Tổng số bit 1: {tong}")
    
    # Đếm số lượng 0 bằng while
    i = 0
    dem_0 = 0
    while i < len(danh_sach_nhi_phan):
        if danh_sach_nhi_phan[i] == 0:
            dem_0 += 1
        i += 1
    print(f"Số lượng bit 0: {dem_0}")


def bai_tap_nho():
    """
    Bài tập nhỏ: Nhập danh sách số và xử lý
    Yêu cầu: Nhập 5 số nguyên từ bàn phím, in ra số lớn nhất, nhỏ nhất và trung bình
    """
    print("\n=== Bài tập nhỏ: Xử lý danh sách số ===")
    
    danh_sach = []
    print("Nhập 5 số nguyên:")
    
    for i in range(5):
        while True:
            try:
                so = int(input(f"Số thứ {i+1}: "))
                danh_sach.append(so)
                break
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ!")
    
    # Xử lý và in kết quả
    print(f"\nDanh sách bạn nhập: {danh_sach}")
    print(f"Số lớn nhất: {max(danh_sach)}")
    print(f"Số nhỏ nhất: {min(danh_sach)}")
    print(f"Trung bình: {sum(danh_sach) / len(danh_sach):.2f}")
    
    # In các số chẵn
    so_chan = [x for x in danh_sach if x % 2 == 0]
    print(f"Các số chẵn: {so_chan}")


def main():
    """
    Hàm chính chạy các ví dụ và bài tập
    """
    print("📘 BÀI HỌC: XỬ LÝ DANH SÁCH VÀ VÒNG LẶP")
    print("=" * 50)
    
    vi_du_1_duyet_danh_sach()
    vi_du_2_xu_ly_danh_sach()
    vi_du_3_vong_lap_while()
    
    print("\n" + "=" * 50)
    bai_tap_nho()
    
    print("\n✅ Hoàn thành bài học! Hãy luyện tập thêm với các danh sách khác.")


# Chạy chương trình
if __name__ == "__main__":
    main()
```

---

**Giải thích ngắn:**

- **Ví dụ 1**: Dùng `for` để duyệt danh sách, in món ăn.
- **Ví dụ 2**: Các thao tác với list như `append`, `insert`, `remove`, `sort`, `reverse`, tính toán.
- **Ví dụ 3**: Dùng `while` để duyệt và xử lý danh sách nhị phân.
- **Bài tập nhỏ**: Người dùng nhập 5 số, chương trình tính max, min, trung bình, lọc số chẵn.

> ✅ Chạy file `.py` này để thực hành!