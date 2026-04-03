### Ví dụ 1: Đọc file và xử lý các lỗi có thể xảy ra
def doc_file_an_toan(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            noi_dung = f.read()
            print("Nội dung file:")
            print(noi_dung)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'.")
    except PermissionError:
        print(f"Lỗi: Không có quyền truy cập file '{ten_file}'.")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")
    else:
        print("Đọc file thành công!")
    finally:
        print("(Khối finally: Luôn chạy, dù có lỗi hay không)")

# Gọi hàm thử (có thể thay tên file để kiểm tra các lỗi)
doc_file_an_toan('khong_ton_tai.txt')


### Ví dụ 2: Tính chia hai số với ngoại lệ tùy chỉnh
class InvalidInputError(Exception):
    """Ngoại lệ khi người dùng nhập dữ liệu không hợp lệ"""
    def __init__(self, message="Giá trị đầu vào không hợp lệ"):
        self.message = message
        super().__init__(self.message)

def chia_hai_so(a, b):
    try:
        # Kiểm tra kiểu dữ liệu
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise InvalidInputError("Cả hai số phải là số thực hoặc nguyên")
        
        ket_qua = a / b
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")
    except InvalidInputError as e:
        print(f"Lỗi đầu vào: {e.message}")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
    else:
        print(f"Kết quả: {a} / {b} = {ket_qua}")
    finally:
        print("(Hoàn tất phép chia)")

# Thử các trường hợp
chia_hai_so(10, 2)
chia_hai_so(10, 0)
chia_hai_so("abc", 5)


### Ví dụ 3: Quản lý tài khoản ngân hàng với ngoại lệ tùy chỉnh
class InsufficientFundsError(Exception):
    """Ngoại lệ khi số dư không đủ"""
    def __init__(self, so_du, so_tien_rut):
        self.so_du = so_du
        self.so_tien_rut = so_tien_rut
        super().__init__(f"Số dư không đủ: cần {so_tien_rut}, hiện có {so_du}")

class TaiKhoanNganHang:
    def __init__(self, chu_tai_khoan, so_du=0):
        self.chu_tai_khoan = chu_tai_khoan
        self.so_du = so_du
    
    def rut_tien(self, so_tien):
        try:
            if so_tien <= 0:
                raise InvalidInputError("Số tiền rút phải lớn hơn 0")
            if so_tien > self.so_du:
                raise InsufficientFundsError(self.so_du, so_tien)
            
            self.so_du -= so_tien
            print(f"Rút thành công {so_tien}. Số dư còn: {self.so_du}")
        except InvalidInputError as e:
            print(f"Lỗi đầu vào: {e.message}")
        except InsufficientFundsError as e:
            print(f"Lỗi rút tiền: {e}")
        except Exception as e:
            print(f"Lỗi không xác định: {e}")
        else:
            print("Giao dịch hoàn tất! Cảm ơn bạn.")
        finally:
            print("(Kết thúc giao dịch rút tiền)")

# Thử nghiệm
tk = TaiKhoanNganHang("Nguyễn Văn A", 1000)
tk.rut_tien(500)
tk.rut_tien(600)
tk.rut_tien(-100)