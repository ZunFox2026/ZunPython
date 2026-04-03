import asyncio
import random

# Ví dụ 1: Tải dữ liệu từ nhiều URL đồng thời
class AsyncDownloader:
    async def fetch_data(self, url):
        # Mô phỏng thời gian tải dữ liệu
        delay = random.uniform(1, 3)
        print(f"Đang tải từ {url} (mất {delay:.2f}s)")
        await asyncio.sleep(delay)
        return f"Dữ liệu từ {url}"

    async def download_all(self, urls):
        print("Bắt đầu tải đồng thời...")
        # Chạy tất cả các tác vụ song song
        results = await asyncio.gather(*[self.fetch_data(url) for url in urls])
        return results

# Ví dụ 2: Xử lý nhiều tệp tin cùng lúc
async def read_file(filename):
    # Mô phỏng đọc tệp tin (thay vì dùng open() đồng bộ, dùng async)
    await asyncio.sleep(0.1)  # Giả lập thời gian I/O
    # Trả về số dòng trong tệp tin (mô phỏng)
    line_count = random.randint(50, 200)
    print(f"Đã đọc {filename}: {line_count} dòng")
    return line_count

async def process_files(filenames):
    print("Bắt đầu đọc các tệp tin...")
    total_lines = 0
    # Đọc tất cả các tệp đồng thời
    results = await asyncio.gather(*[read_file(name) for name in filenames])
    total_lines = sum(results)
    print(f"Tổng cộng: {total_lines} dòng từ {len(filenames)} tệp tin.")
    return total_lines

# Ví dụ 3: Mô phỏng tác vụ dài hạn với báo cáo tiến độ
async def long_task(task_id, duration):
    print(f"Tác vụ {task_id} bắt đầu (dự kiến {duration}s)")
    for i in range(duration):
        await asyncio.sleep(1)
        print(f"Tác vụ {task_id}: {i+1}/{duration} giây")
    print(f"Tác vụ {task_id} hoàn thành!")
    return f"Tác vụ {task_id} hoàn tất sau {duration} giây"

async def run_multiple_tasks():
    print("Chạy nhiều tác vụ bất đồng bộ...")
    tasks = [
        long_task(1, 3),
        long_task(2, 2),
        long_task(3, 4)
    ]
    results = await asyncio.gather(*tasks)
    return results

# Hàm chính để chạy các ví dụ
def main():
    print("=== Ví dụ 1: Tải đồng thời từ nhiều URL ===")
    downloader = AsyncDownloader()
    urls = ["https://api1.example.com", "https://api2.example.com", "https://api3.example.com"]
    results1 = asyncio.run(downloader.download_all(urls))
    for result in results1:
        print(result)
    
    print("\n=== Ví dụ 2: Đọc nhiều tệp tin đồng thời ===")
    filenames = ["data1.txt", "data2.txt", "data3.txt", "data4.txt"]
    total = asyncio.run(process_files(filenames))
    
    print("\n=== Ví dụ 3: Chạy nhiều tác vụ dài hạn ===")
    results3 = asyncio.run(run_multiple_tasks())
    for res in results3:
        print(res)

if __name__ == "__main__":
    main()