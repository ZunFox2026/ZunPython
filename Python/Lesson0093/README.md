# Bài học Python nâng cao số 93: Xử lý bất đồng bộ với asyncio

## Mục tiêu bài học
- Hiểu được khái niệm bất đồng bộ (asynchronous programming) và tại sao nó quan trọng.
- Nắm vững cách sử dụng `asyncio` để viết chương trình bất đồng bộ trong Python.
- Biết cách định nghĩa hàm bất đồng bộ (`async def`), sử dụng `await`, và chạy các tác vụ song song với `asyncio.gather()`.
- Áp dụng `asyncio` vào các tình huống thực tế như tải dữ liệu từ API, xử lý tệp tin, mô phỏng tác vụ chậm.

## Lý thuyết chi tiết

### 1. Bất đồng bộ là gì?
Trong lập trình, **bất đồng bộ** (asynchronous) là kỹ thuật cho phép chương trình thực hiện nhiều tác vụ cùng lúc mà không cần chờ tác vụ trước hoàn thành. Điều này đặc biệt hữu ích khi làm việc với các tác vụ chậm như:
- Gọi API mạng
- Đọc/ghi tệp tin
- Truy vấn cơ sở dữ liệu

Thay vì chờ đợi, chương trình có thể tạm dừng tác vụ đang chạy và chuyển sang xử lý tác vụ khác, tăng hiệu suất tổng thể.

### 2. asyncio trong Python
`asyncio` là thư viện chuẩn của Python dùng để viết mã bất đồng bộ. Các khái niệm chính:

- `async def`: Định nghĩa một hàm bất đồng bộ (gọi là *coroutine*).
- `await`: Dùng để tạm dừng thực thi hàm bất đồng bộ cho đến khi tác vụ hoàn thành.
- `asyncio.run()`: Khởi chạy một hàm bất đồng bộ chính.
- `asyncio.gather()`: Chạy nhiều coroutine đồng thời và chờ tất cả hoàn thành.

### 3. Ví dụ đơn giản
```python
import asyncio

async def say_hello():
    print("Bắt đầu...")
    await asyncio.sleep(1)  # Tạm dừng 1 giây
    print("Xin chào!")

# Chạy hàm bất đồng bộ
coroutine = say_hello()
asyncio.run(coroutine)
```

## Ví dụ minh họa

### Ví dụ 1: Tải dữ liệu từ nhiều URL đồng thời
Chúng ta sẽ mô phỏng việc tải dữ liệu từ các URL khác nhau một cách bất đồng bộ.

### Ví dụ 2: Xử lý nhiều tệp tin cùng lúc
Đọc nhiều tệp tin lớn mà không làm chương trình bị treo.

### Ví dụ 3: Mô phỏng tác vụ dài hạn
Chạy nhiều tác vụ mô phỏng xử lý dữ liệu dài hạn và báo tiến độ.

## Bài tập thực hành
1. Viết hàm bất đồng bộ để in ra số từ 1 đến n với độ trễ 0.5 giây giữa mỗi lần in.
2. Tải dữ liệu từ 3 URL giả lập (sử dụng `asyncio.sleep`) và trả về nội dung.
3. Viết chương trình đọc đồng thời 3 tệp tin và đếm số dòng trong mỗi tệp.
4. Tạo một hàm bất đồng bộ mô phỏng việc đăng nhập người dùng (với độ trễ), và chạy 5 lần song song.
5. Dùng `asyncio.as_completed()` để xử lý các tác vụ theo thứ tự hoàn thành.

## Tổng kết
- `asyncio` giúp tăng hiệu suất khi xử lý các tác vụ I/O.
- Sử dụng `async`/`await` để viết mã bất đồng bộ.
- `asyncio.gather()` giúp chạy nhiều tác vụ song song.
- Tránh sử dụng các hàm đồng bộ (blocking) trong môi trường bất đồng bộ.
- `asyncio` không thay thế cho đa luồng, nhưng phù hợp với I/O-bound tasks.

> **Lưu ý**: `asyncio` không giúp tăng tốc các tác vụ xử lý CPU nặng. Với các tác vụ này, hãy cân nhắc dùng `multiprocessing`.
