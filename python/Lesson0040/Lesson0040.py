# Khởi tạo pygame
import pygame
import sys

# Khởi tạo các mô-đun của pygame
pygame.init()

# Thiết lập chiều rộng và chiều cao của màn hình
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Thiết lập tiêu đề của cửa sổ
pygame.display.set_caption('Tìm hiểu về thư viện Pygame')

# Thiết lập màu nền
background_color = (255, 255, 255)

# Thiết lập màu và kích thước của chữ
font_color = (0, 0, 0)
font_size = 30
font = pygame.font.SysFont('Arial', font_size)

# Hàm vẽ chữ lên màn hình
def draw_text(text, x, y):
    text_surface = font.render(text, True, font_color)
    screen.blit(text_surface, (x, y))

# Vòng lặp chính của game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Vẽ màu nền
    screen.fill(background_color)

    # Vẽ chữ lên màn hình
    draw_text('Tìm hiểu về thư viện Pygame', 100, 100)
    draw_text('Bài 40: Cơ bản', 100, 150)

    # Cập nhật màn hình
    pygame.display.flip()

    # Giới hạn tốc độ khung hình
    pygame.time.Clock().tick(60)