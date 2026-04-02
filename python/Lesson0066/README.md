# Làm quen với thư viện requests
## Giới thiệu
Thư viện `requests` là một trong những thư viện phổ biến nhất trong Python, giúp bạn gửi HTTP request và nhận response từ server. Với `requests`, bạn có thể dễ dàng thực hiện các tác vụ như lấy dữ liệu từ API, tải file, gửi dữ liệu đến server,... Thư viện này cung cấp một cách thức đơn giản và trực quan để làm việc với HTTP request, giúp bạn tiết kiệm thời gian và tăng hiệu suất công việc.

## Lý thuyết
Thư viện `requests` cung cấp các phương thức để gửi HTTP request, bao gồm:
- `get()`: Gửi HTTP GET request
- `post()`: Gửi HTTP POST request
- `put()`: Gửi HTTP PUT request
- `delete()`: Gửi HTTP DELETE request
Mỗi phương thức này đều trả về một đối tượng `Response`, chứa thông tin về HTTP response nhận được từ server. Đối tượng `Response` có các thuộc tính như `status_code`, `text`, `json()`,... giúp bạn dễ dàng truy cập và xử lý dữ liệu nhận được.

## Ví dụ
Ví dụ dưới đây cho thấy cách sử dụng thư viện `requests` để gửi HTTP GET request và lấy dữ liệu từ API:
```python
import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Lỗi:", response.status_code)
```
Kết quả:
```json
{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
}
```
Ví dụ trên cho thấy cách gửi HTTP GET request đến API và lấy dữ liệu ở định dạng JSON.

## Bài tập
Bài tập dưới đây sẽ giúp bạn làm quen với thư viện `requests`:
- Gửi HTTP GET request đến địa chỉ `https://jsonplaceholder.typicode.com/todos` và lấy tất cả các todo item.
- In ra danh sách các todo item với thông tin `id`, `title`, `completed`.
- Gửi HTTP POST request đến địa chỉ `https://jsonplaceholder.typicode.com/todos` với dữ liệu `title` và `completed` để tạo mới một todo item.
- In ra thông tin về todo item vừa tạo.