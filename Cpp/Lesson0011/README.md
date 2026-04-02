# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một phần quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ các tệp trên đĩa cứng. Trong C++, bạn có thể sử dụng các hàm và lớp để thực hiện các thao tác này. Bài viết này sẽ giới thiệu về lý thuyết và ví dụ làm việc với tệp trong C++.

## Lý thuyết
Để làm việc với tệp trong C++, bạn cần sử dụng các lớp và hàm trong thư viện `<fstream>`. Có ba loại tệp chính:
- `ifstream`: dùng để đọc dữ liệu từ tệp.
- `ofstream`: dùng để ghi dữ liệu vào tệp.
- `fstream`: dùng để đọc và ghi dữ liệu từ tệp.

Để mở một tệp, bạn cần sử dụng hàm `open()` và truyền đường dẫn đến tệp vào hàm này. Sau khi mở tệp, bạn có thể sử dụng các hàm như `read()`, `write()`, `getline()` để đọc và ghi dữ liệu.

Ví dụ, để đọc dữ liệu từ một tệp có tên "example.txt", bạn có thể sử dụng đoạn code sau:
```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    std::ifstream file("example.txt");
    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            std::cout << line << std::endl;
        }
        file.close();
    } else {
        std::cout << "Không thể mở tệp.";
    }
    return 0;
}
```

## Ví dụ
Dưới đây là một ví dụ minh họa cách ghi dữ liệu vào một tệp:
```cpp
#include <fstream>
#include <iostream>

int main() {
    std::ofstream file("example.txt");
    if (file.is_open()) {
        file << "Xin chào, thế giới!" << std::endl;
        file.close();
    } else {
        std::cout << "Không thể mở tệp.";
    }
    return 0;
}
```
Sau khi chạy đoạn code này, một tệp mới có tên "example.txt" sẽ được tạo ra và chứa dòng chữ "Xin chào, thế giới!".

## Bài tập
Bài tập cho bạn:
- Tạo một tệp mới có tên "thongtin.txt" và ghi thông tin về tên và tuổi của bạn vào tệp đó.
- Đọc dữ liệu từ tệp "thongtin.txt" và in ra màn hình.
- Tạo một chương trình cho phép người dùng nhập thông tin về tên và tuổi, sau đó ghi thông tin đó vào tệp "thongtin.txt".