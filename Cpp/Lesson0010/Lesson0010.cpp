#include <iostream>
#include <fstream>
#include <string>

// Hàm main, điểm bắt đầu của chương trình
int main() {
    // Tạo một tệp tin mới tên là "test.txt" và mở nó ở chế độ ghi
    std::ofstream tep_tin("test.txt");

    // Kiểm tra nếu tệp tin được mở thành công
    if (tep_tin.is_open()) {
        // Ghi nội dung vào tệp tin
        tep_tin << "Xin chào, đây là nội dung của tệp tin test.txt" << std::endl;

        // Đóng tệp tin
        tep_tin.close();
        std::cout << "Tệp tin được tạo và ghi thành công!" << std::endl;
    } else {
        std::cout << "Không thể mở tệp tin!" << std::endl;
    }

    // Mở lại tệp tin ở chế độ đọc
    std::ifstream doc_tep_tin("test.txt");

    // Kiểm tra nếu tệp tin được mở thành công
    if (doc_tep_tin.is_open()) {
        // Đọc nội dung từ tệp tin và hiển thị
        std::string dong;
        while (std::getline(doc_tep_tin, dong)) {
            std::cout << dong << std::endl;
        }

        // Đóng tệp tin
        doc_tep_tin.close();
    } else {
        std::cout << "Không thể mở tệp tin!" << std::endl;
    }

    return 0;
}