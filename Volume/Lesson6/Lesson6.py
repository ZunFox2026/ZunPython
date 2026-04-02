# Mở tệp để đọc
f = open("test.txt", "r")
 
# Đọc nội dung tệp
noidung = f.read()
 
# In nội dung tệp
print(noidung)
 
# Đóng tệp
f.close()

# Mở tệp để ghi
f = open("test.txt", "w")
 
# Ghi nội dung vào tệp
f.write("Xin chào, thế giới!")
 
# Đóng tệp
f.close()

# Mở tệp để đọc và ghi
f = open("test.txt", "r+")
 
# Đọc nội dung tệp
noidung = f.read()
print(noidung)
 
# Đặt con trỏ về đầu tệp
f.seek(0)
 
# Ghi nội dung vào tệp
f.write("Xin chào, thế giới mới!")
 
# Đóng tệp
f.close()

# Sử dụng with để mở tệp
with open("test.txt", "r") as f:
    # Đọc nội dung tệp
    noidung = f.read()
    print(noidung)

# Lưu ý: Không cần đóng tệp khi sử dụng with