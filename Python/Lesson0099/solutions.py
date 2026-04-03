import asyncio
import aiohttp
import random

# Bài tập 1: Viết một coroutine `wait_random`
async def wait_random(name: str, max_delay: float):
    # Tạo khoảng thời gian chờ ngẫu nhiên
    delay = random.uniform(0, max_delay)
    print(f"{name} sẽ chờ {delay:.2f}s")
    await asyncio.sleep(delay)
    print(f"{name} đã hoàn thành sau {delay:.2f}s")

# Bài tập 2: Chạy 5 coroutine đồng thời
async def run_tasks_concurrently():
    print("\n--- Bài tập 2: Chạy 5 tác vụ ngẫu nhiên ---")
    start = time.time()
    
    # Tạo danh sách các coroutine
    tasks = [wait_random(f"Task-{i}", 3.0) for i in range(1, 6)]
    
    # Chạy song song
    await asyncio.gather(*tasks)
    
    print(f"Tổng thời gian: {time.time() - start:.2f}s")

# Bài tập 3: Tải URL với timeout
async def fetch_with_timeout(session, url):
    try:
        # Đặt thời gian chờ tối đa là 2 giây
        async with asyncio.timeout(2):  # Python 3.11+
            async with session.get(url) as response:
                content = await response.text()
                print(f"{url}: thành công, {len(content)} ký tự")
                return len(content)
    except TimeoutError:
        print(f"{url}: Timeout")
        return 0
    except Exception as e:
        print(f"{url}: Lỗi - {e}")
        return 0

# Bài tập 4: Chạy ví dụ với timeout
async def run_with_timeout_example():
    print("\n--- Bài tập 4: Tải URL với timeout ---")
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/3",  # Sẽ bị timeout
        "https://httpbin.org/json"
    ]
    
    start = time.time()
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            *[fetch_with_timeout(session, url) for url in urls]
        )
    print(f"Tổng dữ liệu nhận được: {sum(results)} ký tự")
    print(f"Thời gian tổng: {time.time() - start:.2f}s")

# Bài tập 5: Mô phỏng xử lý tác vụ qua hàng đợi
async def task_processor(tasks_queue):
    """Xử lý các tác vụ từ hàng đợi"""
    while True:
        try:
            # Lấy tác vụ từ hàng đợi với timeout 1 giây
            task = await asyncio.wait_for(tasks_queue.get(), timeout=1.0)
            name, delay = task
            print(f"[Bắt đầu] Xử lý {name} trong {delay}s...")
            await asyncio.sleep(delay)
            print(f"[Hoàn thành] {name}")
            tasks_queue.task_done()
        except TimeoutError:
            print("Không còn tác vụ, dừng xử lý.")
            break

async def run_simulation():
    print("\n--- Bài tập 5: Mô phỏng xử lý hàng đợi tác vụ ---")
    
    # Tạo hàng đợi
    queue = asyncio.Queue()
    
    # Thêm các tác vụ vào hàng đợi
    tasks = [
        ("Task-A", 1.0),
        ("Task-B", 0.5),
        ("Task-C", 1.2),
        ("Task-D", 0.3)
    ]
    
    for task in tasks:
        await queue.put(task)
    
    # Chạy processor
    await task_processor(queue)

# Hàm chạy tất cả bài tập
async def main():
    await run_tasks_concurrently()
    await run_with_timeout_example()
    await run_simulation()

if __name__ == "__main__":
    asyncio.run(main())