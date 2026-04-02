
## 🐍 Volume1/Lesson2/Lesson2.py

```python
# ================================
# Bài 2: Cấu trúc rẽ nhánh – if, elif, else
# Học cùng Zunny 🦊
# ================================

print("=== BÀI 2: CẤU TRÚC RẼ NHÁNH ===\n")

# ---------- 1. Câu lệnh if cơ bản ----------
age = 18
if age >= 18:
    print("Bạn đã đủ tuổi trưởng thành.")

# ---------- 2. if – else ----------
temperature = 30
if temperature > 25:
    print("Hôm nay trời nóng.")
else:
    print("Hôm nay trời mát.")

# ---------- 3. if – elif – else ----------
score = 7.5
if score >= 8.5:
    print("Xếp loại: A (Giỏi)")
elif score >= 7.0:
    print("Xếp loại: B (Khá)")
elif score >= 5.5:
    print("Xếp loại: C (Trung bình)")
else:
    print("Xếp loại: D (Yếu)")

# ---------- 4. Toán tử so sánh ----------
a = 10
b = 20
print(f"\nSo sánh a={a}, b={b}:")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a < b : {a < b}")
print(f"a > b : {a > b}")
print(f"a <= b: {a <= b}")
print(f"a >= b: {a >= b}")

# ---------- 5. Toán tử logic ----------
x = 15
print(f"\nKiểm tra x={x}:")
if x > 10 and x < 20:
    print("x nằm trong khoảng 10-20")
if x < 5 or x > 15:
    print("x nhỏ hơn 5 hoặc lớn hơn 15")
if not (x == 10):
    print("x không bằng 10")

# ---------- 6. Câu lệnh if lồng nhau ----------
num = 10
if num >= 0:
    if num == 0:
        print("Số không")
    else:
        print("Số dương")
else:
    print("Số âm")

# ---------- 7. Kiểm tra chẵn lẻ ----------
n = int(input("\nNhập một số nguyên: "))
if n % 2 == 0:
    print(f"{n} là số chẵn")
else:
    print(f"{n} là số lẻ")

# ---------- 8. Xếp loại học lực (chi tiết) ----------
diem = float(input("Nhập điểm trung bình: "))
if diem < 0 or diem > 10:
    print("Điểm không hợp lệ!")
else:
    if diem >= 9.0:
        xep_loai = "Xuất sắc"
    elif diem >= 8.0:
        xep_loai = "Giỏi"
    elif diem >= 6.5:
        xep_loai = "Khá"
    elif diem >= 5.0:
        xep_loai = "Trung bình"
    else:
        xep_loai = "Yếu"
    print(f"Xếp loại: {xep_loai}")

# ---------- 9. Kiểm tra năm nhuận ----------
nam = int(input("Nhập năm: "))
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print(f"{nam} là năm nhuận")
else:
    print(f"{nam} không phải năm nhuận")

# ---------- 10. Tìm số lớn nhất trong 3 số ----------
print("\n--- Tìm số lớn nhất ---")
so1 = float(input("Số thứ nhất: "))
so2 = float(input("Số thứ hai: "))
so3 = float(input("Số thứ ba: "))
max_so = so1
if so2 > max_so:
    max_so = so2
if so3 > max_so:
    max_so = so3
print(f"Số lớn nhất là: {max_so}")

# ---------- 11. Máy tính đơn giản ----------
print("\n--- MÁY TÍNH BỎ TÚI ---")
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
phep_tinh = input("Nhập phép tính (+, -, *, /): ")
if phep_tinh == "+":
    print(f"{a} + {b} = {a + b}")
elif phep_tinh == "-":
    print(f"{a} - {b} = {a - b}")
elif phep_tinh == "*":
    print(f"{a} * {b} = {a * b}")
elif phep_tinh == "/":
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("Lỗi: chia cho 0")
else:
    print("Phép tính không hợp lệ")

# ---------- 12. Kiểm tra tam giác ----------
print("\n--- Kiểm tra tam giác ---")
canh_a = float(input("Cạnh a: "))
canh_b = float(input("Cạnh b: "))
canh_c = float(input("Cạnh c: "))
if canh_a + canh_b > canh_c and canh_a + canh_c > canh_b and canh_b + canh_c > canh_a:
    print("Đây là ba cạnh của một tam giác.")
    if canh_a == canh_b == canh_c:
        print("Đó là tam giác đều.")
    elif canh_a == canh_b or canh_b == canh_c or canh_a == canh_c:
        print("Đó là tam giác cân.")
    elif canh_a**2 + canh_b**2 == canh_c**2 or canh_a**2 + canh_c**2 == canh_b**2 or canh_b**2 + canh_c**2 == canh_a**2:
        print("Đó là tam giác vuông.")
    else:
        print("Đó là tam giác thường.")
else:
    print("Ba cạnh không tạo thành tam giác.")

# ---------- 13. Bài tập tổng hợp ----------
print("\n=== BÀI TẬP THỰC HÀNH ===")
# Bài 1: Nhập số, kiểm tra dấu
so = float(input("Nhập một số: "))
if so > 0:
    print("Số dương")
elif so < 0:
    print("Số âm")
else:
    print("Số không")

# Bài 2: Nhập tháng, in số ngày (giả sử năm không nhuận)
thang = int(input("Nhập tháng (1-12): "))
if thang in (1,3,5,7,8,10,12):
    print("31 ngày")
elif thang in (4,6,9,11):
    print("30 ngày")
elif thang == 2:
    print("28 hoặc 29 ngày (tùy năm nhuận)")
else:
    print("Tháng không hợp lệ")

# Bài 3: Nhập ký tự, kiểm tra nguyên âm/phụ âm
ch = input("Nhập một chữ cái: ").lower()
if len(ch) == 1 and ch.isalpha():
    if ch in "aeiou":
        print("Nguyên âm")
    else:
        print("Phụ âm")
else:
    print("Không phải chữ cái")

print("\n🦊 Kết thúc Bài 2. Hãy chắc chắn bạn đã hiểu rõ if-elif-else!")
