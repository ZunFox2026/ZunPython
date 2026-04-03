import inspect

def hello(name, age=20):
    """Chào một người bằng tên và tuổi"""
    print(f"Xin chào {name}, {age} tuổi.")

# --- Ví dụ 1: Ghi log tham số hàm tự động ---
def log_call(func, *args, **kwargs):
    sig = inspect.signature(func)
    bound_args = sig.bind(*args, **kwargs)
    bound_args.apply_defaults()
    
    print(f"Gọi hàm: {func.__name__}")
    for param_name, value in bound_args.arguments.items():
        print(f"  {param_name} = {value}")

print("=== Ví dụ 1: Ghi log tham số ===")
log_call(hello, "An", 25)

# --- Ví dụ 2: Liệt kê các phương thức của một lớp ---
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def _private_method(self):
        pass

print("\n=== Ví dụ 2: Liệt kê phương thức của lớp ===")
methods = inspect.getmembers(Calculator, predicate=inspect.isfunction)
for name, method in methods:
    if not name.startswith("_"):
        print(f"Phương thức công khai: {name}")

# --- Ví dụ 3: Trích xuất mã nguồn và docstring ---
print("\n=== Ví dụ 3: Trích xuất mã nguồn và docstring ===")
print(f"Docstring của hello: {hello.__doc__}")
print("Mã nguồn của hello:")
print(inspect.getsource(hello))

# --- Ví dụ 4: Kiểm tra call stack ---
def level3():
    print("--- Thông tin ngăn xếp gọi hàm ---")
    for frame_info in inspect.stack():
        filename = frame_info.filename.split('/')[-1]
        print(f"{frame_info.function} gọi từ {filename}:{frame_info.lineno}")

def level2():
    level3()

def level1():
    level2()

print("\n=== Ví dụ 4: Kiểm tra ngăn xếp gọi hàm ===")
level1()
