# Làm quen với C++ (Bài 1, Cấp Cơ bản)
## Giới thiệu
Chào mừng bạn đến với thế giới lập trình C++! C++ là một ngôn ngữ lập trình mạnh mẽ và linh hoạt, được sử dụng rộng rãi trong nhiều lĩnh vực khác nhau, từ phát triển ứng dụng đến hệ điều hành. Trong bài học này, chúng ta sẽ khám phá những khái niệm cơ bản của C++ và cách bắt đầu lập trình với ngôn ngữ này.

C++ được tạo ra bởi Bjarne Stroustrup vào những năm 1980, như một sự mở rộng của ngôn ngữ C. C++ cung cấp nhiều tính năng mới như lập trình hướng đối tượng, xử lý ngoại lệ, và nhiều thư viện chuẩn để giúp việc lập trình trở nên dễ dàng và hiệu quả hơn.

## Lý thuyết
Để bắt đầu lập trình C++, bạn cần hiểu một số khái niệm cơ bản như biến, kiểu dữ liệu, toán tử, và cấu trúc điều khiển. Biến là nơi lưu trữ dữ liệu trong chương trình, và mỗi biến có một kiểu dữ liệu cụ thể như số nguyên, số thực, hoặc chuỗi.

C++ hỗ trợ nhiều kiểu dữ liệu khác nhau, bao gồm:
- Số nguyên (int): lưu trữ số nguyên như 1, 2, 3, v.v.
- Số thực (float, double): lưu trữ số thực như 3.14, -0.5, v.v.
- Chuỗi (string): lưu trữ chuỗi ký tự như "Hello", "World", v.v.

Ví dụ về khai báo biến trong C++:
```cpp
int x = 5;  // khai báo biến x với giá trị 5
float y = 3.14;  // khai báo biến y với giá trị 3.14
string name = "Zunny";  // khai báo biến name với giá trị "Zunny"
```

## Ví dụ
Dưới đây là một ví dụ đơn giản về chương trình C++:
```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 5;
    cout << "Giá trị của x là: " << x << endl;
    return 0;
}
```
Chương trình này sẽ in ra màn hình giá trị của biến `x`. Bạn có thể chạy chương trình này bằng cách lưu nó vào một file có đuôi `.cpp`, rồi biên dịch và chạy bằng trình biên dịch C++.

## Bài tập
Để giúp bạn nắm vững kiến thức, hãy thực hiện các bài tập sau:
- Viết chương trình C++ để in ra màn hình "Xin chào, thế giới!".
- Tạo một biến `age` và gán cho nó giá trị 20, sau đó in ra màn hình giá trị của biến này.
- Viết chương trình C++ để tính tổng của hai số nguyên `a` và `b`, với `a = 5` và `b = 10`.

Hy vọng qua những thông tin này, bạn đã có một cái nhìn tổng quan về C++ và cách bắt đầu lập trình với ngôn ngữ này. Hãy tiếp tục học tập và thực hành để trở thành một lập trình viên C++ giỏi!