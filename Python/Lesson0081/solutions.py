import time
import os
from contextlib import contextmanager

### Bài tập 1: Tạo context manager SuppressErrors
class SuppressErrors:
    def __init__(self, *exceptions):
        # Nhận danh sách các kiểu exception cần bỏ qua
        self.exceptions = exceptions

    def __enter__(self):
        # Không cần làm gì đặc biệt khi bắt đầu
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Nếu exception thuộc loại được chỉ định, bỏ qua (trả về True)
        # Nếu không, để exception lan ra (trả về False)
        if exc_type is not None:
            if issubclass(exc_type, self.exceptions):
                print(f"Bỏ qua lỗi: {exc_value}")
                return True  # Ngăn exception lan ra
        return False  # Cho phép exception lan ra nếu không nằm trong danh sách


### Bài tập 2: Timer ghi log vào file
class TimerLog:
    def __init__(self, log_file):
        self.log_file = log_file
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        # Mở file log để ghi (chế độ append)
        self.log = open(self.log_file, 'a')
        self.log.write(f"Khối lệnh bắt đầu lúc: {time.ctime()}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        duration = end_time - self.start_time
        self.log.write(f", kết thúc lúc: {time.ctime()}, thời gian: {duration:.4f}s\n")
        self.log.close()
        if exc_type is not None:
            print(f"Lỗi xảy ra trong khối: {exc_value}")
        return False


### Bài tập 3: ReadOnlyFile
class ReadOnlyFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        # Mở file ở chế độ chỉ đọc
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file and not self.file.closed:
            self.file.close()
            print(f"File {self.filename} đã được đóng an toàn.")
        return False


### Bài tập 4: ChangeDir an toàn
class ChangeDir:
    def __init__(self, path):
        self.path = path
        self.original_dir = None

    def __enter__(self):
        self.original_dir = os.getcwd()
        print(f"Thư mục ban đầu: {self.original_dir}")
        os.chdir(self.path)
        print(f"Đã chuyển đến: {self.path}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.original_dir)
        print(f"Đã quay lại thư mục ban đầu: {self.original_dir}")
        # Luôn quay lại, dù có lỗi
        return False


### Bài tập 5: In thông báo với @contextmanager
@contextmanager
def log_block(name):
    print(f"Bắt đầu khối '{name}'...")
    try:
        yield
    finally:
        print(f"Kết thúc khối '{name}'.")

# Cách sử dụng:
# with log_block("Xử lý dữ liệu"):
#     print("Đang xử lý...")
#     time.sleep(0.5)