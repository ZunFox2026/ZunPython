import asyncio
import random

# Bài tập 1: In số từ 1 đến n với độ trễ 0.5 giây
async def print_numbers(n):
    for i in range(1, n + 1):
        print(i)
        await asyncio.sleep(0.5)  # Tạm dừng 0.5 giây

# Bài tập 2: Tải dữ liệu từ 3 URL giả lập
async def fetch_url(url):
    delay = random.uniform(1, 2)
    await asyncio.sleep(delay)
    return f"Nội dung từ {url}"

async def fetch_all_urls(urls):
    # Chạy tất cả các tác vụ đồng thời
    results = await asyncio.gather(*[fetch_url(url) for url in urls])
    return results

# Bài tập 3: Đọc đồng thời 3 tệp tin và đếm số dòng
async def count_lines(filename):
    # Mô phỏng thời gian đọc tệp
    await asyncio.sleep(0.1)
    line_count = random.randint(10, 50)
    print(f"Đã xử lý {filename}")
    return line_count

async def read_multiple_files(filenames):
    # Đọc tất cả các tệp song song
    results = await asyncio.gather(*[count_lines(name) for name in filenames])
    return sum(results)

# Bài tập 4: Mô phỏng đăng nhập người dùng
async def login_user(username):
    delay = random.uniform(1, 3)
    await asyncio.sleep(delay)
    print(f"Người dùng {username} đã đăng nhập")
    return True

async def login_all_users(usernames):
    # Đăng nhập tất cả người dùng song song
    await asyncio.gather(*[login_user(name) for name in usernames])

# Bài tập 5: Xử lý theo thứ tự hoàn thành
async def task_with_delay(name, delay):
    await asyncio.sleep(delay)
    return name

async def process_as_completed():
    # Tạo các tác vụ với độ trễ khác nhau
    tasks = [
        task_with_delay("Tác vụ 1", 2),
        task_with_delay("Tác vụ 2", 1),
        task_with_delay("Tác vụ 3", 3)
    ]
    
    # Xử lý theo thứ tự hoàn thành
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(f"{result} hoàn thành!")

# Hàm main để kiểm tra bài tập
async def main():
    print("=== Bài tập 1: In số từ 1 đến 5 ===")
    await print_numbers(5)
    
    print("\n=== Bài tập 2: Tải đồng thời 3 URL ===")
    urls = ["https://site1.com", "https://site2.com", "https://site3.com"]
    results = await fetch_all_urls(urls)
    for res in results:
        print(res)
    
    print("\n=== Bài tập 3: Đọc 3 tệp tin ===")
    filenames = ["file1.txt", "file2.txt", "file3.txt"]
    total = await read_multiple_files(filenames)
    print(f"Tổng số dòng: {total}")
    
    print("\n=== Bài tập 4: Đăng nhập 5 người dùng ===")
    usernames = [f"user{i}" for i in range(1, 6)]
    await login_all_users(usernames)
    
    print("\n=== Bài tập 5: Xử lý theo thứ tự hoàn thành ===")
    await process_as_completed()

if __name__ == "__main__":
    asyncio.run(main())