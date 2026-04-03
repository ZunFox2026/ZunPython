import inspect
from functools import wraps

# Bài tập 1: Liệt kê các hàm trong một module
def list_functions(module):
    """In ra danh sách các hàm trong module cùng với docstring.
    
    Args:
        module: Module Python (ví dụ: math, os, hoặc module tự định nghĩa)
    """
    print(f"=== Các hàm trong module {module.__name__} ===")
    # Lấy tất cả thành viên là hàm
    for name, func in inspect.getmembers(module, inspect.isfunction):
        doc = inspect.getdoc(func)
        if doc:
            print(f"- {name}: {doc.split('.')[0]}...")
        else:
            print(f"- {name}: (Không có mô tả)")

# Bài tập 2: Phân tích một lớp
def analyze_class(cls):
    """In ra thông tin chi tiết về một lớp: tên, các phương thức, thuộc tính, docstring.
    
    Args:
        cls: Lớp Python (class object)
    """
    print(f"=== Phân tích lớp {cls.__name__} ===")
    doc = inspect.getdoc(cls)
    if doc:
        print(f"Docstring: {doc}")
    else:
        print("Docstring: Không có")

    # Lấy các phương thức (hàm)
    methods = inspect.getmembers(cls, inspect.isfunction)
    print(f"Phương thức ({len(methods)}):")
    for name, _ in methods:
        print(f"  - {name}")

    # Lấy các thuộc tính (nếu có)
    # (Chỉ lấy các thuộc tính không phải là hàm)
    attrs = [attr for attr in dir(cls) if not attr.startswith('__') and not callable(getattr(cls, attr))]
    print(f"Thuộc tính ({len(attrs)}): {attrs}")

# Bài tập 3: Decorator ghi log vào file
@wraps
def trace_call(func):
    """Decorator ghi lại tên hàm, tham số và kết quả vào file log.txt."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Lấy thông tin hàm
        func_name = func.__name__
        # Lấy tham số
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        args_str = dict(bound_args.arguments)
        
        # Thực thi hàm
        try:
            result = func(*args, **kwargs)
            result_str = repr(result)
        except Exception as e:
            result_str = f"Exception: {e}"
            raise
        finally:
            # Ghi log vào file
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"[CALL] {func_name}{args_str} -> {result_str}\n")
        
        return result
    return wrapper

# Bài tập 4: Tìm hàm có từ khóa trong docstring
def find_functions_with_keyword(module, keyword):
    """Tìm các hàm trong module có chứa keyword trong docstring.
    
    Returns:
        Danh sách tên hàm (str) thỏa mãn.
    """
    result = []
    for name, func in inspect.getmembers(module, inspect.isfunction):
        doc = inspect.getdoc(func)
        if doc and keyword.lower() in doc.lower():
            result.append(name)
    return result

# Bài tập 5: In call stack
def print_call_stack():
    """In ra toàn bộ call stack hiện tại."""
    print("=== Call Stack hiện tại ===")
    stack = inspect.stack()
    for frame in stack[1:]:  # Bỏ qua chính hàm print_call_stack
        filename = frame.filename.split("\\")[-1]  # Lấy tên file ngắn
        lineno = frame.lineno
        function = frame.function
        print(f"  File '{filename}', line {lineno}, in {function}")

def outer():
    middle()

def middle():
    inner()

def inner():
    print_call_stack()