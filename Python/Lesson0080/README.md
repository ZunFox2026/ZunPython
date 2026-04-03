# Bài học Python nâng cao số 80: Làm việc với Async IO và Event Loop

## Mục tiêu bài học
- Hiểu được khái niệm lập trình bất đồng bộ (asynchronous programming) trong Python.
- Nắm vững cách sử dụng `async`, `await`, `asyncio` để viết chương trình không chặn (non-blocking).
- Biết cách tạo và quản lý các tác vụ bất đồng bộ (tasks) và vòng lặp sự kiện (event loop).
- Vận dụng `asyncio` để xử lý các tác vụ I/O hiệu quả như tải file, gọi API, đọc ghi file, v.v.

## Lý thuyết chi tiết

### 1. Lập trình bất đồng bộ là gì?
Lập trình bất đồng bộ cho phép chương trình thực hiện nhiều nhiệm vụ cùng lúc mà không cần chờ nhiệm vụ trước hoàn thành. Điều này đặc biệt hữu ích khi xử lý các tác vụ I/O như:
- Gọi API
- Đọc ghi file
- Kết nối mạng

Thay vì chờ từng tác vụ hoàn thành (đồng bộ), chương trình có thể "chờ đợi" một cách thông minh và thực hiện các công việc khác trong lúc chờ.

### 2. Các khái niệm chính

#### `async` và `await`
- `async def` định nghĩa một hàm bất đồng bộ.
- `await` dùng để chờ một hàm bất đồng bộ hoàn thành, nhưng không chặn toàn bộ chương trình.

```python
async def say_hello():
    await asyncio.sleep(1)
    print("Xin chào!")
```

#### `asyncio`
- Thư viện chuẩn của Python để làm việc với lập trình bất đồng bộ.
- Cung cấp `event loop` – vòng lặp xử lý các tác vụ bất đồng bộ.

#### `Task`
- Là một công việc bất đồng bộ được lên lịch thực hiện.
- Dùng `asyncio.create_task()` để chạy nhiều tác vụ song song.

### 3. Event Loop
- Là trái tim của `asyncio`.
- Quản lý và thực thi các coroutine.
- Trong một chương trình, chỉ nên có một event loop chạy tại một thời điểm (trừ trường hợp đặc biệt).

## Ví dụ minh họa

Dưới đây là 3 ví dụ thực tế giúp bạn hiểu rõ cách sử dụng `asyncio`:

1. **Gọi nhiều API cùng lúc**
2. **Tải đồng thời nhiều file**
3. **Xử lý tác vụ mô phỏng với thời gian chờ khác nhau**

## Bài tập thực hành

1. Viết hàm bất đồng bộ tải nội dung từ danh sách URL.
2. Tạo một máy chủ đơn giản mô phỏng xử lý yêu cầu bất đồng bộ.
3. Viết chương trình đếm ngược cho nhiều sự kiện cùng lúc.
4. Xử lý ngoại lệ trong môi trường bất đồng bộ.
5. Tối ưu hóa việc đọc nhiều file văn bản lớn.

## Tổng kết
- Lập trình bất đồng bộ giúp cải thiện hiệu suất khi xử lý các tác vụ I/O.
- `async` và `await` là nền tảng để viết code bất đồng bộ trong Python.
- `asyncio` cung cấp công cụ mạnh mẽ để quản lý nhiều tác vụ cùng lúc.
- Việc hiểu rõ `event loop` và `Task` giúp bạn thiết kế hệ thống hiệu quả hơn.

> ⚠️ Lưu ý: Không sử dụng `asyncio` cho các tác vụ tính toán nặng (CPU-bound). Hãy dùng `multiprocessing` thay vì `asyncio` trong trường hợp đó.

---

📌 **Hướng dẫn chạy code**:

1. Lưu mã nguồn vào các file tương ứng: `main.py`, `exercises.py`, `solutions.py`
2. Chạy `python main.py` để xem ví dụ
3. Chạy `python exercises.py` để thực hành
4. Kiểm tra lời giải tại `solutions.py`
