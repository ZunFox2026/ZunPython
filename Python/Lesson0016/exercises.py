############## Bài tập 1 ##############
# Viết decorator @log_calls để in ra tên hàm và các tham số khi gọi
# Ví dụ: log_calls(func) -> in ra "Gọi hàm func với args=..., kwargs=..."

def log_calls(func):
    # TODO: Viết mã ở đây
    pass

############## Bài tập 2 ##############
# Viết decorator @retry để thử lại hàm nếu gặp lỗi, tối đa 3 lần

def retry(func):
    # TODO: Viết mã ở đây
    pass

############## Bài tập 3 ##############
# Viết decorator @memoize để lưu kết quả hàm, tránh tính toán lại

def memoize(func):
    # TODO: Viết mã ở đây
    pass

############## Bài tập 4 ##############
# Viết decorator @timing có thể dùng cho hàm có tham số
# Gợi ý: kết hợp timer ở ví dụ 1 và memoize cách dùng *args, **kwargs

def timing(func):
    # TODO: Viết mã ở đây
    pass

############## Bài tập 5 ##############
# Viết decorator @ensure_positive kiểm tra tất cả tham số là số dương
# Nếu có tham số <= 0, in ra cảnh báo và không thực hiện hàm

def ensure_positive(func):
    # TODO: Viết mã ở đây
    pass