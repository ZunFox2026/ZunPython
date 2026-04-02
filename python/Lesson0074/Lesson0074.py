# Mở tệp tin để đọc
file = open("test.txt", "r")

# Đọc nội dung tệp tin
noidung = file.read()

# In nội dung tệp tin
print(noidung)

# Đóng tệp tin
file.close()

# Mở tệp tin để viết
file = open("test.txt", "w")

# Viết nội dung vào tệp tin
file.write("Xin chào, thế giới!")

# Đóng tệp tin
file.close()

# Mở tệp tin để thêm nội dung
file = open("test.txt", "a")

# Thêm nội dung vào tệp tin
file.write(" Đây là nội dung thêm vào.")

# Đóng tệp tin
file.close()

# Mở tệp tin để đọc
file = open("test.txt", "r")

# Đọc nội dung tệp tin
noidung = file.read()

# In nội dung tệp tin
print(noidung)

# Đóng tệp tin
file.close()