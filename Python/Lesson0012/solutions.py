# solutions.py - Lời giải Bài 12

# Bài 1: Viết hàm nhập số nguyên, yêu cầu nhập lại nếu sai

def bai_1_nhap_so():
    while True:
        try:
            n = int(input("Nhập một số nguyên: "))
            print(f"Bạn đã nhập: {n}")
            return n
        except ValueError:
            print("Sai rồi! Hãy nhập một số nguyên.")

# Bài 2: Đọc file và đếm số dòng

def bai_2_doc_file_dem_dong(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            so_dong = len(f.readlines())
            print(f"File '{ten_file}' có {so_dong} dòng.")
    except FileNotFoundError:
        print(f"Lỗi: File '{ten_file}' không tìm thấy!")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")

# Bài 3: Tính căn bậc hai

def bai_3_can_bac_hai(x):
    try:
        if x < 0:
            # Gây ra lỗi nếu số âm
            raise ValueError("Không thể tính căn bậc hai của số âm")
        import math
        ket_qua = math.sqrt(x)
        print(f"Căn bậc hai của {x} là {ket_qua}")
        return ket_qua
    except ValueError as ve:
        print(f"Lỗi giá trị: {ve}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")

# Bài 4: Truy cập phần tử danh sách an toàn

def bai_4_truy_cap_phan_tu(danh_sach, chi_so):
    try:
        phan_tu = danh_sach[chi_so]
        print(f"Phần tử tại chỉ số {chi_so} là: {phan_tu}")
        return phan_tu
    except IndexError:
        print(f"Lỗi: Chỉ số {chi_so} vượt quá danh sách (độ dài {len(danh_sach)})!")
    except TypeError:
        print("Lỗi: Chỉ số phải là số nguyên!")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")

# Bài 5: Dùng try-except-else-finally

def bai_5_su_dung_finally(ten_file, du_lieu):
    file_handle = None
    try:
        file_handle = open(ten_file, 'w', encoding='utf-8')
        file_handle.write(du_lieu + "\n")
    except PermissionError:
        print(f"Lỗi: Không có quyền ghi vào file '{ten_file}'!")
    except Exception as e:
        print(f"Lỗi khi ghi file: {e}")
    else:
        print("Ghi dữ liệu thành công!")
    finally:
        if file_handle:
            file_handle.close()
            print("File đã được đóng.")