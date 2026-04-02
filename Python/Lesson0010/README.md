# Bài 10: Python Cơ bản  

## Giới thiệu  
Bài 10 là bài học mở đầu cho những ai mới bắt đầu với ngôn ngữ Python. Mục tiêu của bài là giúp học sinh nắm vững cú pháp cơ bản, cách khai báo biến, các kiểu dữ liệu nguyên thuỷ, và cách thực hiện các thao tác đơn giản như nhập/xuất dữ liệu, điều kiện và vòng lặp. Sau khi hoàn thành bài này, bạn sẽ có thể viết được các script Python ngắn gọn để giải quyết các bài toán thực tế nhỏ, từ tính toán số học đến xử lý chuỗi ký tự.

## Lý thuyết  

1. **Cú pháp và indent**  
   - Python sử dụng khoảng trắng (indent) để xác định khối lệnh. Mỗi mức indent thường là 4 dấu cách hoặc một tab.  
   - Không cần dấu `;` ở cuối dòng (trừ khi muốn viết nhiều lệnh trên cùng một dòng).

2. **Biến và kiểu dữ liệu**  
   - Biến được tạo ra bằng phép gán (`=`). Không cần khai báo kiểu trước.  
   - Các kiểu dữ liệu phổ biến:  
     - `int` – số nguyên (ví dụ: `5`, `-3`)  
     - `float` – số thực (ví dụ: `3.14`)  
     - `str` – chuỗi ký tự, bao quanh bởi `'` hoặc `"` (ví dụ: `"Hello"`).  
     - `bool` – giá trị logic `True` hoặc `False`.  

3. **Toán tử**  
   - Toán tử số học: `+`, `-`, `*`, `/`, `//` (chia lấy phần nguyên), `%` (chia lấy dư), `**` (lũy thừa).  
   - Toán tử so sánh: `==`, `!=`, `<`, `>`, `<=`, `>=`.  
   - Toán tử logic: `and`, `or`, `not`.  

4. **Nhập/xuất**  
   - `print()` – in ra màn hình.  
   - `input()` – đọc chuỗi từ bàn phím (luôn trả về `str`; cần ép kiểu nếu cần số).  

5. **Cấu trúc điều khiển**  
   - `if … elif … else` – thực hiện các nhánh dựa trên điều kiện.  
   - Vòng lặp `for` – lặp qua một dãy (ví dụ: `range()` hoặc chuỗi).  
   - Vòng lặp `while` – lặp finché điều kiện còn đúng.  

## Ví dụ  

```python
# Ví dụ 1: Tính chu vi và diện tích hình chữ nhật
def tinh_hinh_chu_nhat():
    dai = float(input("Nhập chiều dài: "))
    rong = float(input("Nhập chiều rộng: "))
    chu_vi = 2 * (dai + rong)
    dien_tich = dai * rong
    print(f"Chu vi: {chu_vi}")
    print(f"Diện tích: {dien_tich}")

tinh_hinh_chu_nhat()
```

```python
# Ví dụ 2: Kiểm tra số nguyên tố đơn giản
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

so = int(input("Nhập một số: "))
if la_so_nguyen_to(so):
    print(f"{so} là số nguyên tố.")
else:
    print(f"{so} không phải là số nguyên tố.")
```

## Bài tập  

1. **Bài tập 1** – Viết chương trình nhập vào ba số thực và in ra số lớn nhất.  
2. **Bài tập 2** – Tính tổng các số chẵn từ 1 đến N (N được nhập nhập