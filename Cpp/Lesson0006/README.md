# Làm quen với File
## Giới thiệu
Trong chương trình C++, việc làm việc với file là một phần quan trọng. File cho phép chúng ta lưu trữ và đọc dữ liệu từ bên ngoài chương trình, giúp tăng tính linh hoạt và khả năng tái sử dụng của chương trình. Trong bài này, chúng ta sẽ tìm hiểu về cách làm việc với file trong C++.

## Lý thuyết
Để làm việc với file trong C++, chúng ta cần sử dụng thư viện `fstream`. Thư viện này cung cấp các lớp `ifstream`, `ofstream` và `fstream` để đọc, viết và đọc/ghi file tương ứng. 

- Lớp `ifstream` được sử dụng để đọc file.
- Lớp `ofstream` được sử dụng để viết file.
- Lớp `fstream` được sử dụng để đọc và viết file.

Chúng ta cũng cần biết về các chế độ mở file:
- `ios::in`: Mở file để đọc.
- `ios::out`: Mở file để viết.
- `ios::app`: Mở file để thêm vào cuối file.
- `ios::trunc`: Mở file và xóa nội dung nếu file đã tồn tại.
- `ios::ate`: Di chuyển con trỏ đến cuối file.
- `ios::binary`: Mở file ở chế độ nhị phân.

Ví dụ về mở file để đọc:
```cpp
ifstream file("example.txt", ios::in);
```

Ví dụ về mở file để viết:
```cpp
ofstream file("example.txt", ios::out);
```

## Ví dụ
Chúng ta có thể đọc và viết file bằng cách sử dụng các hàm như `getline`, `get`, `put`, `write`, `read`. Dưới đây là một ví dụ về việc đọc và viết file:
```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    // Mở file để viết
    ofstream outFile("example.txt", ios::out);
    if (outFile.is_open()) {
        // Viết vào file
        outFile << "Xin chào, thế giới!";
        outFile.close();
    }

    // Mở file để đọc
    ifstream inFile("example.txt", ios::in);
    if (inFile.is_open()) {
        std::string line;
        // Đọc từ file
        while (getline(inFile, line)) {
            std::cout << line << std::endl;
        }
        inFile.close();
    }

    return 0;
}
```

## Bài tập
Bài tập này yêu cầu bạn thực hiện các bước sau:
- Tạo một file văn bản có tên là `test.txt` và thêm một số dòng văn bản vào file đó.
- Viết một chương trình C++ để đọc file `test.txt` và hiển thị nội dung của file lên màn hình.
- Thêm một số dòng văn bản mới vào file `test.txt` bằng cách sử dụng chương trình C++.
- Đọc lại file `test.txt` và hiển thị nội dung mới lên màn hình.

Hãy thử thực hiện các bước trên và xem kết quả!