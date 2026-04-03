import inspect
import functools
import logging

# Cấu hình logging cho ví dụ 2
logging.basicConfig(filename='debug.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# Ví dụ 1: Decorator ghi log tham số hàm
def log_arguments(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Lấy signature của hàm
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        print(f"[LOG] Gọi hàm: {func.__name__}")
        print(f"[LOG] Tham số: {dict(bound_args.arguments)}")
        
        result = func(*args, **kwargs)
        print(f"[LOG] Kết quả: {result}")
        return result
    return wrapper

@log_arguments
def tinh_tong(a, b=0, c=0):
    """Tính tổng 3 số"""
    return a + b + c

# Ví dụ 2: In mã nguồn của các hàm trong một module
def print_function_sources(module):
    """In mã nguồn của tất cả các hàm trong module"""
    print("=== Mã nguồn các hàm trong module ===")
    for name, obj in inspect.getmembers(module, inspect.isfunction):
        if hasattr(obj, '__module__') and obj.__module__ == module.__name__:
            try:
                source = inspect.getsource(obj)
                print(f"Hàm: {name}\n{source}\n")
            except OSError:
                print(f"Không thể lấy mã nguồn của hàm {name}")

# Ví dụ 3: Ghi lại call stack khi có lỗi
def debug_call_stack():
    """In ra các hàm trong call stack"""
    print("--- Call Stack ---")
    for frame_info in inspect.stack()[1:]:  # Bỏ frame hiện tại
        filename = frame_info.filename.split('/')[-1]
        function = frame_info.function
        line = frame_info.lineno
        print(f"  File '{filename}', line {line}, trong {function}")


def outer():
    inner()

def inner():
    debug_call_stack()

# Chạy các ví dụ
if __name__ == "__main__":
    print("Ví dụ 1: Ghi log tham số")
    tinh_tong(5, b=3)
    
    print("\nVí dụ 2: In mã nguồn các hàm")
    print_function_sources(__name__)
    
    print("\nVí dụ 3: Ghi lại call stack")
    outer()