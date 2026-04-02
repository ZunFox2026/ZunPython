# Bài 11: Làm việc với file

# Mở file và đọc nội dung
def doc_file(file_name):
    try:
        # Mở file ở chế độ đọc
        with open(file_name, 'r', encoding='utf-8') as file:
            # Đọc nội dung file
            content = file.read()
            return content
    except FileNotFoundError:
        print("File không tồn tại")
        return None

# Ghi nội dung vào file
def ghi_file(file_name, content):
    try:
        # Mở file ở chế độ ghi
        with open(file_name, 'w', encoding='utf-8') as file:
            # Ghi nội dung vào file
            file.write(content)
    except Exception as e:
        print("Lỗi ghi file:", str(e))

# Chương trình chính
def main():
    file_name = 'example.txt'
    content = 'Xin chào, thế giới!'
    
    # Ghi nội dung vào file
    ghi_file(file_name, content)
    
    # Đọc nội dung từ file
    doc_content = doc_file(file_name)
    
    # In nội dung đọc được
    if doc_content is not None:
        print("Nội dung file:", doc_content)

if __name__ == "__main__":
    main()