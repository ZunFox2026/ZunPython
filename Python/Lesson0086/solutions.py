import inspect

####################
# solutions.py
# Lời giải bài tập lập trình phản xạ
####################

def call_method(obj, method_name, *args):
    """
    Gọi phương thức method_name trên đối tượng obj với các tham số *args.
    Nếu phương thức không tồn tại hoặc không thể gọi, trả về None.
    """
    if hasattr(obj, method_name):
        method = getattr(obj, method_name)
        if callable(method):
            return method(*args)
    return None

def find_classes_in_module(module, base_class):
    """
    Tìm tất cả các lớp trong module kế thừa từ base_class (trừ chính base_class).
    Trả về danh sách các class.
    """
    classes = []
    for name, obj in inspect.getmembers(module):
        # Kiểm tra có phải là class, kế thừa base_class, và không phải chính base_class
        if inspect.isclass(obj) and issubclass(obj, base_class) and obj != base_class:
            classes.append(obj)
    return classes

def safe_get(obj, attr_path, default=None):
    """
    Lấy giá trị từ thuộc tính lồng nhau theo đường dẫn chuỗi.
    Ví dụ: safe_get(user, 'profile.theme', 'dark')
    """
    attrs = attr_path.split('.')
    current = obj
    for attr in attrs:
        if hasattr(current, attr):
            current = getattr(current, attr)
        else:
            return default  # Không tìm thấy thuộc tính
    return current

def log_calls(func):
    """
    Decorator: in ra tên hàm đã gọi hàm được trang trí.
    Sử dụng inspect.stack() để lấy thông tin.
    """
    def wrapper(*args, **kwargs):
        # inspect.stack()[1] là hàm gọi hàm hiện tại
        caller_name = inspect.stack()[1].function
        print(f"[LOG] Hàm '{func.__name__}' được gọi bởi hàm '{caller_name}'")
        return func(*args, **kwargs)
    return wrapper

class Plugin:
    """Base class cho plugin"""
    def execute(self):
        raise NotImplementedError

class DataPlugin(Plugin):
    def execute(self):
        return "Xử lý dữ liệu"

class ReportPlugin(Plugin):
    def execute(self):
        return "Tạo báo cáo"

def load_plugins():
    """
    Tự động tìm tất cả các lớp kế thừa từ Plugin trong module hiện tại
    và trả về danh sách các instance.
    """
    import sys
    current_module = sys.modules[__name__]
    plugins = []
    # Tìm các class kế thừa Plugin
    for name, obj in inspect.getmembers(current_module):
        if inspect.isclass(obj) and issubclass(obj, Plugin) and obj != Plugin:
            instance = obj()
            plugins.append(instance)
    return plugins