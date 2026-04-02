#include <iostream>
using namespace std;

// Hàm đổi chỗ hai số nguyên
void swap(int &a, int &b) {
    // Tạo biến tạm để lưu giá trị của a
    int temp = a;
    // Gán giá trị của b cho a
    a = b;
    // Gán giá trị của temp (ban đầu là a) cho b
    b = temp;
}

// Hàm sắp xếp mảng số nguyên tăng dần
void sortArray(int arr[], int n) {
    // Duyệt qua mảng từ đầu đến cuối
    for (int i = 0; i < n - 1; i++) {
        // Duyệt qua mảng từ vị trí i + 1 đến cuối
        for (int j = i + 1; j < n; j++) {
            // Nếu phần tử tại vị trí i lớn hơn phần tử tại vị trí j
            if (arr[i] > arr[j]) {
                // Đổi chỗ hai phần tử
                swap(arr[i], arr[j]);
            }
        }
    }
}

// Hàm in mảng số nguyên
void printArray(int arr[], int n) {
    // Duyệt qua mảng và in từng phần tử
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    // Xuống dòng
    cout << endl;
}

int main() {
    // Khai báo mảng số nguyên
    int arr[] = {5, 2, 8, 1, 9};
    // Khai báo số lượng phần tử trong mảng
    int n = sizeof(arr) / sizeof(arr[0]);
    
    // In mảng trước khi sắp xếp
    cout << "Mảng trước khi sắp xếp: ";
    printArray(arr, n);
    
    // Sắp xếp mảng
    sortArray(arr, n);
    
    // In mảng sau khi sắp xếp
    cout << "Mảng sau khi sắp xếp: ";
    printArray(arr, n);
    
    return 0;
}