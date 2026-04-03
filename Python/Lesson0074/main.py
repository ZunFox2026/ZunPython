import inspect

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Xin chào, tôi là {self.name}, {self.age} tuổi."

    def have_birthday(self):
        self.age += 1
        return f"{self.name} vừa tròn {self.age} tuổi!"

    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"


# Ví dụ 1: Tự động in tất cả thuộc tính và phương thức của một đối tượng
def print_object_info(obj):
    print(f"Thông tin về đối tượng {type(obj).__name__}:")
    # Lấy tất cả thành viên
    members = inspect.getmembers(obj)
    for name, value in members:
        # Bỏ qua các thuộc tính nội bộ
        if not name.startswith('_'):
            if inspect.ismethod(value) or inspect.isfunction(value):
                print(f"Phương thức: {name}")
            else:
                print(f"Thuộc tính: {name} = {value}")

# Tạo đối tượng và kiểm tra
p = Person("Mai", 25)
print_object_info(p)
print('-' * 40)


# Ví dụ 2: Gọi phương thức theo tên chuỗi
def call_method_if_exists(obj, method_name, *args, **kwargs):
    if hasattr(obj, method_name):
        method = getattr(obj, method_name)
        if callable(method):
            return method(*args, **kwargs)
        else:
            return f"{method_name} tồn tại nhưng không phải là phương thức."
    else:
        return f"Đối tượng không có phương thức {method_name}."

# Kiểm tra gọi phương thức động
print(call_method_if_exists(p, 'greet'))
print(call_method_if_exists(p, 'have_birthday'))
print(call_method_if_exists(p, 'unknown_method'))
print('-' * 40)


# Ví dụ 3: Serialize một đối tượng thành từ điển dùng reflection
def object_to_dict(obj):
    result = {}
    # Lấy tất cả thuộc tính (không phải phương thức)
    for key, value in inspect.getmembers(obj):
        # Chỉ lấy các thuộc tính dữ liệu, bỏ qua phương thức và nội bộ
        if not key.startswith('_') and not inspect.ismethod(value) and not inspect.isfunction(value):
            result[key] = value
    return result

# Chuyển đổi đối tượng thành dict
person_dict = object_to_dict(p)
print("Phiên bản từ điển của đối tượng:")
print(person_dict)
