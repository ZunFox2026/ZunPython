import inspect

class Sample:
    def __init__(self, x=10):
        self.x = x

    def method_a(self, a, b=5):
        pass

    def method_b(self, msg="Hello"):
        pass

    def _private(self):
        pass

###############
# Bài tập 1 #
###############
def safe_call_method(obj, method_name):
    """
    Kiểm tra và gọi phương thức của đối tượng nếu tồn tại và có thể gọi.
    Nếu không, trả về None.
    """
    if hasattr(obj, method_name):
        method = getattr(obj, method_name)
        if callable(method):
            return method()
    return None

###############
# Bài tập 2 #
###############
def list_public_methods(cls):
    """
    Trả về danh sách tên các phương thức công khai của một lớp (không bắt đầu bằng _)
    """
    methods = []
    for name, obj in inspect.getmembers(cls, predicate=inspect.isfunction):
        if not name.startswith('_'):
            methods.append(name)
    return methods

###############
# Bài tập 3 #
###############
def print_function_signature(func):
    """
    In ra thông tin chi tiết về tham số của hàm: tên, kiểu (nếu có), giá trị mặc định.
    """
    sig = inspect.signature(func)
    print(f"Hàm: {func.__name__}")
    for name, param in sig.parameters.items():
        default = param.default if param.default != param.empty else "Không có"
        annotation = param.annotation if param.annotation != param.empty else "Không rõ"
        print(f"  Tham số: {name}, Kiểu: {annotation}, Mặc định: {default}")

###############
# Bài tập 4 #
###############
def log_call(func):
    """
    Decorator: in ra tên hàm và các tham số đầu vào khi hàm được gọi.
    """
    def wrapper(*args, **kwargs):
        # Lấy signature để liên kết args với tên tham số
        sig = inspect.signature(func)
        try:
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            print(f"[LOG] Gọi hàm '{func.__name__}' với tham số: {dict(bound_args.arguments)}")
        except Exception as e:
            print(f"[LOG] Gọi hàm '{func.__name__}' với args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

# --- Kiểm thử lời giải ---
if __name__ == "__main__":
    obj = Sample()
    
    print("Bài 1:", safe_call_method(obj, "method_a"))
    print("Bài 2:", list_public_methods(Sample))
    
    print("\nBài 3:")
    print_function_signature(Sample.method_a)
    
    print("\nBài 4:")
    @log_call
    def test(a, b=2):
        return a + b
    
    test(3, b=4)