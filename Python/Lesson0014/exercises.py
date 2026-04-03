import json
import os

# Bài tập 1: Tạo file JSON chứa thông tin sách
# Viết hàm tao_file_sach() để tạo file "sach.json" với ít nhất 3 cuốn sách
def tao_file_sach():
    # Gợi ý: Tạo danh sách các dictionary, mỗi dictionary là một cuốn sách
    pass

# Bài tập 2: Tìm kiếm sách theo tên tác giả
# Viết hàm tim_sach_theo_tac_gia(ten_tac_gia) trả về danh sách sách của tác giả đó
def tim_sach_theo_tac_gia(ten_tac_gia):
    # Gợi ý: Đọc file sach.json, duyệt danh sách và kiểm tra tác giả
    pass

# Bài tập 3: Cập nhật năm xuất bản của sách
# Viết hàm cap_nhat_nam_xb(ten_sach, nam_moi) để cập nhật năm xuất bản
# Trả về True nếu tìm thấy và cập nhật, False nếu không
def cap_nhat_nam_xb(ten_sach, nam_moi):
    # Gợi ý: Đọc file, tìm sách theo tên, cập nhật, ghi lại
    pass

# Bài tập 4: In danh sách sách theo định dạng đẹp
# Viết hàm in_danh_sach_sach() để in ra màn hình danh sách sách
# Định dạng: "[Tựa sách] - Tác giả (Năm)"
def in_danh_sach_sach():
    # Gợi ý: Duyệt danh sách và in theo định dạng
    pass

# Bài tập 5: Xử lý lỗi khi file không tồn tại
# Viết hàm doc_file_an_toan(ten_file) để đọc file JSON an toàn
# Nếu file không tồn tại, in thông báo và trả về danh sách rỗng
def doc_file_an_toan(ten_file):
    # Gợi ý: Dùng try-except hoặc os.path.exists
    pass