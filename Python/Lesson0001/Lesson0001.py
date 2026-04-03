"""
Bài 1: Làm Quen Với Python - In Dữ Liệu và Biến Đơn Giản

Mục tiêu:
- Hiểu cách sử dụng lệnh in (print) để hiển thị dữ liệu.
- Khai báo và sử dụng biến trong Python.
- Làm việc với các kiểu dữ liệu cơ bản: chuỗi (string), số nguyên (int), số thập phân (float).
- Thực hành với một vài ví dụ và bài tập nhỏ.

Học xong bài này, bạn sẽ có thể:
- In ra màn hình các thông tin cơ bản.
- Tạo và sử dụng biến lưu trữ giá trị.
- Hiểu cách Python xử lý các kiểu dữ liệu khác nhau.
"""

def main():
    # ================= VÍ DỤ 1: In dữ liệu ra màn hình =================
    print("=== VÍ DỤ 1: In dữ liệu đơn giản ===")
    
    # In một chuỗi văn bản
    print("Xin chào, mình là Python!")
    
    # In một con số
    print(42)
    
    # In kết hợp chuỗi và số
    print("Năm nay mình học lớp", 10)
    
    # In nhiều giá trị trên cùng một dòng, cách nhau bởi dấu cách
    print("Hà Nội", "Tp.Hồ Chí Minh", "Đà Nẵng")
    
    # In một dòng trống để dễ nhìn
    print()


    # ================= VÍ DỤ 2: Sử dụng biến để lưu trữ dữ liệu =================
    print("=== VÍ DỤ 2: Sử dụng biến ===")
    
    # Khai báo biến lưu tên học sinh
    ten_hoc_sinh = "Nguyễn Văn A"
    tuoi = 15
    diem_trung_binh = 8.7
    
    # In thông tin học sinh sử dụng biến
    print("Học sinh:", ten_hoc_sinh)
    print("Tuổi:", tuoi)
    print("Điểm trung bình:", diem_trung_binh)
    
    # Cập nhật giá trị biến
    diem_trung_binh = 9.0
    print("Sau khi cải thiện, điểm trung bình mới là:", diem_trung_binh)
    
    # Biến có thể thay đổi kiểu dữ liệu (không cần khai báo kiểu)
    bien_khac = "Ban đầu là chuỗi"
    print(bien_khac)
    bien_khac = 100  # giờ là số
    print("Giờ biến thành số:", bien_khac)
    
    print()


    # ================= VÍ DỤ 3: Tính toán đơn giản với biến =================
    print("=== VÍ DỤ 3: Tính toán cơ bản ===")
    
    chieu_dai = 10
    chieu_rong = 5
    
    dien_tich = chieu_dai * chieu_rong
    chu_vi = 2 * (chieu_dai + chieu_rong)
    
    print("Hình chữ nhật có:")
    print("Chiều dài:", chieu_dai)
    print("Chiều rộng:", chieu_rong)
    print("Diện tích:", dien_tich)
    print("Chu vi:", chu_vi)
    
    print()


    # ================= BÀI TẬP NHỎ =================
    print("=== BÀI TẬP NHỎ ===")
    
    # Yêu cầu: Viết chương trình nhỏ mô phỏng một cửa hàng tính tiền
    print("Chương trình tính tiền mua hàng đơn giản")
    
    # Giá các mặt hàng (đơn vị: nghìn đồng)
    gia_sach = 35
    gia_but = 5
    gia_tap = 12
    
    # Số lượng mua
    so_sach = 2
    so_but = 3
    so_tap = 5
    
    # Tính tổng tiền
    tong_tien = (gia_sach * so_sach) + (gia_but * so_but) + (gia_tap * so_tap)
    
    # In hóa đơn
    print("HÓA ĐƠN MUA HÀNG")
    print(f"Sách: {so_sach} x {gia_sach}k = {gia_sach * so_sach}k")
    print(f"Bút: {so_but} x {gia_but}k = {gia_but * so_but}k")
    print(f"Tập: {so_tap} x {gia_tap}k = {gia_tap * so_tap}k")
    print("-" * 20)
    print(f"TỔNG CỘNG: {tong_tien} nghìn đồng")
    
    # Gợi ý mở rộng: Thử thêm phần nhập chiết khấu hoặc thuế
    print()
    print("Chúc mừng bạn đã hoàn thành bài tập!")
    print("Hãy thử tự tạo thêm một ví dụ tương tự với dữ liệu của riêng bạn!")


# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()
```

---

✅ **Giải thích ngắn gọn**:
- `print()` dùng để hiển thị dữ liệu ra màn hình.
- Biến được tạo bằng cách gán giá trị: `ten_bien = gia_tri`.
- Python tự động nhận diện kiểu dữ liệu (chuỗi, số, thập phân...).
- Có thể tính toán với biến như trong toán học.

📌 **Gợi ý luyện tập thêm**:
1. Thay đổi tên, tuổi, điểm trong ví dụ 2.
2. Tạo biến lưu tên trường học và in ra câu: "Tôi học trường XYZ".
3. Tính tổng 3 số bất kỳ và in kết quả.