import math

# Bài tập 1
def tinh_can_bac_hai(x):
    """
    Tính căn bậc hai của x, kiểm tra điều kiện đầu vào
    """
    try:
        if not isinstance(x, (int, float)):
            raise TypeError("Đầu vào phải là một số!")
        if x < 0:
            raise ValueError("Không thể tính căn bậc hai của số âm!")
        return math.sqrt(x)
    except (TypeError, ValueError) as e:
        print(f"Lỗi: {e}")
        return None

# Bài tập 2
def doc_file():
    """
    Đọc file do người dùng nhập tên
    """
    ten_file = input("Nhập tên file để đọc: ")
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            print("Nội dung file:")
            print(f.read())
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'!")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")

# Bài tập 3
def chuyen_doi_chuoi_sang_so(s):
    """
    Chuyển chuỗi sang số nguyên, nếu lỗi thì trả về 0
    """
    try:
        return int(s)
    except ValueError:
        print(f"'{s}' không thể chuyển thành số. Trả về 0.")
        return 0

# Bài tập 4
def rut_tham_trung_thuong():
    """
    Mô phỏng rút thăm trúng thưởng với kiểm tra đầu vào
    """
    for lan in range(3):
        try:
            tien = float(input(f"Nhập số tiền cược (lần {lan+1}/3): "))
            if tien <= 0:
                print("Số tiền phải lớn hơn 0. Vui lòng thử lại.")
                continue
            print(f"Cược thành công với {tien} VNĐ. Chúc bạn may mắn!")
            return
n        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")
    
    print("Hủy phiên cược do nhập sai quá nhiều lần.")

# Bài tập 5
class SoAmError(Exception):
    """
    Ngoại lệ tùy chỉnh cho số âm
    """
    pass

def kiem_tra_so_duong(n):
    """
    Kiểm tra số dương, ném lỗi nếu không
    """
    if n <= 0:
        raise SoAmError("Số phải dương!")
    return True

# Demo bài tập 5
try:
    kiem_tra_so_duong(-5)
except SoAmError as e:
    print(f"Lỗi: {e}")