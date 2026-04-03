import time
import functools
from datetime import datetime

# Bài tập 1: Chuyển kết quả thành chữ in hoa

def in_hoa(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ket_qua = func(*args, **kwargs)
        if isinstance(ket_qua, str):
            return ket_qua.upper()
        return ket_qua  # Nếu không phải chuỗi, trả về nguyên bản
    return wrapper

# Bài tập 2: Kiểm tra tất cả tham số là số dương

def kiem_tra_so_duong(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Kiểm tra các tham số vị trí
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                print("Lỗi: Tất cả tham số phải là số dương!")
                return None
        # Kiểm tra các tham số từ khóa
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)) or value <= 0:
                print("Lỗi: Tất cả tham số phải là số dương!")
                return None
        return func(*args, **kwargs)
    return wrapper

# Bài tập 3: Ghi log vào file

def ghi_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Ghi vào file log.txt
        thoi_gian = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ten_ham = func.__name__
        # Chuyển tham số thành chuỗi
        args_str = ', '.join(repr(arg) for arg in args)
        kwargs_str = ', '.join(f"{k}={repr(v)}" for k, v in kwargs.items())
        tham_so = ', '.join(filter(None, [args_str, kwargs_str]))
        
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{thoi_gian}] {ten_ham}({tham_so})\n")
        
        return func(*args, **kwargs)
    return wrapper

# Bài tập 4: Giới hạn tần suất gọi hàm (2 giây)

def gioi_han_toc_do(func):
    last_called = [0]  # Dùng list để có thể thay đổi trong closure
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        hien_tai = time.time()
        if hien_tai - last_called[0] < 2:
            print("Đang giới hạn tần suất...")
            return None
        last_called[0] = hien_tai
        return func(*args, **kwargs)
    return wrapper

# Bài tập 5: Bắt ngoại lệ và trả về None

def thu_hoach_ngoai_le(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Lỗi khi thực thi {func.__name__}: {e}")
            return None
    return wrapper

# --- Ví dụ sử dụng ---
if __name__ == "__main__":
    # Test bài 1
    @in_hoa
    def chao_ten(ten):
        return f"xin chào {ten}"
    
    print(chao_ten("An"))  # XIN CHÀO AN

    # Test bài 2
    @kiem_tra_so_duong
    def tinh_binh_phuong(n):
        return n ** 2
    
    print(tinh_binh_phuong(5))   # 25
    print(tinh_binh_phuong(-3))  # Lỗi

    # Test bài 3
    @ghi_log
    def test_log(x, y=10):
        return x + y
    
    test_log(5, y=20)

    # Test bài 4
    @gioi_han_toc_do
    def ham_thu_thach():
        print("Thực thi hàm...")
    
    ham_thu_thach()
    ham_thu_thach()  # Sẽ bị giới hạn nếu chạy ngay sau

    # Test bài 5
    @thu_hoach_ngoai_le
    def chia(a, b):
        return a / b
    
    print(chia(10, 2))  # 5.0
    print(chia(10, 0))   # Lỗi chia cho 0, in thông báo và trả về None