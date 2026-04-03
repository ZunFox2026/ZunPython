import asyncio
import time

# --- Ví dụ 1: Gọi API song song ---
async def goi_api(url):
    print(f"Đang gọi API: {url}")
    # Mô phỏng độ trễ mạng
    await asyncio.sleep(1)
    print(f"Hoàn thành: {url}")
    return f"Dữ liệu từ {url}"

async def vi_du_1():
    print("=== Ví dụ 1: Gọi 3 API song song ===")
    start = time.time()
    
    # Chạy song song 3 coroutine
    ket_qua = await asyncio.gather(
        goi_api("https://api1.example.com"),
        goi_api("https://api2.example.com"),
        goi_api("https://api3.example.com")
    )
    
    end = time.time()
    print(f"Tất cả hoàn thành trong {end - start:.2f} giây")
    print("Kết quả:", ket_qua)

# --- Ví dụ 2: Đọc nhiều file bất đồng bộ ---
async def doc_file(ten_file):
    print(f"Đang đọc {ten_file}...")
    await asyncio.sleep(0.5)  # Mô phỏng đọc file chậm
    return f"Nội dung của {ten_file}"

async def vi_du_2():
    print("\n=== Ví dụ 2: Đọc 4 file song song ===")
    start = time.time()
    
    tasks = []
    for i in range(1, 5):
        task = asyncio.create_task(doc_file(f"file_{i}.txt"))
        tasks.append(task)
    
    ket_qua = await asyncio.gather(*tasks)
    end = time.time()
    
    print(f"Tất cả file đã đọc xong trong {end - start:.2f} giây")
    for r in ket_qua:
        print(r)

# --- Ví dụ 3: Xử lý song song với xử lý nhanh ---
async def task_nhe():
    print("Task nhẹ bắt đầu...")
    await asyncio.sleep(1)
    print("Task nhẹ xong.")
    return "Nhẹ"

async def task_nang():
    print("Task nặng bắt đầu...")
    await asyncio.sleep(2)
    print("Task nặng xong.")
    return "Nặng"

async def in_bat_dong_bo():
    print("In bất đồng bộ: Bắt đầu!")

async def vi_du_3():
    print("\n=== Ví dụ 3: Kết hợp nhiều loại tác vụ ===")
    start = time.time()
    
    # Tạo các task
    task1 = asyncio.create_task(task_nhe())
    task2 = asyncio.create_task(task_nang())
    task3 = asyncio.create_task(in_bat_dong_bo())
    
    # Chờ tất cả hoàn thành
    ket_qua = await asyncio.gather(task1, task2, task3)
    end = time.time()
    
    print(f"Tổng thời gian: {end - start:.2f} giây")
    print("Kết quả các task:", ket_qua)

# Chạy tất cả ví dụ
async def main():
    await vi_du_1()
    await vi_du_2()
    await vi_du_3()

if __name__ == "__main__":
    asyncio.run(main())