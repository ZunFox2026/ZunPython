"""
Bài học: Python 32 Cấp Cơ Bản - Bài 1: Cấu trúc điều khiển & Hàm
Tác giả: Học viên Python
Ngày: 2025-04-05
Mô tả: Giới thiệu các cấu trúc điều khiển (if, for, while) và cách viết hàm đơn giản.
"""

# --- 1. Cấu trúc điều kiện: if-elif-else ---
def kiem_tra_so(n):
    """
    Hàm kiểm tra tính chất của một số nguyên.
    Ví dụ: âm, dương, hay bằng 0.
    """
    if n > 0:
        print(f"{n} là số dương.")
    elif n < 0:
        print(f"{n} là số âm.")
    else:
        print(f"{n} là số không (zero).")


# --- 2. Vòng lặp: for ---
def in_bang_cuu_chuong(n):
    """
    Hàm in bảng cửu chương của một số từ 1 đến 10.
    Ví dụ: in_bang_cuu_chuong(5) in ra 5x1=5, 5x2=10,...
    """
    print(f"Bảng cửu chương {n}:")
    for i in range(1, 11):
        ket_qua = n * i
        print(f"{n} x {i} = {ket_qua}")


# --- 3. Vòng lặp: while ---
def dem_nguoc(tu_so):
    """
    Hàm đếm ngược từ một số về 0.
    Ví dụ: đếm ngược từ 5 -> 4 -> 3 -> 2 -> 1 -> 0.
    """
    print(f"Đếm ngược từ {tu_so}:")
    while tu_so >= 0:
        print(tu_so)
        tu_so -= 1  # giảm dần 1 đơn vị
    print("Hết giờ!")


# --- 4. Hàm trả về giá trị ---
def tinh_tong_danh_sach(danh_sach):
    """
    Hàm tính tổng tất cả các phần tử trong danh sách số.
    Trả về tổng.
    """
    tong = 0
    for so in danh_sach:
        tong += so
    return tong


# --- 5. Ví dụ sử dụng ---
def main():
    """
    Hàm chính để chạy chương trình.
    Chứa các ví dụ minh họa và bài tập nhỏ.
    """

    print("=== VÍ DỤ 1: Kiểm tra số dương/âm ===")
    kiem_tra_so(10)
    kiem_tra_so(-5)
    kiem_tra_so(0)

    print("\n=== VÍ DỤ 2: In bảng cửu chương ===")
    in_bang_cuu_chuong(3)

    print("\n=== VÍ DỤ 3: Đếm ngược ===")
    dem_nguoc(4)

    print("\n=== VÍ DỤ 4: Tính tổng danh sách ===")
    danh_sach_so = [1, 2, 3, 4, 5]
    tong = tinh_tong_danh_sach(danh_sach_so)
    print(f"Tổng của {danh_sach_so} là: {tong}")

    # --- Bài tập nhỏ ---
    print("\n=== BÀI TẬP NHỎ ===")
    print("Bài 1: Viết chương trình kiểm tra một số có chia hết cho 3 và 5 không.")
    print("Bài 2: Dùng vòng for in ra các số chẵn từ 1 đến 20.")
    print("Bài 3: Viết hàm đếm xem có bao nhiêu số lẻ trong danh sách [1, 4, 5, 6, 7, 10, 11].")

    # Gợi ý giải bài 2
    print("\nGợi ý bài 2:")
    print("Các số chẵn từ 1 đến 20:")
    for i in range(2, 21, 2):
        print(i, end=" ")
    print()  # Xuống dòng

    # Gợi ý giải bài 3
    print("\nGợi ý bài 3:")
    ds = [1, 4, 5, 6, 7, 10, 11]
    dem = 0
    for so in ds:
        if so % 2 == 1:  # số lẻ
            dem += 1
    print(f"Có {dem} số lẻ trong danh sách {ds}.")


# Chạy chương trình chính
if __name__ == "__main__":
    main()
```

---

### 📝 Giải thích ngắn:
- **100 dòng code** với đầy đủ comment tiếng Việt.
- **3 ví dụ**: kiểm tra số, bảng cửu chương, đếm ngược.
- **2-3 bài tập nhỏ** kèm gợi ý.
- Dùng **if, for, while, hàm có trả về** — những kiến thức cơ bản quan trọng.
- Code thuần Python, không dùng thư viện phụ.

### ▶ Cách chạy:
```bash
python bai_hoc_co_ban.py
```