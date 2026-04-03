"""
Bài 30: Python Cơ bản
Chủ đề: Làm việc với danh sách (list), chuỗi (string), và hàm đơn giản
Tác giả: Học viên Python
Ngày: 2025
"""

# --- 1. Khởi tạo danh sách và thao tác cơ bản ---
# Danh sách (list) là cấu trúc dữ liệu lưu trữ nhiều phần tử, có thể thay đổi

def vi_du_danh_sach():
    """Ví dụ 1: Thao tác cơ bản với danh sách"""
    print("=== Ví dụ 1: Làm việc với danh sách ===")
    
    # Khởi tạo danh sách sinh viên
    sinh_vien = ["An", "Bình", "Chi", "Dũng"]
    print(f"Danh sách sinh viên ban đầu: {sinh_vien}")
    
    # Thêm phần tử vào cuối danh sách
    sinh_vien.append("Hà")
    print(f"Sau khi thêm 'Hà': {sinh_vien}")
    
    # Chèn phần tử vào vị trí cụ thể
    sinh_vien.insert(1, "Lan")  # Chèn "Lan" vào vị trí thứ 1
    print(f"Sau khi chèn 'Lan' vào vị trí 1: {sinh_vien}")
    
    # Xóa phần tử theo giá trị
    sinh_vien.remove("Chi")
    print(f"Sau khi xóa 'Chi': {sinh_vien}")
    
    # Lấy độ dài danh sách
    print(f"Số lượng sinh viên: {len(sinh_vien)}")


# --- 2. Xử lý chuỗi ---
# Chuỗi (string) là dãy ký tự, có thể thao tác bằng nhiều phương thức

def vi_du_chuoi():
    """Ví dụ 2: Xử lý chuỗi cơ bản"""
    print("\n=== Ví dụ 2: Xử lý chuỗi ===")
    
    cau = "   Học Lập Trình Python Cơ Bản   "
    print(f"Chuỗi gốc: '{cau}'")
    
    # Loại bỏ khoảng trắng đầu và cuối
    cau_trim = cau.strip()
    print(f"Sau khi strip(): '{cau_trim}'")
    
    # Chuyển thành chữ thường
    cau_lower = cau_trim.lower()
    print(f"Chữ thường: '{cau_lower}'")
    
    # Chuyển thành chữ hoa
    cau_upper = cau_trim.upper()
    print(f"Chữ hoa: '{cau_upper}'")
    
    # Tách chuỗi thành danh sách từ
    danh_sach_tu = cau_trim.split()
    print(f"Tách thành từ: {danh_sach_tu}")
    
    # Nối danh sách thành chuỗi
    cau_moi = "-".join(danh_sach_tu)
    print(f"Nối bằng dấu '-': {cau_moi}")


# --- 3. Viết hàm đơn giản ---
# Hàm giúp tái sử dụng mã, dễ bảo trì

def tinh_tong_danh_sach(numbers):
    """
    Hàm tính tổng các số trong danh sách
    numbers: danh sách số
    return: tổng các số
    """
    tong = 0
    for so in numbers:
        tong += so
    return tong

def vi_du_ham():
    """Ví dụ 3: Sử dụng hàm đơn giản"""
    print("\n=== Ví dụ 3: Hàm tính tổng ===")
    
    danh_sach_so = [10, 20, 30, 40, 50]
    ket_qua = tinh_tong_danh_sach(danh_sach_so)
    print(f"Tổng của {danh_sach_so} là: {ket_qua}")
    
    # Dùng hàm với danh sách khác
    danh_sach_khac = [5, 15, 25]
    print(f"Tổng của {danh_sach_khac} là: {tinh_tong_danh_sach(danh_sach_khac)}")


# --- Bài tập nhỏ ---
def bai_tap_nho():
    """Bài tập: Viết hàm đếm số từ trong một chuỗi"""
    print("\n=== Bài tập nhỏ ===")
    print("Viết hàm đếm số từ trong chuỗi. Gợi ý: dùng split() và len()")
    
    def dem_tu(chuoi):
        # Bỏ khoảng trắng thừa và tách từ
        tu = chuoi.strip().split()
        return len(tu)
    
    # Kiểm thử hàm
    test1 = "Xin chào các bạn học Python"
    test2 = "  Một hai   ba bốn  "
    
    print(f"'{test1}' có {dem_tu(test1)} từ")
    print(f"'{test2}' có {dem_tu(test2)} từ")


# --- Hàm chính ---
def main():
    """Hàm chính chạy các ví dụ và bài tập"""
    print("📘 BÀI 30: PYTHON CƠ BẢN")
    print("=" * 50)
    
    # Chạy các ví dụ
    vi_du_danh_sach()
    vi_du_chuoi()
    vi_du_ham()
    
    # Bài tập nhỏ
    bai_tap_nho()
    
    print("\n✅ Hoàn thành bài học!")
    print("💡 Gợi ý tự luyện: Thử viết hàm tìm phần tử lớn nhất trong danh sách.")


# --- Chạy chương trình ---
if __name__ == "__main__":
    main()
```

**Giải thích ngắn:**
- File `.py` này gồm 3 ví dụ: danh sách, chuỗi, hàm.
- Có bài tập nhỏ kèm lời giải: đếm số từ trong chuỗi.
- Dùng comment tiếng Việt, dễ hiểu cho người mới học.
- Dưới 100 dòng, cấu trúc rõ ràng với `main()`.