import pygame

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

# Параметры мяча
ball_radius = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
step = 20  # Шаг движения

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

running = True
while running:
    pygame.time.delay(50)  # Небольшая задержка для плавности движения

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получение нажатых клавиш
    keys = pygame.key.get_pressed()

    # Обработка движения с ограничением границ экрана
    if keys[pygame.K_LEFT] and ball_x - ball_radius - step >= 0:
        ball_x -= step
    if keys[pygame.K_RIGHT] and ball_x + ball_radius + step <= WIDTH:
        ball_x += step
    if keys[pygame.K_UP] and ball_y - ball_radius - step >= 0:
        ball_y -= step
    if keys[pygame.K_DOWN] and ball_y + ball_radius + step <= HEIGHT:
        ball_y += step

    # Обновление экрана
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.display.update()

pygame.quit()
