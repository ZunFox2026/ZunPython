def vi_du_1_xu_ly_loi_chia():
    """
    Ví dụ 1: Xử lý lỗi chia cho 0
    """
    print("=== Ví dụ 1: Xử lý lỗi chia cho 0 ===")
    a = 10
    b = 0
    try:
        ket_qua = a / b
        print(f"Kết quả: {ket_qua}")
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")


def vi_du_2_nhap_lieu_nguoi_dung():
    """
    Ví dụ 2: Xử lý lỗi nhập liệu không hợp lệ
    """
    print("\n=== Ví dụ 2: Xử lý lỗi nhập số nguyên ===")
    try:
        so = int(input("Nhập một số nguyên: "))
        print(f"Bạn đã nhập: {so}")
    except ValueError:
        print("Lỗi: Giá trị nhập vào không phải là số nguyên!")


def vi_du_3_mo_file_va_finally():
    """
    Ví dụ 3: Xử lý lỗi mở file và dùng finally
    """
    print("\n=== Ví dụ 3: Mở file và khối finally ===")
    try:
        f = open("khong_ton_tai.txt", "r")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("Không tìm thấy file!")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
    else:
        print("File đã được đọc thành công!")
    finally:
        print("Khối finally: Luôn được thực thi, dùng để dọn dẹp tài nguyên.")


def vi_du_4_nem_ngoai_le_tuy_chinh():
    """
    Ví dụ 4: Chủ động ném ngoại lệ
    """
    print("\n=== Ví dụ 4: Ném ngoại lệ tùy chỉnh ===")
    def kiem_tra_tuoi(tuoi):
        if tuoi < 0:
            raise ValueError("Tuổi không thể là số âm!")
        elif tuoi > 150:
            raise ValueError("Tuổi không thể lớn hơn 150!")
        else:
            print(f"Tuổi hợp lệ: {tuoi}")
    
    try:
        kiem_tra_tuoi(-5)
    except ValueError as e:
        print(f"Lỗi giá trị: {e}")


if __name__ == "__main__":
    vi_du_1_xu_ly_loi_chia()
    vi_du_2_nhap_lieu_nguoi_dung()
    vi_du_3_mo_file_va_finally()
    vi_du_4_nem_ngoai_le_tuy_chinh()