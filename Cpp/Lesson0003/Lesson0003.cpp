#include <iostream>
#include <fstream>
#include <string>

// Hàm main, điểm vào của chương trình
int main() {
    // Tạo một tệp tin mới có tên "example.txt"
    std::ofstream fileOut("example.txt");

    // Kiểm tra nếu tệp được mở thành công
    if (fileOut.is_open()) {
        // Ghi nội dung vào tệp
        fileOut << "Xin chào, thế giới!" << std::endl;
        fileOut << "Đây là một ví dụ về làm việc với tệp tin trong C++." << std::endl;

        // Đóng tệp
        fileOut.close();
        std::cout << "Đã ghi nội dung vào tệp example.txt" << std::endl;
    } else {
        std::cout << "Không thể mở tệp example.txt" << std::endl;
    }

    // Đọc nội dung từ tệp
    std::ifstream fileIn("example.txt");

    // Kiểm tra nếu tệp được mở thành công
    if (fileIn.is_open()) {
        std::string line;
        while (std::getline(fileIn, line)) {
            // In nội dung mỗi dòng
            std::cout << line << std::endl;
        }

        // Đóng tệp
        fileIn.close();
    } else {
        std::cout << "Không thể mở tệp example.txt" << std::endl;
    }

    return 0;
}