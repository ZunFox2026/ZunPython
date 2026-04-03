# Bài học Python nâng cao số 95: Làm việc với AsyncIO – Lập trình bất đồng bộ

## Mục tiêu bài học
- Hiểu được khái niệm và lợi ích của lập trình bất đồng bộ trong Python.
- Nắm vững cách sử dụng `async` và `await` để viết hàm bất đồng bộ.
- Biết cách sử dụng `asyncio` để quản lý nhiều tác vụ đồng thời.
- Áp dụng kiến thức vào các tình huống thực tế như xử lý nhiều yêu cầu mạng, đọc ghi file, hoặc API calls.

## Lý thuyết chi tiết

### 1. Lập trình bất đồng bộ là gì?

Lập trình bất đồng bộ (asynchronous programming) cho phép chương trình thực hiện nhiều công việc cùng lúc mà không cần chờ từng công việc hoàn thành trước khi bắt đầu công việc tiếp theo. Điều này đặc biệt hữu ích khi làm việc với các tác vụ chậm như gọi API, đọc ghi file, hoặc kết nối mạng.

Trong Python, `asyncio` là thư viện chuẩn hỗ trợ lập trình bất đồng bộ. Nó sử dụng mô hình **event loop** để quản lý các tác vụ.

### 2. Từ khóa `async` và `await`

- `async def`: Dùng để định nghĩa một hàm bất đồng bộ.
- `await`: Dùng để tạm dừng thực thi hàm bất đồng bộ cho đến khi một coroutine khác hoàn thành.

> Lưu ý: Bạn chỉ có thể dùng `await` bên trong một hàm `async`.

### 3. Event Loop

Event loop là trái tim của `asyncio`. Nó quản lý và phân phối các tác vụ bất đồng bộ. Bạn có thể chạy một coroutine bằng cách sử dụng `asyncio.run()` (từ Python 3.7+).

### 4. Ví dụ đơn giản

```python
import asyncio

async def say_hello():
    print("Bắt đầu...")
    await asyncio.sleep(1)  # Giả lập tác vụ chậm
    print("Xong sau 1 giây")

asyncio.run(say_hello())
```

## Ví dụ minh họa

### Ví dụ 1: Gọi nhiều API đồng thời

Giả sử bạn cần lấy dữ liệu từ 3 API khác nhau. Nếu dùng đồng bộ (synchronous), bạn phải chờ từng cái một. Với bất đồng bộ, bạn có thể gọi cùng lúc.

### Ví dụ 2: Đọc nhiều file lớn

Khi đọc nhiều file lớn, bạn có thể tận dụng bất đồng bộ để tiết kiệm thời gian.

### Ví dụ 3: Xử lý tác vụ định kỳ (scheduling)

Sử dụng `asyncio.sleep()` để lập lịch chạy các tác vụ theo chu kỳ.

## Bài tập thực hành

1. Viết một hàm bất đồng bộ `fetch_data(name, delay)` mô phỏng việc tải dữ liệu từ máy chủ với tên và độ trễ cho trước. Gọi 3 lần hàm này đồng thời và in kết quả.
2. Tạo một hàm `read_file_async(filename)` để đọc nội dung file một cách bất đồng bộ. Dùng `asyncio` để đọc 2 file cùng lúc.
3. Viết chương trình mô phỏng một máy in chia sẻ, nơi nhiều người dùng gửi tài liệu in. Mỗi bản in mất 2 giây. In theo thứ tự gửi nhưng không chờ đợi (dùng queue bất đồng bộ).
4. Dùng `asyncio.gather()` để chạy song song 5 tác vụ, mỗi tác vụ in ra số từ 1 đến 3 với độ trễ 0.5 giây giữa các số.
5. Viết hàm `timeout_example()` sử dụng `asyncio.wait_for()` để giới hạn thời gian thực thi một coroutine (ví dụ: nếu quá 2 giây thì hủy).

## Tổng kết

- Lập trình bất đồng bộ giúp cải thiện hiệu suất khi xử lý các tác vụ I/O.
- `async` và `await` là nền tảng của bất đồng bộ trong Python.
- `asyncio` cung cấp nhiều công cụ như `gather`, `wait_for`, `sleep`, và `queue` để xử lý tác vụ phức tạp.
- Hiểu rõ khi nào nên dùng bất đồng bộ (I/O-bound) và khi nào không cần (CPU-bound).

> 💡 Gợi ý: Dùng bất đồng bộ khi làm việc với mạng, file, database, API. Với tính toán nặng, hãy cân nhắc dùng `multiprocessing` thay vì `asyncio`.
