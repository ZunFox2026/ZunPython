# Import thư viện Pygame
import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước màn hình
man_hinh = pygame.display.set_mode((800, 600))

# Thiết lập tiêu đề màn hình
pygame.display.set_caption("Làm quen với thư viện Pygame")

# Thiết lập màu sắc
mau_den = (0, 0, 0)
mau_trang = (255, 255, 255)

# Vòng lặp chính
while True:
    for su_kien in pygame.event.get():
        if su_kien.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Vẽ nền màu đen
    man_hinh.fill(mau_den)

    # Vẽ chữ "Xin chào" màu trắng
    font = pygame.font.Font(None, 36)
    chu = font.render("Xin chào", True, mau_trang)
    man_hinh.blit(chu, (350, 250))

    # Cập nhật màn hình
    pygame.display.flip()

    # Giới hạn tốc độ khung hình
    pygame.time.Clock().tick(60)