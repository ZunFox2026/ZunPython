# Làm việc với tệp tin
## Giới thiệu
Làm việc với tệp tin là một kỹ năng quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ các tệp tin trên đĩa cứng. Trong C++, có nhiều cách để làm việc với tệp tin, bao gồm việc sử dụng các hàm tiêu chuẩn như `fopen`, `fread`, `fwrite`,... và các lớp như `ifstream`, `ofstream`. Trong bài này, chúng ta sẽ tìm hiểu cách làm việc với tệp tin trong C++.

## Lý thuyết
Để làm việc với tệp tin trong C++, bạn cần bao gồm các thư viện cần thiết, chẳng hạn như `fstream` cho việc đọc và ghi tệp tin. Sau đó, bạn có thể tạo đối tượng của lớp `ifstream` hoặc `ofstream` để đọc hoặc ghi tệp tin. Để đọc tệp tin, bạn có thể sử dụng đối tượng `ifstream` và các hàm như `operator>>` để đọc dữ liệu từ tệp tin. Để ghi tệp tin, bạn có thể sử dụng đối tượng `ofstream` và các hàm như `operator<<` để ghi dữ liệu vào tệp tin.

Ví dụ về việc đọc và ghi tệp tin trong C++:
```cpp
#include <fstream>
#include <iostream>

int main() {
    // Tạo đối tượng để đọc tệp tin
    std::ifstream inputFile("input.txt");

    // Đọc dữ liệu từ tệp tin
    int data;
    inputFile >> data;
    std::cout << "Đọc từ tệp tin: " << data << std::endl;

    // Tạo đối tượng để ghi tệp tin
    std::ofstream outputFile("output.txt");

    // Ghi dữ liệu vào tệp tin
    outputFile << "Dữ liệu được ghi vào tệp tin" << std::endl;

    return 0;
}
```

## Ví dụ
Một ví dụ khác về việc sử dụng tệp tin trong C++ là việc lưu trữ và đọc dữ liệu người dùng. Chẳng hạn, bạn có thể tạo một chương trình cho phép người dùng nhập thông tin và lưu trữ thông tin đó vào một tệp tin. Sau đó, bạn có thể đọc thông tin từ tệp tin và hiển thị nó lên màn hình.

Ví dụ về việc lưu trữ và đọc thông tin người dùng:
```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    // Nhập thông tin người dùng
    std::string ten, diaChi;
    std::cout << "Nhập tên: ";
    std::getline(std::cin, ten);
    std::cout << "Nhập địa chỉ: ";
    std::getline(std::cin, diaChi);

    // Lưu trữ thông tin người dùng vào tệp tin
    std::ofstream outputFile("thongtin.txt");
    outputFile << "Tên: " << ten << std::endl;
    outputFile << "Địa chỉ: " << diaChi << std::endl;

    // Đọc thông tin người dùng từ tệp tin
    std::ifstream inputFile("thongtin.txt");
    std::string line;
    while (std::getline(inputFile, line)) {
        std::cout << line << std::endl;
    }

    return 0;
}
```

## Bài tập
Bài tập cho bạn:
- Tạo một chương trình cho phép người dùng nhập thông tin và lưu trữ thông tin đó vào một tệp tin.
- Đọc thông tin từ tệp tin và hiển thị nó lên màn hình.
- Thêm chức năng cho phép người dùng xóa thông tin từ tệp tin.
- Thêm chức năng cho phép người dùng tìm kiếm thông tin trong tệp tin.