# Bài 8: Python Cơ bản
# Yêu cầu: Nhập vào một số nguyên n (n ≥ 0) từ bàn phím.
# Tính và in ra tổng S = 1 + 2 + ... + n.
# Nếu n = 0 thì tổng bằng 0.

def tinh_tong(n: int) -> int:
    """
    Tính tổng các số nguyên từ 1 tới n.
    :param n: số nguyên không âm
    :return: tổng S = 1 + 2 + ... + n
    """
    return n * (n + 1) // 2   # Công thức tổng cấp số cộng

def main() -> None:
    """
    Hàm chính: đọc đầu vào, gọi hàm tính tổng và in kết quả.
    """
    try:
        # Đọc số nguyên từ người dùng
        n_str = input("Nhập một số nguyên n (n ≥ 0): ").strip()
        n = int(n_str)
        if n < 0:
            print("Vui lòng nhập số không âm.")
            return
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")
        return

    tong = tinh_tong(n)
    print(f"Tổng S = 1 + 2 + ... + {n} là: {tong}")

if __name__ == "__main__":
    main()