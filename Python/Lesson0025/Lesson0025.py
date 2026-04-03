# Python 25 Cấp Cơ Bản
# Bài học: Học lập trình Python từ cơ bản đến nâng cao dần qua 25 cấp độ
# File: python_25_cap_co_ban.py
# Mô tả: Giới thiệu các khái niệm cơ bản trong Python: biến, kiểu dữ liệu, điều kiện, vòng lặp, hàm, danh sách, chuỗi.

def main():
    print("=== PYTHON 25 CẤP CƠ BẢN - BÀI HỌC MẪU ===\n")

    # Cấp 1: In ra màn hình
    print("Cấp 1: In ra màn hình")
    print("Xin chào, đây là bài học Python cơ bản!")
    print()

    # Cấp 2: Biến và kiểu dữ liệu
    print("Cấp 2: Biến và kiểu dữ liệu")
    ten = "An"           # Chuỗi (string)
    tuoi = 16            # Số nguyên (int)
    chieu_cao = 1.75     # Số thực (float)
    la_hoc_sinh = True   # Boolean (True/False)

    print(f"Tên: {ten}, Tuổi: {tuoi}, Chiều cao: {chieu_cao}m, Là học sinh: {la_hoc_sinh}")
    print()

    # Cấp 3: Nhập dữ liệu từ người dùng
    print("Cấp 3: Nhập dữ liệu")
    ten_nguoi_dung = input("Nhập tên của bạn: ")
    print(f"Chào bạn {ten_nguoi_dung}!")
    print()

    # Cấp 4: Câu điều kiện (if-else)
    print("Cấp 4: Câu điều kiện")
    diem = 8
    if diem >= 8:
        print("Bạn đạt loại Giỏi!")
    elif diem >= 6.5:
        print("Bạn đạt loại Khá!")
    else:
        print("Bạn cần cố gắng hơn!")
    print()

    # Cấp 5: Vòng lặp for
    print("Cấp 5: Vòng lặp for")
    print("In các số từ 1 đến 5:")
    for i in range(1, 6):
        print(f"Số: {i}")
    print()

    # Cấp 6: Danh sách (list)
    print("Cấp 6: Danh sách")
    danh_sach_lop = ["Lan", "Huy", "Mai", "Tùng"]
    print(f"Danh sách học sinh: {danh_sach_lop}")
    danh_sach_lop.append("Hoàng")  # Thêm phần tử
    print(f"Sau khi thêm Hoàng: {danh_sach_lop}")
    print()

    # Cấp 7: Hàm (function)
    print("Cấp 7: Hàm")
    # Ví dụ 1: Hàm đơn giản
    def xin_chao():
        print("Xin chào từ bên trong hàm!")

    xin_chao()

    # Ví dụ 2: Hàm có tham số và trả về giá trị
    def tinh_tong(a, b):
        return a + b

    ket_qua = tinh_tong(5, 7)
    print(f"Tổng của 5 và 7 là: {ket_qua}")
    print()

    # Cấp 8: Xử lý chuỗi
    print("Cấp 8: Xử lý chuỗi")
    chuoi = "  học lập trình python  "
    print(f"Chuỗi gốc: '{chuoi}'")
    print(f"Viết hoa: '{chuoi.strip().upper()}'")
    print(f"Tách từ: {chuoi.strip().split()}")
    print()

    # Bài tập nhỏ
    print("=== BÀI TẬP NHỎ ===")
    print("Bài 1: Viết chương trình nhập 3 số và in ra số lớn nhất.")
    try:
        a = float(input("Nhập số thứ nhất: "))
        b = float(input("Nhập số thứ hai: "))
        c = float(input("Nhập số thứ ba: "))
        so_lon_nhat = max(a, b, c)
        print(f"Số lớn nhất là: {so_lon_nhat}")
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")
    print()

    print("Bài 2: Tạo danh sách tên bạn bè và in theo thứ tự ngược.")
    danh_sach_ban = ["Minh", "Hà", "Nam", "Trang"]
    print(f"Danh sách bạn bè: {danh_sach_ban}")
    danh_sach_ban.reverse()
    print(f"Theo thứ tự ngược: {danh_sach_ban}")

    print("\nChúc mừng bạn đã hoàn thành bài học cơ bản!")
    print("Hãy tiếp tục luyện tập để lên các cấp cao hơn!")


# Chạy chương trình
if __name__ == "__main__":
    main()
```

---

**Giải thích:**

- **Độ dài:** Khoảng 100 dòng, đầy đủ cấu trúc.
- **Comment tiếng Việt:** Tất cả các phần đều có chú thích rõ ràng.
- **Ví dụ:** 2 ví dụ về hàm, 1 về xử lý chuỗi.
- **Bài tập nhỏ:** 2 bài tập đơn giản để người học thực hành.
- **Mục tiêu:** Giúp người mới bắt đầu làm quen với các khái niệm cơ bản trong Python theo từng "cấp độ".

Bạn có thể mở rộng lên 25 cấp bằng cách chia nhỏ từng chủ đề (ví dụ: Cấp 9: Từ điển, Cấp 10: Vòng lặp while,...) trong các file riêng hoặc chương trình lớn hơn.