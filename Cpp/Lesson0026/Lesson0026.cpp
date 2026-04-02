#include <iostream>
#include <thread>
#include <chrono>

// Hàm này sẽ chạy trong một luồng riêng
void chaoMung() {
    // In ra thông điệp chào mừng trong vòng 5 giây
    for (int i = 0; i < 5; i++) {
        std::cout << "Chào mừng bạn!" << std::endl;
        // Ngủ trong 1 giây
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
}

int main() {
    // Tạo một luồng mới chạy hàm chaoMung
    std::thread luongChaoMung(chaoMung);
    
    // Trong khi đó, luồng chính vẫn tiếp tục chạy
    for (int i = 0; i < 5; i++) {
        std::cout << "Xin chào từ luồng chính!" << std::endl;
        // Ngủ trong 1 giây
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    
    // Đợi luồng chaoMung kết thúc
    luongChaoMung.join();
    
    return 0;
}