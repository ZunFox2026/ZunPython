# Làm việc với File
## Giới thiệu
Làm việc với file là một phần quan trọng trong lập trình, vì nó cho phép chúng ta lưu trữ và đọc dữ liệu từ các tệp tin trên đĩa cứng. Trong C++, chúng ta có thể sử dụng các hàm và đối tượng để thực hiện các thao tác này. Bài viết này sẽ giới thiệu về cách làm việc với file trong C++.

## Lý thuyết
Trong C++, chúng ta có thể sử dụng các đối tượng thuộc lớp `fstream` để làm việc với file. Lớp `fstream` cung cấp các hàm và đối tượng để đọc và ghi file. Có ba loại đối tượng chính:
- `ifstream`: để đọc file
- `ofstream`: để ghi file
- `fstream`: để đọc và ghi file

Chúng ta có thể sử dụng các hàm như `open()` để mở file, `close()` để đóng file, `read()` và `write()` để đọc và ghi dữ liệu.

Ví dụ:
```cpp
#include <fstream>
using namespace std;

int main() {
    ifstream file("example.txt");
    if (file.is_open()) {
        cout << "File đã được mở" << endl;
        file.close();
    } else {
        cout << "Không thể mở file" << endl;
    }
    return 0;
}
```

## Ví dụ
Để minh họa cách làm việc với file, chúng ta sẽ xem xét một ví dụ sau:
Giả sử chúng ta muốn tạo một chương trình để ghi thông tin của sinh viên vào một file. Chúng ta có thể sử dụng đối tượng `ofstream` để thực hiện việc này.

Ví dụ:
```cpp
#include <fstream>
#include <string>
using namespace std;

struct SinhVien {
    string ten;
    int tuoi;
};

int main() {
    SinhVien sv;
    cout << "Nhập tên sinh viên: ";
    cin >> sv.ten;
    cout << "Nhập tuổi sinh viên: ";
    cin >> sv.tuoi;

    ofstream file("sinhVien.txt");
    if (file.is_open()) {
        file << "Tên: " << sv.ten << endl;
        file << "Tuổi: " << sv.tuoi << endl;
        file.close();
        cout << "Thông tin đã được ghi vào file" << endl;
    } else {
        cout << "Không thể mở file" << endl;
    }
    return 0;
}
```

## Bài tập
Để củng cố kiến thức về làm việc với file, bạn có thể thực hiện các bài tập sau:
- Tạo một chương trình để đọc thông tin từ một file và hiển thị ra màn hình.
- Tạo một chương trình để ghi thông tin của một hình chữ nhật (độ dài, độ rộng) vào một file.
- Tạo một chương trình để đọc thông tin của một hình chữ nhật từ một file và tính toán diện tích của nó.