### BÀI TẬP 1
# Viết decorator @uppercase biến kết quả hàm thành chữ in hoa.
# Áp dụng cho hàm say_hello()

def uppercase(func):
    # TODO: Hoàn thành decorator
    pass

@uppercase
def say_hello(name):
    return f"Xin chào {name}!"


### BÀI TẬP 2
# Viết decorator @retry thử lại hàm 3 lần nếu xảy ra ngoại lệ.

def retry(func):
    # TODO: Hoàn thành decorator
    pass

@retry
def may_fail():
    import random
    if random.choice([True, False]):
        raise Exception("Lỗi ngẫu nhiên!")
    return "Thành công!"


### BÀI TẬP 3
# Viết decorator @cache đơn giản lưu kết quả theo tham số.

def cache(func):
    # TODO: Hoàn thành decorator
    pass

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


### BÀI TẬP 4
# Viết decorator @admin_only chỉ cho phép user tên "admin" thực hiện.

def admin_only(func):
    # TODO: Hoàn thành decorator
    pass

@admin_only
def backup_system(user_name):
    return f"Sao lưu hệ thống bởi {user_name}"


### BÀI TẬP 5
# Viết decorator @validate_types kiểm tra kiểu dữ liệu đầu vào.
# Ví dụ: hàm chỉ nhận int, nếu str thì cảnh báo.

def validate_types(*expected_types):
    # TODO: Hoàn thành decorator
    pass

@validate_types(int, int)
def add_numbers(a, b):
    return a + b