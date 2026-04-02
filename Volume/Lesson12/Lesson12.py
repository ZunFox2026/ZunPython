# Mở tệp tin và đọc nội dung
def doc_tep_tin(ten_tep):
    try:
        # Mở tệp tin ở chế độ đọc
        f = open(ten_tep, 'r')
        # Đọc nội dung tệp tin
        noi_dung = f.read()
        # Đóng tệp tin
        f.close()
        return noi_dung
    except FileNotFoundError:
        print("Tệp tin không tồn tại")
        return None

# Ghi nội dung vào tệp tin
def ghi_tep_tin(ten_tep, noi_dung):
    try:
        # Mở tệp tin ở chế độ ghi
        f = open(ten_tep, 'w')
        # Ghi nội dung vào tệp tin
        f.write(noi_dung)
        # Đóng tệp tin
        f.close()
    except Exception as e:
        print("Lỗi khi ghi tệp tin: ", str(e))

# Chương trình chính
ten_tep = "example.txt"
noi_dung = "Xin chào, thế giới!"

# Ghi nội dung vào tệp tin
ghi_tep_tin(ten_tep, noi_dung)

# Đọc nội dung từ tệp tin
noi_dung_doc = doc_tep_tin(ten_tep)

# In nội dung đã đọc
if noi_dung_doc is not None:
    print("Nội dung đã đọc: ", noi_dung_doc)