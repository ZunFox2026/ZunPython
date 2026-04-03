def doc_file_an_toan(ten_file):
    """Đọc nội dung file và in ra, xử lý nếu file không tồn tại"""
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            noi_dung = f.read()
            print(f"Nội dung file {ten_file}:")
            print(noi_dung)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'!")
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file '{ten_file}'!")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
    else:
        print("Đọc file thành công!")
    finally:
        print("--- Hoàn tất thao tác đọc file ---")


def nhap_so_nguyen():
    """Yêu cầu người dùng nhập số nguyên, lặp lại nếu nhập sai"""
    while True:
        try:
            so = int(input("Nhập một số nguyên: "))
            print(f"Bạn đã nhập: {so}")
            return so
        except ValueError:
            print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
        except KeyboardInterrupt:
            print("\nNgười dùng đã hủy nhập.")
            break


def tinh_diem_trung_binh(danh_sach_diem):
    """Tính điểm trung bình, xử lý danh sách rỗng hoặc dữ liệu không hợp lệ"""
    try:
        # Kiểm tra danh sách rỗng
        if len(danh_sach_diem) == 0:
            raise ValueError("Danh sách điểm rỗng!")
        
        # Kiểm tra từng điểm có phải là số không
        for diem in danh_sach_diem:
            if not isinstance(diem, (int, float)):
                raise TypeError(f"Điểm '{diem}' không hợp lệ!")
            if diem < 0 or diem > 10:
                raise ValueError(f"Điểm {diem} nằm ngoài thang điểm 0-10!")
        
        dtb = sum(danh_sach_diem) / len(danh_sach_diem)
        print(f"Điểm trung bình: {dtb:.2f}")
        return dtb
        
    except ValueError as e:
        if "rỗng" in str(e):
            print("Lỗi: Không có điểm nào để tính!")
        else:
            print(f"Lỗi giá trị: {e}")
    except TypeError as e:
        print(f"Lỗi kiểu dữ liệu: {e}")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")
    finally:
        print("Hoàn tất tính toán điểm.")

# Chạy các ví dụ
if __name__ == "__main__":
    print("=== Ví dụ 1: Đọc file an toàn ===")
    doc_file_an_toan("khong_ton_tai.txt")
    
    print("\n=== Ví dụ 2: Nhập số nguyên an toàn ===")
    # Bỏ comment dòng dưới để thử (nhập abc hoặc Ctrl+C)
    # nhap_so_nguyen()
    
    print("\n=== Ví dụ 3: Tính điểm trung bình ===")
    tinh_diem_trung_binh([8.5, 9, 7.5, 10])
    tinh_diem_trung_binh([])
    tinh_diem_trung_binh([8, 9, 'A', 10])