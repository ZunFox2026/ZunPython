import time
import os
from datetime import datetime

class TimerContext:
    """Context Manager để đo thời gian thực thi"""
    def __enter__(self):
        self.start_time = time.time()
        print(f"[LOG] Bắt đầu thực thi lúc {datetime.now().strftime('%H:%M:%S')}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed = self.end_time - self.start_time
        print(f"[LOG] Kết thúc thực thi lúc {datetime.now().strftime('%H:%M:%S')}")
        print(f"[THỜI GIAN] Thực thi mất {elapsed:.4f} giây")
        # Không xử lý lỗi, để lỗi ném ra ngoài
        return False


class DatabaseConnection:
    """Mô phỏng Context Manager quản lý kết nối CSDL"""
    def __enter__(self):
        print("Đang kết nối đến cơ sở dữ liệu...")
        # Giả lập kết nối
        self.connection = "DB_CONNECTION_OBJECT"
        print("✅ Kết nối thành công")
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        print("Đang đóng kết nối...")
        self.connection = None
        print("❌ Đã đóng kết nối")
        if exc_type:
            print(f"⚠️ Lỗi xảy ra trong quá trình làm việc: {exc_value}")
        return False  # Không bắt lỗi


class LoggerContext:
    """Context Manager ghi log khi bắt đầu và kết thúc"""
    def __init__(self, message=""):n        self.message = message

    def __enter__(self):
        print(f"[LOG] BẮT ĐẦU: {self.message}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"[LOG] LỖI: {exc_value}")
        print(f"[LOG] KẾT THÚC: {self.message}")
        return False  # Cho phép lỗi ném ra


# === VÍ DỤ CHẠY THỬ ===

if __name__ == "__main__":
    print("=== VÍ DỤ 1: Đo thời gian thực thi ===")
    with TimerContext():
        time.sleep(1)  # Giả lập công việc mất 1 giây
        print("Đang thực hiện công việc...")

    print("\n=== VÍ DỤ 2: Quản lý kết nối CSDL ===")
    try:
        with DatabaseConnection() as db:
            print(f"Sử dụng kết nối: {db}")
            # Giả lập truy vấn
            print("Truy vấn dữ liệu...")
            # Gây lỗi để kiểm tra __exit__
            # raise ValueError("Lỗi truy vấn")
    except Exception as e:
        print(f"Lỗi bị bắt ở ngoài: {e}")

    print("\n=== VÍ DỤ 3: Ghi log tự động ===")
    with LoggerContext("Xử lý dữ liệu người dùng"):
        print("Đang xử lý...")
        # Giả lập lỗi
        # raise RuntimeError("Xử lý thất bại")
