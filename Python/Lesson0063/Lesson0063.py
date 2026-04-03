"""
Bài học: Python 63 - Lập Trình Cơ Bản cho Người Mới Bắt Đầu
Tác giả: Học viên Python
Mục tiêu:
- Giới thiệu cú pháp cơ bản của Python
- Sử dụng biến, kiểu dữ liệu, vòng lặp, điều kiện
- Viết hàm đơn giản và giải quyết bài toán thực tế
"""

# === 1. Biến và Kiểu Dữ Liệu Cơ Bản ===
# Biến dùng để lưu trữ dữ liệu
ten = "An"           # Chuỗi (string)
tuoi = 16            # Số nguyên (int)
chieu_cao = 1.75     # Số thực (float)
la_hoc_sinh = True   # Boolean (True/False)

# In thông tin ra màn hình
print("=== Ví dụ 1: Sử dụng biến ===")
print(f"Tên: {ten}")
print(f"Tuổi: {tuoi}")
print(f"Chiều cao: {chieu_cao} mét")
print(f"Là học sinh: {la_hoc_sinh}")


# === 2. Cấu Trúc Điều Kiện (if-elif-else) ===
print("\n=== Ví dụ 2: Điều kiện kiểm tra tuổi ===")
if tuoi >= 18:
    print(f"{ten} đã đủ tuổi trưởng thành.")
elif tuoi >= 13:
    print(f"{ten} là thanh thiếu niên.")
else:
    print(f"{ten} là trẻ em.")


# === 3. Vòng lặp for ===
print("\n=== Ví dụ 3: In danh sách các môn học ===")
cac_mon_hoc = ["Toán", "Văn", "Anh", "Lý", "Hóa"]

print("Danh sách các môn học:")
for mon in cac_mon_hoc:
    print(f"- {mon}")


# === 4. Hàm trong Python ===
# Hàm là khối lệnh có thể tái sử dụng
def tinh_diem_trung_binh(toan, van, anh):
    """
    Hàm tính điểm trung bình của 3 môn
    Input: điểm Toán, Văn, Anh
    Output: điểm trung bình
    """
    return (toan + van + anh) / 3

# Gọi hàm và in kết quả
print("\n=== Ví dụ 4: Sử dụng hàm tính điểm ===")
diem_toan = 8.5
diem_van = 7.0
diem_anh = 9.0
dtb = tinh_diem_trung_binh(diem_toan, diem_van, diem_anh)
print(f"Điểm trung bình: {dtb:.2f}")


# === 5. Bài Tập Nhỏ ===
"""
Bài tập: Viết chương trình kiểm tra số chẵn/lẻ
Yêu cầu:
- Người dùng nhập một số nguyên
- Chương trình kiểm tra và in ra số đó là chẵn hay lẻ
- Sử dụng hàm để xử lý
"""

def kiem_tra_chan_le(so):
    """Hàm kiểm tra số chẵn hay lẻ"""
    if so % 2 == 0:
        return "chẵn"
    else:
        return "lẻ"

def main():
    """Hàm chính chạy chương trình"""
    print("\n" + "="*40)
    print("BÀI TẬP: KIỂM TRA SỐ CHẴN LẺ")
    print("="*40)
    
    try:
        # Nhập số từ người dùng
        n = int(input("Nhập một số nguyên: "))
        
        # Gọi hàm kiểm tra
        ket_qua = kiem_tra_chan_le(n)
        
        # In kết quả
        print(f"Số {n} là số {ket_qua}.")
        
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
    
    # Gợi ý mở rộng
    print("\n💡 Gợi ý mở rộng:")
    print("- Thêm vòng lặp để kiểm tra nhiều số")
    print("- Kiểm tra số nguyên dương, âm hoặc bằng 0")


# Chạy chương trình chính
if __name__ == "__main__":
    main()


# === Gợi ý Tự Học ===
"""
1. Thử thay đổi giá trị biến và xem kết quả
2. Thêm danh sách bạn bè và in theo vòng lặp
3. Viết hàm tính diện tích hình chữ nhật
4. Dùng while để lặp cho đến khi người dùng muốn thoát
"""

# Kết thúc bài học
print("\n🎉 Chúc mừng bạn đã hoàn thành bài học Python cơ bản!")
print("Hãy tiếp tục luyện tập để thành thạo hơn!")
```