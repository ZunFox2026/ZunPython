# solutions.py
# Lời giải bài tập Bài 7: Xử lý chuỗi và file

# --- Bài 1: Đếm số dòng ---

def dem_so_dong(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            # Cách 1: dùng readlines()
            so_dong = len(f.readlines())
            print(f"File '{ten_file}' có {so_dong} dòng.")
    except FileNotFoundError:
        print(f"Không tìm thấy file: {ten_file}")


# --- Bài 2: Tìm và thay thế từ ---

def tim_va_thay_the(ten_file, tu_can_tim, tu_thay_the):
    try:
        # Đọc toàn bộ nội dung
        with open(ten_file, 'r', encoding='utf-8') as f:
            noi_dung = f.read()
        
        # Thay thế từ
        noi_dung_moi = noi_dung.replace(tu_can_tim, tu_thay_the)
        
        # Ghi lại file
        with open(ten_file, 'w', encoding='utf-8') as f:
            f.write(noi_dung_moi)
        
        print(f"Đã thay thế '{tu_can_tim}' bằng '{tu_thay_the}' trong file '{ten_file}'.")
        
    except FileNotFoundError:
        print(f"Không tìm thấy file: {ten_file}")


# --- Bài 3: Lọc email hợp lệ ---

def loc_email_hop_le(ten_file_nhap, ten_file_xuat):
    hop_le = []
    try:
        with open(ten_file_nhap, 'r', encoding='utf-8') as f:
            for dong in f:
                email = dong.strip()  # Loại bỏ khoảng trắng
                # Kiểm tra email hợp lệ đơn giản
                if '@' in email and '.' in email and ' ' not in email:
                    # Kiểm tra có ký tự trước và sau @
                    phan = email.split('@')
                    if len(phan) == 2 and len(phan[0]) > 0 and len(phan[1]) > 0 and '.' in phan[1]:
                        hop_le.append(email)
        
        # Ghi vào file mới
        with open(ten_file_xuat, 'w', encoding='utf-8') as f:
            for email in hop_le:
                f.write(email + '\n')
        
        print(f"Đã lọc và lưu {len(hop_le)} email hợp lệ vào '{ten_file_xuat}'.")
        
    except FileNotFoundError:
        print(f"Không tìm thấy file: {ten_file_nhap}")


# --- Bài 4: Tạo profile ---

def tao_profile():
    print("Nhập thông tin cá nhân:")
    ho_ten = input("Họ tên: ").strip().title()
    tuoi = input("Tuổi: ").strip()
    dia_chi = input("Địa chỉ: ").strip().title()
    so_dien_thoai = input("Số điện thoại: ").strip()
    
    # Ghi vào file
    with open('profile.txt', 'w', encoding='utf-8') as f:
        f.write("=== HỒ SƠ CÁ NHÂN ===\n")
        f.write(f"Họ tên: {ho_ten}\n")
        f.write(f"Tuổi: {tuoi}\n")
        f.write(f"Địa chỉ: {dia_chi}\n")
        f.write(f"Số điện thoại: {so_dien_thoai}\n")
    
    print("Đã tạo hồ sơ thành công! Xem file 'profile.txt'.")


# --- Bài 5: Nối hai file ---

def noi_file(file1, file2, file_moi):
    try:
        with open(file_moi, 'w', encoding='utf-8') as f_moi:
            # Đọc và ghi file 1
            with open(file1, 'r', encoding='utf-8') as f1:
                f_moi.write(f1.read())
            
            # Thêm dấu phân cách
            f_moi.write("\n--- NỐI TIẾP ---\n\n")
            
            # Đọc và ghi file 2
            with open(file2, 'r', encoding='utf-8') as f2:
                f_moi.write(f2.read())
        
        print(f"Đã nối '{file1}' và '{file2}' thành công vào '{file_moi}'.")
        
    except FileNotFoundError as e:
        print(f"Lỗi: Không tìm thấy file {e.filename}")