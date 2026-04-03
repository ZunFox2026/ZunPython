import inspect

def hello(name: str, age: int = 0) -> str:
    """Chào một người với tên và tuổi"""
    return f"Xin chào {name}, {age} tuổi!"

def greet_multiple(*names):
    return ", ".join(f"Xin chào {name}" for name in names)

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

# --- Ví dụ 1: Tự động ghi log tên hàm và tham số
def debug_log(func):
    """Decorator dùng inspect để ghi log chi tiết khi gọi hàm"""
    def wrapper(*args, **kwargs):
        # Lấy thông tin chữ ký hàm
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        print(f"[DEBUG] Gọi hàm: {func.__name__}")
        print(f"[DEBUG] Tham số: {dict(bound_args.arguments)}")

        result = func(*args, **kwargs)
        print(f"[DEBUG] Kết quả: {result}\n")
        return result

    return wrapper

@debug_log
def test_function(x, y=10):
    return x * y

# --- Ví dụ 2: Liệt kê tất cả hàm trong một module
def list_functions_in_module(module):
    """In ra tất cả các hàm trong module cùng mã nguồn"""
    print(f"\\n=== Các hàm trong module {module.__name__} ===")
    for name, obj in inspect.getmembers(module, inspect.isfunction):
        print(f"- Hàm: {name}")
        try:
            source = inspect.getsource(obj).strip()
            print(f"  Mã nguồn:\n{source}\n")
        except OSError:
            print("  Không thể lấy mã nguồn.\n")

# --- Ví dụ 3: Gỡ lỗi bằng thông tin stack
def log_caller():
    """In ra thông tin về hàm gọi nó"""
    frame = inspect.currentframe().f_back  # Frame của hàm gọi
    filename = inspect.getfile(frame)
    lineno = frame.f_lineno
    func_name = frame.f_code.co_name
    print(f"[LOG] Được gọi từ hàm '{func_name}' trong file '{filename}', dòng {lineno}")

def problematic_function():
    log_caller()  # In ra ai đã gọi hàm này

# Chạy các ví dụ
if __name__ == "__main__":
    print("=== Ví dụ 1: Debug Log ===")
    test_function(5, 3)
    test_function(2)

    print("\n=== Ví dụ 2: Liệt kê hàm trong module ===")
    list_functions_in_module(__import__('__main__'))

    print("\n=== Ví dụ 3: Thông tin người gọi ===")
    problematic_function()

    print("\n=== Ví dụ thêm: Kiểm tra chữ ký hàm ===")
    sig = inspect.signature(hello)
    print(f"Chữ ký hàm 'hello': {sig}")
    for param in sig.parameters.values():
        print(f"  {param.name}: {param.annotation} (mặc định: {param.default})")