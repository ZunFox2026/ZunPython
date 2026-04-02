def tim_so_nguyen_to(n):
    # Khai báo danh sách để lưu trữ các số nguyên tố
    so_nguyen_to = []
    
    # Duyệt qua tất cả các số từ 2 đến n
    for i in range(2, n + 1):
        # Giả định số i là nguyên tố
        la_nguyen_to = True
        
        # Kiểm tra số i có chia hết cho bất kỳ số nào nhỏ hơn nó
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                # Nếu số i chia hết cho j thì nó không phải là số nguyên tố
                la_nguyen_to = False
                break
        
        # Nếu số i là nguyên tố thì thêm nó vào danh sách
        if la_nguyen_to:
            so_nguyen_to.append(i)
    
    # Trả về danh sách các số nguyên tố
    return so_nguyen_to

# Ví dụ sử dụng
n = 50
so_nguyen_to = tim_so_nguyen_to(n)
print(f"Các số nguyên tố nhỏ hơn hoặc bằng {n}: {so_nguyen_to}")