# Làm quen với thư viện requests
## Giới thiệu
Thư viện requests là một trong những thư viện phổ biến nhất trong Python, được sử dụng để gửi các yêu cầu HTTP và tương tác với các dịch vụ web. Trong bài này, chúng ta sẽ tìm hiểu về cách sử dụng thư viện requests để gửi các yêu cầu HTTP và nhận dữ liệu từ các dịch vụ web.

## Lý thuyết
Thư viện requests cung cấp một số phương thức để gửi các yêu cầu HTTP, bao gồm:
- `requests.get()`: Gửi yêu cầu GET để nhận dữ liệu từ một URL.
- `requests.post()`: Gửi yêu cầu POST để gửi dữ liệu đến một URL.
- `requests.put()`: Gửi yêu cầu PUT để cập nhật dữ liệu trên một URL.
- `requests.delete()`: Gửi yêu cầu DELETE để xóa dữ liệu trên một URL.

Mỗi phương thức này sẽ trả về một đối tượng Response, chứa thông tin về yêu cầu và dữ liệu trả về từ dịch vụ web.

## Ví dụ
Dưới đây là một ví dụ về cách sử dụng thư viện requests để gửi yêu cầu GET và nhận dữ liệu từ một trang web:
```python
import requests

url = "https://www.google.com"
response = requests.get(url)

print(response.status_code)  # In mã trạng thái của yêu cầu
print(response.text)  # In nội dung của trang web
```
Trong ví dụ này, chúng ta sử dụng phương thức `requests.get()` để gửi yêu cầu GET đến trang web của Google. Đối tượng Response được trả về sẽ chứa mã trạng thái của yêu cầu (200 nếu thành công) và nội dung của trang web.

## Bài tập
Để thực hành sử dụng thư viện requests, bạn có thể thực hiện các bài tập sau:
- Gửi yêu cầu GET đến một trang web và in nội dung của trang web.
- Gửi yêu cầu POST đến một dịch vụ web và in dữ liệu trả về.
- Sử dụng thư viện requests để lấy dữ liệu từ một dịch vụ web và hiển thị dữ liệu đó trên màn hình.

Hy vọng qua bài này, bạn đã có một cái nhìn tổng quan về cách sử dụng thư viện requests trong Python. Hãy thực hành và khám phá thêm về các tính năng của thư viện này!