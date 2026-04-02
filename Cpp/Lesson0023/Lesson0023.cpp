#include <iostream>
#include <fstream> // Thư viện để xử lý tệp

using namespace std;

int main() {
    // Tạo đối tượng tệp tin
    ofstream tepTinGhi("example.txt"); // Tạo tệp tin example.txt để ghi

    // Kiểm tra nếu tệp tin được mở thành công
    if (tepTinGhi.is_open()) {
        // Ghi nội dung vào tệp tin
        tepTinGhi << "Xin chào, thế giới!\n";
        tepTinGhi << "Đây là nội dung được ghi vào tệp tin.\n";

        // Đóng tệp tin
        tepTinGhi.close();
        cout << "Ghi tệp tin thành công.\n";
    } else {
        cout << "Không thể mở tệp tin để ghi.\n";
    }

    // Tạo đối tượng tệp tin để đọc
    ifstream tepTinDoc("example.txt"); // Mở tệp tin example.txt để đọc

    // Kiểm tra nếu tệp tin được mở thành công
    if (tepTinDoc.is_open()) {
        char line[100]; // Mảng kí tự để lưu trữ từng dòng

        // Đọc từng dòng trong tệp tin
        while (tepTinDoc.getline(line, 100)) {
            cout << line << endl;
        }

        // Đóng tệp tin
        tepTinDoc.close();
        cout << "Đọc tệp tin thành công.\n";
    } else {
        cout << "Không thể mở tệp tin để đọc.\n";
    }

    return 0;
}