# README – Bài 1: Cập nhật biến và thực hiện các phép toán cơ bản (Cấp cơ bản)

## Giới thiệu
Bài tập này giúp bạn làm quen với cách khai báo biến, gán giá trị và thực hiện các phép toán số học đơn giản trong Python. Đây là nền tảng quan trọng để bạn có thể viết các chương trình phức tạp hơn sau này, từ xử lý dữ liệu cho đến xây dựng trò chơi hoặc ứng dụng web. Khi hoàn thành bài này, bạn sẽ biết cách:

- Tạo và sử dụng biến để lưu trữ dữ liệu.
- Thực hiện phép cộng, trừ, nhân, chia và lấy phần dư.
- In kết quả ra màn hình bằng hàm `print()`.

## Lý thuyết
Trong Python, **biến** là tên được gán cho một vùng nhớ để lưu trữ một giá trị cụ thể. Không cần khai báo kiểu dữ liệu trước; Python tự động suy luận kiểu dựa trên giá trị gán.

Cú pháp khai báo biến:
```python
ten_bien = gia_tri
```

Các toán tử số học phổ biến:
| Toán tử | Mô tả                | Ví dụ          |
|---------|----------------------|----------------|
| `+`     | Cộng                 | `a + b`        |
| `-`     | Trừ                  | `a - b`        |
| `*`     | Nhân                 | `a * b`        |
| `/`     | Chia (kết quả float) | `a / b`        |
| `//`    | Chia lấy phần nguyên | `a // b`       |
| `%`     | Lấy phần dư (modulo) | `a % b`        |
| `**`    | Lũy thừa             | `a ** b`       |

Khi in ra màn hình, chúng ta thường dùng hàm `print()` và có thể kết hợp chuỗi với biến bằng f‑string (Python 3.6+):
```python
print(f"Tổng của {a} và {b} là {a + b}")
```

## Ví dụ
Dưới đây là một chương trình ngắn tính tổng và tích của hai số mà người dùng nhập từ bàn phím.

```python
# Nhập hai số từ người dùng
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

# Tính toán
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b if b != 0 else "Không thể chia cho 0"
chia_lay_nguyen = a // b if b != 0 else "Không thể chia cho 0"
phan_du = a % b if b != 0 else "Không thể chia cho 0"

# In kết quả
print(f"\nKết quả cho {a} và {b}:")
print(f"Tổng: {tong}")
print(f"Hiệu: {hieu}")
print(f"Tích: {tich}")
print(f"Thương: {thuong}")
print(f"Chia lấy phần nguyên: {chia_lay_nguyen}")
print(f"Phần dư: {phan_du}")
```

**Giải thích:**
- `input()` trả về chuỗi; chúng ta chuyển đổi sang `float` để chấp nhận cả số nguyên và số thập phân.
- Các phép toán được thực hiện và lưu vào các biến tương ứng.
- Để tránh lỗi chia cho 0, chúng ta dùng biểu thức điều kiện (`if b != 0 else …`).
- Cuối cùng, `print()` với f‑string hiển thị kết quả rõ ràng.

## Bài tập
1. **Tính chu vi và diện tích hình chữ nhật**  
   - Yêu cầu: Nhập chiều dài và chiều rộng (số thực).