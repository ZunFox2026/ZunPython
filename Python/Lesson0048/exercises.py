from contextlib import contextmanager
import os
import time

# Bài tập 1: Viết Context Manager để tạm thời thay đổi thư mục làm việc
# Gợi ý: Lưu thư mục hiện tại, đổi sang thư mục mới, rồi quay lại

class TemporaryDirectory:
    # Hoàn thiện class này
    pass

# Bài tập 2: Viết Context Manager để đếm số lần gọi hàm
# Gợi ý: Dùng biến toàn cục hoặc attribute để đếm

class CallCounter:
    # Hoàn thiện class này
    pass

# Bài tập 3: Viết Context Manager để tắt/bật logging
# Gợi ý: Giả lập bằng biến toàn cục LOG_ENABLED

LOG_ENABLED = True

class LoggingControl:
    # Hoàn thiện class này
    pass

# Bài tập 4: Viết Context Manager tạo file tạm và tự xóa
# Gợi ý: Dùng @contextmanager và os.remove()

@contextmanager
def temporary_file(filename):
    # Hoàn thiện hàm này
    pass

# Bài tập 5: Viết Context Manager giới hạn thời gian thực thi (timeout giả lập)
# Gợi ý: Đo thời gian, in cảnh báo nếu vượt quá timeout

class Timeout:
    def __init__(self, seconds):
        self.seconds = seconds
    # Hoàn thiện class
    pass