# main.py - Bài học 22: Xử lý ngoại lệ

# Ví dụ 1: Xử lý chia cho 0
def vi_du_chia_hai_so():
    print("=== Ví dụ 1: Xử lý chia cho 0 ===")
    try:
        a = int(input("Nhập số a: "))
        b = int(input("Nhập số b: "))
        ket_qua = a / b
        print(f"a / b = {ket_qua}")
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")

# Ví dụ 2: Đọc file an toàn
def vi_du_doc_file():
    print("\n=== Ví dụ 2: Đọc file an toàn ===")
    try:
        with open("data.txt", "r", encoding="utf-8") as f:
            content = f.read()
            print("Nội dung file:")
            print(content)
    except FileNotFoundError:
        print("File không tồn tại. Vui lòng kiểm tra lại tên file.")
    except PermissionError:
        print("Không có quyền truy cập file này.")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")

# Ví dụ 3: Xử lý danh sách
def vi_du_truy_cap_danh_sach():
    print("\n=== Ví dụ 3: Truy cập danh sách ===")
    numbers = [10, 20, 30]
    try:
        index = int(input("Nhập chỉ số muốn truy cập: "))
        print(f"Giá trị tại chỉ số {index}: {numbers[index]}")
    except IndexError:
        print("Lỗi: Chỉ số vượt quá kích thước danh sách!")
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên!")

# Chạy các ví dụ
if __name__ == "__main__":
    vi_du_chia_hai_so()
    vi_du_doc_file()
    vi_du_truy_cap_danh_sach()