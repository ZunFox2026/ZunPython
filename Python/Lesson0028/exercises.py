# Bài tập 1: Viết hàm chia hai số với xử lý ngoại lệ
# Yêu cầu:
# - Nếu b = 0, bắt ZeroDivisionError
# - Nếu a hoặc b không phải số, bắt TypeError
# - In ra kết quả hoặc thông báo lỗi
# - Không trả về giá trị

def chia_hai_so(a, b):
    # Viết code tại đây
    pass


# Bài tập 2: Đọc danh sách tên từ file
# Yêu cầu:
# - Đọc file và tách các tên theo dấu phẩy
# - Xử lý FileNotFoundError
# - Nếu nội dung rỗng hoặc không có tên, ném ValueError
# - Trả về danh sách tên (đã strip và bỏ phần tử rỗng)

def doc_danh_sach_tu_file(filename):
    # Viết code tại đây
    pass


# Bài tập 3: Kiểm tra mật khẩu với ngoại lệ tùy chỉnh
# Tạo ngoại lệ tùy chỉnh: MatKhauYeuError
# Yêu cầu mật khẩu:
# - Ít nhất 8 ký tự
# - Có ít nhất 1 chữ in hoa
# - Có ít nhất 1 số
# Nếu không, ném ngoại lệ

class MatKhauYeuError(Exception):
    """Ngoại lệ khi mật khẩu không đủ mạnh"""
    pass


def kiem_tra_mat_khau(password):
    # Viết code tại đây
    # Ném MatKhauYeuError nếu không hợp lệ
    # Nếu hợp lệ, in ra "Mật khẩu mạnh!"
    pass