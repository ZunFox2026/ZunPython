import requests

# Gửi yêu cầu GET đến một trang web
url = "https://www.google.com"
response = requests.get(url)

# Kiểm tra trạng thái của yêu cầu
if response.status_code == 200:
    print("Yêu cầu thành công")
else:
    print("Yêu cầu thất bại")

# In nội dung của trang web
print(response.text)

# Gửi yêu cầu POST đến một trang web
url_post = "https://httpbin.org/post"
data = {"key": "value"}
response_post = requests.post(url_post, data=data)

# Kiểm tra trạng thái của yêu cầu
if response_post.status_code == 200:
    print("Yêu cầu POST thành công")
else:
    print("Yêu cầu POST thất bại")

# In nội dung của trang web
print(response_post.text)

# Gửi yêu cầu GET với tham số
url_get_param = "https://httpbin.org/get"
params = {"key": "value", "key2": "value2"}
response_get_param = requests.get(url_get_param, params=params)

# Kiểm tra trạng thái của yêu cầu
if response_get_param.status_code == 200:
    print("Yêu cầu GET với tham số thành công")
else:
    print("Yêu cầu GET với tham số thất bại")

# In nội dung của trang web
print(response_get_param.text)

# Gửi yêu cầu với header
url_header = "https://httpbin.org/headers"
headers = {"User-Agent": "My Browser"}
response_header = requests.get(url_header, headers=headers)

# Kiểm tra trạng thái của yêu cầu
if response_header.status_code == 200:
    print("Yêu cầu với header thành công")
else:
    print("Yêu cầu với header thất bại")

# In nội dung của trang web
print(response_header.text)