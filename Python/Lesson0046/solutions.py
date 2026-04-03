import inspect
import math

def exercise_1():
    """Hàm ghi log tự động khi gọi hàm"""
    def log_call(func):
        def wrapper(*args, **kwargs):
            # Lấy chữ ký hàm
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            # In thông tin gọi hàm
            print(f"[LOG] Gọi hàm: {func.__name__}")
            print(f"[LOG] Tham số: {dict(bound_args.arguments)}")

            # Gọi hàm và lấy kết quả
            result = func(*args, **kwargs)
            print(f"[LOG] Kết quả: {result}")

            return result
        return wrapper

    # Thử nghiệm
    @log_call
    def add(a, b=10):
        """Cộng hai số"""
        return a + b

    add(5)
    add(3, 7)


def exercise_2():
    """Kiểm tra tính toàn vẹn của lớp"""
    def validate_class(cls):
        errors = []

        # Kiểm tra có __init__
        if not hasattr(cls, '__init__'):
            errors.append("Thiếu phương thức __init__")
        else:
            init_method = getattr(cls, '__init__')
            if not callable(init_method):
                errors.append("__init__ không phải là phương thức")

        # Kiểm tra các phương thức public có docstring
        methods = inspect.getmembers(cls, predicate=inspect.isfunction)
        for name, method in methods:
            if not name.startswith('_'):  # Chỉ kiểm tra phương thức public
                if not method.__doc__:
                    errors.append(f"Phương thức '{name}' thiếu docstring")

        return errors

    # Thử nghiệm
    class ValidClass:
        def __init__(self, value):
            """Khởi tạo với giá trị"""
            self.value = value

        def show(self):
            """Hiển thị giá trị"""
            return self.value

    class InvalidClass:
        def __init__(self, x):
            self.x = x

        def calc(self):  # Thiếu docstring
            return self.x * 2

    print("Lỗi trong ValidClass:", validate_class(ValidClass))
    print("Lỗi trong InvalidClass:", validate_class(InvalidClass))


def exercise_3():
    """Phân tích một module"""
    def analyze_module(module):
        functions = []
        classes = []
        constants = []

        # Lấy tất cả thành viên của module
        for name, obj in inspect.getmembers(module):
            if name.startswith('_'):  # Bỏ qua nội bộ
                continue
            if inspect.isfunction(obj):
                functions.append(name)
            elif inspect.isclass(obj):
                classes.append(name)
            else:
                # Coi là hằng số nếu là kiểu dữ liệu cơ bản
                if isinstance(obj, (int, float, str, bool, type(None))):
                    constants.append(name)

        print(f"Module {module.__name__}")
        print(f"- Hàm ({len(functions)}):", functions)
        print(f"- Lớp ({len(classes)}):", classes)
        print(f"- Hằng số ({len(constants)}):", constants)

    # Thử nghiệm với module math
    analyze_module(math)


def exercise_4():
    """Tạo instance từ tên lớp"""
    def create_instance_by_name(class_name, *args, **kwargs):
        # Lấy tất cả đối tượng toàn cục
        for name, obj in globals().items():
            if name == class_name and inspect.isclass(obj):
                return obj(*args, **kwargs)
        return None  # Không tìm thấy

    # Định nghĩa một lớp để thử
    class Dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __repr__(self):
            return f"Dog(name='{self.name}', age={self.age})"

    # Thử tạo instance
    dog = create_instance_by_name("Dog", "Lucky", 3)
    print("Instance tạo được:", dog)

    # Thử với tên sai
    invalid = create_instance_by_name("Cat")
    print("Tạo Cat:", invalid)

if __name__ == "__main__":
    print("=== Bài tập 1 ===")
    exercise_1()
    
    print("\n=== Bài tập 2 ===")
    exercise_2()
    
    print("\n=== Bài tập 3 ===")
    exercise_3()
    
    print("\n=== Bài tập 4 ===")
    exercise_4()
