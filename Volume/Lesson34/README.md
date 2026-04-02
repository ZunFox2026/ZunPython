# Làm việc với thư viện requests
## Giới thiệu
Thư viện requests là một trong những thư viện phổ biến nhất trong Python, giúp bạn gửi các yêu cầu HTTP và nhận lại phản hồi từ máy chủ. Thư viện này cung cấp một cách thức đơn giản và dễ sử dụng để làm việc với các giao thức mạng, giúp bạn có thể tập trung vào việc phát triển ứng dụng mà không cần phải lo lắng về các chi tiết kỹ thuật.

## Lý thuyết
Thư viện requests cung cấp các phương thức để gửi các yêu cầu HTTP như GET, POST, PUT, DELETE,... Mỗi phương thức này có thể được sử dụng để thực hiện các hành động khác nhau trên máy chủ. Ví dụ, phương thức GET được sử dụng để lấy dữ liệu từ máy chủ, trong khi phương thức POST được sử dụng để gửi dữ liệu đến máy chủ.

Để sử dụng thư viện requests, bạn cần nhập thư viện này vào chương trình của mình bằng cách sử dụng câu lệnh `import requests`. Sau đó, bạn có thể sử dụng các phương thức của thư viện này để gửi yêu cầu và nhận lại phản hồi.

Một số phương thức phổ biến của thư viện requests bao gồm:
- `requests.get(url)`: Gửi yêu cầu GET đến máy chủ.
- `requests.post(url, data)`: Gửi yêu cầu POST đến máy chủ với dữ liệu được gửi trong phần body của yêu cầu.
- `requests.put(url, data)`: Gửi yêu cầu PUT đến máy chủ với dữ liệu được gửi trong phần body của yêu cầu.
- `requests.delete(url)`: Gửi yêu cầu DELETE đến máy chủ.

## Ví dụ
Dưới đây là một ví dụ về cách sử dụng thư viện requests để gửi yêu cầu GET đến một máy chủ:
```python
import requests

url = "https://www.example.com"
response = requests.get(url)

print(response.status_code)
print(response.text)
```
Trong ví dụ này, chúng ta gửi yêu cầu GET đến máy chủ tại địa chỉ `https://www.example.com` và nhận lại phản hồi. Chúng ta sau đó in ra mã trạng thái của phản hồi và nội dung của phản hồi.

## Bài tập
Bài tập này yêu cầu bạn viết một chương trình Python sử dụng thư viện requests để gửi yêu cầu GET đến một máy chủ và nhận lại phản hồi. Sau đó, bạn cần in ra mã trạng thái của phản hồi và nội dung của phản hồi.

Yêu cầu cụ thể:
- Gửi yêu cầu GET đến máy chủ tại địa chỉ `https://www.example.com`.
- In ra mã trạng thái của phản hồi.
- In ra nội dung của phản hồi.

Lưu ý: Bạn cần sử dụng thư viện requests và nhập thư viện này vào chương trình của mình trước khi sử dụng.