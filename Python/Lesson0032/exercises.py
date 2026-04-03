####################
# BÀI TẬP THỰC HÀNH
####################

# Bài 1: Viết decorator @log_calls để in tên hàm và tham số khi gọi
# Gợi ý: Dùng *args, **kwargs để nhận mọi tham số

def log_calls(func):
    # Viết code tại đây
    pass

# Bài 2: Viết decorator @retry để thử lại hàm nếu lỗi, tối đa 3 lần
# Gợi ý: Dùng vòng lặp và try-except

def retry(func):
    # Viết code tại đây
    pass

# Bài 3: Viết decorator @cache đơn giản để lưu kết quả theo tham số
# Gợi ý: Dùng dictionary để lưu (args, kwargs) -> kết quả

def cache(func):
    # Viết code tại đây
    pass

# Bài 4: Viết decorator @timing_smart chỉ in thời gian nếu > 1 giây
# Gợi ý: Dùng time.time() và kiểm tra điều kiện

def timing_smart(func):
    # Viết code tại đây
    pass

# Bài 5: Viết decorator @ensure_positive kiểm tra tất cả tham số là số dương
# Gợi ý: Duyệt qua args và kwargs, kiểm tra kiểu và giá trị

def ensure_positive(func):
    # Viết code tại đây
    pass