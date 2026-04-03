import inspect

class Person:
    def __init__(self, name="Người dùng", age=0):
        self.name = name
        self.age = age

    def greet(self):
        return f"Xin chào, tôi là {self.name}"

    def have_birthday(self):
        self.age += 1


class Animal:
    def speak(self):
        return "Động vật kêu!"


####################
# Bài tập 1: Kiểm tra và gọi phương thức nếu tồn tại
def check_and_call_method(obj, method_name):
    # Kiểm tra sự tồn tại của phương thức
    if hasattr(obj, method_name):
        method = getattr(obj, method_name)
        # Kiểm tra xem có phải là callable không
        if callable(method):
            print(f"Gọi phương thức: {method_name}")
            return method()
        else:
            print(f"{method_name} tồn tại nhưng không phải là phương thức.")
            return None
    else:
        print(f"Phương thức {method_name} không tồn tại.")
        return None


####################
# Bài tập 2: Tạo đối tượng từ tên lớp (chuỗi)
def create_instance(class_name):
    # Lấy toàn bộ namespace hiện tại
    globals_dict = globals()
    # Kiểm tra xem tên lớp có tồn tại không
    if class_name in globals_dict:
        cls = globals_dict[class_name]
        # Kiểm tra có phải là kiểu class không
        if inspect.isclass(cls):
            return cls()  # Tạo thể hiện mới
        else:
            print(f"{class_name} không phải là một lớp.")
            return None
    else:
        print(f"Lớp {class_name} không tồn tại.")
        return None


####################
# Bài tập 3: Sao chép đối tượng bằng reflection
def manual_deep_copy(obj):
    # Tạo đối tượng mới cùng lớp
    new_obj = obj.__class__.__new__(obj.__class__)
    
    # Duyệt qua tất cả các thành viên
    for key, value in inspect.getmembers(obj):
        # Chỉ sao chép các thuộc tính dữ liệu, không sao chép phương thức
        if not key.startswith('_') and not inspect.ismethod(value) and not inspect.isfunction(value):
            setattr(new_obj, key, value)
    
    return new_obj


####################
# Bài tập 4: Liệt kê các phương thức public
def list_public_methods(obj):
    methods = []
    # Duyệt qua các thành viên
    for name, value in inspect.getmembers(obj):
        # Kiểm tra có phải là phương thức và không bắt đầu bằng '_'
        if not name.startswith('_') and inspect.ismethod(value):
            methods.append(name)
    return methods


####################
# Bài tập 5: Decorator ghi log tham số đầu vào
def log_args(func):
    def wrapper(*args, **kwargs):
        # Lấy thông tin về tham số của hàm gốc
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        print(f"Hàm '{func.__name__}' được gọi với:")
        for param_name, value in bound_args.arguments.items():
            print(f"  {param_name} = {value}")
        
        # Gọi hàm gốc và trả về kết quả
        return func(*args, **kwargs)
    
    return wrapper


# --- Kiểm thử các bài tập ---
if __name__ == "__main__":
    # Kiểm thử bài 1
    p = Person("Lan", 20)
    print(check_and_call_method(p, 'greet'))
    print(check_and_call_method(p, 'unknown'))
    print('-' * 30)

    # Kiểm thử bài 2
    animal = create_instance('Animal')
    if animal:
        print(animal.speak())
    print('-' * 30)

    # Kiểm thử bài 3
    p1 = Person("Minh", 30)
    p2 = manual_deep_copy(p1)
    print(f"Sao chép: {p2}")
    p2.name = "Sao chép"
    print(f"Gốc: {p1}, Sao chép: {p2}")
    print('-' * 30)

    # Kiểm thử bài 4
    methods = list_public_methods(p)
    print(f"Các phương thức public: {methods}")
    print('-' * 30)

    # Kiểm thử bài 5
    @log_args
    def example_function(x, y=10, mode='normal'):
        return x * y

    result = example_function(5, mode='fast')
    print(f"Kết quả: {result}")