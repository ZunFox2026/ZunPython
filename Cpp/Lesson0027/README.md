# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một kỹ năng quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ các tệp trên đĩa cứng. Trong C++, việc làm việc với tệp được thực hiện thông qua các hàm và lớp trong thư viện `<fstream>`. Bài này sẽ giới thiệu về cách làm việc với tệp trong C++.

## Lý thuyết
Để làm việc với tệp trong C++, bạn cần bao gồm thư viện `<fstream>` vào chương trình của mình. Thư viện này cung cấp các lớp `ifstream`, `ofstream` và `fstream` để đọc, viết và đọc/ghi tệp.

- `ifstream`: lớp này cho phép bạn đọc dữ liệu từ một tệp.
- `ofstream`: lớp này cho phép bạn viết dữ liệu vào một tệp.
- `fstream`: lớp này cho phép bạn đọc và viết dữ liệu vào một tệp.

Để mở một tệp, bạn cần sử dụng hàm `open()` và truyền vào đường dẫn đến tệp. Để đọc hoặc viết dữ liệu, bạn có thể sử dụng các toán tử `>>` và `<<`.

Ví dụ:
```cpp
#include <fstream>
#include <iostream>

int main() {
    std::ifstream file("example.txt");
    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            std::cout << line << std::endl;
        }
        file.close();
    } else {
        std::cout << "Không thể mở tệp";
    }
    return 0;
}
```

## Ví dụ
Dưới đây là ví dụ về cách đọc và viết tệp trong C++:
```cpp
#include <fstream>
#include <iostream>

int main() {
    // Tạo tệp và viết dữ liệu
    std::ofstream outFile("example.txt");
    if (outFile.is_open()) {
        outFile << "Xin chào, thế giới!" << std::endl;
        outFile.close();
    } else {
        std::cout << "Không thể mở tệp";
    }

    // Đọc dữ liệu từ tệp
    std::ifstream inFile("example.txt");
    if (inFile.is_open()) {
        std::string line;
        while (std::getline(inFile, line)) {
            std::cout << line << std::endl;
        }
        inFile.close();
    } else {
        std::cout << "Không thể mở tệp";
    }
    return 0;
}
```

## Bài tập
Để rèn luyện kỹ năng làm việc với tệp trong C++, bạn có thể thực hiện các bài tập sau:

- Tạo một chương trình đọc dữ liệu từ một tệp và in ra màn hình.
- Tạo một chương trình viết dữ liệu vào một tệp.
- Tạo một chương trình đọc và viết dữ liệu vào một tệp.
- Tạo một chương trình sao chép nội dung từ một tệp sang một tệp khác.

Hãy nhớ kiểm tra lỗi khi mở tệp và đóng tệp sau khi sử dụng để tránh rò rỉ bộ nhớ. Chúc bạn thành công!