import functools
import time

# --- Bài tập 1: Decorator uppercase ---
def uppercase(func):
    """
    Decorator biến kết quả trả về của hàm thành chữ in hoa.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

@uppercase
def say_hello(name):
    return f"Xin chào {name}!"

# --- Bài tập 2: Decorator retry ---
def retry(func):
    """
    Thử lại hàm tối đa 3 lần nếu có lỗi.
    """
    @functools.wraps(func)  # Giữ nguyên metadata của hàm gốc
    def wrapper(*args, **kwargs):
        attempts = 0
        while attempts < 3:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                attempts += 1
                print(f"Lỗi: {e}, thử lại lần {attempts}/3...")
                if attempts == 3:
                    print("Thử lại quá số lần cho phép.")
                    raise
    return wrapper

@retry
def may_fail():
    import random
    if random.choice([True, False]):
        raise Exception("Lỗi ngẫu nhiên!")
    return "Thành công!"

# --- Bài tập 3: Decorator cache ---
def cache(func):
    """
    Lưu kết quả của hàm để tránh tính lại.
    """
    stored = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Tạo khóa từ tham số (chỉ dùng cho tham số hashable)
        key = str(args) + str(sorted(kwargs.items()))
        if key not in stored:
            stored[key] = func(*args, **kwargs)
        return stored[key]
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# --- Bài tập 4: Decorator admin_only ---
def admin_only(func):
    """
    Chỉ cho phép người dùng có tên là "admin".
    """
    @functools.wraps(func)
    def wrapper(user_name, *args, **kwargs):
        if user_name != "admin":
            print(f"Truy cập bị từ chối: {user_name} không phải admin.")
            return None
        return func(user_name, *args, **kwargs)
    return wrapper

@admin_only
def backup_system(user_name):
    return f"Sao lưu hệ thống bởi {user_name}"

# --- Bài tập 5: Decorator validate_types ---
def validate_types(*expected_types):
    """
    Kiểm tra kiểu dữ liệu của các tham số đầu vào.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Kiểm tra kiểu của các tham số vị trí
            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected_type):
                    print(f"Cảnh báo: Tham số thứ {i+1} không phải kiểu {expected_type.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(int, int)
def add_numbers(a, b):
    return a + b