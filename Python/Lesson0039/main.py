from datetime import datetime, date, time, timedelta, timezone

# ----------------------------
# Ví dụ 1: Tính tuổi từ ngày sinh
# ----------------------------

def tinh_tuoi(ngay_sinh):
    hom_nay = date.today()
    tuoi = hom_nay.year - ngay_sinh.year
    
    # Kiểm tra nếu chưa đến sinh nhật trong năm nay
    if (hom_nay.month, hom_nay.day) < (ngay_sinh.month, ngay_sinh.day):
        tuoi -= 1
    
    return tuoi

# Tạo ngày sinh
ngay_sinh = date(1990, 5, 20)
tuoi = tinh_tuoi(ngay_sinh)
print(f"Tuổi của bạn là: {tuoi} tuổi")

# ----------------------------
# Ví dụ 2: Chuyển đổi múi giờ
# ----------------------------

# Tạo thời gian tại Việt Nam (UTC+7)
tz_vn = timezone(timedelta(hours=7))
dt_vn = datetime(2025, 7, 15, 14, 30, tzinfo=tz_vn)

# Tạo múi giờ New York (UTC-4)
tz_ny = timezone(timedelta(hours=-4))
dt_ny = dt_vn.astimezone(tz_ny)

print(f"Thời gian ở Việt Nam: {dt_vn.strftime('%d/%m/%Y %H:%M')}")
print(f"Thời gian ở New York: {dt_ny.strftime('%d/%m/%Y %H:%M')}")

# ----------------------------
# Ví dụ 3: Lập lịch nhắc nhở
# ----------------------------

def lap_lich_nhap_nho(su_kien, thoi_gian_cho):
    thoi_diem_hien_tai = datetime.now()
    thoi_diem_nhap_nho = thoi_diem_hien_tai + timedelta(minutes=thoi_gian_cho)
    
    print(f"Đã đặt nhắc nhở cho sự kiện '{su_kien}' sau {thoi_gian_cho} phút.")
    print(f"Thời gian nhắc: {thoi_diem_nhap_nho.strftime('%H:%M:%S')}")

lap_lich_nhap_nho("Họp nhóm", 5)