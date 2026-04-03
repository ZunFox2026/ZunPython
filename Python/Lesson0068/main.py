import inspect
import time
from datetime import datetime

# Ví dụ 1: In tên và tham số của hàm đang gọi


def log_call():
    # Lấy thông tin frame hiện tại
    frame = inspect.currentframe().f_back
    func_name = frame.f_code.co_name
    args_info = inspect.getargvalues(frame)
    print(f"[LOG] Hàm '{func_name}' được gọi với tham số:")
    for arg_name in args_info.args:
        arg_value = args_info.locals[arg_name]
        print(f"  {arg_name} = {arg_value}")


def tinh_tong(a, b, c=0):
    log_call()
    return a + b + c


# Ví dụ 2: Liệt kê tất cả các hàm trong module hiện tại

def liet_ke_ham_trong_module(module):
    print(f"Các hàm trong module '{module.__name__}':")
    for name, obj in inspect.getmembers(module, inspect.isfunction):
        if not name.startswith("_"):  # Bỏ qua các hàm private
            sig = inspect.signature(obj)
            print(f"- {name}{sig}")


# Ví dụ 3: Tự động phát hiện và chạy các hàm test

def test_cong():
    assert 1 + 1 == 2
    print("test_cong: OK")


def test_nhan():
    assert 2 * 3 == 6
    print("test_nhan: OK")


def test_chia_zero():
    try:
        1 / 0
    except ZeroDivisionError:
        print("test_chia_zero: OK")


def chay_cac_test(module):
    print("Đang chạy các test...")
    for name, func in inspect.getmembers(module, inspect.isfunction):
        if name.startswith("test_"):
            try:
                func()
            except Exception as e:
                print(f"{name}: FAILED - {e}")


# Chạy ví dụ
if __name__ == "__main__":
    print("=== Ví dụ 1: Ghi log khi gọi hàm ===")
    tinh_tong(10, 20, c=5)

    print("\n=== Ví dụ 2: Liệt kê hàm trong module ===")
    liet_ke_ham_trong_module(__name__)

    print("\n=== Ví dụ 3: Chạy tự động các test ===")
    chay_cac_test(__name__)
