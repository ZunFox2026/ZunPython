import inspect
import time

# Bài tập 1: Viết hàm in ra tên và giá trị các tham số trong hàm gọi nó

def in_tham_so():
    # Lấy frame trước đó (hàm gọi hàm này)
    frame = inspect.currentframe().f_back
    # Lấy tên các tham số và giá trị tương ứng
    args, _, _, values = inspect.getargvalues(frame)
    print("Các tham số đầu vào:")
    for arg in args:
        print(f"  {arg} = {values[arg]}")


def ham_thu(a, b, c="mac_dinh"):
    in_tham_so()


# Bài tập 2: Viết hàm in ra tất cả các lớp trong một module

def liet_ke_lop(module):
    print(f"Các lớp trong module '{module.__name__}':")
    # Duyệt qua tất cả thành viên của module, lọc ra các lớp
    for name, obj in inspect.getmembers(module, inspect.isclass):
        # Bỏ qua các lớp hệ thống (bắt đầu bằng '_')
        if not name.startswith("_"):
            print(f"- {name}")


class LopA:
    pass

class LopB:
    pass


# Bài tập 3: Tạo decorator ghi log tên hàm và thời gian thực thi

def thoi_gian_thuc_thi(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"[LOG] Bắt đầu thực thi hàm '{func.__name__}' tại {time.strftime('%H:%M:%S')}")
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[LOG] Kết thúc hàm '{func.__name__}' sau {end - start:.4f} giây")
        return result
    return wrapper


# Bài tập 4: Liệt kê các phương thức public của một lớp

def liet_ke_phuong_thuc_public(cls):
    print(f"Các phương thức public của lớp '{cls.__name__}':")
    # Lấy tất cả thành viên là hàm và không bắt đầu bằng '_'
    for name, method in inspect.getmembers(cls, inspect.isfunction):
        if not name.startswith("_"):
            print(f"- {name}")

class MauLop:
    def cong(self, a, b):
        return a + b

    def _rieng_tu(self):
        pass

    def __duoc_bao_ve(self):
        pass


# Bài tập 5: Tìm các hàm bắt đầu bằng 'test_' trong module hiện tại

def tim_ham_test(module):
    print("Các hàm test tìm thấy:")
    # Lấy tất cả hàm trong module
    for name, func in inspect.getmembers(module, inspect.isfunction):
        if name.startswith("test_"):
            print(f"- {name}")


def test_tinh_tong():
    assert 2 + 3 == 5


def test_khong_lam_gi():
    pass
