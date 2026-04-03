import json
import os

#####################
# Bài tập 1: Ghi log thời gian bắt đầu và kết thúc
#####################
class LogExecution:
    def __init__(self, action_name="Hành động"):
        self.action_name = action_name

    def __enter__(self):
        self.start_time = time.time()
        print(f"[LOG] Bắt đầu {self.action_name} tại {time.ctime()}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        print(f"[LOG] Kết thúc {self.action_name} tại {time.ctime()}")
        print(f"[LOG] Thời gian thực thi: {end_time - self.start_time:.4f} giây")
        return False


#####################
# Bài tập 2: Quản lý file JSON an toàn
#####################
class JSONFile:
    def __init__(self, filename, data=None):
        self.filename = filename
        self.data = data or {}
        self.original_data = None  # Để kiểm tra thay đổi

    def __enter__(self):
        # Đọc dữ liệu nếu file tồn tại
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Nếu file không tồn tại hoặc lỗi định dạng, dùng dữ liệu mặc định
            self.data = self.data or {}
        self.original_data = self.data.copy()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Ghi lại nếu dữ liệu thay đổi
        if self.data != self.original_data:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=4)
            print(f"Dữ liệu đã được lưu vào {self.filename}")
        return False


#####################
# Bài tập 3: Đếm số dòng xử lý trong file
#####################
class CountLines:
    def __init__(self, filename):
        self.filename = filename
        self.line_count = 0

    def __enter__(self):
        self.file = open(self.filename, 'r', encoding='utf-8')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print(f"Đã xử lý tổng cộng {self.line_count} dòng.")
        return False

    def readlines(self):
        lines = self.file.readlines()
        self.line_count += len(lines)
        return lines


#####################
# Bài tập 4: Thay đổi biến môi trường tạm thời
#####################
@contextmanager
def temporary_env(name, value):
    old_value = os.environ.get(name)  # Lưu giá trị cũ
    os.environ[name] = value
    try:
        yield
    finally:
        # Khôi phục giá trị cũ
        if old_value is None:
            os.environ.pop(name, None)
        else:
            os.environ[name] = old_value


#####################
# Bài tập 5: Xử lý ngoại lệ và ghi log
#####################
class SafeExecution:
    def __init__(self, log_file="error.log"):
        self.log_file = log_file

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(f"Lỗi: {exc_type.__name__}: {exc_value}\n")
            print(f"Lỗi đã được ghi vào {self.log_file}")
            return True  # Kìm nén ngoại lệ
        return False