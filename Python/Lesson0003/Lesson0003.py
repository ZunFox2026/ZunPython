"""
Bài 1: Làm Quen Với Python - In Dữ Liệu Và Biến Đơn Giản

Mục tiêu:
- Hiểu cách in dữ liệu ra màn hình bằng lệnh print()
- Khai báo và sử dụng biến trong Python
- Làm việc với các kiểu dữ liệu cơ bản: chuỗi (str), số nguyên (int), số thực (float)
- Thực hành với các phép toán đơn giản
"""

def main():
    # =================== 1. In dữ liệu ra màn hình ===================
    # Sử dụng hàm print() để hiển thị thông tin
    print("Chào mừng bạn đến với bài học Python đầu tiên!")
    print("Python là ngôn ngữ lập trình dễ học và mạnh mẽ.")

    # In số
    print(123)
    print(3.14)

    # In kết hợp chuỗi và số (cần chuyển đổi kiểu dữ liệu)
    print("Số 5 là: " + str(5))

    # In nhiều giá trị cùng lúc, cách nhau bởi dấu phẩy
    print("Xin", "chào", "bạn", "đọc!")
    print("1 + 2 =", 1 + 2)


    # =================== 2. Khai báo và sử dụng biến ===================
    # Biến là nơi lưu trữ dữ liệu
    ten = "An"
    tuoi = 15
    chieu_cao = 1.65
    dat_diem_tuyet_doi = True  # Kiểu boolean

    # In giá trị của biến
    print("\n--- Thông tin cá nhân ---")
    print("Tên:", ten)
    print("Tuổi:", tuoi)
    print("Chiều cao:", chieu_cao, "m")
    print("Đạt điểm tuyệt đối:", dat_diem_tuyet_doi)


    # =================== 3. Ví dụ minh họa ===================
    # Ví dụ 1: Tính tổng hai số
    print("\n--- Ví dụ 1: Tính tổng ---")
    a = 10
    b = 25
    tong = a + b
    print(f"Tổng của {a} và {b} là: {tong}")

    # Ví dụ 2: Chào hỏi người dùng
    print("\n--- Ví dụ 2: Chào hỏi ---")
    ten_nguoi_dung = "Bình"
    print("Xin chào,", ten_nguoi_dung + "!")
    print(f"Rất vui được học cùng bạn {ten_nguoi_dung}.")

    # Ví dụ 3: Tính diện tích hình chữ nhật
    print("\n--- Ví dụ 3: Tính diện tích hình chữ nhật ---")
    chieu_dai = 8
    chieu_rong = 5
    dien_tich = chieu_dai * chieu_rong
    print(f"Diện tích hình chữ nhật {chieu_dai} x {chieu_rong} = {dien_tich}")


    # =================== 4. Bài tập nhỏ ===================
    print("\n--- Bài tập nhỏ ---")
    print("Hãy sửa đoạn code dưới đây để in ra thông tin của chính bạn!")

    # Bài tập: Thay đổi các giá trị dưới đây thành thông tin của bạn
    ho_ten = "Nhập tên bạn ở đây"        # TODO: Thay bằng tên thật của bạn
    nam_sinh = 0                        # TODO: Thay bằng năm sinh
    so_thich = "Nhập sở thích ở đây"    # TODO: Thay bằng sở thích

    # In thông tin (sẽ hiển thị sai nếu chưa sửa)
    print(f"Họ tên: {ho_ten}")
    print(f"Năm sinh: {nam_sinh} (Tuổi: {2025 - nam_sinh})")
    print(f"Sở thích: {so_thich}")

    # Gợi ý: Chạy chương trình, sau đó quay lại sửa và chạy lại


    # =================== 5. Mẹo và lưu ý ===================
    print("\n--- Mẹo và lưu ý ---")
    print("• Tên biến nên có ý nghĩa, ví dụ: 'chieu_cao' thay vì 'a'")
    print("• Dùng dấu # để ghi chú, giúp code dễ hiểu hơn")
    print("• Dùng f-string (f\"...\") để chèn biến vào chuỗi dễ dàng")
    print("• Luôn kiểm tra kiểu dữ liệu nếu gặp lỗi")


    # =================== 6. Thử thách nhỏ (nâng cao) ===================
    print("\n--- Thử thách nhỏ ---")
    print("Tính chu vi và diện tích hình tròn với bán kính r = 7")
    r = 7
    pi = 3.14
    chu_vi = 2 * pi * r
    dien_tich_tron = pi * r ** 2
    print(f"Bán kính: {r}")
    print(f"Chu vi: {chu_vi}")
    print(f"Diện tích: {dien_tich_tron}")


    # Kết thúc chương trình
    print("\nChúc mừng bạn đã hoàn thành bài học đầu tiên!")
    print("Hãy thực hành nhiều để quen với cú pháp Python nhé!")

# Gọi hàm main để thực thi chương trình
if __name__ == "__main__":
    main()
```

---

**Hướng dẫn sử dụng:**
1. Lưu đoạn code trên vào file `bai1_lam_quen_python.py`
2. Chạy bằng lệnh: `python bai1_lam_quen_python.py`
3. Thực hiện các yêu cầu trong phần **Bài tập nhỏ**

**Nội dung học được:**
- Cách sử dụng `print()`
- Khai báo biến và kiểu dữ liệu cơ bản
- In dữ liệu kết hợp với biến
- Các ví dụ thực tế và bài tập áp dụng

> ✅ Phù hợp cho người mới bắt đầu học Python!