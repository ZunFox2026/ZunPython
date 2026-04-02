# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một kỹ năng quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ tệp. Trong C++, việc này có thể được thực hiện thông qua các lớp và hàm trong thư viện chuẩn. Trong bài này, chúng ta sẽ tìm hiểu cách làm việc với tệp trong C++.

## Lý thuyết
Để làm việc với tệp trong C++, bạn cần bao gồm thư viện `fstream` vào chương trình của mình. Thư viện này cung cấp hai lớp chính: `ifstream` (lưu trữ tệp nhập) và `ofstream` (lưu trữ tệp xuất). Ngoài ra, còn có lớp `fstream` cho phép thực hiện cả nhập và xuất tệp.

- `ifstream`: Dùng để đọc dữ liệu từ tệp.
- `ofstream`: Dùng để ghi dữ liệu vào tệp.
- `fstream`: Dùng để đọc và ghi dữ liệu trong tệp.

Mở tệp có thể được thực hiện bằng cách tạo một đối tượng của lớp tương ứng và truyền đường dẫn tệp vào constructor. Ví dụ:
```cpp
#include <fstream>

int main() {
    std::ifstream inputFile("input.txt");
    std::ofstream outputFile("output.txt");
    return 0;
}
```

## Ví dụ
Dưới đây là một ví dụ về cách đọc dữ liệu từ tệp và ghi dữ liệu vào tệp khác:
```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    // Mở tệp nhập
    std::ifstream inputFile("input.txt");
    
    if (inputFile.is_open()) {
        std::string line;
        
        // Đọc từng dòng trong tệp nhập
        while (std::getline(inputFile, line)) {
            std::cout << line << std::endl;
        }
        
        inputFile.close();
    }
    
    // Mở tệp xuất
    std::ofstream outputFile("output.txt");
    
    if (outputFile.is_open()) {
        // Ghi dữ liệu vào tệp xuất
        outputFile << "Xin chào, thế giới!" << std::endl;
        outputFile.close();
    }
    
    return 0;
}
```

## Bài tập
Bài tập cho bạn:
- Tạo một chương trình C++ đọc nội dung từ tệp `input.txt` và sao chép nội dung đó vào tệp `output.txt`.
- Thêm chức năng kiểm tra nếu tệp `input.txt` không tồn tại hoặc không thể mở được, chương trình sẽ thông báo lỗi và kết thúc.
- Thực hiện viết chương trình trên và kiểm tra với các trường hợp khác nhau.