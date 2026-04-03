# Lời giải bài tập

# Bài tập 1: In bảng cửu chương 5
print("=== Bài tập 1: Bảng cửu chương 5 ===")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# Bài tập 2: Tính tổng các số từ 1 đến n
print("\n=== Bài tập 2: Tính tổng từ 1 đến n ===")
n = int(input("Nhập n: "))
i = 1
tong = 0
while i <= n:
    tong += i
    i += 1
print(f"Tổng các số từ 1 đến {n} là: {tong}")

# Bài tập 3: Đếm ngược từ 10 về 0
print("\n=== Bài tập 3: Đếm ngược từ 10 về 0 ===")
for i in range(10, -1, -1):  # từ 10 đến 0, bước -1
    print(i)

# Hoặc dùng while:
# i = 10
# while i >= 0:
#     print(i)
#     i -= 1

# Bài tập 4: In hình vuông ký tự
print("\n=== Bài tập 4: In hình vuông ký tự ===")
kich_thuoc = int(input("Nhập kích thước hình vuông: "))
for i in range(kich_thuoc):
    for j in range(kich_thuoc):
        print("*", end="")  # in mà không xuống dòng
    print()  # xuống dòng sau mỗi hàng

# Bài tập 5: Kiểm tra số nguyên tố
print("\n=== Bài tập 5: Kiểm tra số nguyên tố ===")
n = int(input("Nhập một số: "))

if n < 2:
    print(f"{n} không phải là số nguyên tố.")
else:
    la_nguyen_to = True
    for i in range(2, int(n ** 0.5) + 1):  # chỉ cần kiểm tra đến căn bậc 2 của n
        if n % i == 0:
            la_nguyen_to = False
            break  # tìm thấy ước số thì không phải nguyên tố
    
    if la_nguyen_to:
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")