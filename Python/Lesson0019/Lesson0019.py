# Bài 19: Python Cơ bản
# Tác giả: Trợ lý AI
# Mô tả: Tổng hợp các kiến thức nền tảng Python bao gồm biến, kiểu dữ liệu,
# câu lệnh điều kiện, vòng lặp, hàm, danh sách và xử lý ngoại lệ cơ bản.

def hien_thi_chao_hoi(ten):
    """Hàm hiển thị lời chào cơ bản."""
    print(f"Xin chào {ten}, chúc bạn học Python vui vẻ!")


def kiem_tra_so_chan_le(so):
    """Kiểm tra một số nguyên là chẵn hay lẻ."""
    if so % 2 == 0:
        print(f"Số {so} là số CHẴN.")
    else:
        print(f"Số {so} là số LẺ.")


def tinh_tong_danh_sach(danh_sach_so):
    """Tính tổng các phần tử trong danh sách số."""
    tong = 0
    for so in danh_sach_so:
        tong += so
    return tong


def tim_so_lon_nhat(danh_sach_so):
    """Tìm giá trị lớn nhất trong danh sách."""
    if not danh_sach_so:
        return None
    lon_nhat = danh_sach_so[0]
    for so in danh_sach_so[1:]:
        if so > lon_nhat:
            lon_nhat = so
    return lon_nhat


def menu_tuong_tac():
    """Menu lựa chọn để người dùng thực hành các chức năng cơ bản."""
    while True:
        print("\n" + "="*40)
        print("          MENU THỰC HÀNH CƠ BẢN")
        print("="*40)
        print("1. Kiểm tra số chẵn/lẻ")
        print("2. Nhập danh sách số & tính tổng")
        print("3. Tìm số lớn nhất trong danh sách")
        print("4. Thoát chương trình")
        
        lua_chon = input("\nNhập lựa chọn của bạn (1-4): ").strip()
        
        if lua_chon == "1":
            try:
                so_nhap = int(input("Nhập một số nguyên: "))
                kiem_tra_so_chan_le(so_nhap)
            except ValueError:
                print("Lỗi: Vui lòng nhập đúng định dạng số nguyên.")
                
        elif lua_chon == "2":
            try:
                chuoi = input("Nhập các số cách nhau bởi dấu phẩy (vd: 1, 5, 9): ")
                ds = [float(x.strip()) for x in chuoi.split(",") if x.strip()]
                if ds:
                    tong = tinh_tong_danh_sach(ds)
                    print(f"Danh sách: {ds}")
                    print(f"Tổng các phần tử: {tong}")
                else:
                    print("Danh sách rỗng, vui lòng nhập số hợp lệ.")
            except ValueError:
                print("Lỗi: Dữ liệu nhập không đúng định dạng số.")
                
        elif lua_chon == "3":
            try:
                chuoi = input("Nhập các số cách nhau bởi dấu phẩy (vd: 3, 7, 2): ")
                ds = [float(x.strip()) for x in chuoi.split(",") if x.strip()]
                if ds:
                    lon_nhat = tim_so_lon_nhat(ds)
                    print(f"Danh sách: {ds}")
                    print(f"Số lớn nhất là: {lon_nhat}")
                else:
                    print("Danh sách rỗng, vui lòng nhập số hợp lệ.")
            except ValueError:
                print("Lỗi: Dữ liệu nhập không đúng định dạng số.")
                
        elif lua_chon == "4":
            print("\nCảm ơn bạn đã sử dụng chương trình. Hẹn gặp lại!")
            break
            
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 4.")


def main():
    """Hàm chính: Khởi tạo thông tin và chạy chương trình."""
    hien_thi_chao_hoi("Học viên")
    
    # 1. Biến và kiểu dữ liệu cơ bản
    bai_hoc = 19
    ten_bai = "Python Cơ bản"
    cap_do = "Nền tảng"
    co_the_thuc_hanh = True
    
    print(f"\n📘 Thông tin bài học:")
    print(f"   - Bài số: {bai_hoc}")
    print