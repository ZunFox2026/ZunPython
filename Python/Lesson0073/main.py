import inspect

def hello(name: str, age: int = 20) -> str:
    """Chào một người với tên và tuổi"""
    return f"Xin chào {name}, {age} tuổi."

def goodbye(name):
    return f"Tạm biệt {name}."

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

# ---------------------- VÍ DỤ 1: In danh sách hàm trong module ----------------------
def print_functions_in_module(module):
    """In ra tất cả các hàm trong một module"""
    print("Các hàm trong module:")
    for name, obj in inspect.getmembers(module, inspect.isfunction):
        print(f" - {name}{inspect.signature(obj)}")

# Gọi ví dụ 1
print_functions_in_module(__name__)
print("\n" + "="*50 + "\n")

# ---------------------- VÍ DỤ 2: Tự động ghi log khi gọi hàm ----------------------
def log_function_call(func, *args, **kwargs):
    """Ghi log khi gọi hàm, bao gồm tham số và giá trị trả về"""
    sig = inspect.signature(func)
    bound_args = sig.bind(*args, **kwargs)
    bound_args.apply_defaults()
    
    print(f"[LOG] Gọi hàm: {func.__name__}")
    print(f"[LOG] Tham số: {dict(bound_args.arguments)}")
    
    result = func(*args, **kwargs)
    print(f"[LOG] Kết quả: {result}")
    return result

# Gọi ví dụ 2
log_function_call(hello, "An", 25)
print("\n" + "="*50 + "\n")

# ---------------------- VÍ DỤ 3: In mã nguồn của các phương thức trong lớp ----------------------
def print_method_sources(cls):
    """In ra mã nguồn của các phương thức trong một lớp"""
    print(f"Mã nguồn các phương thức trong lớp {cls.__name__}:")
    for name, method in inspect.getmembers(cls, inspect.isfunction):
        try:
            source = inspect.getsource(method)
            print(f"\n--- Phương thức: {name} ---")
            print(source.strip())
        except OSError:
            print(f"Không thể lấy mã nguồn của {name}")

# Gọi ví dụ 3
print_method_sources(Calculator)