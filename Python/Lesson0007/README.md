# README – Bài 7 (Cấp Cơ bản)

## Giới thiệu  
Bài 7 là phần tiếp theo của chuỗi bài học lập trình Python cho người mới bắt đầu. Mục tiêu của bài này là giúp sinh viên nắm vững **cấu trúc điều khiển luồng** bằng cách sử dụng câu lệnh `if‑elif‑else` và vòng lặp `while`. Khi hoàn thành bài này, bạn sẽ có thể:

- Xác định điều kiện và viết ra các nhánh xử lý khác nhau.  
- Sử dụng vòng lặp để lặp lại một đoạn code cho đến khi một điều kiện nhất định được thỏa mãn.  
- Kết hợp cả hai cấu trúc để giải quyết các bài toán thực tế như kiểm tra đầu vào, đếm số lượng, hoặc tìm kiếm trong danh sách.  

Nội dung bài tập được thiết kế để củng cố lý thuyết thông qua các ví dụ minh họa và các bài tập thực hành dần tăng độ khó.

## Lý thuyết  

### 1. Câu lệnh điều kiện `if‑elif‑else`  
Cú pháp cơ bản:

```python
if <điều kiện 1>:
    # khối lệnh khi điều kiện 1 đúng
elif <điều kiện 2>:
    # khối lệnh khi điều kiện 1 sai và điều kiện 2 đúng
else:
    # khối lệnh khi tất cả các điều kiện trên đều sai
```

- Mỗi điều kiện là một biểu thức logic trả về `True` hoặc `False`.  
- Khi một điều kiện đúng, khối lệnh tương ứng được thực hiện và các điều kiện còn lại bị bỏ qua.  
- `elif` (từ “else if”) có thể xuất hiện 0 hoặc nhiều lần; `else` là tùy chọn.

### 2. Vòng lặp `while`  
Cú pháp:

```python
while <điều kiện>:
    # khối lệnh lặp lại
```

- Vòng lặp sẽ tiếp tục thực hiện khối lệnh miễn là điều kiện còn `True`.  
- Nên luôn có một cách để thay đổi điều kiện bên trong vòng lặp (thường là cập nhật biến) để tránh lặp vô hạn.  

### 3. Kết hợp `if` và `while`  
Trong thực tế, chúng ta thường đặt các câu lệnh điều kiện bên trong vòng lặp để xử lý từng bước lặp (ví dụ: kiểm tra đầu vào hợp lệ, dừng khi người dùng nhập một giá trị cụ thể).

## Ví dụ  

**Bài toán:** Nhập liên tục các số nguyên từ bàn phím và tính tổng cho đến khi người dùng nhập số `0`. Sau đó in ra tổng và trung bình của các số đã nhập (không kể số `0`).

```python
def tinh_tong_trung_binh():
    tong = 0
    dem = 0

    while True:                     # Vòng lặp vô hạn, sẽ break khi đáp ứng điều kiện
        try:
            so = int(input("Nhập một số nguyên (0 để dừng): "))
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")
            continue                # quay lại đầu vòng lặp để yêu cầu nhập lại

        if so == 0:                 # Điều kiện dừng
            break

        tong += so                  # Cập nhật tổng
        dem += 1                    # Đếm số lượng số hợp lệ

    if dem == 0:
        print("Bạn chưa nhập bất kỳ số nào khác 0.")
    else:
        trung_binh = tong / dem
        print(f"Tổng của {dem} số là: {tong}")
        print(f"Trung bình là: {trung_binh:.2f}")

# G CALL