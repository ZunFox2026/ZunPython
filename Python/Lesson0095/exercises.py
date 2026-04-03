import asyncio

# Bài tập 1
# Viết hàm fetch_data(name, delay) mô phỏng tải dữ liệu
# Gọi 3 lần đồng thời và in kết quả
async def fetch_data(name, delay):
    # Gợi ý: dùng asyncio.sleep(delay)
    pass

async def exercise_1():
    # Gọi fetch_data 3 lần với các tham số khác nhau
    # Dùng asyncio.gather để chạy song song
    pass

# Bài tập 2
# Viết hàm read_file_async(filename) để đọc file bất đồng bộ
# Dùng aiofiles.open
async def read_file_async(filename):
    # Gợi ý: cài đặt aiofiles, dùng async with
    pass

async def exercise_2():
    # Tạo 2 file mẫu, rồi đọc bất đồng bộ
    pass

# Bài tập 3
# Mô phỏng máy in chia sẻ với hàng đợi
async def printer_task(queue):
    # Xử lý in từng tài liệu trong queue
    pass

async def user_submit(queue, user_name, doc_name):
    # Người dùng gửi tài liệu vào queue
    pass

async def exercise_3():
    # Tạo queue, printer task, và mô phỏng 3 người gửi
    pass

# Bài tập 4
# In số từ 1 đến 3 với độ trễ 0.5s, chạy 5 tác vụ song song
async def print_numbers(task_id):
    # In 1, 2, 3 với await asyncio.sleep(0.5)
    pass

async def exercise_4():
    # Dùng asyncio.gather để chạy 5 task
    pass

# Bài tập 5
# Dùng asyncio.wait_for để giới hạn thời gian thực thi
async def slow_task():
    await asyncio.sleep(3)
    return "Xong!"

async def timeout_example():
    # Chạy slow_task với timeout 2 giây
    # Nếu quá thời gian, in ra "Timeout!"
    pass

# Chạy tất cả bài tập
async def main():
    print("=== Bài tập 1 ===")
    await exercise_1()
    
    print("\n=== Bài tập 2 ===")
    await exercise_2()
    
    print("\n=== Bài tập 3 ===")
    await exercise_3()
    
    print("\n=== Bài tập 4 ===")
    await exercise_4()
    
    print("\n=== Bài tập 5 ===")
    await timeout_example()

if __name__ == "__main__":
    asyncio.run(main())