import inspect

def hello(name, age=20, city='Hanoi'):
    """Chào một người với tên, tuổi và thành phố."""
    print(f'Xin chào {name}, {age} tuổi, đến từ {city}')

def greet_multiple(*names, prefix='Hello'):
    for name in names:
        print(f'{prefix} {name}')

class Animal:
    def __init__(self, species):
        self.species = species

class Dog(Animal):
    def bark(self):
        print('Gau gau!')

# Ví dụ 1: Tự động ghi log tham số đầu vào
def log_arguments(func, args, kwargs):
    sig = inspect.signature(func)
    bound_args = sig.bind(*args, **kwargs)
    bound_args.apply_defaults()
    print(f'=== Gọi hàm {func.__name__} với các tham số:')
    for arg_name, arg_value in bound_args.arguments.items():
        print(f'  {arg_name} = {arg_value}')

# Kiểm thử
print('--- Ví dụ 1: Ghi log tham số ---')
log_arguments(hello, ('An', 25), {'city': 'Da Nang'})

# Ví dụ 2: Tạo tài liệu API tự động
def document_module(module):
    print(f'=== Tài liệu cho module {module.__name__} ===')
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj) and obj.__module__ == module.__name__:
            print(f'\nHàm: {name}')
            print(f'  Docstring: {obj.__doc__}')
            sig = inspect.signature(obj)
            print(f'  Signature: {sig}')

print('\n--- Ví dụ 2: Tài liệu API ---')
document_module(__name__)

# Ví dụ 3: Debug - Xác định ai gọi hàm này
def who_called_me():
    stack = inspect.stack()
    caller_frame = stack[1]  # Frame gọi hàm này
    print(f'Hàm hiện tại: {caller_frame.function}')
    print(f'Được gọi từ file: {caller_frame.filename}')
    print(f'Tại dòng số: {caller_frame.lineno}')

def some_function():
    who_called_me()

print('\n--- Ví dụ 3: Debug stack ---')
some_function()

# Bonus: Kiểm tra mã nguồn
def show_source_code(func):
    print(f'\n--- Mã nguồn của hàm {func.__name__} ---')
    try:
        print(inspect.getsource(func))
    except OSError:
        print('Không thể lấy mã nguồn (hàm built-in hoặc không có source)')

show_source_code(hello)