# Làm việc với File
## Giới thiệu
Làm việc với file là một kỹ năng quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ các file trên đĩa cứng. Trong C++, việc làm việc với file được thực hiện thông qua các hàm và đối tượng trong thư viện `<fstream>`. Bài viết này sẽ giới thiệu về cách làm việc với file trong C++, bao gồm đọc và ghi file, cũng như một số ví dụ minh họa.

## Lý thuyết
Trong C++, có hai loại file chính: file văn bản (text file) và file nhị phân (binary file). File văn bản chứa dữ liệu dưới dạng văn bản, trong khi file nhị phân chứa dữ liệu dưới dạng nhị phân. Để làm việc với file, bạn cần sử dụng các đối tượng sau:
- `ifstream`: đối tượng này cho phép bạn đọc dữ liệu từ file.
- `ofstream`: đối tượng này cho phép bạn ghi dữ liệu vào file.
- `fstream`: đối tượng này cho phép bạn đọc và ghi dữ liệu từ/ vào file.

Để đọc hoặc ghi file, bạn cần mở file bằng cách sử dụng hàm `open()` và đóng file bằng cách sử dụng hàm `close()`. Nếu bạn không đóng file sau khi sử dụng, chương trình sẽ tự động đóng file khi đối tượng file bị hủy.

## Ví dụ
Dưới đây là một ví dụ minh họa về cách đọc và ghi file trong C++:
```cpp
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    // Ghi file
    ofstream outFile("example.txt");
    if (outFile.is_open()) {
        outFile << "Xin chào, thế giới!" << endl;
        outFile.close();
    } else {
        cout << "Không thể mở file để ghi!" << endl;
    }

    // Đọc file
    ifstream inFile("example.txt");
    if (inFile.is_open()) {
        char buffer[100];
        inFile.getline(buffer, 100);
        cout << buffer << endl;
        inFile.close();
    } else {
        cout << "Không thể mở file để đọc!" << endl;
    }

    return 0;
}
```
Trong ví dụ này, chúng ta tạo một file văn bản có tên "example.txt" và ghi chuỗi "Xin chào, thế giới!" vào file đó. Sau đó, chúng ta đọc file và in nội dung của file ra màn hình.

## Bài tập
Bài tập này yêu cầu bạn thực hiện các bước sau:
- Tạo một file văn bản có tên "sinh_vien.txt" và ghi thông tin của một sinh viên vào file đó, bao gồm họ tên, tuổi và điểm trung bình.
- Đọc file "sinh_vien.txt" và in thông tin của sinh viên ra màn hình.
- Tạo một file nhị phân có tên "sinh_vien.dat" và ghi thông tin của một sinh viên vào file đó.
- Đọc file "sinh_vien.dat" và in thông tin của sinh viên ra màn hình.

Hy vọng những thông tin trên sẽ giúp bạn hiểu rõ hơn về cách làm việc với file trong C++. Chúc bạn thành công với các bài tập và dự án của mình!