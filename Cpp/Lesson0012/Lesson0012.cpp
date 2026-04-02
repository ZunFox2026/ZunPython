#include <iostream>
#include <fstream>

using namespace std;

int main() {
    // Tạo file xuất
    ofstream fileXuat("xuat.txt");
    if (fileXuat.is_open()) {
        // Ghi dữ liệu vào file
        fileXuat << "Xin chào, thế giới!" << endl;
        fileXuat << "Đây là một ví dụ về việc xuất dữ liệu ra file." << endl;
        fileXuat.close();
        cout << "Đã ghi dữ liệu vào file xuất.txt" << endl;
    } else {
        cout << "Không thể mở file xuất.txt" << endl;
    }

    // Tạo file nhập
    ifstream fileNhap("xuat.txt");
    if (fileNhap.is_open()) {
        // Đọc dữ liệu từ file
        string dong;
        while (getline(fileNhap, dong)) {
            cout << dong << endl;
        }
        fileNhap.close();
        cout << "Đã đọc dữ liệu từ file xuất.txt" << endl;
    } else {
        cout << "Không thể mở file xuất.txt" << endl;
    }

    return 0;
}