def kiem_tra_so_nguyen_to(n):
    # Nếu số nhỏ hơn 2, không phải là số nguyên tố
    if n < 2:
        return False
    # Kiểm tra từ 2 đến căn bậc hai của số
    for i in range(2, int(n**0.5) + 1):
        # Nếu số chia hết cho bất kỳ số nào, không phải là số nguyên tố
        if n % i == 0:
            return False
    # Nếu số không chia hết cho bất kỳ số nào, là số nguyên tố
    return True

# Ví dụ sử dụng
so_can_kiem_tra = 25
ket_qua = kiem_tra_so_nguyen_to(so_can_kiem_tra)

if ket_qua:
    print(f"{so_can_kiem_tra} là số nguyên tố")
else:
    print(f"{so_can_kiem_tra} không là số nguyên tố")