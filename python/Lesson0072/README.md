# Làm quen với thư viện Requests
## Giới thiệu
Thư viện Requests là một trong những thư viện phổ biến nhất của Python, giúp bạn gửi HTTP request và nhận response từ server một cách dễ dàng. Với Requests, bạn có thể gửi request GET, POST, PUT, DELETE, v.v. và nhận response dưới dạng JSON, XML, v.v. Trong bài này, chúng ta sẽ tìm hiểu về cách sử dụng thư viện Requests để gửi request và nhận response.

## Lý thuyết
Trước khi bắt đầu, bạn cần hiểu về các khái niệm cơ bản sau:
- **HTTP Request**: Là một yêu cầu gửi từ client (trình duyệt, ứng dụng) đến server để yêu cầu thực hiện một hành động nào đó (ví dụ: lấy dữ liệu, gửi dữ liệu, xóa dữ liệu, v.v.).
- **HTTP Response**: Là phản hồi từ server sau khi nhận được request từ client.
- **HTTP Method**: Là phương thức được sử dụng để gửi request (ví dụ: GET, POST, PUT, DELETE, v.v.).
- **URL**: Là địa chỉ của tài nguyên trên server.

Thư viện Requests cung cấp các phương thức sau để gửi request:
- `requests.get()`: Gửi request GET
- `requests.post()`: Gửi request POST
- `requests.put()`: Gửi request PUT
- `requests.delete()`: Gửi request DELETE

## Ví dụ
Dưới đây là ví dụ về cách sử dụng thư viện Requests để gửi request GET và nhận response:
```python
import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

print(response.json())
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
Trong ví dụ trên, chúng ta gửi request GET đến địa chỉ `https://jsonplaceholder.typicode.com/todos/1` và nhận response dưới dạng JSON.

## Bài tập
Bài tập 1: Gửi request GET đến địa chỉ `https://jsonplaceholder.typicode.com/todos` và nhận response dưới dạng JSON. In ra màn hình danh sách các todo item.

Bài tập 2: Gửi request POST đến địa chỉ `https://jsonplaceholder.typicode.com/todos` với dữ liệu `{"title": "Learn Python", "completed": false}`. In ra màn hình response từ server.

Bài tập 3: Gửi request PUT đến địa chỉ `https://jsonplaceholder.typicode.com/todos/1` với dữ liệu `{"title": "Learn Python", "completed": true}`. In ra màn hình response từ server.

Bài tập 4: Gửi request DELETE đến địa chỉ `https://jsonplaceholder.typicode.com/todos/1`. In ra màn hình response từ server.