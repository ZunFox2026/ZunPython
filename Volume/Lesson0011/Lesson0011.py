# Bài 11: Làm việc với tệp tin

# Mở tệp tin để đọc
def doc_tap_tin(ten_tap_tin):
    try:
        # Mở tệp tin và đọc nội dung
        with open(ten_tap_tin, 'r') as f:
            noi_dung = f.read()
            return noi_dung
    except FileNotFoundError:
        print("Tệp tin không tồn tại")
        return None

# Mở tệp tin để ghi
def ghi_tap_tin(ten_tap_tin, noi_dung):
    try:
        # Mở tệp tin và ghi nội dung
        with open(ten_tap_tin, 'w') as f:
            f.write(noi_dung)
        print("Ghi thành công")
    except Exception as e:
        print("Lỗi khi ghi tệp tin: ", str(e))

# Thêm nội dung vào tệp tin
def them_noi_dung_tap_tin(ten_tap_tin, noi_dung):
    try:
        # Mở tệp tin và thêm nội dung
        with open(ten_tap_tin, 'a') as f:
            f.write(noi_dung)
        print("Thêm nội dung thành công")
    except Exception as e:
        print("Lỗi khi thêm nội dung: ", str(e))

# Đọc và ghi tệp tin
def main():
    ten_tap_tin = "example.txt"
    noi_dung = "Xin chào, thế giới!"

    # Ghi nội dung vào tệp tin
    ghi_tap_tin(ten_tap_tin, noi_dung)

    # Đọc nội dung từ tệp tin
    noi_dung_doc = doc_tap_tin(ten_tap_tin)
    print("Nội dung tệp tin: ", noi_dung_doc)

    # Thêm nội dung vào tệp tin
    them_noi_dung_tap_tin(ten_tap_tin, "\nThèm nội dung mới")

    # Đọc lại nội dung từ tệp tin
    noi_dung_doc = doc_tap_tin(ten_tap_tin)
    print("Nội dung tệp tin sau khi thêm: ", noi_dung_doc)

if __name__ == "__main__":
    main()