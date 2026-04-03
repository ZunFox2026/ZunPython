# Bài học Python số 100 - Cấp độ nâng cao

## Chủ đề: Lập trình phản xạ (Reflection) và sử dụng `inspect` để phân tích mã nguồn tại thời gian chạy

Trong bài học này, chúng ta sẽ tìm hiểu về **lập trình phản xạ (reflection)** trong Python và cách sử dụng module `inspect` để khám phá cấu trúc mã nguồn như hàm, lớp, tham số, và stack call tại thời điểm chương trình đang chạy. Đây là một chủ đề nâng cao, rất hữu ích khi phát triển các công cụ như framework, thư viện kiểm thử, debuggers, hoặc các decorator thông minh.

### ✅ Mục tiêu bài học
- Hiểu được khái niệm lập trình phản xạ (reflection) trong Python.
- Biết cách sử dụng module `inspect` để:
  - Lấy thông tin về hàm, lớp, tham số.
  - Kiểm tra stack call.
  - Phân tích mã nguồn đang chạy.
- Ứng dụng `inspect` trong các tình huống thực tế như logging thông minh, validation tham số tự động, hoặc tạo decorator mạnh mẽ.

### 📘 Lý thuyết chi tiết

#### 1. Lập trình phản xạ là gì?
Lập trình phản xạ (Reflection) là khả năng của một chương trình để kiểm tra, phân tích hoặc thay đổi cấu trúc và hành vi của chính nó trong lúc chạy (runtime). Python hỗ trợ phản xạ rất mạnh mẽ thông qua các hàm như `getattr`, `hasattr`, `setattr`, `type`, `isinstance`, và đặc biệt là module `inspect`.

#### 2. Module `inspect`
Module `inspect` cung cấp các hàm để lấy thông tin chi tiết về các đối tượng Python như:
- Hàm, phương thức
- Lớp và thể hiện
- Frame (khung thực thi)
- Tham số, default values, annotations

Một số hàm phổ biến:
- `inspect.getmembers(obj)`: Lấy danh sách các thành viên của đối tượng.
- `inspect.isfunction(obj)`, `inspect.isclass(obj)`: Kiểm tra loại.
- `inspect.signature(func)`: Trích xuất thông tin về tham số của hàm.
- `inspect.currentframe()`: Lấy frame hiện tại, dùng để truy vết stack.
- `inspect.getframeinfo(frame)`: Lấy thông tin file, dòng lệnh của frame.

#### 3. Ứng dụng thực tế
- Tự động sinh tài liệu (doc generation)
- Kiểm tra tham số đầu vào trong decorator
- Ghi log chi tiết về nơi gọi hàm
- Xây dựng framework web hoặc ORM thông minh

### 💡 Ví dụ minh họa
Xem file `main.py` để chạy các ví dụ dưới đây.

### 📝 Bài tập thực hành
Thử hoàn thành các bài tập trong `exercises.py`, sau đó so sánh với lời giải trong `solutions.py`.

### 🧠 Tổng kết
Module `inspect` là công cụ mạnh mẽ cho các lập trình viên Python nâng cao. Khi kết hợp với lập trình phản xạ, bạn có thể xây dựng các hệ thống linh hoạt, tự động và thông minh. Tuy nhiên, cần sử dụng cẩn trọng vì nó có thể làm giảm hiệu suất và làm code khó đọc hơn nếu lạm dụng.

---
> *Chúc bạn học tốt và tận dụng được sức mạnh của Python tại runtime!*