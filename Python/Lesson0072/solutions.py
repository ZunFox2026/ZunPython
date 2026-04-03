import inspect
from functools import wraps

# Bài tập 1: In thông tin lớp
def print_class_info(cls):
    """In ra tất cả phương thức và thuộc tính của một lớp."""
    print(f"Thông tin về lớp: {cls.__name__}")
    members = inspect.getmembers(cls)
    
    for name, obj in members:
        if name.startswith("__") and name.endswith("__"):
            continue  # Bỏ qua các phương thức nội bộ
        if inspect.isfunction(obj) or inspect.ismethod(obj) or inspect.isroutine(obj):
            print(f"  Phương thức: {name}")
        else:
            print(f"  Thuộc tính: {name} = {obj}")

# Bài tập 2: Decorator ghi log
def log_call(func):
    """Decorator ghi log khi hàm được gọi."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Lấy thông tin nơi gọi
        caller_frame = inspect.stack()[1]
        caller_name = caller_frame.function
        caller_line = caller_frame.lineno
        filename = caller_frame.filename
        
        print(f"[LOG] Gọi hàm '{func.__name__}' với args={args}, kwargs={kwargs}")
        print(f"      Từ hàm '{caller_name}' tại dòng {caller_line} trong {filename}")
        
        return func(*args, **kwargs)
    return wrapper

# Bài tập 3: Tìm hàm theo từ khóa trong docstring
def find_functions_by_doc_keyword(module, keyword):
    """Tìm các hàm trong module có từ khóa trong docstring."""
    functions = []
    for name, obj in inspect.getmembers(module, inspect.isfunction):
        doc = inspect.getdoc(obj)
        if doc and keyword.lower() in doc.lower():
            functions.append(name)
    return functions

# Bài tập 4: Decorator kiểm tra kiểu
def validate_types(func):
    """Decorator kiểm tra kiểu tham số dựa trên type hints."""
    sig = inspect.signature(func)
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Gộp args và kwargs thành binding
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        for name, value in bound_args.arguments.items():
            param = sig.parameters[name]
            if param.annotation is not inspect.Parameter.empty:
                expected_type = param.annotation
                # Hỗ trợ kiểu đơn giản như int, str
                if not isinstance(value, expected_type):
                    print(f"Cảnh báo: Tham số '{name}' của hàm '{func.__name__}'" 
                          f"kiểu {type(value).__name__}, kỳ vọng {expected_type.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Bài tập 5: Thông tin người gọi
def get_caller_info():
    """Trả về thông tin về nơi gọi hàm."""
    stack = inspect.stack()
    if len(stack) < 2:
        return None
    caller_frame = stack[1]
    return (caller_frame.function, caller_frame.lineno, caller_frame.filename)