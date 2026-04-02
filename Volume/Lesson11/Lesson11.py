# Import thư viện requests
import requests

# Gửi một yêu cầu GET đến địa chỉ URL
def gui_yeu_cau_get():
    url = "https://www.google.com"
    response = requests.get(url)
    
    # Kiểm tra trạng thái của yêu cầu
    if response.status_code == 200:
        print("Yêu cầu thành công!")
    else:
        print("Yêu cầu thất bại!")

# Gửi một yêu cầu POST đến địa chỉ URL
def gui_yeu_cau_post():
    url = "https://httpbin.org/post"
    data = {"key": "value"}
    response = requests.post(url, data=data)
    
    # In ra nội dung của yêu cầu
    print(response.text)

# Gửi một yêu cầu GET với tham số đến địa chỉ URL
def gui_yeu_cau_get_voi_tham_so():
    url = "https://httpbin.org/get"
    params = {"key": "value"}
    response = requests.get(url, params=params)
    
    # In ra nội dung của yêu cầu
    print(response.text)

# Gửi một yêu cầu GET với header đến địa chỉ URL
def gui_yeu_cau_get_voi_header():
    url = "https://httpbin.org/get"
    headers = {"User-Agent": "My Browser"}
    response = requests.get(url, headers=headers)
    
    # In ra nội dung của yêu cầu
    print(response.text)

# Gọi các hàm để minh họa
gui_yeu_cau_get()
gui_yeu_cau_post()
gui_yeu_cau_get_voi_tham_so()
gui_yeu_cau_get_voi_header()