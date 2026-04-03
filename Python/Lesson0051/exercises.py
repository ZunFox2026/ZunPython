import inspect

class Calculator:
    """Một lớp máy tính đơn giản."""
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result


def greet(name, title="Thưa ông/bà"):
    """Hàm chào hỏi."""
    print(f"{title} {name}, chào bạn!")


def goodbye(name, time="tối"): 
    """Hàm chia tay."""
    print(f"Tạm biệt {name}, chúc bạn một buổi {time} tốt lành!")

# Bài tập 1: Viết hàm log_call để in ra tên hàm và tham số
# Gợi ý: Dùng inspect.stack() để lấy tên hàm gọi

def log_call():
    # TODO: Hoàn thành hàm này
    pass

# Bài tập 2: Viết hàm in thông tin về một lớp

def print_class_info(cls):
    # TODO: In ra tất cả phương thức và thuộc tính của lớp
    pass

# Bài tập 3: Viết hàm tìm tất cả hàm trong một module

def find_functions_in_module(module):
    # TODO: Trả về danh sách tên các hàm trong module
    pass

# Bài tập 4: Viết decorator @debug_calls sử dụng inspect

def debug_calls(func):
    # TODO: Trả về hàm bao bọc in ra thông tin khi gọi
    pass