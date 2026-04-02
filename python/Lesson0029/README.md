# Làm quen với thư viện Requests
## Giới thiệu
Thư viện Requests là một trong những thư viện phổ biến nhất trong Python, được sử dụng để gửi các yêu cầu HTTP. Với thư viện này, bạn có thể dễ dàng gửi các yêu cầu GET, POST, PUT, DELETE,... và nhận lại các phản hồi từ máy chủ. Trong bài này, chúng ta sẽ tìm hiểu về cách sử dụng thư viện Requests để gửi các yêu cầu HTTP.

## Lý thuyết
Trước khi bắt đầu sử dụng thư viện Requests, chúng ta cần hiểu về các phương thức HTTP cơ bản:
- GET: Được sử dụng để nhận dữ liệu từ máy chủ.
- POST: Được sử dụng để gửi dữ liệu đến máy chủ.
- PUT: Được sử dụng để cập nhật dữ liệu trên máy chủ.
- DELETE: Được sử dụng để xóa dữ liệu trên máy chủ.

Để sử dụng thư viện Requests, bạn cần cài đặt nó bằng cách chạy lệnh `pip install requests` trong terminal. Sau khi cài đặt, bạn có thể nhập thư viện vào chương trình của mình bằng cách sử dụng lệnh `import requests`.

## Ví dụ
Dưới đây là một ví dụ về cách sử dụng thư viện Requests để gửi yêu cầu GET:
```python
import requests

url = "https://www.google.com"
response = requests.get(url)

print(response.status_code)
print(response.text)
```
Trong ví dụ này, chúng ta gửi yêu cầu GET đến địa chỉ `https://www.google.com` và nhận lại phản hồi từ máy chủ. Chúng ta có thể kiểm tra mã trạng thái của phản hồi bằng cách sử dụng thuộc tính `status_code` và nhận lại nội dung của phản hồi bằng cách sử dụng thuộc tính `text`.

## Bài tập
Bài tập 1: Gửi yêu cầu GET đến địa chỉ `https://www.facebook.com` và nhận lại nội dung của phản hồi.

Bài tập 2: Gửi yêu cầu POST đến địa chỉ `https://httpbin.org/post` với dữ liệu `{"name": "John", "age": 30}` và nhận lại nội dung của phản hồi.

Bài tập 3: Sử dụng thư viện Requests để gửi yêu cầu GET đến địa chỉ `https://jsonplaceholder.typicode.com/todos/1` và nhận lại nội dung của phản hồi. Sau đó, hãy giải析 nội dung của phản hồi và in ra giá trị của thuộc tính `title`.