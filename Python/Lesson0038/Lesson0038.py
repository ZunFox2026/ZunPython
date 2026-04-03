"""
Bài học: Python 38 - Lập Trình Cơ Bản cho Người Mới Bắt Đầu
Tác giả: Học viên Python
Mục tiêu: Giới thiệu các khái niệm cơ bản trong Python: biến, kiểu dữ liệu, vòng lặp, điều kiện, hàm.
"""

# 1. Biến và Kiểu Dữ liệu
# Biến dùng để lưu trữ dữ liệu. Python tự động nhận diện kiểu dữ liệu.

ten = "An"           # Chuỗi (string)
tuoi = 20            # Số nguyên (int)
chieu_cao = 1.75     # Số thực (float)
la_sinh_vien = True  # Boolean (True/False)

# In thông tin ra màn hình
print("Thông tin cá nhân:")
print(f"Tên: {ten}")
print(f"Tuổi: {tuoi}")
print(f"Chiều cao: {chieu_cao} m")
print(f"Là sinh viên: {la_sinh_vien}")

# 2. Cấu trúc điều kiện (if-elif-else)
# Dùng để kiểm tra điều kiện và thực hiện hành động tương ứng

def kiem_tra_tuoi(tuoi):
    """
    Hàm kiểm tra độ tuổi và phân loại theo nhóm
    """
    if tuoi < 13:
        return "Trẻ em"
    elif tuoi < 18:
        return "Vị thành niên"
    elif tuoi < 60:
        return "Người trưởng thành"
    else:
        return "Người cao tuổi"

# Ví dụ 1: Kiểm tra tuổi
print("\n--- Ví dụ 1: Kiểm tra độ tuổi ---")
tuoi_mau = 25
loai_nguoi = kiem_tra_tuoi(tuoi_mau)
print(f"Người {tuoi_mau} tuổi thuộc nhóm: {loai_nguoi}")

# Ví dụ 2: Vòng lặp for
# In bảng cửu chương của một số

def in_bang_cuu_chuong(n):
    """
    In bảng cửu chương từ 1 đến 10 của số n
    """
    print(f"\nBảng cửu chương {n}:")
    for i in range(1, 11):  # lặp từ 1 đến 10
        ket_qua = n * i
        print(f"{n} x {i} = {ket_qua}")

print("\n--- Ví dụ 2: Bảng cửu chương ---")
in_bang_cuu_chuong(5)

# Ví dụ 3: Vòng lặp while và danh sách (list)
# Nhập danh sách tên bạn bè và in ra

def nhap_danh_sach_ban_be():
    """
    Hàm nhập danh sách bạn bè cho đến khi người dùng nhập 'xong'
    """
    danh_sach = []  # tạo danh sách rỗng
    print("\n--- Ví dụ 3: Nhập danh sách bạn bè ---")
    print("Nhập tên bạn bè (gõ 'xong' để dừng):")
    
    while True:
        ten = input("Tên bạn: ")
        if ten.lower() == 'xong':
            break
        danh_sach.append(ten)  # thêm tên vào danh sách
    
    print(f"\nDanh sách bạn bè của bạn ({len(danh_sach)} người):")
    for i, ten in enumerate(danh_sach, start=1):
        print(f"{i}. {ten}")

# Gọi hàm (bạn có thể bỏ qua nếu không muốn nhập tay khi test)
# nhap_danh_sach_ban_be()  # Bỏ dấu # để chạy ví dụ 3

# 3. Bài tập nhỏ
# Viết hàm tính tổng các số chẵn từ 1 đến n

def tinh_tong_so_chan(n):
    """
    Tính tổng các số chẵn từ 1 đến n (bao gồm n nếu là chẵn)
    """
    tong = 0
    for i in range(2, n + 1, 2):  # bắt đầu từ 2, bước nhảy 2
        tong += i
    return tong

# Kiểm thử bài tập
print("\n--- Bài tập: Tính tổng số chẵn ---")
so_n = 10
ket_qua_bai_tap = tinh_tong_so_chan(so_n)
print(f"Tổng các số chẵn từ 1 đến {so_n} là: {ket_qua_bai_tap}")

# Gợi ý mở rộng: Viết hàm tính tổng số lẻ, hoặc số chia hết cho 3, v.v.

def main():
    """
    Hàm chính để chạy chương trình
    """
    print("Chào mừng bạn đến với bài học Python cơ bản!")
    
    # Chạy các ví dụ
    tuoi_mau = 25
    print(f"Người {tuoi_mau} tuổi thuộc nhóm: {kiem_tra_tuoi(tuoi_mau)}")
    
    in_bang_cuu_chuong(3)
    
    # Bỏ qua phần nhập tay để chạy tự động
    # nhap_danh_sach_ban_be()
    
    # Bài tập
    print(f"\nBài tập: Tổng chẵn đến 15 = {tinh_tong_so_chan(15)}")
    
    print("\nChúc mừng! Bạn đã hoàn thành bài học cơ bản.")

# Gọi hàm main khi chạy file
if __name__ == "__main__":
    main()
```

---

**Tóm tắt nội dung:**
- Biến và kiểu dữ liệu: `int`, `float`, `str`, `bool`
- Cấu trúc điều kiện: `if`, `elif`, `else`
- Vòng lặp: `for`, `while`
- Hàm: định nghĩa và gọi hàm
- Danh sách: `list`, `append()`, `enumerate()`
- Bài tập: tính tổng số chẵn

**Cách sử dụng:**
- Lưu file với tên `python38_bai_hoc_co_ban.py`
- Chạy bằng lệnh: `python python38_bai_hoc_co_ban.py`