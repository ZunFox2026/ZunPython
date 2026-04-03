from contextlib import contextmanager
import os
import time

# Bài tập 1: Quản lý trạng thái thiết bị

class DeviceManager:
    def __init__(self, device_name):
        self.device_name = device_name
        self.busy = False

    def __enter__(self):
        # Đánh dấu thiết bị đang bận
        self.busy = True
        print(f"[{self.device_name}] Bắt đầu sử dụng. Trạng thái: bận")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Đặt lại trạng thái rảnh
        self.busy = False
        print(f"[{self.device_name}] Đã giải phóng. Trạng thái: rảnh")
        return False  # Không xử lý ngoại lệ


# Bài tập 2: Tạm thời thay đổi thư mục làm việc

@contextmanager
def change_dir(target_dir):
    # Lưu thư mục hiện tại
    current_dir = os.getcwd()
    print(f"Thư mục ban đầu: {current_dir}")
    try:
        # Chuyển đến thư mục mới
        os.chdir(target_dir)
        print(f"Đã chuyển đến: {target_dir}")
        yield  # Trả quyền điều khiển cho khối with
    finally:
        # Luôn quay lại thư mục ban đầu
        os.chdir(current_dir)
        print(f"Đã quay lại thư mục: {current_dir}")


# Bài tập 3: Ghi log hành động theo thời gian

@contextmanager
def log_action(action_name):
    # Lấy thời gian hiện tại
    start_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[BẮT ĐẦU] Hành động: {action_name} | Thời gian: {start_time}")
    try:
        yield  # Thực hiện các hành động trong khối with
    finally:
        end_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[KẾT THÚC] Hành động: {action_name} | Thời gian: {end_time}")


# === Ví dụ sử dụng các lời giải ===
if __name__ == "__main__":
    print("=== Giải bài tập 1 ===")
    with DeviceManager("Máy in") as dm:
        print(f"Thiết bị đang bận: {dm.busy}")
        time.sleep(1)

    print("\n=== Giải bài tập 2 ===")
    print(f"Trước khi with: {os.getcwd()}")
    with change_dir(".."):
        print(f"Trong khối with: {os.getcwd()}")
    print(f"Sau khi with: {os.getcwd()}")

    print("\n=== Giải bài tập 3 ===")
    with log_action("Xử lý dữ liệu"):
        print("Đang thực hiện xử lý...")
        time.sleep(1)
        # Có thể có lỗi, nhưng log kết thúc vẫn chạy
        # raise ValueError("Lỗi giả lập")  # Thử bỏ comment để kiểm tra
