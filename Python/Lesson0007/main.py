# main.py
# Bài học 7: Xử lý chuỗi và file

# --- Ví dụ 1: Đếm số từ trong file ---

def dem_so_tu_trong_file(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            noi_dung = f.read()  # Đọc toàn bộ nội dung
            # Tách từ theo khoảng trắng và đếm
            tu = noi_dung.split()
            print(f"File '{ten_file}' có {len(tu)} từ.")
    except FileNotFoundError:
        print(f"Không tìm thấy file: {ten_file}")

# Tạo file tạm để minh họa
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write("Xin chào! Đây là bài học về xử lý chuỗi và file trong Python.\n")
    f.write("Chúng ta sẽ học cách đọc và ghi file, cũng như xử lý văn bản.")

# Gọi hàm đếm từ
dem_so_tu_trong_file('data.txt')


# --- Ví dụ 2: Ghi nhật ký (log) ---

import datetime

def ghi_nhat_ky():
    # Lấy thời gian hiện tại
    thoi_gian = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dong_log = f"[LOG] Chương trình được chạy lúc: {thoi_gian}\n"
    
    # Ghi tiếp vào file log.txt
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(dong_log)
    
    print("Đã ghi nhật ký thành công.")

# Gọi hàm ghi nhật ký
ghi_nhat_ky()


# --- Ví dụ 3: Làm sạch dữ liệu tên ---

def lam_sach_du_lieu_ten():
    # Tạo file đầu vào với dữ liệu bẩn
    with open('ten_ban.txt', 'w', encoding='utf-8') as f:
        f.write("  Nguyễn Văn An  \n")
        f.write("Trần Thị  BÌnh\n")
        f.write("  Lê Minh    Cường  \n")
    
    danh_sach_ten = []
    with open('ten_ban.txt', 'r', encoding='utf-8') as f:
        for dong in f:
            # Làm sạch: bỏ khoảng trắng thừa, viết hoa chữ cái đầu
            ten_sach = dong.strip().title()
            # Chuẩn hóa khoảng trắng giữa các từ
            ten_sach = ' '.join(ten_sach.split())
            danh_sach_ten.append(ten_sach)
    
    # Ghi ra file mới
    with open('ten_sach.txt', 'w', encoding='utf-8') as f:
        for ten in danh_sach_ten:
            f.write(ten + '\n')
    
    print("Đã làm sạch và lưu danh sách tên vào 'ten_sach.txt'")

# Gọi hàm làm sạch dữ liệu
lam_sach_du_lieu_ten()