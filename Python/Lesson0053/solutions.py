import inspect
import logging

# Cấu hình logging cho bài 2
logging.basicConfig(filename='debug.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# Bài 1: In thông tin các phương thức của lớp
def print_class_info(cls):
    """In tên và tham số của tất cả phương thức trong lớp"""
    print(f"Thông tin lớp: {cls.__name__}")
    for name, method in inspect.getmembers(cls, predicate=inspect.isfunction):
        try:
            sig = inspect.signature(method)
            print(f"  Phương thức: {name}{sig}")
        except ValueError:
            print(f"  Phương thức: {name} (không thể lấy signature)")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self, greeting="Xin chào"):
        return f"{greeting}, tôi là {self.name}"

    def have_birthday(self):
        self.age += 1

# Bài 2: Decorator ghi log vào file
def log_calls(func):
    """Decorator ghi tên hàm, tham số, kết quả vào file debug.log"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        result = func(*args, **kwargs)
        
        log_msg = f"Gọi {func.__name__} với {dict(bound_args.arguments)} -> trả về {result}"
        logging.info(log_msg)
        
        return result
    return wrapper

# Bài 3: Tìm các hàm không có docstring
def find_functions_without_docstring(module):
    """Trả về danh sách tên các hàm trong module không có docstring"""
    functions_without_doc = []
    for name, obj in inspect.getmembers(module, inspect.isfunction):
        # Kiểm tra nếu hàm thuộc về module hiện tại
        if obj.__module__ == module:
            if not inspect.getdoc(obj):  # docstring rỗng hoặc không có
                functions_without_doc.append(name)
    return functions_without_doc

# Bài 4: In ra tên hàm đã gọi hàm hiện tại
def who_called_me():
    """In ra tên hàm đã gọi hàm này"""
    stack = inspect.stack()
    if len(stack) >= 2:
        caller_name = stack[1].function
        print(f"Hàm hiện tại được gọi bởi: {caller_name}")
    else:
        print("Không xác định được ai gọi hàm này")

def caller():
    who_called_me()

# Gọi các hàm để kiểm tra
if __name__ == "__main__":
    print_class_info(Person)
    
    @log_calls
    def test_func(x, y=10):
        return x * y
    
    test_func(5, y=3)
    
    print("Hàm không có docstring:", find_functions_without_docstring(__name__))
    
    caller()