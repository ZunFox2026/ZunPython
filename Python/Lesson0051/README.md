# Bài 51: Xử Lý Tập Tin và Thư Mục với Module `os` và `shutil`

## Giới thiệu

Trong lập trình Python, việc thao tác với hệ thống tập tin và thư mục là một nhu cầu phổ biến. Hai module quan trọng hỗ trợ công việc này là `os` và `shutil`. Module `os` cung cấp các hàm để tương tác với hệ điều hành, giúp tạo, xóa, đổi tên thư mục, kiểm tra sự tồn tại của tập tin, v.v. Module `shutil` hỗ trợ các thao tác cấp cao hơn như sao chép, di chuyển, nén và giải nén thư mục.

## Lý thuyết

- **Module `os`**: Dùng để làm việc với hệ điều hành. Một số hàm phổ biến:
  - `os.getcwd()`: Lấy đường dẫn thư mục làm việc hiện tại.
  - `os.listdir(path)`: Liệt kê các tập tin và thư mục trong đường dẫn.
  - `os.mkdir(path)`: Tạo thư mục mới.
  - `os.remove(path)`: Xóa tập tin.
  - `os.path.exists(path)`: Kiểm tra sự tồn tại của tập tin hoặc thư mục.

- **Module `shutil`**: Hỗ trợ sao chép và di chuyển:
  - `shutil.copy(src, dst)`: Sao chép tập tin.
  - `shutil.move(src, dst)`: Di chuyển hoặc đổi tên tập tin/thư mục.
  - `shutil.rmtree(path)`: Xóa cả thư mục và toàn bộ nội dung bên trong.

## Ví dụ

```python
import os
import shutil

# Tạo thư mục mới
os.mkdir("thu_muc_moi")

# Tạo một tập tin trong thư mục đó
with open("thu_muc_moi/file.txt", "w") as f:
    f.write("Xin chào từ Python!")

# Sao chép tập tin
shutil.copy("thu_muc_moi/file.txt", "thu_muc_moi/file_copy.txt")

# Di chuyển tập tin
shutil.move("thu_muc_moi/file_copy.txt", "file_di_chuyen.txt")

# Kiểm tra và xóa thư mục
if os.path.exists("thu_muc_moi"):
    shutil.rmtree("thu_muc_moi")

print("Hoàn tất thao tác với tập tin và thư mục!")
```

## Bài tập

1. Viết chương trình tạo một thư mục tên `data`, sau đó tạo 3 tập tin `.txt` bên trong.
2. Sao chép toàn bộ thư mục `data` thành `backup_data`.
3. Đổi tên tập tin `data/file1.txt` thành `data/renamed.txt`.
4. Viết hàm kiểm tra xem một thư mục có tồn tại không, nếu có thì xóa nó.

> Gợi ý: Sử dụng `os.path.exists()` và `shutil.rmtree()`.