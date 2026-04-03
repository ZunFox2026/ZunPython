import inspect

# Bài 1: Viết hàm in ra thông tin về hàm gọi nó
def print_caller_info():
    # Gợi ý: dùng inspect.stack()
    pass

def test_caller():
    print_caller_info()

test_caller()  # Gọi để kiểm tra

# Bài 2: Viết decorator @log_calls
# Gợi ý: dùng inspect.signature và bind

def log_calls(func):
    # Viết decorator ở đây
    pass

# Hàm để kiểm tra decorator
@log_calls
def greet(name, greeting="Xin chào"):
    print(f"{greeting}, {name}!")

greet("Mai", "Chào bạn")

greet("Lan")

# Bài 3: Khám phá một module
# Gợi ý: dùng inspect.getmembers, isfunction, isclass
def explore_module(module):
    # In ra các hàm và lớp trong module
    pass

# Kiểm thử với module hiện tại
import sys
explore_module(sys.modules[__name__])

# Bài 4: Kiểm tra kiểu tham số dựa trên type hints
def validate_types(func, *args, **kwargs):
    # Dùng inspect.signature và annotation để kiểm tra kiểu
    # Trả về True nếu đúng kiểu, False nếu sai
    pass

def sample_function(x: int, y: str):
    pass

print(validate_types(sample_function, 10, "abc"))  # True
print(validate_types(sample_function, "xyz", 123))  # False

# Bài 5: Tìm các hàm có docstring trong module
def find_functions_with_docstring(module):
    # Dùng inspect.getmembers và kiểm tra __doc__
    # Trả về danh sách tên hàm có docstring
    pass

# Kiểm thử
functions_with_docs = find_functions_with_docstring(sys.modules[__name__])
print("Các hàm có docstring:", functions_with_docs)
