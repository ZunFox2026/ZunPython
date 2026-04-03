import time
import functools

# Ví dụ 1: Đo thời gian thực thi

def do_thoi_gian(func):
    @functools.wraps(func)  # Giữ nguyên thông tin hàm gốc
    def wrapper(*args, **kwargs):
        bat_dau = time.time()
        ket_qua = func(*args, **kwargs)
        ket_thuc = time.time()
        print(f"Hàm {func.__name__} thực thi trong {ket_thuc - bat_dau:.4f} giây")
        return ket_qua
    return wrapper

@do_thoi_gian
def tinh_tong_lap_phuong(n):
    "Tính tổng lập phương từ 1 đến n"
    return sum(i**3 for i in range(1, n+1))

# Ví dụ 2: Kiểm tra quyền truy cập

user_session = {"dang_nhap": True, "vai_tro": "user"}

def can_dang_nhap(func):
    def wrapper(*args, **kwargs):
        if not user_session.get("dang_nhap"):
            return "Lỗi: Cần đăng nhập để thực hiện hành động này."
        return func(*args, **kwargs)
    return wrapper

def can_quan_tri(func):
    def wrapper(*args, **kwargs):
        if not user_session.get("dang_nhap"):
            return "Lỗi: Cần đăng nhập."
        if user_session.get("vai_tro") != "admin":
            return "Lỗi: Cần quyền quản trị."
        return func(*args, **kwargs)
    return wrapper

@can_dang_nhap
def xem_thong_tin_ca_nhan():
    return "Hiển thị thông tin cá nhân..."

@can_quan_tri
def xoa_nguoi_dung(user_id):
    return f"Xóa người dùng có ID: {user_id}"

# Ví dụ 3: Cache đơn giản

def cache(func):
    _cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Tạo khóa từ tham số (chỉ dùng khi tham số là hashable)
        key = str(args) + str(sorted(kwargs.items()))
        if key in _cache:
            print(f"[Cache] Sử dụng giá trị đã lưu cho {func.__name__}")
            return _cache[key]
        
        print(f"[Tính toán] Thực hiện hàm {func.__name__}...")
        ket_qua = func(*args, **kwargs)
        _cache[key] = ket_qua
        return ket_qua
    return wrapper

@cache
def fibonacci(n):
    "Tính số Fibonacci thứ n"
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Chạy các ví dụ
if __name__ == "__main__":
    print("=== Ví dụ 1: Đo thời gian ===")
    ket_qua1 = tinh_tong_lap_phuong(1000)
    print(f"Kết quả: {ket_qua1}\n")
    
    print("=== Ví dụ 2: Kiểm tra quyền truy cập ===")
    print(xem_thong_tin_ca_nhan())  # Thành công
    print(xoa_nguoi_dung(123))       # Thành công vì vai trò là user? Không, cần admin
    
    user_session["vai_tro"] = "admin"
    print(xoa_nguoi_dung(123))       # Bây giờ thành công
    print() 
    
    print("=== Ví dụ 3: Cache ===")
    print(fibonacci(10))
    print(fibonacci(10))  # Lần này dùng cache
