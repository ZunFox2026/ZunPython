# Bài 24: Làm việc với thư viện thời gian

# Import thư viện thời gian
import time

# Lấy thời gian hiện tại
thoi_gian_hien_tai = time.time()
print("Thời gian hiện tại (số giây từ 1/1/1970): ", thoi_gian_hien_tai)

# Chuyển đổi thời gian thành định dạng dễ đọc
thoi_gian_doc = time.ctime(thoi_gian_hien_tai)
print("Thời gian hiện tại (định dạng dễ đọc): ", thoi_gian_doc)

# Ngủ (delay) trong 2 giây
print("Đang delay 2 giây...")
time.sleep(2)
print("Đã delay xong!")

# Lấy thời gian hiện tại sau khi delay
thoi_gian_hien_tai_sau_delay = time.time()
print("Thời gian hiện tại sau khi delay: ", thoi_gian_hien_tai_sau_delay)

# Tính toán thời gian trôi qua
thoi_gian_troi_qua = thoi_gian_hien_tai_sau_delay - thoi_gian_hien_tai
print("Thời gian trôi qua: ", thoi_gian_troi_qua, " giây")