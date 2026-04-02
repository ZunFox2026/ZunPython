# Làm quen với thư viện requests
## Giới thiệu
Thư viện `requests` là một trong những thư viện phổ biến nhất trong Python, giúp chúng ta gửi các yêu cầu HTTP và nhận phản hồi từ máy chủ. Thư viện này cung cấp một cách đơn giản và dễ sử dụng để tương tác với các dịch vụ web.

## Lý thuyết
Thư viện `requests` hỗ trợ các phương thức HTTP cơ bản như `GET`, `POST`, `PUT`, `DELETE`,... Để sử dụng thư viện này, bạn cần nhập nó vào chương trình của mình bằng câu lệnh `import requests`. Sau đó, bạn có thể sử dụng các hàm như `requests.get()`, `requests.post()`,... để gửi yêu cầu đến máy chủ.

Ví dụ, để gửi một yêu cầu `GET` đến trang web `http://example.com`, bạn có thể sử dụng đoạn code sau:
```python
import requests
response = requests.get('http://example.com')
print(response.text)
```
Thư viện `requests` cũng hỗ trợ việc gửi dữ liệu kèm theo yêu cầu, thông qua các tham số như `params` cho phương thức `GET` và `data` cho phương thức `POST`.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách sử dụng thư viện `requests`:

- Gửi yêu cầu `GET` đến trang web `http://example.com`:
```python
import requests
response = requests.get('http://example.com')
print(response.text)
```

- Gửi yêu cầu `POST` đến trang web `http://example.com` với dữ liệu kèm theo:
```python
import requests
data = {'name': 'Zunny', 'age': 25}
response = requests.post('http://example.com', data=data)
print(response.text)
```

- Gửi yêu cầu `GET` đến trang web `http://example.com` với tham số `params`:
```python
import requests
params = {'name': 'Zunny', 'age': 25}
response = requests.get('http://example.com', params=params)
print(response.text)
```

## Bài tập
Để củng cố kiến thức về thư viện `requests`, bạn có thể thực hiện các bài tập sau:

- Gửi yêu cầu `GET` đến trang web `http://example.com` và in ra mã trạng thái của phản hồi.
- Gửi yêu cầu `POST` đến trang web `http://example.com` với dữ liệu kèm theo và in ra nội dung của phản hồi.
- Tìm hiểu về các phương thức HTTP khác như `PUT`, `DELETE` và thực hiện các yêu cầu tương ứng đến trang web `http://example.com`.

Hy vọng qua bài học này, bạn đã có thể làm quen với thư viện `requests` và biết cách sử dụng nó để gửi các yêu cầu HTTP và nhận phản hồi từ máy chủ.