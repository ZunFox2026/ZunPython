## Giới thiệu
Chào mừng bạn đến với **Bài 29: Python Cơ bản**! Đây là bài học tổng hợp và củng cố các kiến thức nền tảng nhất của ngôn ngữ Python, được thiết kế riêng cho người mới bắt đầu. Dù bạn đã làm quen với cú pháp, bài 29 sẽ hệ thống hóa lại cách khai báo biến, cấu trúc điều khiển và hàm cơ bản – những viên gạch đầu tiên để bạn xây dựng các ứng dụng phức tạp hơn. Mục tiêu của bài học là giúp bạn tự tin viết code Python đúng chuẩn, dễ đọc và dễ bảo trì.

## Lý thuyết
Python là ngôn ngữ thông dịch, cú pháp gọn gàng và ưu tiên tính minh bạch. Trong bài này, chúng ta tập trung vào 3 trụ cột:
- **Biến & Kiểu dữ liệu:** Python tự động suy luận kiểu (dynamic typing). Các kiểu cốt lõi gồm `int`, `float`, `str`, `bool` và cấu trúc tập hợp như `list`.
- **Cấu trúc điều khiển:** `if/elif/else` xử lý rẽ nhánh; `for` lặp qua iterable; `while` lặp khi điều kiện đúng. Lưu ý quan trọng: Python dùng **thụt lề (4 khoảng trắng)** để xác định khối lệnh, thay vì dấu ngoặc nhọn `{}`.
- **Hàm (Function):** Khai báo bằng `def`, giúp đóng gói logic, tái sử dụng mã nguồn và giảm lặp code. Có thể truyền tham số và dùng `return` để xuất kết quả.

## Ví dụ
Minh họa thực tế cho lý thuyết trên:
```python
# Ví dụ 1: Phân loại điểm & vòng lặp
danh_sach_diem = [85, 45, 92, 68]

for diem in danh_sach_diem:
    if diem >= 70:
        print(f"{diem} điểm: Đạt")
    else:
        print(f"{diem} điểm: Chưa đạt")

# Ví dụ 2: Hàm cơ bản
def tinh_dien_tich(chieu_dai, chieu_rong):
    return chieu_dai * chieu_rong

ket_qua = tinh_dien_tich(5, 3)
print(f"Diện tích: {ket_qua}")
```

## Bài tập
Thực hành ngay để khắc sâu kiến thức:
1. Viết hàm `kiem_tra_nam_nhuan(nam)` trả về `True` nếu năm chia hết cho 4 nhưng không chia hết cho 100, trừ khi chia hết cho 400.
2. Dùng vòng lặp `for` và `range()` in ra bảng cửu chương của số 7 (từ 1 đến 10).
3. (Vận dụng) Viết chương trình yêu cầu người dùng nhập một chuỗi, đếm số lượng nguyên âm (`a, e, i, o, u`) trong chuỗi đó.
*Mẹo:* Luôn kiểm tra thụt lề, dùng `type()` để debug kiểu dữ liệu. Nếu gặp lỗi, hãy đọc kỹ traceback – đó là bạn đồng hành tốt nhất của lập trình viên. Chúc bạn hoàn thành bài tập xuất sắc!