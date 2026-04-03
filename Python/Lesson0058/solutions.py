import inspect
from functools import wraps

def hello(name, age=20):
    pass

def greet(*names, prefix="Hi"):
    pass
class Vehicle:
    pass
class Car(Vehicle):
    pass

def print_caller_info():
    # Lấy thông tin stack, phần tử [1] là hàm gọi hàm này
    frame = inspect.stack()[1]
    print(f'Hàm \"{frame.function}\" đã gọi print_caller_info()')
    print(f'Trên file: {frame.filename}')
    print(f'Tại dòng: {frame.lineno}')

def analyze_function(func):
    # Lấy chữ ký của hàm
    sig = inspect.signature(func)
    print(f'Tên hàm: {func.__name__}')
    print('Tham số:')
    for name, param in sig.parameters.items():
        default = param.default if param.default != inspect.Parameter.empty else 'Không có'
        param_type = param.annotation if param.annotation != inspect.Parameter.empty else 'Không xác định'
        print(f'  {name}: kiểu={param_type}, mặc định={default}')

def log_call(func):
    # Decorator ghi log khi gọi hàm
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'[LOG] Đang gọi hàm: {func.__name__}')
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        for arg_name, arg_value in bound_args.arguments.items():
            print(f'  {arg_name} = {arg_value}')
        return func(*args, **kwargs)
    return wrapper

def find_functions_with_default(module):
    # Duyệt các thành viên trong module
    functions_with_default = []
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj) and obj.__module__ == module.__name__:
            sig = inspect.signature(obj)
            for param in sig.parameters.values():
                if param.default != inspect.Parameter.empty:
                    functions_with_default.append(name)
                    break  # Chỉ cần 1 tham số có default là đủ
    return functions_with_default

def get_class_hierarchy(cls):
    # Lấy danh sách kế thừa bằng getmro (Method Resolution Order)
    mro = inspect.getmro(cls)
    print(f'Phân cấp lớp của {cls.__name__}:')
    for i, c in enumerate(mro):
        print(f'  {i+1}. {c.__name__}')