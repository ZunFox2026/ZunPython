# Bài học 9: Module và Package trong Python

## Mục tiêu bài học
- Hiểu được khái niệm module và package trong Python.
- Biết cách tạo và sử dụng module.
- Hiểu cách tổ chức mã nguồn thành package.
- Biết cách sử dụng lệnh `import` để tải module và package.
- Áp dụng được module và package vào các chương trình thực tế.

## Lý thuyết chi tiết

### 1. Module là gì?
- **Module** là một file chứa mã Python (`.py`), có thể chứa các hàm, biến, lớp.
- Mục đích: tái sử dụng mã, tổ chức mã gọn gàng.
- Ví dụ: file `math_utils.py` là một module.

### Cách sử dụng module
Dùng câu lệnh `import` để sử dụng module:
```python
import ten_module
```
Hoặc:
```python
from ten_module import ten_ham
```

### 2. Package là gì?
- **Package** là một thư mục chứa các module, và phải có file `__init__.py` (có thể để trống).
- Giúp tổ chức các module liên quan thành nhóm.
- Ví dụ: thư mục `my_package/` chứa nhiều file `.py`.

### 3. Cách tạo và sử dụng Package
- Tạo thư mục: `my_package/`
- Tạo file `__init__.py` trong thư mục đó.
- Thêm các module như `calculator.py`, `greeting.py`.
- Import từ package:
```python
from my_package import calculator
```

## Ví dụ minh họa

### Ví dụ 1: Tạo và dùng module
Tạo file `helper.py`:
```python
def say_hello(name):
    return f"Xin chào, {name}!"

def add(a, b):
    return a + b
```

Sử dụng trong file chính:
```python
import helper

print(helper.say_hello("An"))
print(helper.add(5, 3))
```

### Ví dụ 2: Tạo package đơn giản
Cấu trúc thư mục:
```
my_package/
    __init__.py
    math_ops.py
    text_utils.py
```

File `math_ops.py`:
```python
def multiply(x, y):
    return x * y
```

File `text_utils.py`:
```python
def to_upper(text):
    return text.upper()
```

Sử dụng:
```python
from my_package import math_ops, text_utils

print(math_ops.multiply(4, 5))
print(text_utils.to_upper("xin chào"))
```

## Bài tập thực hành
1. Tạo một module `temperature.py` với hàm `celsius_to_fahrenheit(c)`.
2. Tạo package `utilities` với 2 module: `string_tools.py` và `number_tools.py`.
3. Viết chương trình sử dụng các module và package vừa tạo.
4. Sử dụng `from ... import ...` để nhập hàm cụ thể.
5. Thử dùng `__init__.py` để xuất các hàm khi import package.

## Tổng kết
- Module giúp chia nhỏ chương trình thành các file dễ quản lý.
- Package giúp tổ chức các module thành nhóm.
- Sử dụng `import` linh hoạt để tái sử dụng mã.
- Đây là nền tảng để viết chương trình Python quy mô lớn.