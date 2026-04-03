####################
# Bài tập 1
# Viết decorator @time_logger (nếu chưa làm trong ví dụ)
# Nhưng lần này áp dụng cho hàm có tham số và trả về giá trị.

####################
# Bài tập 2
# Viết decorator @ensure_positive
# Kiểm tra tất cả các tham số kiểu số (int, float) phải > 0
# Nếu có số <= 0 thì báo lỗi

def ensure_positive(func):
    # Gợi ý: Duyệt qua args và kwargs, kiểm tra kiểu và giá trị
    pass

####################
# Bài tập 3
# Viết decorator @memoize để lưu kết quả hàm theo tham số
# Tránh tính toán lại khi gọi hàm với cùng tham số

def memoize(func):
    # Gợi ý: dùng dictionary để lưu (args, kwargs) -> kết quả
    pass

####################
# Bài tập 4
# Viết decorator @admin_required
# Mô phỏng kiểm tra quyền: chỉ cho phép nếu user['role'] == 'admin'

def admin_required(func):
    # Gợi ý: kiểm tra tham số đầu vào là user dict
    pass

####################
# Bài tập 5
# Viết decorator @retry
# Tự động gọi lại hàm nếu có lỗi, tối đa n lần

def retry(max_attempts=3):
    # Gợi ý: dùng vòng lặp và try-except
    pass