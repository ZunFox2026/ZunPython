####################
# Bài tập 1
# Viết decorator `in_hoa` chuyển kết quả trả về của hàm (chuỗi) thành chữ in hoa.
# Gợi ý: Dùng .upper()

def in_hoa(func):
    # Viết code tại đây
    pass

# Bài tập 2
# Viết decorator `kiem_tra_so_duong` chỉ cho phép hàm được gọi nếu tất cả tham số là số dương.
# Nếu có tham số <= 0, in ra "Lỗi: Tất cả tham số phải là số dương!" và không gọi hàm.

def kiem_tra_so_duong(func):
    # Viết code tại đây
    pass

# Bài tập 3
# Viết decorator `ghi_log` ghi lại thời gian gọi hàm và tham số vào file log.txt.
# Ghi theo định dạng: [YYYY-MM-DD HH:MM:SS] Tên_hàm(args, kwargs)

def ghi_log(func):
    # Viết code tại đây
    pass

# Bài tập 4
# Viết decorator `gioi_han_toc_do` giới hạn tần suất gọi hàm (chỉ cho phép gọi mỗi 2 giây một lần).
# Nếu gọi quá nhanh, in ra "Đang giới hạn tần suất..."

def gioi_han_toc_do(func):
    # Viết code tại đây
    pass

# Bài tập 5
# Viết decorator `thu_hoach_ngoai_le` bắt mọi ngoại lệ và in ra thông báo, trả về None nếu có lỗi.

def thu_hoach_ngoai_le(func):
    # Viết code tại đây
    pass