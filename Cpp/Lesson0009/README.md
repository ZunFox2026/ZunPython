# Xử lý tệp
## Giới thiệu
Trong lập trình C++, việc xử lý tệp là một phần quan trọng và cần thiết. Xử lý tệp cho phép chúng ta lưu trữ và truy xuất dữ liệu từ các tệp trên đĩa cứng, giúp chương trình của chúng ta có thể lưu trữ và quản lý dữ liệu một cách hiệu quả. Bài viết này sẽ giới thiệu về các khái niệm cơ bản và cách thức xử lý tệp trong C++.

## Lý thuyết
Để xử lý tệp trong C++, chúng ta cần sử dụng các hàm và lớp có sẵn trong thư viện `<fstream>`. Có ba loại tệp chính mà chúng ta có thể xử lý: 
- **Tệp nhập** (input file): là tệp mà chương trình đọc dữ liệu từ đó.
- **Tệp xuất** (output file): là tệp mà chương trình ghi dữ liệu vào đó.
- **Tệp nhập/xuất** (input/output file): là tệp mà chương trình có thể đọc và ghi dữ liệu.

Chúng ta có thể sử dụng các lớp `ifstream`, `ofstream` và `fstream` để tương tác với các loại tệp này. Ví dụ:
```cpp
#include <fstream>
#include <iostream>

int main() {
    std::ifstream inputFile("input.txt"); // Mở tệp nhập
    std::ofstream outputFile("output.txt"); // Mở tệp xuất
    std::fstream ioFile("ioFile.txt", std::ios::in | std::ios::out); // Mở tệp nhập/xuất

    // Đọc và ghi dữ liệu
    char buffer[100];
    inputFile.getline(buffer, 100);
    std::cout << buffer << std::endl;
    outputFile << "Xin chào!" << std::endl;

    // Đóng tệp
    inputFile.close();
    outputFile.close();
    ioFile.close();

    return 0;
}
```

## Ví dụ
Giả sử chúng ta muốn tạo một chương trình đơn giản để lưu trữ và hiển thị danh sách sinh viên. Chúng ta có thể sử dụng tệp để lưu trữ thông tin sinh viên.

```cpp
#include <fstream>
#include <iostream>
#include <string>

struct SinhVien {
    std::string ten;
    int tuoi;
};

int main() {
    std::ofstream fileOut("sinh_vien.txt");
    if (fileOut.is_open()) {
        SinhVien sv;
        sv.ten = "Nguyễn Văn A";
        sv.tuoi = 20;
        fileOut << sv.ten << "," << sv.tuoi << std::endl;
        fileOut.close();
    }

    std::ifstream fileIn("sinh_vien.txt");
    if (fileIn.is_open()) {
        std::string line;
        while (std::getline(fileIn, line)) {
            std::size_t pos = line.find(",");
            std::string ten = line.substr(0, pos);
            int tuoi = std::stoi(line.substr(pos + 1));
            std::cout << "Tên: " << ten << ", Tuổi: " << tuoi << std::endl;
        }
        fileIn.close();
    }

    return 0;
}
```

## Bài tập
1. Tạo một chương trình cho phép người dùng nhập thông tin sinh viên và lưu trữ vào một tệp.
2. Đọc thông tin từ tệp và hiển thị ra màn hình.
3. Thực hiện việc tìm kiếm thông tin sinh viên theo tên hoặc tuổi.
4. Cho phép người dùng cập nhật thông tin sinh viên.

Bài tập này sẽ giúp bạn hiểu rõ hơn về cách thức xử lý tệp trong C++ và ứng dụng vào các tình huống thực tế. Hãy thử nghiệm và tìm hiểu thêm về các hàm và lớp khác trong thư viện `<fstream>` để mở rộng kiến thức của mình.