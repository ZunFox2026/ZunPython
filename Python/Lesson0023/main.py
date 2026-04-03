### Bài học 23: Xử lý ngoại lệ và thiết kế chương trình chống lỗi

# Ví dụ 1: Nhập số nguyên an toàn
print("=== Ví dụ 1: Nhập số nguyên an toàn ===")

def nhap_so_nguyen():
    while True:
        try:
            n = int(input("Nhập một số nguyên: "))
            return n
        except ValueError:
            print("Lỗi: Bạn phải nhập một số nguyên!")

# Gọi hàm (bạn có thể bỏ comment để chạy)
# so = nhap_so_nguyen()
# print(f"Bạn đã nhập: {so}")


# Ví dụ 2: Đọc file điểm số học sinh
print("\n=== Ví dụ 2: Đọc file điểm số ===")

def doc_diem_hoc_sinh(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            diem = []
            for dong in f:
                try:
                    # Chuyển từng dòng thành số
                    diem.append(float(dong.strip()))
                except ValueError:
                    print(f"Bỏ qua dòng không hợp lệ: {dong.strip()}")
            return diem
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'")
        return []
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file '{ten_file}'")
        return []

# Gọi hàm (giả sử có file 'diem.txt' trong thư mục)
# diem = doc_diem_hoc_sinh('diem.txt')
# if diem:
#     print(f"Các điểm: {diem}")
#     print(f"Điểm trung bình: {sum(diem)/len(diem):.2f}")


# Ví dụ 3: Chia hai số với ngoại lệ tùy chỉnh
print("\n=== Ví dụ 3: Ngoại lệ tùy chỉnh ===")

class NegativeNumberError(Exception):
    """Ngoại lệ khi số là âm"""
    pass

def chia_so(a, b):
    try:
        if a < 0 or b < 0:
            raise NegativeNumberError("Các số phải không âm")
        if b == 0:
            raise ZeroDivisionError("Không thể chia cho 0")
        
        ket_qua = a / b
        print(f"{a} / {b} = {ket_qua}")
        
    except NegativeNumberError as e:
        print(f"Lỗi số âm: {e}")
    except ZeroDivisionError as e:
        print(f"Lỗi chia 0: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")
    else:
        print("Phép chia thành công!")
    finally:
        print("Hoàn tất xử lý phép chia.")

# Thử các trường hợp
chia_so(10, 2)
chia_so(10, 0)
chia_so(-5, 2)