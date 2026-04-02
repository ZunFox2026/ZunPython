#include <iostream>
#include <thread>
#include <chrono>

// Hàm này sẽ được chạy trong một luồng riêng
void chaoLuong(int soLuong) {
    // In ra thông điệp chào từ luồng này
    std::cout << "Chào từ luồng " << soLuong << std::endl;
    // Dừng luồng trong 1 giây
    std::this_thread::sleep_for(std::chrono::seconds(1));
    // In ra thông điệp tạm biệt từ luồng này
    std::cout << "Tạm biệt từ luồng " << soLuong << std::endl;
}

int main() {
    // Tạo 5 luồng riêng
    std::thread luong1(chaoLuong, 1);
    std::thread luong2(chaoLuong, 2);
    std::thread luong3(chaoLuong, 3);
    std::thread luong4(chaoLuong, 4);
    std::thread luong5(chaoLuong, 5);

    // Đợi các luồng kết thúc
    luong1.join();
    luong2.join();
    luong3.join();
    luong4.join();
    luong5.join();

    // In ra thông điệp từ chương trình chính
    std::cout << "Kết thúc chương trình chính" << std::endl;

    return 0;
}