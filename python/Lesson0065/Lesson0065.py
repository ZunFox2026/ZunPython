# Mở tệp tin và đọc nội dung
def doc_tepp_tin(ten_tep):
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

# Mở tệp tin và ghi nội dung
def ghi_tepp_tin(ten_tep, noi_dung):
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
def main():
    ten_tep = 'test.txt'
    # Ghi nội dung vào tệp tin
    noi_dung = 'Xin chào, thế giới!'
    ghi_tepp_tin(ten_tep, noi_dung)
    # Đọc và hiển thị nội dung tệp tin
    print(doc_tepp_tin(ten_tep))

if __name__ == "__main__":
    main()