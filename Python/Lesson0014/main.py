import json
import os

# Ví dụ 1: Quản lý danh sách sinh viên
# Tạo dữ liệu sinh viên
sinh_vien = [
    {"ten": "An", "tuoi": 20, "diem": 8.5},
    {"ten": "Binh", "tuoi": 21, "diem": 7.2},
    {"ten": "Cuong", "tuoi": 19, "diem": 9.0}
]

# Ghi danh sách sinh viên vào file JSON
ten_file = "sinh_vien.json"
with open(ten_file, "w", encoding="utf-8") as f:
    json.dump(sinh_vien, f, ensure_ascii=False, indent=4)

print("Đã ghi danh sách sinh viên vào file.")

# Đọc lại danh sách sinh viên
tam_thoi = []
if os.path.exists(ten_file):
    with open(ten_file, "r", encoding="utf-8") as f:
        tam_thoi = json.load(f)
    print("Danh sách sinh viên đã đọc:")
    for sv in tam_thoi:
        print(f"- {sv['ten']}, {sv['tuoi']} tuổi, điểm: {sv['diem']}")

# Ví dụ 2: Cập nhật điểm số sinh viên
def cap_nhat_diem(ten, diem_moi, file_path):
    """Cập nhật điểm của sinh viên theo tên"""
    if not os.path.exists(file_path):
        print("Không tìm thấy file.")
        return False
    
    with open(file_path, "r", encoding="utf-8") as f:
        danh_sach = json.load(f)
    
    cap_nhat = False
    for sv in danh_sach:
        if sv["ten"].lower() == ten.lower():
            sv["diem"] = diem_moi
            cap_nhat = True
            break
    
    if cap_nhat:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(danh_sach, f, ensure_ascii=False, indent=4)
        print(f"Đã cập nhật điểm cho {ten} thành {diem_moi}")
    else:
        print(f"Không tìm thấy sinh viên tên {ten}")
    
    return cap_nhat

# Cập nhật điểm cho An
cap_nhat_diem("An", 9.5, ten_file)

# Ví dụ 3: Xử lý dữ liệu từ API giả lập
def gia_lap_api():
    """Mô phỏng dữ liệu trả về từ API"""
    du_lieu_tho = '''
    {
        "nguoi_dung": [
            {"id": 1, "ten": "Nguyen Van A", "email": "a@example.com"},
            {"id": 2, "ten": "Tran Thi B", "email": "b@example.com"}
        ],
        "tong_so": 2
    }
    '''
    # Chuyển chuỗi JSON thành đối tượng Python
    du_lieu = json.loads(du_lieu_tho)
    
    print("Dữ liệu người dùng từ API:")
    for nguoi in du_lieu["nguoi_dung"]:
        print(f"ID: {nguoi['id']}, Tên: {nguoi['ten']}, Email: {nguoi['email']}")
    
    return du_lieu

# Gọi hàm giả lập API
gia_lap_api()