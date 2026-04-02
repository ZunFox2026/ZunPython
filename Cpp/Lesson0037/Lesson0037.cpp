#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    // Tạo một tệp tin mới và viết dữ liệu vào đó
    ofstream tepTinGhi("test.txt");
    if (tepTinGhi.is_open()) {
        // Viết dữ liệu vào tệp tin
        tepTinGhi << "Xin chào, thế giới!" << endl;
        tepTinGhi << "Đây là một tệp tin mẫu." << endl;
        tepTinGhi.close();
        cout << "Đã ghi dữ liệu vào tệp tin test.txt" << endl;
    } else {
        cout << "Không thể mở tệp tin để ghi" << endl;
    }

    // Đọc dữ liệu từ tệp tin
    ifstream tepTinDoc("test.txt");
    if (tepTinDoc.is_open()) {
        string dong;
        while (getline(tepTinDoc, dong)) {
            // In dữ liệu đọc được
            cout << dong << endl;
        }
        tepTinDoc.close();
        cout << "Đã đọc xong tệp tin test.txt" << endl;
    } else {
        cout << "Không thể mở tệp tin để đọc" << endl;
    }

    return 0;
}