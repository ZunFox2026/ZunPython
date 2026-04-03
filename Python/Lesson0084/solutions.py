import inspect

class SampleClass:
    """Một lớp mẫu để kiểm thử."""
    
    def method_a(self, x, y=10):
        """Phương thức A với tham số mặc định."""
        return x + y

    def method_b(self, *args, **kwargs):
        """Phương thức B nhận args và kwargs."""
        return len(args) + len(kwargs)

# Bài tập 1: Phân tích lớp
def analyze_class(cls):
    """Phân tích một lớp và in thông tin chi tiết về các phương thức."""
    print(f"Phân tích lớp: {cls.__name__}")
    print(f"Docstring của lớp: {cls.__doc__ or 'Không có'}")
    
    # Lấy các phương thức
    methods = inspect.getmembers(cls, predicate=inspect.isfunction)
    
    for name, method in methods:
        print(f"\n--- Phương thức: {name} ---")
        print(f"Docstring: {method.__doc__ or 'Không có'}")
        sig = inspect.signature(method)
        print(f"Chữ ký: {sig}")

# Bài tập 2: Ghi lại người gọi
def log_caller():
    """In ra tên hàm đang gọi và tên hàm gọi nó."""
    stack = inspect.stack()
    current_func = stack[0].function  # Hàm hiện tại
    caller_func = stack[1].function  # Hàm gọi hàm hiện tại
    print(f"Hàm '{current_func}' đang được gọi bởi hàm '{caller_func}'")

def test_log():
    log_caller()

# Bài tập 3: Lấy thông tin hàm
def get_function_info(func):
    """Trả về thông tin chi tiết về một hàm."""
    sig = inspect.signature(func)
    params = sig.parameters
    
    # Đếm số tham số
    num_params = len(params)
    
    # Kiểm tra *args và **kwargs
    has_var_args = any(p.kind == inspect.Parameter.VAR_POSITIONAL for p in params.values())
    has_var_kwargs = any(p.kind == inspect.Parameter.VAR_KEYWORD for p in params.values())
    
    return {
        "name": func.__name__,
        "docstring": func.__doc__,
        "num_parameters": num_params,
        "has_var_args": has_var_args,
        "has_var_kwargs": has_var_kwargs
    }

# Chạy thử nghiệm
if __name__ == "__main__":
    print("=== Bài tập 1 ===")
    analyze_class(SampleClass)
    
    print("\n=== Bài tập 2 ===")
    test_log()
    
    print("\n=== Bài tập 3 ===")
    info = get_function_info(SampleClass.method_a)
    print(info)
    info2 = get_function_info(SampleClass.method_b)
    print(info2)