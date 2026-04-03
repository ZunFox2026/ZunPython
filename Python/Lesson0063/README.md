# Bài học Python số 63: Xử lý bất đồng bộ với Asyncio (Cấp độ nâng cao)

## Mục tiêu bài học
- Hiểu được khái niệm bất đồng bộ (asynchronous programming) và vai trò của `asyncio` trong Python.
- Biết cách sử dụng `async`, `await` để viết hàm bất đồng bộ.
- Hiểu được vòng lặp sự kiện (event loop) và cách quản lý nhiều tác vụ đồng thời.
- Ứng dụng `asyncio` để tăng hiệu suất trong các tác vụ I/O như tải trang web, xử lý tệp, kết nối mạng.

## Lý thuyết chi tiết

### 1. Bất đồng bộ là gì?

Trong lập trình đồng bộ (synchronous), các tác vụ được thực hiện tuần tự. Nếu một tác vụ chậm (như tải trang web), toàn bộ chương trình bị chặn cho đến khi tác vụ đó hoàn tất.

Lập trình bất đồng bộ cho phép chương trình thực hiện nhiều tác vụ cùng lúc, đặc biệt hiệu quả với các tác vụ I/O (input/output) như:
- Gửi yêu cầu HTTP
- Đọc/ghi tệp
- Kết nối cơ sở dữ liệu

### 2. Async và Await

- `async def`: khai báo một hàm là hàm bất đồng bộ.
- `await`: tạm dừng thực thi hàm bất đồng bộ hiện tại để chờ một coroutine khác hoàn tất, mà không chặn toàn bộ chương trình.

```python
async def say_hello():
    await asyncio.sleep(1)
    print("Xin chào!")
```

### 3. Vòng lặp sự kiện (Event Loop)

`asyncio` sử dụng một vòng lặp sự kiện để quản lý và thực thi các coroutine. Bạn có thể chạy một coroutine bằng:

```python
asyncio.run(your_async_function())
```

### 4. Chạy song song nhiều tác vụ

Dùng `asyncio.gather()` để chạy nhiều coroutine đồng thời:

```python
await asyncio.gather(task1(), task2(), task3())
```

## Ví dụ minh họa

### Ví dụ 1: Chào hỏi không đồng bộ

Mô phỏng việc chờ một giây để in lời chào.

### Ví dụ 2: Tải nhiều trang web song song

Sử dụng `aiohttp` để gửi nhiều yêu cầu HTTP cùng lúc, tiết kiệm thời gian.

### Ví dụ 3: Xử lý tệp bất đồng bộ

Đọc nhiều tệp lớn mà không làm chậm chương trình.

## Bài tập thực hành

1. Viết một hàm bất đồng bộ `countdown(n)` in số từ n về 0, mỗi số cách nhau 0.5 giây.
2. Tạo 3 tác vụ bất đồng bộ mô phỏng việc nấu ăn: rửa rau (2 giây), cắt hành (1 giây), nấu súp (3 giây). Chạy song song.
3. Viết chương trình tải 3 URL mẫu và in độ dài nội dung mỗi trang.
4. Tạo một hàm `read_files_async(filenames)` để đọc nhiều tệp văn bản cùng lúc.
5. Viết hàm `fetch_with_timeout(url, timeout)` dùng để tải URL với giới hạn thời gian.

## Tổng kết

- `asyncio` là công cụ mạnh để xử lý các tác vụ I/O một cách hiệu quả.
- Sử dụng `async` và `await` để viết code bất đồng bộ.
- `asyncio.gather()` giúp chạy nhiều tác vụ song song.
- Asyncio đặc biệt hữu ích trong web scraping, API, và xử lý tệp lớn.
- Cần cẩn thận với các thư viện không hỗ trợ async — phải dùng `loop.run_in_executor()` nếu cần.

> 💡 Mẹo: Async không giúp tăng tốc xử lý CPU, mà chỉ tối ưu hóa việc chờ I/O. Với tác vụ nặng CPU, nên dùng đa luồng hoặc đa tiến trình.