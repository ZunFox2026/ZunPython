# main.py - Các ví dụ minh họa về Module và Package

# --- Ví dụ 1: Sử dụng module đơn giản ---
# Giả sử có file helper.py bên cạnh file này

# Tạo nội dung helper.py nếu chưa có
import os

helper_code = """
def say_hello(name):
    return f\"Xin chào, {name}!\"

def add(a, b):
    return a + b
"""

# Tạo file helper.py nếu chưa tồn tại
if not os.path.exists('helper.py'):
    with open('helper.py', 'w', encoding='utf-8') as f:
        f.write(helper_code)

# Import module helper
import helper

print("--- Ví dụ 1: Sử dụng module ---")
print(helper.say_hello("Minh"))
print("5 + 7 =", helper.add(5, 7))


# --- Ví dụ 2: Sử dụng package ---
# Tạo cấu trúc package my_package nếu chưa có

package_dir = 'my_package'
if not os.path.exists(package_dir):
    os.makedirs(package_dir)

# Tạo file __init__.py
init_code = """# File khởi tạo package
# Có thể để trống hoặc thêm mã khởi tạo
"""
if not os.path.exists(f'{package_dir}/__init__.py'):
    with open(f'{package_dir}/__init__.py', 'w', encoding='utf-8') as f:
        f.write(init_code)

# Tạo module math_ops.py
math_ops_code = """
def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Lỗi: Chia cho 0!"
    return x / y
"""
if not os.path.exists(f'{package_dir}/math_ops.py'):
    with open(f'{package_dir}/math_ops.py', 'w', encoding='utf-8') as f:
        f.write(math_ops_code)

# Tạo module text_utils.py
text_utils_code = """
def to_upper(text):
    return text.upper()

def count_chars(text):
    return len(text)
"""
if not os.path.exists(f'{package_dir}/text_utils.py'):
    with open(f'{package_dir}/text_utils.py', 'w', encoding='utf-8') as f:
        f.write(text_utils_code)

# Import từ package
from my_package import math_ops
from my_package import text_utils

print("\n--- Ví dụ 2: Sử dụng package ---")
print("4 * 6 =", math_ops.multiply(4, 6))
print("10 / 2 =", math_ops.divide(10, 2))
print("Chuyển thành in hoa:", text_utils.to_upper("xin chào python"))
print("Độ dài chuỗi:", text_utils.count_chars("Hello"))


# --- Ví dụ 3: Sử dụng from để import hàm cụ thể ---
print("\n--- Ví dụ 3: Import hàm cụ thể ---")
from helper import say_hello
from my_package.math_ops import multiply

print(say_hello("Lan"))
print("7 * 8 =", multiply(7, 8))


# --- Ví dụ 4: Sử dụng __init__.py để tiện lợi hơn ---
# Sửa file __init__.py để tự động import một số hàm
init_code_updated = """
# Tự động import khi ai đó import my_package
from .math_ops import multiply, divide
from .text_utils import to_upper

# Định nghĩa những gì được export khi dùng from my_package import *
__all__ = ['multiply', 'divide', 'to_upper']
"""

# Cập nhật __init__.py
with open(f'{package_dir}/__init__.py', 'w', encoding='utf-8') as f:
    f.write(init_code_updated)

# Giờ có thể import trực tiếp từ package
from my_package import multiply, to_upper

print("\n--- Ví dụ 4: Dùng __init__.py để rút gọn import ---")
print("5 * 9 =", multiply(5, 9))
print("In hoa:", to_upper("package thật tiện lợi"))