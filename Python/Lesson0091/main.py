import asyncio
import aiohttp
import time

# Ví dụ 1: Tải dữ liệu từ nhiều API đồng thời
async def fetch_weather(session, city):
    # Giả lập API thời tiết
    print(f'Đang lấy thời tiết cho {city}...')
    async with session.get(f'https://httpbin.org/delay/1', params={'city': city}) as response:
        data = await response.json()
        print(f'Thời tiết {city}: OK (trạng thái {response.status})')
        return {city: 'sunny'}

async def get_all_weather():
    async with aiohttp.ClientSession() as session:
        # Gọi 3 API đồng thời
        results = await asyncio.gather(
            fetch_weather(session, 'Hà Nội'),
            fetch_weather(session, 'TP.HCM'),
            fetch_weather(session, 'Đà Nẵng')
        )
        return results

# Ví dụ 2: Đọc nhiều tệp tin bất đồng bộ
async def read_file(filename):
    # Dùng asyncio để không chặn event loop khi đọc file
    return await asyncio.to_thread(read_file_sync, filename)

def read_file_sync(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f'Đã đọc {len(content)} ký tự từ {filename}')
        return content

async def read_files_async(file_list):
    # Đọc tất cả các tệp đồng thời
    contents = await asyncio.gather(*(read_file(f) for f in file_list))
    return contents

# Ví dụ 3: Xử lý yêu cầu bất đồng bộ với thứ tự hoàn thành
async def task_with_delay(name, delay):
    print(f'Tác vụ {name} bắt đầu, chờ {delay}s...')
    await asyncio.sleep(delay)
    print(f'Tác vụ {name} hoàn thành!')
    return f'Kết quả từ {name}'

async def run_with_as_completed():
    tasks = [
        task_with_delay('T1', 3),
        task_with_delay('T2', 1),
        task_with_delay('T3', 2)
    ]
    # In kết quả theo thứ tự hoàn thành
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(f'Nhận được: {result}')

# Hàm chính để chạy tất cả ví dụ
async def main():
    print('=== Ví dụ 1: Lấy dữ liệu thời tiết ===')
    start = time.time()
    weather_data = await get_all_weather()
    print('Dữ liệu thời tiết:', weather_data)
    print(f'Thời gian: {time.time() - start:.2f}s\n')

    print('=== Ví dụ 2: Đọc nhiều tệp tin ===')
    # Tạo tệp tin mẫu trước
    sample_files = ['file1.txt', 'file2.txt', 'file3.txt']
    for i, fname in enumerate(sample_files):
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(f'Nội dung mẫu {i+1} ' * 1000)

    start = time.time()
    contents = await read_files_async(sample_files)
    print(f'Đã đọc {len(contents)} tệp tin.')
    print(f'Thời gian: {time.time() - start:.2f}s\n')

    print('=== Ví dụ 3: Xử lý theo thứ tự hoàn thành ===')
    start = time.time()
    await run_with_as_completed()
    print(f'Tổng thời gian: {time.time() - start:.2f}s')

# Chạy chương trình chính
if __name__ == '__main__':
    asyncio.run(main())