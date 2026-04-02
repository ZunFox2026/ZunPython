#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    // Tạo một tệp tin mới và ghi dữ liệu vào tệp
    ofstream tepTinGhi("example.txt");
    if (tepTinGhi.is_open()) {
        // Ghi dữ liệu vào tệp
        tepTinGhi << "Xin chào, thế giới!" << endl;
        tepTinGhi << "Đây là một ví dụ về tệp tin." << endl;
        tepTinGhi.close();
        cout << "Đã ghi dữ liệu vào tệp thành công!" << endl;
    } else {
        cout << "Không thể mở tệp tin để ghi!" << endl;
    }

    // Đọc dữ liệu từ tệp
    ifstream tepTinDoc("example.txt");
    if (tepTinDoc.is_open()) {
        string dong;
        while (getline(tepTinDoc, dong)) {
            // In dữ liệu đọc được từ tệp
            cout << dong << endl;
        }
        tepTinDoc.close();
        cout << "Đã đọc dữ liệu từ tệp thành công!" << endl;
    } else {
        cout << "Không thể mở tệp tin để đọc!" << endl;
    }

    return 0;
}