from functools import wraps
import time

# --- VÍ DỤ 1: Ghi log với mức độ tùy chọn ---

def log_level(level="INFO"):
    """
    Decorator ghi log với mức độ được chỉ định.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{level}] Đang thực thi {func.__name__}...")
            result = func(*args, **kwargs)
            print(f"[{level}] {func.__name__} hoàn thành.")
            return result
        return wrapper
    return decorator

@log_level("INFO")
def tinh_tong(a, b):
    time.sleep(0.1)  # Giả lập xử lý
    return a + b

@log_level("ERROR")
def chia(a, b):
    if b == 0:
        raise ValueError("Không thể chia cho 0")
    return a / b


# --- VÍ DỤ 2: Giới hạn tần suất gọi hàm (Rate Limiting) ---

def rate_limit(seconds=1):
    """
    Decorator đảm bảo hàm chỉ được gọi sau mỗi `seconds` giây.
    """
    def decorator(func):
        last_called = [0]

        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            if elapsed < seconds:
                print(f"Chờ {seconds - elapsed:.2f}s trước khi gọi lại {func.__name__}")
                time.sleep(seconds - elapsed)
            last_called[0] = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(seconds=2)
def gui_email(noi_dung):
    print(f"[EMAIL] Đã gửi: {noi_dung}")


# --- VÍ DỤ 3: Class-based decorator: Đếm và ghi log ---

class CountAndLog:
    """
    Class decorator: đếm số lần gọi và ghi log.
    """
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"[CALL #{self.count}] Đang gọi {self.func.__name__}")
        start = time.time()
        result = self.func(*args, **kwargs)
        duration = time.time() - start
        print(f"[THỜI GIAN] Thực thi trong {duration:.4f}s")
        return result

@CountAndLog
def ham_tai_su_dung(x, y):
    time.sleep(0.05)
    return x ** y


# --- CHẠY CÁC VÍ DỤ ---
if __name__ == "__main__":
    print("=== VÍ DỤ 1: Log với mức độ ===")
    print(tinh_tong(3, 5))
    try:
        print(chia(10, 2))
    except ValueError as e:
        print("Lỗi:", e)

    print("\n=== VÍ DỤ 2: Rate Limiting ===")
    for i in range(3):
        gui_email(f"Thông báo {i+1}")

    print("\n=== VÍ DỤ 3: Class-based Decorator ===")
    for i in range(2):
        print(ham_tai_su_dung(2, i+5))