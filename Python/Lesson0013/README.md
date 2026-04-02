# README – Bài 13 (Cấp Cơ bản): Vòng lặp `for` trong Python  

---

## Giới thiệu  

Bài học này giới thiệu cách sử dụng vòng lặp `for` – một trong những công cụ lặp cơ bản nhất trong Python. Với `for`, bạn có thể duyệt qua các phần tử của một chuỗi, danh sách, tuple, từ điển hoặc bất kỳ đối tượng nào hỗ trợ giao thức iterable. Việc nắm vững vòng lặp `for` giúp bạn viết mã ngắn gọn, dễ đọc và hiệu quả hơn khi thực hiện các tác vụ lặp lại như xử lý dữ liệu, tạo báo cáo, hoặc thực hiện các phép tính lặp lại.  

---

## Lý thuyết  

### Cú pháp cơ bản  

```python
for bien in iterable:
    # thân vòng lặp
    # có thể sử dụng bien ở mỗi lần lặp
```

- **`bien`**: biến tạm thời nhận giá trị của phần tử hiện tại trong `iterable`.  
- **`iterable`**: đối tượng có thể lặp (list, tuple, string, range, dict, set, …).  
- Thân vòng lặp được thụt lề (보통 4 dấu cách) và sẽ thực hiện cho mỗi phần tử cho tới khi hết `iterable`.  

### Các hàm hỗ trợ thường dùng  

| Hàm | Mô tả | Ví dụ |
|-----|-------|-------|
| `range(start, stop[, step])` | Tạo dãy số nguyên | `range(5)` → 0,1,2,3,4 |
| `enumerate(iterable, start=0)` | Trả về cặp (index, giá trị) | `enumerate(['a','b'])` → (0,'a'), (1,'b') |
| `zip(*iterables)` | Ghép các iterable thành tuple | `zip([1,2], ['a','b'])` → (1,'a'), (2,'b') |
| `reversed(iterable)` | Duyệt ngược | `reversed([1,2,3])` → 3,2,1 |

### Các từ khóa điều khiển vòng lặp  

- `break`: thoát ngay khỏi vòng lặp.  
- `continue`: bỏ qua phần còn lại của lần lặp hiện tại và chuyển sang lần lặp tiếp theo.  
- `else`: (tùy chọn) thực hiện sau khi vòng lặp kết thúc **không** gặp `break`.  

---

## Ví dụ  

### 1. In ra các số từ 0 đến 4  

```python
for i in range(5):
    print(i)
```
**Kết quả:**  
```
0
1
2
3
4
```

### 2. Duyệt qua danh sách tên và in ra lời chào  

```python
ten_list = ["An", "Bình", "Cường"]
for ten in ten_list:
    print(f"Xin chào, {ten}!")
```
**Kết quả:**  
```
Xin chào, An!
Xin chào, Bình!
Xin chào, Cường!
```

### 3. Sử dụng `enumerate` để biết vị trí phần tử  

```python
mon_hoc = ["Toán", "Lý", "Hóa"]
for idx, mon in enumerate(mon_hoc, start=1):
    print(f"{idx}. {mon}")
```
**Kết quả:**  
```
1. Toán
2. Lý
3. Hóa
```

### 4. Lặp qua từ điển  

```python
diem = {"An": 8.5, "Bình": 7.0, "Cường": 9.0}
for ten, diem_so in diem.items():
    print(f"{ten}: {diem_so}")
}