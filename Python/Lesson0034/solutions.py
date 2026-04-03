import time
import functools

# ================== Bài 1: Giới hạn thời gian ==================

def gioi_han_thoi_gian(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        bat_dau = time.time()
        ket_qua = func(*args, **kwargs)
        thoi_gian_chay = time.time() - bat_dau
        
        if thoi_gian_chay > 1:
            print(f"[CẢNH BÁO] Hàm '{func.__name__}' chạy quá 1 giây! (Thời gian: {thoi_gian_chay:.2f}s)")
        
        return ket_qua
    return wrapper

# ================== Bài 2: Kiểm tra lỗi ==================

def kiem_tra_loi(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[LỖI] Hàm '{func.__name__}' gặp lỗi: {str(e)}")
            return None  # hoặc giá trị mặc định
    return wrapper

# ================== Bài 3: Chạy n lần ==================

def chay_n_nhieu_lan(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ket_qua = None
            for i in range(n):
                print(f"Lần chạy thứ {i+1}")
                ket_qua = func(*args, **kwargs)
            return ket_qua
        return wrapper
    return decorator

# ================== Bài 4: Cache kết quả ==================

def cache_ket_qua(func):
    cache = {}  # Dictionary lưu kết quả
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Tạo key từ args và kwargs
        key = str(args) + str(sorted(kwargs.items()))
        
        if key in cache:
            print(f"[CACHE] Sử dụng kết quả đã lưu cho {func.__name__}")
            return cache[key]
        
        # Tính và lưu kết quả
        ket_qua = func(*args, **kwargs)
        cache[key] = ket_qua
        print(f"[TÍNH MỚI] Đã tính kết quả cho {func.__name__}")
        return ket_qua
    
    return wrapper

# ================== Bài 5: Yêu cầu đăng nhập ==================

def yeu_cau_dang_nhap(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Giả định có tham số 'da_dang_nhap' trong kwargs
        if not kwargs.get('da_dang_nhap', False):
            print("[TRUY CẬP BỊ TỪ CHỐI] Bạn cần đăng nhập để thực hiện hành động này.")
            return None
        
        return func(*args, **kwargs)
    return wrapper

# ================== Kiểm thử lời giải ==================
if __name__ == "__main__":
    # Test Bài 1
    @gioi_han_thoi_gian
    def chay_cham():
        time.sleep(1.5)
        return "Xong!"
    
    print("=== Bài 1: Giới hạn thời gian ===")
    chay_cham()
    print()

    # Test Bài 2
    @kiem_tra_loi
    def chia(a, b):
        return a / b
    
    print("=== Bài 2: Kiểm tra lỗi ===")
    chia(10, 2)
    chia(10, 0)  # Sẽ có lỗi nhưng không crash
    print()

    # Test Bài 3
    @chay_n_nhieu_lan(3)
    def xin_chao():
        print("Xin chào từ bài tập!")
    
    print("=== Bài 3: Chạy n lần ===")
    xin_chao()
    print()

    # Test Bài 4
    @cache_ket_qua
    def tinh_phi(n):
        print(f"Tính số Fibonacci thứ {n}...")
        if n < 2:
            return n
        return tinh_phi(n-1) + tinh_phi(n-2)
    
    print("=== Bài 4: Cache kết quả ===")
    print(f"F(5) = {tinh_phi(5)}")
    print(f"F(5) = {tinh_phi(5)}")  # Dùng lại kết quả
    print()

    # Test Bài 5
    @yeu_cau_dang_nhap
    def xoa_tap_tin(ten):
        return f"Đã xóa tập tin {ten}"
    
    print("=== Bài 5: Yêu cầu đăng nhập ===")
    print(xoa_tap_tin("data.txt", da_dang_nhap=True))
    print(xoa_tap_tin("config.txt", da_dang_nhap=False))