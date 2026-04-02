# Xử lý tệp
## Giới thiệu
Xử lý tệp là một phần quan trọng trong lập trình, cho phép bạn đọc và ghi dữ liệu vào tệp tin. Trong C++, việc xử lý tệp được thực hiện thông qua các luồng tệp (file stream). Bài viết này sẽ giới thiệu về các khái niệm cơ bản và cách sử dụng tệp trong C++.

## Lý thuyết
Trong C++, có ba loại luồng tệp chính: `ifstream` (đọc), `ofstream` (ghi) và `fstream` (đọc và ghi). Để sử dụng tệp, bạn cần bao gồm thư viện `fstream` vào chương trình của mình. Sau đó, bạn có thể tạo một đối tượng luồng tệp và sử dụng các phương thức như `open()`, `close()`, `read()`, `write()` để thực hiện các hoạt động trên tệp.

Ví dụ, để mở một tệp tin để đọc, bạn có thể sử dụng `ifstream` như sau:
```cpp
#include <fstream>
using namespace std;

int main() {
    ifstream file("example.txt");
    if (file.is_open()) {
        cout << "Tệp tin được mở thành công." << endl;
        file.close();
    } else {
        cout << "Không thể mở tệp tin." << endl;
    }
    return 0;
}
```

## Ví dụ
Dưới đây là một ví dụ minh họa việc đọc và ghi tệp tin:
```cpp
#include <fstream>
using namespace std;

int main() {
    // Ghi tệp tin
    ofstream outFile("example.txt");
    if (outFile.is_open()) {
        outFile << "Xin chào, thế giới!" << endl;
        outFile.close();
        cout << "Đã ghi tệp tin thành công." << endl;
    } else {
        cout << "Không thể ghi tệp tin." << endl;
    }

    // Đọc tệp tin
    ifstream inFile("example.txt");
    if (inFile.is_open()) {
        string line;
        while (getline(inFile, line)) {
            cout << line << endl;
        }
        inFile.close();
    } else {
        cout << "Không thể đọc tệp tin." << endl;
    }
    return 0;
}
```

## Bài tập
Bài tập cho bạn:
- Tạo một chương trình cho phép người dùng nhập thông tin (tên, tuổi, địa chỉ) và lưu vào một tệp tin.
- Đọc thông tin từ tệp tin và hiển thị ra màn hình.
- Thêm chức năng xóa và sửa thông tin trong tệp tin.

Hãy thử thực hiện các bài tập trên và khám phá thêm về các chức năng khác của xử lý tệp trong C++.