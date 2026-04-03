from contextlib import contextmanager
import time
import os

# Ví dụ 1: Quản lý tệp tin bằng class

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Mở file {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        print(f"Đóng file {self.filename}")
        if exc_type:
            print(f"Có lỗi xảy ra: {exc_value}")
        return False  # Không xử lý ngoại lệ, để chương trình xử lý

# Sử dụng
print("=== Ví dụ 1: Quản lý tệp tin ===")
with FileManager('test.txt', 'w') as f:
    f.write('Xin chào từ Context Manager!')

# Ví dụ 2: Đo thời gian thực thi

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        print("Bắt đầu đếm thời gian...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        print(f"Thời gian thực thi: {end_time - self.start_time:.4f} giây")

print("\n=== Ví dụ 2: Đo thời gian ===")
with Timer():
    time.sleep(1)
    print("Đang thực hiện công việc...")

# Ví dụ 3: Quản lý kết nối cơ sở dữ liệu giả lập

class DatabaseConnection:
    def __enter__(self):
        print("Đang kết nối đến cơ sở dữ liệu...")
        # Giả lập kết nối
        self.connection = "DB_CONNECTION_OBJECT"
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        print("Đóng kết nối cơ sở dữ liệu...")
        self.connection = None

print("\n=== Ví dụ 3: Quản lý DB ===")
with DatabaseConnection() as conn:
    print(f"Sử dụng kết nối: {conn}")
    print("Thực hiện truy vấn...")

# Ví dụ 4: Dùng @contextmanager để tạo context đơn giản

@contextmanager
def change_dir(destination):
    current_dir = os.getcwd()
    print(f"Đổi thư mục từ {current_dir} sang {destination}")
    try:
        os.chdir(destination)
        yield
    finally:
        os.chdir(current_dir)
        print(f"Trở lại thư mục: {current_dir}")

print("\n=== Ví dụ 4: Đổi thư mục tạm thời ===")
print(f"Thư mục hiện tại: {os.getcwd()}")
with change_dir('..'):
    print(f"Thư mục hiện tại trong with: {os.getcwd()}")
print(f"Thư mục sau khi thoát: {os.getcwd()}")