# Làm quen với thư viện Requests
## Giới thiệu
Thư viện Requests là một trong những thư viện phổ biến nhất trong Python, được sử dụng để gửi HTTP request và tương tác với các trang web. Với thư viện này, bạn có thể dễ dàng gửi các yêu cầu GET, POST, PUT, DELETE và nhận phản hồi từ máy chủ. Trong bài này, chúng ta sẽ tìm hiểu cách sử dụng thư viện Requests để gửi yêu cầu và nhận phản hồi từ máy chủ.

## Lý thuyết
Thư viện Requests cung cấp một số phương thức chính để gửi yêu cầu, bao gồm:
- `requests.get()`: gửi yêu cầu GET
- `requests.post()`: gửi yêu cầu POST
- `requests.put()`: gửi yêu cầu PUT
- `requests.delete()`: gửi yêu cầu DELETE
Mỗi phương thức này đều nhận một số tham số, bao gồm `url`, `params`, `data`, `headers`, v.v.

Khi gửi yêu cầu, thư viện Requests sẽ trả về một đối tượng `Response`, chứa thông tin về phản hồi từ máy chủ. Đối tượng `Response` có một số thuộc tính quan trọng, bao gồm:
- `status_code`: mã trạng thái của phản hồi
- `text`: nội dung của phản hồi dưới dạng văn bản
- `json()`: nội dung của phản hồi dưới dạng JSON

## Ví dụ
Dưới đây là một ví dụ về cách sử dụng thư viện Requests để gửi yêu cầu GET và nhận phản hồi từ máy chủ:
```python
import requests

url = "https://www.example.com"
response = requests.get(url)

print("Mã trạng thái:", response.status_code)
print("Nội dung phản hồi:", response.text)
```
Trong ví dụ này, chúng ta gửi một yêu cầu GET đến địa chỉ `https://www.example.com` và nhận phản hồi từ máy chủ. Chúng ta sau đó in ra mã trạng thái và nội dung của phản hồi.

## Bài tập
Bài tập này yêu cầu bạn gửi một yêu cầu GET đến địa chỉ `https://jsonplaceholder.typicode.com/posts` và nhận phản hồi từ máy chủ. Sau đó, bạn cần in ra mã trạng thái và nội dung của phản hồi dưới dạng JSON.

Đầu tiên, bạn cần cài đặt thư viện Requests bằng cách chạy lệnh `pip install requests` trong terminal. Sau đó, bạn có thể viết mã Python để gửi yêu cầu và nhận phản hồi.

Gợi ý: bạn cần sử dụng phương thức `requests.get()` để gửi yêu cầu và thuộc tính `json()` để nhận nội dung phản hồi dưới dạng JSON.