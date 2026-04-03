import os
import shutil

def main():
    """
    Bài 51: Xử Lý Tập Tin và Thư Mục với Module os và shutil
    Mục tiêu: Làm quen với các thao tác phổ biến trên hệ thống tập tin và thư mục
    bằng cách sử dụng các hàm từ module os và shutil.
    """

    print("=== BÀI 51: XỬ LÝ TẬP TIN VÀ THƯ MỤC ===\n")

    # Ví dụ 1: Tạo và kiểm tra thư mục
    print("VÍ DỤ 1: Tạo và kiểm tra thư mục")
    folder_name = "test_folder"
    
    # Kiểm tra nếu thư mục chưa tồn tại thì tạo mới
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"✅ Đã tạo thư mục: {folder_name}")
    else:
        print(f"📁 Thư mục '{folder_name}' đã tồn tại.")

    # Tạo một file trong thư mục vừa tạo
    file_path = os.path.join(folder_name, "example.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Đây là nội dung ví dụ.\n")
        f.write("Module os và shutil giúp thao tác với file và folder dễ dàng hơn.\n")
    print(f"📄 Đã tạo file: {file_path}")

    # Ví dụ 2: Liệt kê nội dung thư mục và sao chép file
    print("\nVÍ DỤ 2: Liệt kê nội dung và sao chép file")
    
    # Liệt kê tất cả các file và thư mục con
    print("📁 Nội dung trong thư mục hiện tại:")
    for item in os.listdir("."):
        if os.path.isfile(item):
            print(f"  📄 {item}")
        elif os.path.isdir(item):
            print(f"  📂 {item}")

    # Tạo thư mục đích để sao chép
    backup_folder = "backup_folder"
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    # Sao chép file bằng shutil
    backup_file = os.path.join(backup_folder, "example_backup.txt")
    shutil.copy(file_path, backup_file)
    print(f"📎 Đã sao chép file đến: {backup_file}")

    # Ví dụ 3: Di chuyển và xóa file/thư mục
    print("\nVÍ DỤ 3: Di chuyển và xóa file/thư mục")
    
    # Di chuyển file (đổi tên cũng là một dạng di chuyển)
    moved_file = os.path.join(folder_name, "example_renamed.txt")
    shutil.move(file_path, moved_file)
    print(f"🔄 Đã đổi tên file thành: {moved_file}")

    # Xóa file backup (sử dụng os.remove)
    if os.path.exists(backup_file):
        os.remove(backup_file)
        print(f"🗑️ Đã xóa file: {backup_file}")

    # Xóa toàn bộ thư mục và nội dung bên trong (shutil.rmtree)
    if os.path.exists(backup_folder):
        shutil.rmtree(backup_folder)
        print(f"🗑️ Đã xóa thư mục: {backup_folder}")

    # Bài tập nhỏ: Tạo một hàm kiểm tra và xóa thư mục nếu tồn tại
    print("\n=== BÀI TẬP NHỎ ===")
    print("Viết hàm xóa thư mục nếu tồn tại. Dưới đây là ví dụ hoàn chỉnh:")

    def delete_folder_if_exists(folder):
        """Xóa một thư mục nếu nó tồn tại"""
        if os.path.exists(folder) and os.path.isdir(folder):
            shutil.rmtree(folder)
            print(f"✅ Đã xóa thư mục: {folder}")
        else:
            print(f"❌ Thư mục '{folder}' không tồn tại hoặc không phải thư mục.")

    # Kiểm thử hàm
    delete_folder_if_exists("test_folder")  # Xóa thư mục test_folder

    # Tạo lại và kiểm thử xóa lần nữa
    os.makedirs("temp_test")
    print(f"📁 Đã tạo thư mục tạm: temp_test")
    delete_folder_if_exists("temp_test")

    print("\n✅ Hoàn thành tất cả các thao tác ví dụ và bài tập.")


# Gọi hàm chính
if __name__ == "__main__":
    main()
```

---

### 💡 Mô tả:
- **Module `os`**: Dùng để kiểm tra, tạo, xóa, duyệt thư mục và file.
- **Module `shutil`**: Dùng cho các thao tác cấp cao như sao chép, di chuyển, xóa thư mục có nội dung.
- **Ví dụ**:
  1. Tạo thư mục và file.
  2. Liệt kê nội dung, sao chép file.
  3. Di chuyển, đổi tên, xóa file và thư mục.
- **Bài tập nhỏ**: Viết hàm xóa thư mục an toàn nếu tồn tại.

> ✅ Chạy script này sẽ thực hiện các thao tác trên hệ thống file — hãy chạy trong môi trường an toàn (ví dụ: thư mục test riêng).