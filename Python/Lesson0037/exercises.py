### Bài tập 1: Viết hàm chia an toàn
def chia_so_an_toan(a, b):
    # Viết mã xử lý ngoại lệ: ZeroDivisionError, TypeError, và các lỗi khác
    # In kết quả hoặc thông báo lỗi
    # Dùng else và finally
    pass

### Bài tập 2: Đọc danh sách số từ file
def doc_danh_sach_so(ten_file):
    # Đọc file, mỗi dòng là một số
    # Xử lý: file không tồn tại, lỗi định dạng số (ValueError), v.v.
    # Trả về danh sách số hợp lệ hoặc in thông báo
    pass

### Bài tập 3: Lớp Student với kiểm tra điểm
# Tạo lớp ngoại lệ InvalidGradeError
# Tạo lớp Student với phương thức them_diem(grade)
# Nếu điểm < 0 hoặc > 10 -> ném ngoại lệ

### Bài tập 4: Mở file an toàn với finally
def mo_file_va_doc(ten_file):
    # Mở file, đọc nội dung
    # Đảm bảo file luôn được đóng bằng finally
    # Xử lý các lỗi có thể xảy ra
    pass

### Bài tập 5: Kiểm tra độ tuổi với ngoại lệ tùy chỉnh
class AgeLimitError(Exception):
    # Tạo ngoại lệ với thông báo tùy chỉnh
    pass
def kiem_tra_dang_ky(age):
    # Nếu tuổi < 18 hoặc > 65 -> ném AgeLimitError
    # In thông báo đăng ký thành công nếu hợp lệ
    pass