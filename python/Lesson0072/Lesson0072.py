# Bài 72: Làm quen với thư viện Requests

# Thư viện Requests giúp chúng ta gửi các yêu cầu HTTP đến một trang web
import requests

# Gửi yêu cầu GET đến trang web
def guiyeucau_get():
    # Yêu cầu GET đến trang chủ của Google
    url = "https://www.google.com"
    response = requests.get(url)
    
    # Kiểm tra trạng thái của yêu cầu
    if response.status_code == 200:
        print("Yêu cầu GET thành công!")
        # In nội dung của trang web
        print(response.text)
    else:
        print("Yêu cầu GET thất bại!")

# Gửi yêu cầu POST đến trang web
def guiyeucau_post():
    # Yêu cầu POST đến trang web
    url = "https://httpbin.org/post"
    data = {"key": "value"}
    response = requests.post(url, data=data)
    
    # Kiểm tra trạng thái của yêu cầu
    if response.status_code == 200:
        print("Yêu cầu POST thành công!")
        # In nội dung của trang web
        print(response.text)
    else:
        print("Yêu cầu POST thất bại!")

# Gửi yêu cầu GET với tham số
def guiyeucau_get_voi_thamso():
    # Yêu cầu GET đến trang web với tham số
    url = "https://httpbin.org/get"
    params = {"key": "value"}
    response = requests.get(url, params=params)
    
    # Kiểm tra trạng thái của yêu cầu
    if response.status_code == 200:
        print("Yêu cầu GET với tham số thành công!")
        # In nội dung của trang web
        print(response.text)
    else:
        print("Yêu cầu GET với tham số thất bại!")

# Gửi yêu cầu với header
def guiyeucau_voi_header():
    # Yêu cầu GET đến trang web với header
    url = "https://httpbin.org/get"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    # Kiểm tra trạng thái của yêu cầu
    if response.status_code == 200:
        print("Yêu cầu với header thành công!")
        # In nội dung của trang web
        print(response.text)
    else:
        print("Yêu cầu với header thất bại!")

# Chạy các hàm để.demo
guiyeucau_get()
guiyeucau_post()
guiyeucau_get_voi_thamso()
guiyeucau_voi_header()