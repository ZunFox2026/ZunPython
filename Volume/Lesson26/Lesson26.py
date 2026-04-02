from datetime import datetime, timedelta

# Lấy thời gian hiện tại
thoi_gian_hien_tai = datetime.now()
print("Thời gian hiện tại:", thoi_gian_hien_tai)

# Lấy phần ngày, tháng, năm từ thời gian hiện tại
ngay_hien_tai = thoi_gian_hien_tai.day
thang_hien_tai = thoi_gian_hien_tai.month
nam_hien_tai = thoi_gian_hien_tai.year
print("Ngày hiện tại:", ngay_hien_tai)
print("Tháng hiện tại:", thang_hien_tai)
print("Năm hiện tại:", nam_hien_tai)

# Tính thời gian sau 30 ngày
thoi_gian_sau_30_ngay = thoi_gian_hien_tai + timedelta(days=30)
print("Thời gian sau 30 ngày:", thoi_gian_sau_30_ngay)

# Tính thời gian trước 30 ngày
thoi_gian_truoc_30_ngay = thoi_gian_hien_tai - timedelta(days=30)
print("Thời gian trước 30 ngày:", thoi_gian_truoc_30_ngay)

# So sánh thời gian
if thoi_gian_hien_tai > thoi_gian_truoc_30_ngay:
    print("Thời gian hiện tại lớn hơn thời gian trước 30 ngày")
else:
    print("Thời gian hiện tại nhỏ hơn hoặc bằng thời gian trước 30 ngày")