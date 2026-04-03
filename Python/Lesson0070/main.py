import inspect

def hello(name: str, age: int = 18):
    """Chào một người với tên và tuổi."""
    print(f"Xin chào {name}, bạn {age} tuổi.")

class Calculator:
    def __init__(self, base=0):
        self.base = base

    def add(self, x, y):
        return self.base + x + y

    @staticmethod
    def pi():
        return 3.14159

# --- Ví dụ 1: Kiểm tra thông tin hàm bằng inspect.signature ---
def example_1():
    print("=== Ví dụ 1: Lấy thông tin tham số hàm ===")
    sig = inspect.signature(hello)
    print(f"Chữ ký hàm 'hello': {sig}")
    
    for name, param in sig.parameters.items():
        print(f"- Tham số: {name}, Kiểu: {param.annotation}, Mặc định: {param.default}")

# --- Ví dụ 2: Lấy mã nguồn và thông tin lớp ---
def example_2():
    print("\n=== Ví dụ 2: Lấy mã nguồn và thành viên của lớp ===")
    
    # Lấy mã nguồn của hàm
    print("Mã nguồn của hàm hello:")
    print(inspect.getsource(hello))
    
    # Lấy danh sách thành viên của lớp
    members = inspect.getmembers(Calculator, predicate=inspect.isfunction)
    print("Các phương thức trong Calculator:")
    for name, func in members:
        print(f"- {name}: {func}")

# --- Ví dụ 3: Ghi log tự động tên hàm và tham số gọi ---
def debug_call(func):
    """Decorator ghi log tên hàm và tham số khi gọi"""
    def wrapper(*args, **kwargs):
        # Lấy thông tin từ stack
        frame = inspect.currentframe().f_back
        filename = frame.f_code.co_filename
        lineno = frame.f_lineno
        
        # Lấy thông tin hàm
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        print(f"[DEBUG] Gọi {func.__name__} tại {filename}:{lineno}")
        print(f"  Tham số: {dict(bound_args.arguments)}")
        
        return func(*args, **kwargs)
    return wrapper

@debug_call
def multiply(a, b, debug=False):
    if debug:
        print("Đang thực hiện phép nhân...")
    return a * b

def example_3():
    print("\n=== Ví dụ 3: Decorator debug thông minh ===")
    result = multiply(5, 6, debug=True)
    print(f"Kết quả: {result}")

if __name__ == "__main__":
    example_1()
    example_2()
    example_3()