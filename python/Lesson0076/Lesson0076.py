# Bài 76: Lập trình mạng

# Import thư viện socket để tạo kết nối mạng
import socket

# Tạo một socket mới
# AF_INET là địa chỉ IP phiên bản 4, SOCK_STREAM là giao thức TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Đặt địa chỉ IP và cổng cho socket
# Địa chỉ IP '127.0.0.1' là địa chỉ localhost
# Cổng 8080 là cổng được chọn để kết nối
server_address = ('127.0.0.1', 8080)

# Kết nối đến server
print("Kết nối đến server...")
sock.connect(server_address)

# Gửi tin nhắn đến server
tin_nhan = "Xin chào server!"
print("Gửi tin nhắn:", tin_nhan)
sock.sendall(tin_nhan.encode())

# Nhận tin nhắn từ server
print("Nhận tin nhắn từ server...")
data = sock.recv(1024)
print("Tin nhắn từ server:", data.decode())

# Đóng kết nối
print("Đóng kết nối...")
sock.close()