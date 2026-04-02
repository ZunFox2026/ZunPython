# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một phần quan trọng trong lập trình C++. Trong bài này, chúng ta sẽ tìm hiểu cách đọc và ghi dữ liệu vào tệp, cũng như cách sử dụng các hàm và đối tượng liên quan đến tệp.

## Lý thuyết
Để làm việc với tệp trong C++, chúng ta cần sử dụng thư viện `fstream`. Thư viện này cung cấp các đối tượng và hàm để đọc và ghi dữ liệu vào tệp.

Có hai loại tệp chính: tệp văn bản (text file) và tệp nhị phân (binary file). Tệp văn bản chứa dữ liệu dưới dạng văn bản, trong khi tệp nhị phân chứa dữ liệu dưới dạng nhị phân.

Để đọc và ghi dữ liệu vào tệp, chúng ta cần thực hiện các bước sau:

- Mở tệp: Sử dụng hàm `open()` để mở tệp.
- Đọc hoặc ghi dữ liệu: Sử dụng các hàm `read()` hoặc `write()` để đọc hoặc ghi dữ liệu vào tệp.
- Đóng tệp: Sử dụng hàm `close()` để đóng tệp.

Ví dụ về việc mở và đóng tệp:
```cpp
#include <fstream>

int main() {
    std::ofstream file("example.txt");
    if (file.is_open()) {
        file << "Xin chào, thế giới!";
        file.close();
    }
    return 0;
}
```

## Ví dụ
Dưới đây là ví dụ về việc đọc và ghi dữ liệu vào tệp:

```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    // Ghi dữ liệu vào tệp
    std::ofstream fileGhi("example.txt");
    if (fileGhi.is_open()) {
        std::string ten = "Nguyễn Văn A";
        int tuoi = 20;
        fileGhi << "Tên: " << ten << "\n";
        fileGhi << "Tuổi: " << tuoi << "\n";
        fileGhi.close();
    }

    // Đọc dữ liệu từ tệp
    std::ifstream fileDoc("example.txt");
    if (fileDoc.is_open()) {
        std::string dong;
        while (std::getline(fileDoc, dong)) {
            std::cout << dong << "\n";
        }
        fileDoc.close();
    }
    return 0;
}
```

## Bài tập
Bài tập 1: Tạo một chương trình C++ để ghi dữ liệu vào tệp. Dữ liệu bao gồm tên, tuổi và địa chỉ.

Bài tập 2: Tạo một chương trình C++ để đọc dữ liệu từ tệp và hiển thị ra màn hình.

Bài tập 3: Tạo một chương trình C++ để chỉnh sửa dữ liệu trong tệp. Ví dụ, thay thế tên cũ bằng tên mới.

Hy vọng qua các ví dụ và bài tập trên, bạn đã hiểu rõ hơn về cách làm việc với tệp trong C++. Hãy thực hành và hoàn thiện kỹ năng của mình!