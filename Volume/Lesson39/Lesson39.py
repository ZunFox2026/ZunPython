# Bài 39: Tìm phần tử lớn nhất

def tim_phan_tu_lon_nhat(danh_sach):
    # Khởi tạo giá trị lớn nhất là phần tử đầu tiên trong danh sách
    phan_tu_lon_nhat = danh_sach[0]
    
    # Duyệt qua từng phần tử trong danh sách
    for phan_tu in danh_sach:
        # Nếu phần tử hiện tại lớn hơn phần tử lớn nhất hiện tại
        if phan_tu > phan_tu_lon_nhat:
            # Cập nhật phần tử lớn nhất
            phan_tu_lon_nhat = phan_tu
    
    # Trả về phần tử lớn nhất
    return phan_tu_lon_nhat

# Ví dụ sử dụng
danh_sach_so = [12, 45, 7, 23, 56, 89, 34]
print("Danh sách số:", danh_sach_so)
print("Phần tử lớn nhất:", tim_phan_tu_lon_nhat(danh_sach_so))