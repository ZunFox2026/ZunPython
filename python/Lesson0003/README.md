# Làm việc với chuỗi
Bài này sẽ hướng dẫn bạn cách làm việc với chuỗi trong Python, bao gồm các phương thức và thuộc tính của chuỗi.

## Giới thiệu
Chuỗi là một loại dữ liệu quan trọng trong lập trình, được sử dụng để lưu trữ và xử lý văn bản. Trong Python, chuỗi được thể hiện dưới dạng một dãy các ký tự được đặt trong dấu ngoặc kép hoặc ngoặc đơn. Chuỗi có thể chứa các ký tự chữ, số, ký tự đặc biệt và thậm chí là các ký tự không visible.

## Lý thuyết
Chuỗi trong Python có nhiều phương thức và thuộc tính giúp bạn có thể thao tác và xử lý chúng một cách dễ dàng. Dưới đây là một số phương thức và thuộc tính cơ bản:
- `len()`: Trả về độ dài của chuỗi.
- `upper()`: Trả về chuỗi với tất cả các ký tự được chuyển thành chữ hoa.
- `lower()`: Trả về chuỗi với tất cả các ký tự được chuyển thành chữ thường.
- `strip()`: Loại bỏ các ký tự trắng ở đầu và cuối chuỗi.
- `split()`: Chia chuỗi thành một danh sách các chuỗi con dựa trên một ký tự phân cách.
- `join()`: Nối các chuỗi con thành một chuỗi duy nhất.

Ví dụ, bạn có thể sử dụng phương thức `upper()` để chuyển một chuỗi thành chữ hoa như sau:
Xâu "hello" khi dùng `upper()` sẽ trở thành "HELLO".

## Ví dụ
Dưới đây là một số ví dụ cụ thể về việc sử dụng các phương thức và thuộc tính của chuỗi trong Python:
```python
# Ví dụ về việc sử dụng len()
chuoi = "Xin chào"
do_dai = len(chuoi)
print(f"Độ dài của chuỗi '{chuoi}' là {do_dai}")

# Ví dụ về việc sử dụng upper() và lower()
chuoi = "Hello World"
chuoi_hoa = chuoi.upper()
chuoi_thuong = chuoi.lower()
print(f"Chuỗi '{chuoi}' khi chuyển thành chữ hoa là '{chuoi_hoa}'")
print(f"Chuỗi '{chuoi}' khi chuyển thành chữ thường là '{chuoi_thuong}'")

# Ví dụ về việc sử dụng strip()
chuoi = "   Hello World   "
chuoi_loai_bo_ky_tu_trang = chuoi.strip()
print(f"Chuỗi '{chuoi}' sau khi loại bỏ ký tự trắng là '{chuoi_loai_bo_ky_tu_trang}'")

# Ví dụ về việc sử dụng split()
chuoi = "Hello,World,Python"
danh_sach_chuoi = chuoi.split(",")
print(f"Chuỗi '{chuoi}' sau khi chia thành danh sách là {danh_sach_chuoi}")

# Ví dụ về việc sử dụng join()
danh_sach_chuoi = ["Hello", "World", "Python"]
chuoi_noi = ",".join(danh_sach_chuoi)
print(f"Danh sách chuỗi {danh_sach_chuoi} sau khi nối thành chuỗi là '{chuoi_noi}'")
```

## Bài tập
Bài tập này yêu cầu bạn thực hành sử dụng các phương thức và thuộc tính của chuỗi trong Python. Hãy viết một chương trình Python để thực hiện các nhiệm vụ sau:
- Nhập vào một chuỗi từ người dùng.
- In ra độ dài của chuỗi đó.
- Chuyển chuỗi đó thành chữ hoa và in ra.
- Chuyển chuỗi đó thành chữ thường và in ra.
- Loại bỏ các ký tự trắng ở đầu và cuối chuỗi, sau đó in ra.
- Chia chuỗi đó thành một danh sách các chuỗi con dựa trên dấu cách và in ra.
- Nối các chuỗi con đó lại thành một chuỗi duy nhất với dấu phẩy ngăn cách và in ra.