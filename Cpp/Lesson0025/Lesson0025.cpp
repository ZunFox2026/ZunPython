#include <iostream>
#include <fstream>
#include <string>

// Hàm main để bắt đầu chương trình
int main() {
    // Tạo một file mới tên là "example.txt"
    std::ofstream outFile("example.txt");
    
    // Kiểm tra xem file đã được mở thành công
    if (outFile.is_open()) {
        // Ghi dữ liệu vào file
        outFile << "Xin chào, đây là nội dung của file example.txt" << std::endl;
        
        // Đóng file
        outFile.close();
        
        std::cout << "Đã tạo file example.txt thành công!" << std::endl;
    } else {
        // Thông báo nếu không thể mở file
        std::cout << "Không thể tạo file!" << std::endl;
    }
    
    // Đọc nội dung từ file example.txt
    std::ifstream inFile("example.txt");
    
    // Kiểm tra xem file đã được mở thành công
    if (inFile.is_open()) {
        std::string line;
        
        // Đọc từng dòng từ file
        while (std::getline(inFile, line)) {
            // In nội dung của dòng
            std::cout << line << std::endl;
        }
        
        // Đóng file
        inFile.close();
    } else {
        // Thông báo nếu không thể mở file
        std::cout << "Không thể đọc file!" << std::endl;
    }
    
    return 0;
}