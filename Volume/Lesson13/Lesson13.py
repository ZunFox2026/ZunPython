# Mở tệp tin để đọc
f = open('test.txt', 'r', encoding='utf-8')

# Đọc nội dung tệp tin
noidung = f.read()

# In nội dung tệp tin
print(noidung)

# Đóng tệp tin
f.close()

# Mở tệp tin để ghi
f = open('test.txt', 'w', encoding='utf-8')

# Ghi nội dung vào tệp tin
f.write('Xin chào thế giới!')

# Đóng tệp tin
f.close()

# Mở tệp tin để đọc và ghi
f = open('test.txt', 'r+', encoding='utf-8')

# Đọc nội dung tệp tin
noidung = f.read()

# In nội dung tệp tin
print(noidung)

# Di chuyển con trỏ đến đầu tệp tin
f.seek(0)

# Ghi nội dung vào tệp tin
f.write('Xin chào thế giới mới!')

# Đóng tệp tin
f.close()

# Sử dụng với từ khóa 'with' để không cần đóng tệp tin
with open('test.txt', 'r', encoding='utf-8') as f:
    # Đọc nội dung tệp tin
    noidung = f.read()

    # In nội dung tệp tin
    print(noidung)