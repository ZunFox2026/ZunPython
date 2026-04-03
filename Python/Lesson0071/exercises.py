import asyncio
import aiohttp

# Bài tập 1: Tải danh sách URL và in độ dài nội dung
async def download_and_print_length(urls):
    # TODO: Viết hàm tải từng URL và in độ dài nội dung
    pass

# Bài tập 2: Chạy 5 tác vụ chậm song song
async def slow_counter(name, count):
    # TODO: In số từ 1 đến count, mỗi số cách nhau 0.5s
    pass

async def run_parallel_counters():
    # TODO: Chạy 5 hàm slow_counter song song
    pass

# Bài tập 3: In số chẵn và lẻ song song
async def print_even_numbers():
    # TODO: In số chẵn từ 1 đến 10, mỗi số cách 0.5s
    pass

async def print_odd_numbers():
    # TODO: In số lẻ từ 1 đến 10, mỗi số cách 0.5s
    pass

async def run_even_odd_parallel():
    # TODO: Chạy cả hai hàm song song
    pass

# Bài tập 4: Máy khách kết nối đến máy chủ
async def client_connect_to_server():
    # TODO: Kết nối đến 127.0.0.1:8888, gửi b"Xin chao", nhận và in phản hồi
    pass

# Bài tập 5: Xử lý lỗi trong hàm async
async def risky_task(url):
    # TODO: Gọi URL, nếu lỗi (timeout, 404...) thì in thông báo
    pass