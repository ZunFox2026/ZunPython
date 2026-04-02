# Tìm số lớn nhất trong danh sách số
def tim_so_lon_nhat(danh_sach_so):
    # Nếu danh sách rỗng
    if len(danh_sach_so) == 0:
        return None  # Không có số lớn nhất

    # Giả sử số đầu tiên là số lớn nhất
    so_lon_nhat = danh_sach_so[0]

    # Duyệt qua danh sách số
    for so in danh_sach_so:
        # Nếu số hiện tại lớn hơn số lớn nhất
        if so > so_lon_nhat:
            so_lon_nhat = so  # Cập nhật số lớn nhất

    return so_lon_nhat  # Trả về số lớn nhất


# Ví dụ sử dụng
danh_sach_so = [12, 45, 7, 23, 56, 89, 34]
so_lon_nhat = tim_so_lon_nhat(danh_sach_so)

if so_lon_nhat is not None:
    print("Số lớn nhất là:", so_lon_nhat)
else:
    print("Danh sách số rỗng")