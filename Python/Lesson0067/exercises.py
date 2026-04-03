from typing import Any, Callable
import functools
import inspect
import time

# Bài 1: Viết decorator @debug_calls ghi log tên hàm, tham số, và giá trị trả về
def debug_calls(func):
    # TODO: Hoàn thiện decorator
    pass

# Bài 2: Viết hàm list_public_methods(cls) liệt kê các phương thức công khai
# (không bắt đầu bằng '_') của một lớp
def list_public_methods(cls):
    # TODO: Trả về danh sách tên phương thức công khai
    pass

# Bài 3: Viết decorator @require_kwargs yêu cầu tất cả tham số phải là keyword
# Nếu có tham số được truyền theo vị trí (positional), ném TypeError
def require_kwargs(func):
    # TODO: Kiểm tra cách truyền tham số
    pass

# Bài 4: Viết hàm get_caller_info() trả về tên hàm gọi nó và tên file
def get_caller_info():
    # TODO: Dùng inspect.stack() để lấy thông tin người gọi
    pass

# Bài 5: Viết decorator @log_execution_time ghi log thời gian thực thi và thông tin hàm
def log_execution_time(func):
    # TODO: Đo thời gian và in ra thông tin
    pass