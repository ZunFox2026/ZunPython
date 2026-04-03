import asyncio
import aiohttp

# Bài tập 1: Viết hàm tải danh sách URL bất đồng bộ
# Viết hàm `fetch_urls(urls)` để tải nội dung từ danh sách URL
# Sử dụng aiohttp và trả về danh sách kết quả
async def fetch_urls(urls):
    # TODO: Viết code tại đây
    pass

# Bài tập 2: Tạo máy chủ xử lý yêu cầu bất đồng bộ (mô phỏng)
# Viết hàm `handle_request(request_id)` mô phỏng xử lý một yêu cầu
# với thời gian xử lý ngẫu nhiên từ 0.5 đến 2 giây
# In ra trạng thái bắt đầu và hoàn thành
async def handle_request(request_id):
    # TODO: Viết code tại đây
    pass

async def process_requests(request_ids):
    # TODO: Xử lý tất cả request_id trong danh sách bất đồng bộ
    pass

# Bài tập 3: Đếm ngược bất đồng bộ cho nhiều sự kiện
# Viết hàm `countdown(name, seconds)` in ra đếm ngược mỗi giây
# và in "Xong!" khi kết thúc
async def countdown(name, seconds):
    # TODO: Viết code tại đây
    pass

async def run_countdowns():
    # TODO: Chạy đồng thời các đếm ngược: ('A', 3), ('B', 5), ('C', 2)
    pass

# Bài tập 4: Xử lý ngoại lệ trong tác vụ bất đồng bộ
# Một trong các URL dưới đây sẽ lỗi (404)
# Viết hàm `fetch_with_error_handling(urls)` để tải an toàn
async def risky_fetch(session, url):
    async with session.get(url) as response:
        if response.status == 404:
            raise ValueError(f"Không tìm thấy: {url}")
        return await response.text()

async def fetch_with_error_handling(urls):
    # TODO: Dùng try-except để xử lý lỗi và vẫn tiếp tục các tác vụ khác
    pass

# Bài tập 5: Đọc nhiều file văn bản lớn bất đồng bộ
# Viết hàm `read_files_async(filenames)` để đọc nội dung các file
# Sử dụng asyncio.to_thread() để không chặn event loop khi đọc file
async def read_files_async(filenames):
    # TODO: Đọc từng file trong luồng riêng để không chặn
    pass

# Hàm main để chạy bài tập (bỏ comment khi làm xong)
# async def main():
#     # await fetch_urls(["https://httpbin.org/json", "https://httpbin.org/get"])
#     # await process_requests([1, 2, 3, 4])
#     # await run_countdowns()
#     # await fetch_with_error_handling([
#     #     "https://httpbin.org/status/200",
#     #     "https://httpbin.org/status/404",
#     #     "https://httpbin.org/json"
#     # ])
#     # await read_files_async(["test1.txt", "test2.txt"])  # Tạo file trước

# if __name__ == "__main__":
#     asyncio.run(main())