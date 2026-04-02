# ==============================================================================
# BÀI 1: PYTHON CƠ BẢN (CẤP ĐỘ CƠ BẢN)
# ==============================================================================
# Chào mừng bạn đến với bài học đầu tiên về lập trình Python!
# Mục tiêu: Làm quen với cú pháp cơ bản, cách khai báo biến, kiểu dữ liệu,
# cách nhập/xuất thông tin, toán tử số học và cấu trúc điều kiện if-else.
# Python nổi tiếng vì cú pháp ngắn gọn, dễ đọc, gần gũi với tiếng Anh.

def gioi_thieu_bai_hoc():
    """In ra tiêu đề và mục tiêu bài học."""
    print("=" * 60)
    print("BÀI 1: PYTHON CƠ BẢN")
    print("=" * 60)
    print("Nội dung sẽ đi qua:")
    print("  1. Biến và kiểu dữ liệu cơ bản")
    print("  2. Hàm nhập/xuất (Input & Output)")
    print("  3. Toán tử số học & so sánh")
    print("  4. Câu lệnh rẽ nhánh (if/elif/else)")
    print("  5. Bài tập thực hành cuối bài")
    print("-" * 60)

def kham_pha_bien_va_kieu_du_lieu():
    """
    Biến trong Python hoạt động như một nhãn dán trỏ đến vùng nhớ chứa dữ liệu.
    Python là ngôn ngữ định kiểu động: không cần khai báo kiểu trước khi gán giá trị.
    """
    print("\n[PHẦN 1] BIẾN VÀ KIỂU DỮ LIỆU")
    # Hàm type() dùng để kiểm tra kiểu dữ liệu của biến
    ho_ten = "Lê Văn B"           # Kiểu chuỗi (str): chứa văn bản
    nam_sinh = 1998               # Kiểu số nguyên (int): số không có phần thập phân
    chieu_cao = 1.72              # Kiểu số thực (float): số có phần thập phân
    la_sinh_vien = True           # Kiểu luận lý (bool): chỉ nhận giá trị True hoặc False

    print(f"- Họ tên: '{ho_ten}' | Kiểu: {type(ho_ten).__name__}")
    print(f"- Năm sinh: {nam_sinh} | Kiểu: {type(nam_sinh).__name__}")
    print(f"- Chiều cao: {chieu_cao}m | Kiểu: {type(chieu_cao).__name__}")
    print(f"- Là sinh viên: {la_sinh_vien} | Kiểu: {type(la_sinh_vien).__name__}")

    # Lưu ý: Python cho phép gán lại giá trị với kiểu khác cho cùng một tên biến
    nam_sinh = "Chưa xác định"
    print(f"- Sau khi gán lại: '{nam_sinh}' | Kiểu: {type(nam_sinh).__name__}")

def thuc_hanh_nhap_xuat():
    """
    print() dùng để xuất dữ liệu ra màn hình console.
    input() dùng để đọc chuỗi ký tự người dùng nhập từ bàn phím.
    Lưu ý: input() LUÔN trả về kiểu str, cần ép kiểu (int, float) nếu muốn tính toán.
    """
    print("\n[PHẦN 2] NHẬP VÀ XUẤT DỮ LIỆU")
    print("Sử dụng f-string (chuỗi định dạng) để nhúng biến vào chuỗi dễ dàng.")
    
    ten_mon = "Toán Cao Cấp"
    so_tin_chi = 4
    # Cách định dạng chuỗi hiện đại nhất trong Python
    print(f"-> Môn học: {ten_mon}, Số tín chỉ: {so_tin_chi}")

    # Ví dụ nhập liệu (được bao trong try-except để tránh lỗi crash khi chạy tự động)
    try:
        print("\nThử nhập điểm số của bạn (0-10):")
        diem_so = float(input("Nhập điểm: "))
        print(f"--> Bạn vừa nhập: {diem_so}")
        print(f"--> Đã kiểm tra kiểu: {type(diem_so).__name__}")
    except ValueError:
        print("--> [Bỏ qua nhập liệu] Dữ liệu không hợp lệ hoặc môi trường chạy không hỗ trợ input().")

