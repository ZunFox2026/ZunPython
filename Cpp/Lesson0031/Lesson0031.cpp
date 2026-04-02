#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    // Tạo tệp tin mới và ghi dữ liệu vào tệp tin
    ofstream tepTinGhi("tep_tin_ghi.txt");
    if (tepTinGhi.is_open()) {
        // Ghi dữ liệu vào tệp tin
        tepTinGhi << "Xin chào, tôi là một tệp tin mới!" << endl;
        tepTinGhi.close();
        cout << "Đã tạo tệp tin mới và ghi dữ liệu thành công!" << endl;
    } else {
        cout << "Không thể tạo tệp tin mới!" << endl;
    }

    // Đọc dữ liệu từ tệp tin
    ifstream tepTinDoc("tep_tin_ghi.txt");
    if (tepTinDoc.is_open()) {
        string duLieu;
        while (getline(tepTinDoc, duLieu)) {
            // Đọc và in dữ liệu từ tệp tin
            cout << "Dữ liệu từ tệp tin: " << duLieu << endl;
        }
        tepTinDoc.close();
    } else {
        cout << "Không thể đọc tệp tin!" << endl;
    }

    return 0;
}