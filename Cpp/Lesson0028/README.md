# Tìm hiểu về đa luồng trong C++
## Giới thiệu
Đa luồng (multithreading) là một kỹ thuật cho phép một chương trình thực hiện nhiều tác vụ đồng thời. Trong C++, đa luồng được thực hiện thông qua thư viện `<thread>`. Việc sử dụng đa luồng giúp tăng hiệu suất của chương trình, đặc biệt là khi thực hiện các tác vụ độc lập.

## Lý thuyết
Khi một chương trình C++ được khởi chạy, nó sẽ tạo ra một luồng chính (main thread). Tuy nhiên, chương trình có thể tạo ra các luồng phụ (child thread) để thực hiện các tác vụ khác nhau. Mỗi luồng sẽ chạy độc lập và có thể thực hiện các tác vụ khác nhau.

Ví dụ, chúng ta có thể tạo một luồng phụ để thực hiện một tác vụ tính toán nặng, trong khi luồng chính tiếp tục thực hiện các tác vụ khác. Điều này giúp tăng hiệu suất của chương trình và giảm thời gian chờ đợi.

Dưới đây là một ví dụ đơn giản về tạo luồng phụ trong C++:
```cpp
#include <thread>
#include <iostream>

void hamLuongPhu() {
    std::cout << "Luồng phụ đang chạy..." << std::endl;
}

int main() {
    std::thread luongPhu(hamLuongPhu);
    std::cout << "Luồng chính đang chạy..." << std::endl;
    luongPhu.join();
    return 0;
}
```
Trong ví dụ này, chúng ta tạo một luồng phụ bằng cách gọi hàm `std::thread` và truyền vào hàm `hamLuongPhu` làm đối số. Sau đó, chúng ta gọi hàm `join` để chờ đợi luồng phụ hoàn thành.

## Ví dụ
Dưới đây là một ví dụ minh họa về đa luồng trong C++:
```cpp
#include <thread>
#include <iostream>

void tinhTong(int* arr, int n) {
    int tong = 0;
    for (int i = 0; i < n; i++) {
        tong += arr[i];
    }
    std::cout << "Tổng: " << tong << std::endl;
}

void tinhTich(int* arr, int n) {
    int tich = 1;
    for (int i = 0; i < n; i++) {
        tich *= arr[i];
    }
    std::cout << "Tích: " << tich << std::endl;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    std::thread luongTong(tinhTong, arr, n);
    std::thread luongTich(tinhTich, arr, n);

    luongTong.join();
    luongTich.join();

    return 0;
}
```
Trong ví dụ này, chúng ta tạo hai luồng phụ để tính tổng và tích của một mảng số nguyên. Mỗi luồng sẽ thực hiện một tác vụ khác nhau và chạy độc lập.

## Bài tập
Bài tập: Viết một chương trình C++ sử dụng đa luồng để thực hiện các tác vụ sau:
- Tính tổng của một mảng số nguyên
- Tính tích của một mảng số nguyên
- In ra các phần tử của một mảng số nguyên

Yêu cầu:
- Sử dụng đa luồng để thực hiện các tác vụ trên
- Sử dụng hàm `join` để chờ đợi các luồng phụ hoàn thành
- In ra kết quả của từng tác vụ

Lưu ý: Bài tập này yêu cầu bạn áp dụng kiến thức về đa luồng trong C++ để giải quyết. Hãy thử viết code và chạy thử để xem kết quả!