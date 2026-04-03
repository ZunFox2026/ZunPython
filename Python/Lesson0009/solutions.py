# solutions.py - Lời giải bài tập về Module và Package

import os

# --- Bài 1: Tạo module temperature.py ---
temperature_code = """
def celsius_to_fahrenheit(c):
    \"""
    Chuyển đổi nhiệt độ từ độ C sang độ F
    Công thức: F = C * 9/5 + 32
    \"""
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    \"""
    Chuyển đổi nhiệt độ từ độ F sang độ C
    Công thức: C = (F - 32) * 5/9
    \"""
    return (f - 32) * 5/9
"""

# Tạo file temperature.py nếu chưa có
if not os.path.exists('temperature.py'):
    with open('temperature.py', 'w', encoding='utf-8') as f:
        f.write(temperature_code)

# Import và dùng thử
import temperature

c = 37
f = temperature.celsius_to_fahrenheit(c)
print(f"{c}°C = {f}°F")

f_val = 98.6
c_val = temperature.fahrenheit_to_celsius(f_val)
print(f"{f_val}°F = {c_val:.2f}°C")


# --- Bài 2: Tạo package utilities ---
package_dir = 'utilities'
if not os.path.exists(package_dir):
    os.makedirs(package_dir)

# Tạo string_tools.py
string_tools_code = """
def reverse_string(s):
    \"""Đảo ngược chuỗi s"""
    return s[::-1]

def is_palindrome(s):
    \"""Kiểm tra chuỗi có phải đối xứng (palindrome) không"""
    cleaned = s.lower().replace(' ', '')
    return cleaned == cleaned[::-1]
"""

if not os.path.exists(f'{package_dir}/string_tools.py'):
    with open(f'{package_dir}/string_tools.py', 'w', encoding='utf-8') as f:
        f.write(string_tools_code)

# Tạo number_tools.py
number_tools_code = """
def is_even(n):
    \"""Kiểm tra số n có phải số chẵn không"""
    return n % 2 == 0

def factorial(n):
    \"""Tính giai thừa của n"""
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
"""

if not os.path.exists(f'{package_dir}/number_tools.py'):
    with open(f'{package_dir}/number_tools.py', 'w', encoding='utf-8') as f:
        f.write(number_tools_code)

# Tạo __init__.py
init_code = """
# Import để tiện sử dụng
from .string_tools import reverse_string, is_palindrome
from .number_tools import is_even, factorial

__all__ = ['reverse_string', 'is_palindrome', 'is_even', 'factorial']
"""

if not os.path.exists(f'{package_dir}/__init__.py'):
    with open(f'{package_dir}/__init__.py', 'w', encoding='utf-8') as f:
        f.write(init_code)


# --- Bài 3: Sử dụng package utilities ---
from utilities import is_palindrome, is_even, factorial

print("\n--- Bài 3: Sử dụng package utilities ---")

# Kiểm tra chuỗi đối xứng
text = input("Nhập một chuỗi để kiểm tra đối xứng: ")
if is_palindrome(text):
    print(f"'{text}' là chuỗi đối xứng.")
else:
    print(f"'{text}' không phải chuỗi đối xứng.")

# Kiểm tra chẵn/lẻ và tính giai thừa
try:
    num = int(input("Nhập một số nguyên: "))
    
    if is_even(num):
        print(f"{num} là số chẵn.")
    else:
        print(f"{num} là số lẻ.")
    
    fact = factorial(num)
    if fact is None:
        print("Không thể tính giai thừa của số âm.")
    else:
        print(f"Giai thừa của {num} là {fact}.")

except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ.")


# --- Bài 4: Import riêng lẻ ---
from utilities import is_palindrome
from utilities import factorial

print("\n--- Bài 4: Import riêng lẻ ---")
print("is_palindrome('madam') =", is_palindrome('madam'))
print("factorial(5) =", factorial(5))


# --- Bài 5: Xem tài liệu hàm ---
print("\n--- Bài 5: Xem tài liệu các hàm ---")
print("Tài liệu hàm is_palindrome:")
print(is_palindrome.__doc__)

print("\nTài liệu hàm factorial:")
print(factorial.__doc__)

# Hoặc dùng help()
# help(is_palindrome)
# help(factorial)