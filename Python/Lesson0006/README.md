# Bài 6 – Vòng lặp `for` (Cấp cơ bản)

## Giới thiệu  
Vòng lặp là một trong những khái niệm cốt lõi của lập trình, cho phép thực hiện lặp lại một đoạn mã nhiều lần mà không cần viết lại code. Ở cấp cơ bản, Python cung cấp hai loại vòng lặp chính: `while` và `for`. Bài này tập trung vào vòng lặp `for` – cách duyệt qua các phần tử của một chuỗi (list, tuple, chuỗi ký tự, range…) một cách đơn giản và trực quan. Sau khi hoàn thành bài này, bạn sẽ biết cách:

- Tạo và sử dụng vòng lặp `for` với `range()`.
- Duyệt qua các cấu trúc dữ liệu phổ biến.
- Áp dụng lệnh `break` và `continue` để điều khiển luồng thực thi.
- Viết các chương trình nhỏ giải quyết bài toán thực tế như tính tổng, đếm phần tử, tạo bảng cửu chương.

## Lý thuyết  

### Cú pháp cơ bản  
```python
for biến in iterable:
    # thân vòng lặp
```
- `biến`: tên tạm để lưu giá trị phần tử hiện tại trong mỗi lần lặp.
- `iterable`: đối tượng có thể lặp (list, tuple, string, range, …).  
Mỗi lần lặp, Python lấy một phần tử từ `iterable`, gán cho `biến` và thực thi thân vòng lặp. Khi hết phần tử, vòng lặp kết thúc và chương trình tiếp tục lệnh sau vòng lặp.

### Hàm `range()`  
`range(start, stop, step)` tạo ra một dãy số nguyên:
- `start`: giá trị đầu tiên (mặc định 0).
- `stop`: giá trị cuối (không bao gồm).
- `step`: bước nhảy (mặc định 1).  
Ví dụ: `range(2, 10, 2)` → `[2, 4, 6, 8]`.

### Lệnh điều khiển trong vòng lặp  
- `break`: thoát ngay khỏi vòng lặp, không quan tâm đến điều kiện lặp còn lại.  
- `continue`: bỏ qua phần còn lại của thân vòng lặp trong lần lặp hiện tại và chuyển sang lần lặp tiếp theo.

## Ví dụ  

### 1. In ra các số từ 1 đến 5  
```python
for i in range(1, 6):   # range(1,6) tạo 1,2,3,4,5
    print(i)
```
**Kết quả:**  
```
1
2
3
4
5
```

### 2. Tính tổng các số lẻ từ 1 đến 20  
```python
tong = 0
for i in range(1, 21):          # 1..20
    if i % 2 == 1:              # số lẻ
        tong += i
print("Tổng các số lẻ:", tong)
```
**Kết quả:** `Tổng các số lẻ: 100`

### 3. Duyệt qua danh sách tên và in ra chào hỏi  
```python
ten_list = ["An", "Bình", "Cường", "Dung"]
for ten in ten_list:
    print(f"Xin chào, {ten}!")
```
**Kết quả:**  
```
Xin chào, An!
Xin chào, Bình!
Xin chào, Cường!
Xin chào, Dung!
```

### 4. Sử dụng `break` và `continue`  
```python
for i in range(,