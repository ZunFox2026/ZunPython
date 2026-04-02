#include <iostream>
#include <fstream>
#include <string>

// Hàm main bắt đầu chương trình
int main() {
    // Tạo tệp tin mới
    std::ofstream file("demo.txt");
    if (file.is_open()) {
        // Ghi nội dung vào tệp
        file << "Xin chào, thế giới!\n";
        file << "Đây là nội dung trong tệp.\n";
        file.close();
        std::cout << "Tệp đã được tạo thành công.\n";
    } else {
        std::cout << "Không thể tạo tệp.\n";
    }

    // Đọc nội dung từ tệp
    std::ifstream readFile("demo.txt");
    if (readFile.is_open()) {
        std::string line;
        while (std::getline(readFile, line)) {
            // In nội dung từng dòng
            std::cout << line << std::endl;
        }
        readFile.close();
    } else {
        std::cout << "Không thể mở tệp.\n";
    }

    return 0;
}