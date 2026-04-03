import inspect
import functools
from datetime import datetime

# Bài 1: In thông tin chi tiết về hàm
def print_function_info(func):
    """In ra tên, docstring, tham số, kiểu, và giá trị mặc định."""
    print(f"Tên hàm: {func.__name__}")
    
    doc = inspect.getdoc(func)
    if doc:
        print(f"Docstring: {doc}")
    else:
        print("Docstring: Không có")
    
    sig = inspect.signature(func)
    print("Tham số:")
    for name, param in sig.parameters.items():
        annotation = param.annotation if param.annotation != inspect.Parameter.empty else "Không xác định"
        default = param.default if param.default != inspect.Parameter.empty else "Không có"
        print(f"  {name}: kiểu={annotation}, mặc định={default}")

# Bài 2: Decorator kiểm tra kiểu dữ liệu
def validate_types(func):
    """Decorator kiểm tra kiểu dữ liệu tham số dựa trên type hints."""
    sig = inspect.signature(func)
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Gắn các tham số vào chữ ký
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        # Kiểm tra kiểu dữ liệu
        for name, value in bound_args.arguments.items():
            param = sig.parameters[name]
            annotation = param.annotation
            
            # Bỏ qua nếu không có kiểu được chỉ định
            if annotation == inspect.Parameter.empty:
                continue
            
            # Kiểm tra kiểu
            if not isinstance(value, annotation):
                raise TypeError(
                    f"Tham số '{name}' của hàm '{func.__name__}' cần là {annotation}, nhận được {type(value)}"
                )
        
        return func(*args, **kwargs)
    
    return wrapper

# Bài 3: Tìm hàm test trong module
def find_test_functions(module):
    """Tìm các hàm trong module bắt đầu bằng 'test_'"""
    functions = inspect.getmembers(module, predicate=inspect.isfunction)
    test_funcs = [name for name, obj in functions if name.startswith('test_')]
    return test_funcs

# Bài 4: Liệt kê phương thức công khai
def list_public_methods(cls):
    """Trả về danh sách tên các phương thức công khai."""
    methods = inspect.getmembers(cls, predicate=inspect.isfunction)
    public_methods = [name for name, _ in methods if not name.startswith('_')]
    return public_methods

# Bài 5: Decorator ghi log vào file
def log_call(func):
    """Ghi log tên hàm, tham số, kết quả vào file."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Ghi log vào file
        with open('function_calls.log', 'a', encoding='utf-8') as f:
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            arg_str = ", ".join([f"{k}={v}" for k, v in bound_args.arguments.items()])
            
            result = func(*args, **kwargs)
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {func.__name__}({arg_str}) -> {result}\n")
            
        return result
    return wrapper