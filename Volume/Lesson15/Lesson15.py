import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Thiết lập chiều rộng và chiều cao của màn hình
chieu_rong, chieu_cao = 800, 600
man_hinh = pygame.display.set_mode((chieu_rong, chieu_cao))

# Thiết lập tiêu đề của màn hình
pygame.display.set_caption('Làm việc với thư viện Pygame')

# Thiết lập màu sắc
mau_den = (0, 0, 0)
mau_trang = (255, 255, 255)

# Thiết lập kích thước và màu sắc của chữ
font = pygame.font.SysFont('Arial', 30)
chu = font.render('Xin chào, Pygame!', True, mau_den)

# Vòng lặp chính của chương trình
while True:
    for su_kien in pygame.event.get():
        if su_kien.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Vẽ nền màu trắng
    man_hinh.fill(mau_trang)

    # Vẽ chữ lên màn hình
    man_hinh.blit(chu, (chieu_rong // 2 - chu.get_width() // 2, chieu_cao // 2 - chu.get_height() // 2))

    # Cập nhật màn hình
    pygame.display.flip()

    # Điều chỉnh tốc độ khung hình
    pygame.time.Clock().tick(60)