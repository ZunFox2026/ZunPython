def main():
    """
    Bài 1 - Làm Quen Với Biến Và Kiểu Dữ Liệu trong Python
    
    Mục tiêu:
    - Hiểu khái niệm biến và cách khai báo biến trong Python
    - Biết các kiểu dữ liệu cơ bản: int, float, str, bool
    - Biết cách kiểm tra kiểu dữ liệu bằng hàm type()
    - Áp dụng trong các ví dụ và bài tập đơn giản
    """

    # --- 1. Biến (Variable) ---
    # Biến là một tên dùng để lưu trữ dữ liệu.
    # Trong Python, bạn không cần khai báo kiểu dữ liệu trước khi dùng.
    # Tên biến nên dễ hiểu và tuân theo quy tắc: chữ cái, số, dấu gạch dưới, không bắt đầu bằng số.

    tuoi = 20          # Biến lưu số nguyên (integer)
    chieu_cao = 1.75   # Biến lưu số thực (float)
    ten = "Nguyen Van A"  # Biến lưu chuỗi ký tự (string)
    da_tot_nghiep = True  # Biến lưu giá trị đúng/sai (boolean)

    # In giá trị các biến ra màn hình
    print("Thông tin cá nhân:")
    print(f"Tên: {ten}")
    print(f"Tuổi: {tuoi}")
    print(f"Chiều cao: {chieu_cao} m")
    print(f"Đã tốt nghiệp: {da_tot_nghiep}")


    # --- 2. Kiểm tra kiểu dữ liệu ---
    # Hàm type() dùng để xem kiểu dữ liệu của một biến

    print("\n--- Kiểm tra kiểu dữ liệu ---")
    print(f"Kiểu của 'tuoi': {type(tuoi)}")
    print(f"Kiểu của 'chieu_cao': {type(chieu_cao)}")
    print(f"Kiểu của 'ten': {type(ten)}")
    print(f"Kiểu của 'da_tot_nghiep': {type(da_tot_nghiep)}")


    # --- 3. Một số ví dụ minh họa ---

    # Ví dụ 1: Tính tổng hai số
    print("\n--- Ví dụ 1: Tính tổng ---")
    a = 15
    b = 25
    tong = a + b
    print(f"{a} + {b} = {tong}")

    # Ví dụ 2: Nối chuỗi
    print("\n--- Ví dụ 2: Nối chuỗi ---")
    ho = "Le"
    ten_dem = "Thi"
    ten_goi = "Binh"
    ho_ten = ho + " " + ten_dem + " " + ten_goi
    print(f"Họ tên đầy đủ: {ho_ten}")

    # Ví dụ 3: Sử dụng biến boolean trong điều kiện đơn giản
    print("\n--- Ví dụ 3: Dùng biến boolean ---")
    di_hoc = True
    if di_hoc:
        print("Hôm nay bạn ấy đi học.")
    else:
        print("Hôm nay bạn ấy nghỉ học.")


    # --- 4. Bài tập nhỏ ---
    # Yêu cầu: Tạo các biến mô tả một sản phẩm: tên, giá, số lượng, có sẵn hay không
    # Tính tổng giá trị tồn kho (giá * số lượng) và in ra thông tin

    print("\n--- Bài tập nhỏ: Quản lý sản phẩm ---")
    
    # Bắt đầu bài tập
    ten_san_pham = "Laptop Gaming"
    gia = 25000000      # đơn vị: VND
    so_luong = 10
    co_san = True

    # Tính tổng giá trị tồn kho
    gia_tri_ton_kho = gia * so_luong

    # In thông tin sản phẩm
    print("Thông tin sản phẩm:")
    print(f"Tên: {ten_san_pham}")
    print(f"Giá: {gia:,} VND")
    print(f"Số lượng: {so_luong}")
    print(f"Trạng thái: {'Có sẵn' if co_san else 'Hết hàng'}")
    print(f"Giá trị tồn kho: {gia_tri_ton_kho:,} VND")

    # Kiểm tra kiểu dữ liệu của biến giá trị tồn kho
    print(f"Kiểu dữ liệu của 'gia_tri_ton_kho': {type(gia_tri_ton_kho)}")


    # --- 5. Ghi chú ---
    # - Python tự động nhận diện kiểu dữ liệu khi gán giá trị
    # - Tên biến phân biệt chữ hoa/chữ thường (ten khác với Ten)
    # - Nên dùng tên biến có ý nghĩa để dễ đọc và bảo trì

    print("\n--- Kết thúc bài học ---")
    print("Bạn đã làm quen với biến và các kiểu dữ liệu cơ bản trong Python!")


# Gọi hàm main để thực thi chương trình
if __name__ == "__main__":
    main()
```

---

**Giải thích ngắn:**

- File này dành cho bài học đầu tiên về biến và kiểu dữ liệu.
- Có đầy đủ: lý thuyết, 3 ví dụ, 1 bài tập nhỏ.
- Sử dụng comment tiếng Việt rõ ràng, dễ hiểu.
- Dài khoảng 100 dòng, phù hợp cho người mới bắt đầu.
- Chạy được ngay bằng lệnh: `python bai1_bien_kieu_du_lieu.py`