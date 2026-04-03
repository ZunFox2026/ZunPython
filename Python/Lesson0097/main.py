import inspect
import functools

# Ví dụ 1: Trích xuất thông tin tham số của hàm
def greet(name: str, age: int = 25, city: str = "Hà Nội"):
    return f"Xin chào {name}, {age} tuổi, ở {city}"

# Sử dụng inspect để lấy chữ ký hàm
def print_function_signature(func):
    sig = inspect.signature(func)
    print(f"Chữ ký của hàm {func.__name__}:")
    for param_name, param in sig.parameters.items():
        default = param.default if param.default != param.empty else "không có"
        annotation = param.annotation if param.annotation != param.empty else "không có"
        print(f" - {param_name}: kiểu={annotation}, mặc định={default}")

print("=== Ví dụ 1: Trích xuất tham số ===")
print_function_signature(greet)

# Ví dụ 2: Decorator ghi log thông minh sử dụng inspect
def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Lấy thông tin về tham số
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        print(f"[LOG] Gọi hàm {func.__name__} với tham số:")
        for arg_name, arg_value in bound_args.arguments.items():
            print(f"  {arg_name} = {arg_value}")
        
        result = func(*args, **kwargs)
        print(f"[LOG] Kết quả: {result}")
        return result
    
    return wrapper

@log_call
def calculate_area(width, height=10, unit="m"):
    return f"{width * height} {unit}²"

print("\n=== Ví dụ 2: Decorator ghi log thông minh ===")
calculate_area(5, 3, "cm")

calculate_area(4)

# Ví dụ 3: Kiểm tra mã nguồn và stack trace
def show_source_and_stack(func):
    print(f"Mã nguồn của {func.__name__}:")
    print(inspect.getsource(func))
    
    print("Stack trace hiện tại:")
    for frame in inspect.stack()[1:4]:  # Lấy 3 frame đầu
        print(f" - Gọi từ {frame.function} trong file {frame.filename}, dòng {frame.lineno}")

print("\n=== Ví dụ 3: Mã nguồn và Stack trace ===")
def outer():
    def inner():
        show_source_and_stack(greet)
    inner()

outer()