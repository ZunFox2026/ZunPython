# README – Bài 12: Python Cơ bản  

## Giới thiệu  
Bài học này là phần **cơ bản** trong chuỗi khóa học Python. Mục tiêu là giúp người học nắm vững cách **cài đặt môi trường**, **cú pháp cơ bản**, **biến và kiểu dữ liệu**, cũng như **cấu trúc điều khiển** (if‑else, vòng lặp). Sau khi hoàn thành bài này, bạn sẽ có thể viết các chương trình ngắn gọn để thực hiện các tác vụ xử lý chuỗi, số học đơn giản và thao tác với danh sách.

> **Đối tượng:** Sinh viên, người mới bắt đầu học lập trình, hoặc ai muốn ôn lại kiến thức nền tảng Python.  
> **Thời gian dự kiến:** 45‑60 phút (bao gồm lý thuyết, ví dụ và bài tập).  

## Lý thuyết  

### 1. Cài đặt và chạy Python  
- Tải Python từ <https://www.python.org/downloads/> (phiên bản 3.11 trở lên).  
- Kiểm tra phiên bản bằng lệnh `python --version` hoặc `python3 --version` trong terminal.  
- Chạy script: `python ten_file.py` hoặc sử dụng môi trường tương tác `python` (REPL).  

### 2. Cú pháp cơ bản  
- **Indent (thụt lề):** Python dùng khoảng trắng (thường là 4 spaces) để xác định khối lệnh.  
- **Comment:** `#` cho comment một dòng; `'''` hoặc `"""` cho comment nhiều dòng.  
- **Kết thúc lệnh:** không cần dấu `;`, nhưng có thể dùng để ghi nhiều lệnh trên một dòng.  

### 3. Biến và kiểu dữ liệu  
| Kiểu | Mô tả | Ví dụ |
|------|-------|-------|
| `int` | Số nguyên | `age = 25` |
| `float` | Số thực | `height = 1.75` |
| `str` | Chuỗi ký tự | `name = "An"` |
| `bool` | Logic True/False | `is_student = True` |
| `list` | Danh sách có thứ tự, thay đổi được | `scores = [8, 9, 7]` |
| `tuple` | Tuple không thay đổi | `point = (3, 4)` |
| `dict` | Từ điển key‑value | `info = {"tuoi":20, "lop":"12A"}` |

### 4. Toán tử và biểu thức  
- Toán tử số học: `+ - * / // % **`  
- Toán tử so sánh: `== != < > <= >=`  
- Toán tử logic: `and or not`  
- Toán tử gán: `+= -= *= /= %= **=`  

### 5. Cấu trúc điều khiển  
- **If‑elif‑else:**  
  ```python
  if diem >= 8.5:
      xep_loai = "Giỏi"
  elif diem >= 6.5:
      xep_loai = "Khá"
  else:
      xep_loai = "Yếu"
  ```
- **Vòng lặp `for`:** lặp qua iterable (list, range, string…).  
- **Vòng lặp `while`:** lặp finché điều kiện còn đúng.  

### 6. Hàm cơ bản  
```python
def binh_phuong(n):
    """Trả về bình phương của n."""
    return n * n
```
- Định nghĩa bằng `def`, có docstring (chuỗi triple quotes) để mô tả.  
- Gọi hàm: `ket_qua = binh_phuong(5)`.  

## Ví dụ  

### Ví dụ 1: Chương trình hello world  
```python
# hello.py
print("Xin chào, thế giới!")
```
Chạy: `python hello.py` → xuất ra `Xin chào, thế giới!`.

### Ví dụ 2: Tínhừ