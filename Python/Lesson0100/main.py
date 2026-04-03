import inspect
import functools

# Ví dụ 1: Lấy thông tin chi tiết về một hàm

def tinh_tong(a: int, b: int = 0) -> int:
    """Tính tổng hai số nguyên"""
    return a + b

def vi_du_1():
    print("=== Ví dụ 1: Phân tích hàm bằng inspect.signature ===")
    sig = inspect.signature(tinh_tong)
    print(f"Tên hàm: tinh_tong")
    print(f"Chữ ký: {sig}")
    
    for name, param in sig.parameters.items():
        print(f" - Tham số: {name}")
        print(f"   - Kiểu: {param.annotation if param.annotation != inspect.Parameter.empty else 'Không xác định'}")
        print(f"   - Giá trị mặc định: {param.default if param.default != inspect.Parameter.empty else 'Không có'}")
    
    print(f"Kiểu trả về: {sig.return_annotation if sig.return_annotation != inspect.Signature.empty else 'Không xác định'}")

# Ví dụ 2: Tạo decorator ghi log thông minh với inspect

def log_thong_minh(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Lấy thông tin về nơi gọi hàm
        frame = inspect.currentframe().f_back
        filename = inspect.getframeinfo(frame).filename
        line_number = frame.f_lineno
        
        # Lấy danh sách tham số của hàm gốc
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        print(f"[LOG] Gọi hàm '{func.__name__}'")
        print(f"      Tại: {filename}:{line_number}")
        print(f"      Với tham số: {dict(bound_args.arguments)}")
        
        result = func(*args, **kwargs)
        print(f"      Kết quả: {result}")
        return result
    return wrapper

def vi_du_2():
    print("\n=== Ví dụ 2: Decorator ghi log thông minh ===")
    
    @log_thong_minh
    def chia(a, b):
        if b == 0:
            raise ValueError("Không thể chia cho 0")
        return a / b
    
    try:
        chia(10, 2)
        chia(5, 0)
    except ValueError as e:
        print(f"Lỗi: {e}")

# Ví dụ 3: Kiểm tra tất cả phương thức trong một lớp

class MayTinh:
    def cong(self, x, y):
        return x + y

    def tru(self, x, y):
        return x - y

    def nhan(self, x, y):
        return x * y

    def chia(self, x, y):
        return x / y if y != 0 else None

    def _noi_bo(self):
        pass  # Phương thức riêng

    def __str__(self):
        return "Máy tính đơn giản"

def vi_du_3():
    print("\n=== Ví dụ 3: Liệt kê các phương thức công khai của lớp ===")
    obj = MayTinh()
    
    # Lấy tất cả thành viên, lọc ra các phương thức công khai
    members = inspect.getmembers(obj, predicate=inspect.ismethod)
    public_methods = [name for name, method in members if not name.startswith('_')]
    
    print(f"Các phương thức công khai của lớp MayTinh:")
    for method_name in public_methods:
        method = getattr(obj, method_name)
        sig = inspect.signature(method)
        print(f" - {method_name}{sig}")

if __name__ == "__main__":
    vi_du_1()
    vi_du_2()
    vi_du_3()