#include <iostream>
#include <fstream>

using namespace std;

int main() {
    // Tạo tệp tin mới
    ofstream tepTin("example.txt");

    // Kiểm tra nếu tệp tin được mở thành công
    if (tepTin.is_open()) {
        // Ghi nội dung vào tệp tin
        tepTin << "Xin chào, thế giới!" << endl;
        tepTin << "Đây là một ví dụ về việc làm việc với tệp tin trong C++." << endl;

        // Đóng tệp tin
        tepTin.close();
        cout << "Tệp tin đã được tạo và ghi nội dung thành công!" << endl;
    } else {
        cout << "Không thể mở tệp tin!" << endl;
    }

    // Đọc tệp tin
    ifstream docTepTin("example.txt");

    // Kiểm tra nếu tệp tin được mở thành công
    if (docTepTin.is_open()) {
        string dong;
        while (getline(docTepTin, dong)) {
            // In nội dung của tệp tin
            cout << dong << endl;
        }
        // Đóng tệp tin
        docTepTin.close();
    } else {
        cout << "Không thể mở tệp tin!" << endl;
    }

    return 0;
}