def thao_tac_toan_tu():
    """Giới thiệu toán tử số học, so sánh và logic cơ bản."""
    print("\n[PHẦN 3] CÁC TOÁN TỬ QUAN TRỌNG")
    x, y = 15, 4
    print(f"Giá trị mẫu: x = {x}, y = {y}")
    
    # Toán tử số học cơ bản
    print(f"   x + y = {x + y}   | x - y = {x - y}")
    print(f"   x * y = {x * y}   | x / y = {x / y:.2f}")  # Làm tròn 2 chữ số thập phân
    print(f"   x // y = {x // y}  | x % y = {x % y}")      # Chia lấy nguyên và chia lấy dư
    print(f"   x ** y = {x ** y}")                          # Lũy thừa

    # Toán tử so sánh (trả về boolean)
    print("\nToán tử so sánh:")
    print(f"   x == y : {x == y}  | x != y : {x != y}")
    print(f"   x > y  : {x > y}   | x <= y : {x <= y}")

    # Toán tử logic (and, or, not) dùng để kết hợp điều kiện
    print("\nToán tử logic:")
    print(f"   (x > 10) and (y > 2) -> { (x > 10) and (y > 2) }")
    print(f"   (x < 10) or (y < 2)  -> { (x < 10) or (y < 2) }")

def cau_lenh_re_nhanh():
    """
    Cấu trúc điều khiển luồng chạy chương trình.
    if: kiểm tra điều kiện đúng -> thực thi khối lệnh
    elif: nếu if sai, kiểm tra điều kiện tiếp theo
    else: nếu tất cả điều kiện trên sai -> thực thi khối cuối
    """
    print("\n[PHẦN 4] CÂU LỆNH ĐIỀU KIỆN (IF/ELIF/ELSE)")
    diem_thi = 8.2
    print(f"Điểm thi: {diem_thi}")

    if diem_thi >= 9.0:
        xep_loai = "Xuất sắc"
    elif diem_thi >= 7.5:
        xep_loai = "Giỏi"
    elif diem_thi >= 6.5:
        xep_loai = "Khá"
    elif diem_thi >= 5.0:
        xep_loai = "Trung bình"
    else:
        xep_loai = "Yếu/Kém"
    
    print(f"-> Kết quả xếp loại: {xep_loai}")

    # Mẹo Python: Có thể viết điều kiện rút gọn (ternary operator)
    ket_qua = "Đỗ" if diem_thi >= 5.0 else "Trượt"
    print(f"-> Kết quả thi: {ket_qua}")

def bai_tap_va_loi_giai():
    """Tổng hợp bài tập nhỏ kèm lời giải tham khảo để người học ôn tập."""
    print("\n" + "=" * 60)
    print("PHẦN 5: BÀI TẬP THỰC HÀNH & LỜI GIẢI")
    print("=" * 60)
    
    # Bài 1
    print("Bài 1: Tính chu vi và diện tích hình chữ nhật.")
    print("Đề bài: Cho chiều dài 12m, chiều rộng 7m.")
    cd, cr = 12, 7
    chu_vi = 2 * (cd + cr)
    dien_tich = cd * cr
    print(f"Lời giải: CV = {chu_vi}m, DT = {dien_tich}m²\n")

    # Bài 2
    print("Bài 2: Kiểm tra số chẵn hay số lẻ.")
    print("Đề bài: Sử dụng toán tử % để kiểm tra số 25.")
    so_kiem_tra = 25
    if so_kiem_tra % 2 == 0:
        print(f"Lời giải: Số {so_kiem_tra} là số chẵn.")
    else:
        print(f"Lời giải: Số {so_kiem_tra} là số lẻ.")
        
    # Bài 3
    print("\nBài 3: Đổi điểm thang 10 sang thang 4 (Mỹ).")
    print("Quy tắc: >= 9 -> 4.0, >= 7.5 -> 3.5, >= 6.0 -> 2.5, < 6.0 -> 0.0")
    diem_goc = 8.5
    if diem_goc >= 9.0:
        diem_4 = 4.0
    elif diem_goc >= 7.5:
        diem_4 = 3.5
    elif diem_goc >= 6.0:
        diem_4 = 2.5
    else:
        diem_4 = 0.0
    print(f"Lời giải: Điểm {diem_goc}/10 quy đổi là {diem_4}/4.0")

def main():
    """
    Hàm chính: Đóng vai trò điều phối toàn bộ chương trình.
    Giúp code có cấu trúc rõ ràng, dễ bảo trì và mở rộng.
    """
    gioi_thieu_bai_hoc()
    kham_pha_bien_va_kieu_du_lieu()
    thuc_hanh_nhap_xuat()
    thao_tac_toan_tu()
    cau_lenh_re_nhanh()
    bai_tap_va_loi_giai()
    print("\n" + "=" * 60)
    print("ĐÃ HOÀN THÀNH BÀI 1. HÃY CHẠY THỬ, SỬA ĐỔI VÀ THỰC HÀNH THÊM!")
    print("=" * 60)

# Khối if __name__ == "__main__" đảm bảo hàm main() chỉ được gọi
# khi file này được chạy trực tiếp, không phải khi import sang file khác.
if __name__ == "__main__":
    main()