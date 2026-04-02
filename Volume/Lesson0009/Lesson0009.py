# Mở tệp tin để đọc
file = open('test.txt', 'r')
 
# Đọc nội dung của tệp tin
noidung = file.read()
 
# In nội dung của tệp tin
print(noidung)
 
# Đóng tệp tin
file.close()

# Mở tệp tin để ghi
file = open('test.txt', 'w')
 
# Ghi nội dung vào tệp tin
file.write('Xin chào thế giới!')
 
# Đóng tệp tin
file.close()

# Mở tệp tin để đọc và ghi
file = open('test.txt', 'r+')
 
# Đọc nội dung của tệp tin
noidung = file.read()
print(noidung)
 
# Di chuyển con trỏ về đầu tệp tin
file.seek(0)
 
# Ghi nội dung vào tệp tin
file.write('Xin chào thế giới mới!')
 
# Đóng tệp tin
file.close()

# Sử dụng with để mở tệp tin
with open('test.txt', 'r') as file:
    # Đọc nội dung của tệp tin
    noidung = file.read()
    print(noidung)

# Tạo một tệp tin mới
with open('new_file.txt', 'w') as file:
    # Ghi nội dung vào tệp tin
    file.write('Nội dung mới')

# Đọc từng dòng của tệp tin
with open('test.txt', 'r') as file:
    # Đọc từng dòng của tệp tin
    for line in file:
        print(line)

# Đọc tất cả các dòng của tệp tin
with open('test.txt', 'r') as file:
    # Đọc tất cả các dòng của tệp tin
    lines = file.readlines()
    print(lines)