from typing import Any, Callable, List
import functools
import inspect
import time

# Bài 1: Viết decorator @debug_calls ghi log tên hàm, tham số, và giá trị trả về
def debug_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Lấy thông tin chữ ký hàm
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        # In thông tin gọi hàm
        args_str = ", ".join(
            [f"{k}={v}" for k, v in bound_args.arguments.items()]
        )
        print(f"[DEBUG] Gọi: {func.__name__}({args_str})")
        
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        
        print(f"[DEBUG] Trả về: {result} (thời gian: {duration:.4f}s)")
        
        return result
    return wrapper

# Bài 2: Viết hàm list_public_methods(cls) liệt kê các phương thức công khai
def list_public_methods(cls) -> List[str]:
    # Lấy tất cả thành viên là hàm và tên không bắt đầu bằng '_'
    methods = inspect.getmembers(cls, predicate=inspect.isfunction)
    public_method_names = [
        name for name, func in methods
        if not name.startswith('_')
    ]
    return public_method_names

# Bài 3: Viết decorator @require_kwargs yêu cầu tất cả tham số phải là keyword
def require_kwargs(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Nếu có tham số vị trí (args), ném lỗi
        if args:
            raise TypeError(
                f"Hàm '{func.__name__}' yêu cầu tất cả tham số phải là keyword argument. "
                f"Nhận được {len(args)} tham số vị trí."
            )
        return func(*args, **kwargs)
    return wrapper

# Bài 4: Viết hàm get_caller_info() trả về tên hàm gọi nó và tên file
def get_caller_info():
    # inspect.stack()[1] là frame của hàm gọi hàm hiện tại
    frame = inspect.stack()[1]
    filename = frame.filename
    function_name = frame.function
    return {
        "filename": filename,
        "function_name": function_name
    }

# Bài 5: Viết decorator @log_execution_time ghi log thời gian thực thi và thông tin hàm
def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Lấy thông tin hàm
        module_name = func.__module__
        func_name = func.__name__
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(f"[LOG] Hàm '{module_name}.{func_name}' thực thi trong {execution_time:.4f}s")
        
        return result
    return wrapper