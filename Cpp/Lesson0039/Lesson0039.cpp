#include <iostream>
#include <thread>
#include <chrono>

// Hàm này sẽ được chạy trong một luồng riêng
void hamLuong1() {
    // In ra thông điệp từ luồng 1
    std::cout << "Luồng 1: Bắt đầu" << std::endl;
    
    // Dừng lại trong 2 giây
    std::this_thread::sleep_for(std::chrono::seconds(2));
    
    // In ra thông điệp từ luồng 1 sau khi dừng lại
    std::cout << "Luồng 1: Kết thúc" << std::endl;
}

// Hàm này sẽ được chạy trong một luồng riêng
void hamLuong2() {
    // In ra thông điệp từ luồng 2
    std::cout << "Luồng 2: Bắt đầu" << std::endl;
    
    // Dừng lại trong 1 giây
    std::this_thread::sleep_for(std::chrono::seconds(1));
    
    // In ra thông điệp từ luồng 2 sau khi dừng lại
    std::cout << "Luồng 2: Kết thúc" << std::endl;
}

int main() {
    // Tạo 2 luồng
    std::thread luong1(hamLuong1);
    std::thread luong2(hamLuong2);
    
    // Chờ cho đến khi cả 2 luồng kết thúc
    luong1.join();
    luong2.join();
    
    // In ra thông điệp từ hàm main
    std::cout << "Hàm main: Kết thúc" << std::endl;
    
    return 0;
}