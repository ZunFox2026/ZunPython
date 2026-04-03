### Bài tập 1: Metaclass kiểm tra thuộc tính version

class VersionRequiredMeta(type):
    def __new__(cls, name, bases, attrs):
        # Kiểm tra xem có thuộc tính 'version' và là int
        if 'version' not in attrs:
            raise TypeError(f"Lớp {name} phải có thuộc tính 'version' kiểu int.")
        if not isinstance(attrs['version'], int):
            raise TypeError(f"'version' trong lớp {name} phải là kiểu int.")
        return super().__new__(cls, name, bases, attrs)

class MyComponent(metaclass=VersionRequiredMeta):
    version = 1


### Bài tập 2: Đăng ký lớp vào registry
class PluginRegistryMeta(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        registry[name] = new_class  # Đăng ký vào từ điển
        return new_class

# Khai báo registry ở module level
registry = {}

class AudioPlugin(metaclass=PluginRegistryMeta):
    pass

class VideoPlugin(metaclass=PluginRegistryMeta):
    pass


### Bài tập 3: Kiểm tra tên lớp bắt đầu bằng chữ hoa
class ValidClassNameMeta(type):
    def __new__(cls, name, bases, attrs):
        if not name[0].isupper():
            raise NameError(f"Tên lớp phải bắt đầu bằng chữ in hoa, nhưng nhận được: {name}")
        return super().__new__(cls, name, bases, attrs)

class MyValidClass(metaclass=ValidClassNameMeta):
    pass

# Nếu mở comment dòng dưới đây sẽ lỗi:
# class invalidClass(metaclass=ValidClassNameMeta):
#     pass


### Bài tập 4: Tự động thêm to_dict cho thuộc tính public
class AutoToDictMeta2(type):
    def __new__(cls, name, bases, attrs):
        # Chỉ thêm nếu lớp chưa định nghĩa to_dict
        if 'to_dict' not in attrs:
            def to_dict(self):
                return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
            attrs['to_dict'] = to_dict
        return super().__new__(cls, name, bases, attrs)

class Product(metaclass=AutoToDictMeta2):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self._id = 123  # không xuất hiện trong to_dict


### Bài tập 5: Metaclass tạo lớp Singleton
class SingletonMeta(type):
    _instances = {}  # Lưu trữ các instance theo lớp

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # Chỉ tạo mới nếu chưa có
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "connected"

# Kiểm tra singleton
# db1 = Database()
# db2 = Database()
# print(db1 is db2)  # True