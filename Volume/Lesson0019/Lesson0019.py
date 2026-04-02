# Mở tệp tin để đọc
file = open("test.txt", "r")
 
# Đọc nội dung của tệp tin
noidung = file.read()
 
# In nội dung của tệp tin
print(noidung)
 
# Đóng tệp tin
file.close()

# Mở tệp tin để ghi
file = open("test.txt", "w")
 
# Ghi nội dung vào tệp tin
file.write("Xin chào thế giới!")
 
# Đóng tệp tin
file.close()

# Mở tệp tin để thêm nội dung
file = open("test.txt", "a")
 
# Thêm nội dung vào tệp tin
file.write("\nThế giới của lập trình!")
 
# Đóng tệp tin
file.close()

# Sử dụng with để mở tệp tin, không cần đóng tệp tin
with open("test.txt", "r") as file:
    noidung = file.read()
    print(noidung)