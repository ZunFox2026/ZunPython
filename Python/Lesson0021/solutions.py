import math
import random

##############
# Bài tập 1 #
##############
def chia_hai_so(a, b):
    """
    Hàm chia a cho b, xử lý lỗi chia cho 0 và kiểu dữ liệu không hợp lệ.
    """
    try:
        ket_qua = a / b
        return ket_qua
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")
        return None
    except TypeError:
        print("Lỗi: Cả a và b phải là số!")
        return None


##############
# Bài tập 2 #
##############
def tinh_trung_binh_file(filename):
    """
    Đọc file chứa các số nguyên, mỗi dòng một số, tính trung bình.
    Xử lý lỗi file không tồn tại, dòng không phải số.
    """
    try:
        danh_sach_so = []
        with open(filename, "r", encoding="utf-8") as f:
            for dong in f:
                dong = dong.strip()
                if dong:  # Bỏ qua dòng trống
                    try:
                        so = int(dong)
                        danh_sach_so.append(so)
                    except ValueError:
                        print(f"Cảnh báo: Dòng '{dong}' không phải số, bỏ qua.")
        
        if len(danh_sach_so) == 0:
            print("Không có số hợp lệ để tính trung bình.")
            return None
        
        trung_binh = sum(danh_sach_so) / len(danh_sach_so)
        return trung_binh
        
    except FileNotFoundError:
        print(f"Lỗi: File '{filename}' không tồn tại.")
        return None
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file '{filename}'.")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None


##############
# Bài tập 3 #
##############
def tinh_can_bac_hai(x):
    """
    Tính căn bậc hai của x.
    Nếu x < 0, báo lỗi.
    """
    try:
        if x < 0:
            raise ValueError("Không thể tính căn bậc hai của số âm.")
        return math.sqrt(x)
    except ValueError as e:
        print(f"Lỗi: {e}")
        return None
    except TypeError:
        print("Lỗi: Giá trị đầu vào phải là số.")
        return None


##############
# Bài tập 4 #
##############
def chon_ten_ngau_nhien():
    """
    Người dùng nhập danh sách tên, ngăn cách dấu phẩy.
    In ra một tên ngẫu nhiên.
    Xử lý trường hợp không nhập gì.
    """
    try:
        danh_sach_nhap = input("Nhập các tên, ngăn cách bởi dấu phẩy: ").strip()
        
        if not danh_sach_nhap:
            raise ValueError("Bạn chưa nhập tên nào.")
        
        danh_sach_ten = [ten.strip() for ten in danh_sach_nhap.split(",") if ten.strip()]
        
        if len(danh_sach_ten) == 0:
            raise ValueError("Danh sách tên rỗng sau khi lọc.")
        
        ten_chon = random.choice(danh_sach_ten)
        print(f"Tên được chọn ngẫu nhiên: {ten_chon}")
        
    except ValueError as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")


##############
# Bài tập 5 #
##############
def doc_danh_sach_tu_file(filename):
    """
    Đọc file, mỗi dòng là một phần tử danh sách.
    Xử lý file không tồn tại và file rỗng.
    """
    try:
        danh_sach = []
        with open(filename, "r", encoding="utf-8") as f:
            for dong in f:
                dong = dong.strip()
                if dong:
                    danh_sach.append(dong)
        
        if len(danh_sach) == 0:
            raise ValueError("File tồn tại nhưng rỗng hoặc chỉ chứa dòng trống.")
        
        return danh_sach
        
    except FileNotFoundError:
        print(f"Lỗi: File '{filename}' không tồn tại.")
        return None
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file '{filename}'.")
        return None
    except ValueError as e:
        print(f"Lỗi: {e}")
        return None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return None