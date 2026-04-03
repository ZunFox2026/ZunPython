import inspect

def hello(name: str, age: int = 20) -> str:
    """Chào một người với tên và tuổi."""
    return f"Xin chào {name}, {age} tuổi."

def greet_multiple(*names: str, separator: str = ", "):
    """Chào nhiều người cùng lúc."""
    return "Xin chào " + separator.join(names)

# --- Ví dụ 1: Tự động sinh tài liệu từ hàm ---
def generate_function_docs(module):
    """In ra tài liệu của tất cả các hàm trong một module."""
    print("=== Tài liệu tự động sinh cho các hàm ===")
    for name, func in inspect.getmembers(module, inspect.isfunction):
        if func.__doc__:  # Chỉ hiển thị hàm có docstring
            sig = inspect.signature(func)
            print(f"- {name}{sig}")
            print(f"  {func.__doc__.strip()}")
            print()

# --- Ví dụ 2: Ghi log tự động tên hàm và tham số ---
def debug_log(func):
    """Decorator: ghi log khi hàm được gọi."""
    def wrapper(*args, **kwargs):
        # Lấy thông tin về tham số
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        print(f"[DEBUG] Gọi hàm: {func.__name__} với tham số: {dict(bound_args.arguments)}")
        result = func(*args, **kwargs)
        print(f"[DEBUG] {func.__name__} trả về: {result}")
        return result
    return wrapper

@debug_log
def add(a: int, b: int) -> int:
    return a + b

# --- Ví dụ 3: Kiểm tra kiểu tham số tại runtime ---
def type_check(func):
    """Decorator: kiểm tra kiểu tham số dựa trên type hints."""
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        for name, value in bound_args.arguments.items():
            param = sig.parameters[name]
            if param.annotation != inspect.Parameter.empty:
                expected_type = param.annotation
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Tham số '{name}' của hàm {func.__name__} cần là {expected_type}, nhận được {type(value)}"
                    )
        return func(*args, **kwargs)
    return wrapper

@type_check
def multiply(x: float, y: float) -> float:
    return x * y

# Chạy ví dụ
if __name__ == "__main__":
    # Ví dụ 1
    generate_function_docs(__name__)
    
    # Ví dụ 2
    add(3, 5)
    
    # Ví dụ 3
    try:
        print(multiply(2.5, 4.0))  # OK
        print(multiply(2, "abc"))   # Lỗi kiểu
    except TypeError as e:
        print(f"Lỗi kiểu: {e}")