"""
Python 19: Xử Lý Danh Sách và Vòng Lặp
Tài liệu học tập: Các thao tác phổ biến với danh sách và vòng lặp trong Python.
"""

def vidu_1_duyet_danh_sach():
    """Ví dụ 1: Duyệt danh sách bằng vòng lặp for"""
    print("=== Ví dụ 1: Duyệt danh sách bằng vòng lặp for ===")
    
    # Khởi tạo danh sách các môn học
    mon_hoc = ["Toán", "Lý", "Hóa", "Sinh", "Văn"]
    
    print("Danh sách các môn học:")
    for mon in mon_hoc:
        print(f"- {mon}")
    
    # Duyệt với chỉ số bằng hàm enumerate
    print("\nDuyệt với chỉ số:")
    for i, mon in enumerate(mon_hoc, start=1):
        print(f"{i}. {mon}")


def vidu_2_xu_ly_danh_sach():
    """Ví dụ 2: Các thao tác thêm, xóa, sửa danh sách"""
    print("\n=== Ví dụ 2: Xử lý danh sách (thêm, xóa, sửa) ===")
    
    # Danh sách điểm số ban đầu
    diem = [8, 7, 9, 6]
    print(f"Điểm ban đầu: {diem}")
    
    # Thêm điểm mới
    diem.append(10)  # Thêm vào cuối
    print(f"Sau khi thêm 10: {diem}")
    
    # Chèn điểm vào vị trí cụ thể
    diem.insert(1, 5)  # Chèn 5 vào vị trí thứ 1
    print(f"Sau khi chèn 5 vào vị trí 1: {diem}")
    
    # Xóa điểm
    diem.remove(7)  # Xóa giá trị 7 đầu tiên
    print(f"Sau khi xóa điểm 7: {diem}")
    
    # Sửa điểm tại vị trí 0
    diem[0] = 9
    print(f"Sửa điểm đầu thành 9: {diem}")
    
    # Sắp xếp danh sách
    diem.sort(reverse=True)  # Sắp xếp giảm dần
    print(f"Điểm sau khi sắp xếp giảm dần: {diem}")


def vidu_3_vong_lap_while():
    """Ví dụ 3: Sử dụng vòng lặp while để xử lý danh sách"""
    print("\n=== Ví dụ 3: Vòng lặp while với danh sách ===")
    
    danh_sach_mua_sam = ["sữa", "trứng", "bánh mì", "táo"]
    da_mua = []
    
    print("Danh sách cần mua:", danh_sach_mua_sam)
    
    # Dùng while để mô phỏng việc mua từng món
    while len(danh_sach_mua_sam) > 0:
        mat_hang = danh_sach_mua_sam.pop(0)  # Lấy và xóa món đầu
        da_mua.append(mat_hang)
        print(f"Đã mua: {mat_hang}")
    
    print("Các món đã mua:", da_mua)


def bai_tap_nho():
    """Bài tập nhỏ: Tính trung bình cộng các số chẵn trong danh sách"""
    print("\n=== Bài tập nhỏ: Tính trung bình cộng số chẵn ===")
    
    # Danh sách số nguyên
    so_nguyen = [3, 8, 12, 7, 4, 15, 6, 9, 10]
    print(f"Danh sách số: {so_nguyen}")
    
    tong_chan = 0
    dem_chan = 0
    
    # Duyệt danh sách để tìm số chẵn
    for so in so_nguyen:
        if so % 2 == 0:  # Kiểm tra số chẵn
            tong_chan += so
            dem_chan += 1
    
    # Tính trung bình
    if dem_chan > 0:
        trung_binh = tong_chan / dem_chan
        print(f"Có {dem_chan} số chẵn. Tổng = {tong_chan}, Trung bình = {trung_binh:.2f}")
    else:
        print("Không có số chẵn nào trong danh sách.")


def main():
    """Hàm chính thực hiện tất cả ví dụ và bài tập"""
    print("📘 PYTHON 19: XỬ LÝ DANH SÁCH VÀ VÒNG LẶP\n")
    
    # Gọi các ví dụ
    vidu_1_duyet_danh_sach()
    vidu_2_xu_ly_danh_sach()
    vidu_3_vong_lap_while()
    
    # Bài tập nhỏ
    bai_tap_nho()
    
    # Tổng kết
    print("\n✅ Học xong bài: Bạn đã biết cách:")
    print("- Duyệt danh sách bằng for và while")
    print("- Thêm, xóa, sửa phần tử danh sách")
    print("- Xử lý dữ liệu danh sách trong vòng lặp")
    print("\nChúc mừng bạn đã hoàn thành bài học!")


# Gọi hàm main khi chạy file
if __name__ == "__main__":
    main()
```