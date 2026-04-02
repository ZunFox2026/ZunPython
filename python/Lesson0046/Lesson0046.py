# Bài 46: Lập Trình Tạo Trò Chơi

# Import thư viện cần thiết
import random

# Hàm tạo trò chơi
def tro_choi():
    # Khởi tạo điểm số
    diem = 0
    
    # Trò chơi gồm 5 câu hỏi
    for i in range(5):
        # Tạo câu hỏi và đáp án ngẫu nhiên
        so_ngau_nhien = random.randint(1, 10)
        dap_an = so_ngau_nhien * 2
        
        # Nhập câu trả lời từ người dùng
        cau_tra_loi = int(input(f"Câu {i+1}: {so_ngau_nhien} x 2 = ? "))
        
        # Kiểm tra câu trả lời
        if cau_tra_loi == dap_an:
            print("Đáp án đúng!")
            diem += 1
        else:
            print(f"Đáp án sai! Đáp án chính xác là {dap_an}.")
    
    # In điểm số cuối cùng
    print(f"Điểm số cuối cùng: {diem} / 5")

# Chạy trò chơi
tro_choi()