import asyncio
import random

# Bài tập 1: In số từ 1 đến n với độ trễ 0.5 giây
async def print_numbers(n):
    # TODO: Viết hàm in từ 1 đến n, mỗi lần in cách nhau 0.5 giây
    pass

# Bài tập 2: Tải dữ liệu từ 3 URL giả lập
async def fetch_url(url):
    # TODO: Mô phỏng tải dữ liệu từ URL với độ trễ ngẫu nhiên từ 1-2 giây
    # Trả về: f"Nội dung từ {url}"
    pass

async def fetch_all_urls(urls):
    # TODO: Dùng asyncio.gather để tải đồng thời tất cả URL
    pass

# Bài tập 3: Đọc đồng thời 3 tệp tin và đếm số dòng
async def count_lines(filename):
    # TODO: Mô phỏng đọc tệp tin, trả về số dòng ngẫu nhiên từ 10-50
    # In ra: Đã xử lý {filename}
    pass

async def read_multiple_files(filenames):
    # TODO: Đọc tất cả các tệp và trả về tổng số dòng
    pass

# Bài tập 4: Mô phỏng đăng nhập người dùng
async def login_user(username):
    # TODO: Mô phỏng đăng nhập với độ trễ 1-3 giây
    # In ra: Người dùng {username} đã đăng nhập
    # Trả về True nếu thành công
    pass

async def login_all_users(usernames):
    # TODO: Đăng nhập tất cả người dùng song song
    pass

# Bài tập 5: Xử lý theo thứ tự hoàn thành
async def task_with_delay(name, delay):
    # TODO: Chờ delay giây rồi in ra hoàn thành
    # Trả về tên tác vụ
    pass

async def process_as_completed():
    # TODO: Dùng asyncio.as_completed để xử lý các tác vụ theo thứ tự hoàn thành
    # Tạo 3 tác vụ với độ trễ 2, 1, 3 giây
    # In ra thứ tự hoàn thành
    pass