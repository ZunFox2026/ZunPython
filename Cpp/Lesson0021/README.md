# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một phần quan trọng trong lập trình, cho phép chúng ta lưu trữ và đọc dữ liệu từ các tệp. Trong C++, chúng ta có thể làm việc với tệp bằng cách sử dụng các hàm và lớp trong thư viện chuẩn. Bài viết này sẽ giới thiệu về cách làm việc với tệp trong C++.

## Lý thuyết
Để làm việc với tệp trong C++, chúng ta cần sử dụng các hàm và lớp sau:
- `fstream`: Đây là lớp cơ bản để làm việc với tệp. Nó cung cấp các hàm để mở, đọc và viết tệp.
- `ifstream`: Đây là lớp con của `fstream`, sử dụng để đọc tệp.
- `ofstream`: Đây là lớp con của `fstream`, sử dụng để viết tệp.
- `open()`: Hàm này dùng để mở tệp.
- `close()`: Hàm này dùng để đóng tệp.
- `read()`: Hàm này dùng để đọc dữ liệu từ tệp.
- `write()`: Hàm này dùng để viết dữ liệu vào tệp.

Ví dụ về cách mở và đóng tệp:
```cpp
#include <fstream>

int main() {
    std::ifstream file("example.txt");
    if (file.is_open()) {
        // Đọc hoặc viết tệp
        file.close();
    } else {
        std::cout << "Không thể mở tệp";
    }
    return 0;
}
```

## Ví dụ
Dưới đây là ví dụ về cách đọc và viết tệp:
```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    // Viết tệp
    std::ofstream outFile("example.txt");
    if (outFile.is_open()) {
        outFile << "Xin chào, thế giới!";
        outFile.close();
        std::cout << "Đã viết tệp thành công";
    } else {
        std::cout << "Không thể viết tệp";
    }

    // Đọc tệp
    std::ifstream inFile("example.txt");
    if (inFile.is_open()) {
        std::string line;
        while (std::getline(inFile, line)) {
            std::cout << line << std::endl;
        }
        inFile.close();
    } else {
        std::cout << "Không thể đọc tệp";
    }

    return 0;
}
```

## Bài tập
Bài tập 1: Tạo một chương trình C++ để viết một chuỗi vào tệp. Sau đó, đọc chuỗi từ tệp và in ra màn hình.
Bài tập 2: Tạo một chương trình C++ để đọc tất cả các dòng từ một tệp và in ra màn hình. Sử dụng hàm `std::getline()` để đọc từng dòng.
Bài tập 3: Tạo một chương trình C++ để sao chép nội dung từ một tệp sang một tệp khác.