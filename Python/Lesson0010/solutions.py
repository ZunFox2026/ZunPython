# solutions.py
# Lời giải bài tập - Bài 10: Ôn tập và Dự án nhỏ

# Bài 1: Viết hàm tinh_giai_thua(n)
def tinh_giai_thua(n):
    # Nếu n âm, không có giai thừa
    if n < 0:
        return None
    
    # Giai thừa của 0 và 1 là 1
    giai_thua = 1
    for i in range(1, n + 1):
        giai_thua *= i  # Nhân dồn
    return giai_thua

# Bài 2: Viết hàm dem_tu_chuoi(chuoi, tu)
def dem_tu_chuoi(chuoi, tu):
    # Chuyển cả chuỗi và từ cần tìm về chữ thường để so sánh
    chuoi = chuoi.lower()
    tu = tu.lower()
    
    # Tách chuỗi thành danh sách các từ
    cac_tu = chuoi.split()
    
    # Đếm số lần xuất hiện
    dem = 0
    for tu_trong_chuoi in cac_tu:
        # Loại bỏ dấu câu đơn giản (chỉ xét dấu . và ,)
        tu_sach = tu_trong_chuoi.strip(".,")
        if tu_sach == tu:
            dem += 1
    
    return dem

# Bài 3: Viết chương trình đăng nhập đơn giản
def dang_nhap():
    # Số lần thử tối đa
    so_lan_thu = 0
    max_thu = 3
    
    while so_lan_thu < max_thu:
        ten_dang_nhap = input("Nhập tên đăng nhập: ")
        mat_khau = input("Nhập mật khẩu: ")
        
        # Kiểm tra đúng thông tin
        if ten_dang_nhap == "admin" and mat_khau == "123456":
            print("Đăng nhập thành công!")
            return True  # Thoát nếu thành công
        else:
            so_lan_thu += 1
            print(f"Sai thông tin! Bạn còn {max_thu - so_lan_thu} lần thử.")
    
    print("Bạn đã nhập sai quá 3 lần. Khóa đăng nhập.")
    return False

# Bài 4: Viết hàm in_cac_so_le(a, b)
def in_cac_so_le(a, b):
    # Nếu a > b, hoán đổi để đảm bảo a <= b
    if a > b:
        a, b = b, a  # Hoán đổi giá trị
    
    print(f"Các số lẻ từ {a} đến {b} là:")
    for i in range(a, b + 1):
        if i % 2 == 1:  # Kiểm tra số lẻ
            print(i, end=" ")
    print()  # Xuống dòng

# Bài 5: Viết hàm kiem_tra_so_nguyen_to(n)
def kiem_tra_so_nguyen_to(n):
    # Số nhỏ hơn 2 không phải số nguyên tố
    if n < 2:
        return False
    
    # Kiểm tra chia hết từ 2 đến căn bậc hai của n
    import math
    can_bac_hai = int(math.sqrt(n))
    
    for i in range(2, can_bac_hai + 1):
        if n % i == 0:
            return False  # Nếu chia hết thì không phải số nguyên tố
    
    return True  # Nếu không chia hết cho số nào thì là số nguyên tố