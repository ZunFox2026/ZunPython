# Mở tệp tin trong chế độ đọc
f = open('test.txt', 'r')
 
# Đọc nội dung tệp tin
noidung = f.read()
 
# In nội dung tệp tin
print(noidung)
 
# Đóng tệp tin
f.close()

# Mở tệp tin trong chế độ ghi
f = open('test.txt', 'w')
 
# Ghi nội dung vào tệp tin
f.write('Xin chào, thế giới!')
 
# Đóng tệp tin
f.close()

# Mở tệp tin trong chế độ thêm
f = open('test.txt', 'a')
 
# Thêm nội dung vào tệp tin
f.write('\nThế giới của Python!')
 
# Đóng tệp tin
f.close()

# Sử dụng with để mở tệp tin, không cần đóng tệp tin
with open('test.txt', 'r') as f:
    noidung = f.read()
    print(noidung)