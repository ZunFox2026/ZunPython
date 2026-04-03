"""
Bài 7: Luyện Tập Cơ Bản Về Cấu Trúc Điều Khiển Và Vòng Lặp Trong Python

Mục tiêu:
- Ôn tập cấu trúc rẽ nhánh: if, elif, else
- Ôn tập vòng lặp: for, while
- Áp dụng vào các bài toán thực tế đơn giản

Tác giả: Luyện tập Python
Ngày: 2023
"""

def vidu_if_elif_else():
    """
    Ví dụ 1: Sử dụng if, elif, else để đánh giá điểm số học sinh
    """
    print("=== Ví dụ 1: Đánh giá điểm số ===")
    diem = float(input("Nhập điểm của học sinh (0-10): "))
    
    if diem >= 9:
        xep_loai = "Xuất sắc"
    elif diem >= 7:
        xep_loai = "Giỏi"
    elif diem >= 5:
        xep_loai = "Trung bình"
    else:
        xep_loai = "Yếu"
    
    print(f"Điểm: {diem} => Xếp loại: {xep_loai}")


def vidu_vong_lap_for():
    """
    Ví dụ 2: Sử dụng vòng lặp for để in bảng cửu chương
    """
    print("\n=== Ví dụ 2: Bảng cửu chương 5 ===")
    so = 5
    for i in range(1, 11):
        print(f"{so} x {i} = {so * i}")


def vidu_vong_lap_while():
    """
    Ví dụ 3: Sử dụng vòng lặp while để đếm ngược
    """
    print("\n=== Ví dụ 3: Đếm ngược từ 5 đến 1 ===")
    dem = 5
    while dem > 0:
        print(f"Đếm ngược: {dem}")
        dem -= 1  # giảm 1 đơn vị
    print("Hết giờ!")


def bai_tap_nho():
    """
    Bài tập nhỏ: Viết chương trình kiểm tra số nguyên tố
    Yêu cầu: Nhập một số nguyên dương, kiểm tra xem có phải số nguyên tố không
    """
    print("\n=== Bài tập nhỏ: Kiểm tra số nguyên tố ===")
    try:
        n = int(input("Nhập một số nguyên dương: "))
        
        if n < 2:
            print(f"{n} không phải là số nguyên tố.")
            return
        
        la_nguyen_to = True  # giả sử ban đầu là số nguyên tố
        
        # Kiểm tra từ 2 đến căn bậc 2 của n
        i = 2
        while i * i <= n:
            if n % i == 0:
                la_nguyen_to = False
                break  # thoát vòng lặp ngay khi tìm thấy ước
            i += 1
        
        if la_nguyen_to:
            print(f"{n} là số nguyên tố.")
        else:
            print(f"{n} không phải là số nguyên tố.")
            
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")


def menu_chon_chuc_nang():
    """
    Hiển thị menu và cho người dùng chọn chức năng
    """
    while True:
        print("\n" + "="*50)
        print("CHỌN CHỨC NĂNG:")
        print("1. Ví dụ if-elif-else (xếp loại học sinh)")
        print("2. Ví dụ vòng lặp for (bảng cửu chương)")
        print("3. Ví dụ vòng lặp while (đếm ngược)")
        print("4. Bài tập nhỏ: Kiểm tra số nguyên tố")
        print("5. Thoát")
        print("="*50)
        
        lua_chon = input("Nhập lựa chọn của bạn (1-5): ")
        
        if lua_chon == '1':
            vidu_if_elif_else()
        elif lua_chon == '2':
            vidu_vong_lap_for()
        elif lua_chon == '3':
            vidu_vong_lap_while()
        elif lua_chon == '4':
            bai_tap_nho()
        elif lua_chon == '5':
            print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


def main():
    """
    Hàm chính để chạy chương trình
    """
    print("📘 BÀI 7: LUYỆN TẬP CƠ BẢN VỀ CẤU TRÚC ĐIỀU KHIỂN VÀ VÒNG LẶP")
    print("Chương trình này giúp bạn luyện tập các cấu trúc điều khiển cơ bản trong Python.")
    
    # Chạy menu chức năng
    menu_chon_chuc_nang()


# Gọi hàm main để thực thi chương trình
if __name__ == "__main__":
    main()
```