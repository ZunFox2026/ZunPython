# Làm việc với File
## Giới thiệu
Làm việc với file là một phần quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ các file trên đĩa cứng. Trong C++, bạn có thể sử dụng các hàm và đối tượng trong thư viện `<fstream>` để thực hiện các操作 này. Bài viết này sẽ giới thiệu về cách làm việc với file trong C++.

## Lý thuyết
Để làm việc với file trong C++, bạn cần sử dụng các đối tượng sau:
- `ifstream`: Đối tượng này được sử dụng để đọc dữ liệu từ một file.
- `ofstream`: Đối tượng này được sử dụng để ghi dữ liệu vào một file.
- `fstream`: Đối tượng này được sử dụng để đọc và ghi dữ liệu từ/đến một file.

Các hàm thường dùng khi làm việc với file:
- `open()`: Mở một file để đọc hoặc ghi.
- `close()`: Đóng một file sau khi đã đọc hoặc ghi xong.
- `read()`: Đọc dữ liệu từ file vào một biến.
- `write()`: Ghi dữ liệu từ một biến vào file.
- `getline()`: Đọc một dòng từ file.

Ví dụ sử dụng `ofstream` để ghi dữ liệu vào file:
```cpp
#include <fstream>
using namespace std;

int main() {
    ofstream file("example.txt");
    if (file.is_open()) {
        file << "Xin chào, thế giới!";
        file.close();
    } else {
        cout << "Không thể mở file.";
    }
    return 0;
}
```

## Ví dụ
Dưới đây là ví dụ về việc đọc và ghi file:
```cpp
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    // Ghi dữ liệu vào file
    ofstream fileGhi("example.txt");
    if (fileGhi.is_open()) {
        fileGhi << "Đây là nội dung được ghi vào file.";
        fileGhi.close();
    } else {
        cout << "Không thể mở file để ghi.";
    }

    // Đọc dữ liệu từ file
    ifstream fileDoc("example.txt");
    if (fileDoc.is_open()) {
        string dong;
        while (getline(fileDoc, dong)) {
            cout << dong << endl;
        }
        fileDoc.close();
    } else {
        cout << "Không thể mở file để đọc.";
    }
    return 0;
}
```

## Bài tập
Bài tập 1: Tạo một chương trình cho phép người dùng nhập tên và tuổi, sau đó ghi thông tin này vào một file có tên là "thongtin.txt".

Bài tập 2: Tạo một chương trình đọc thông tin từ file "thongtin.txt" và hiển thị ra màn hình.

Bài tập 3: Tạo một chương trình cho phép người dùng thêm, xóa, sửa thông tin trong file "thongtin.txt".