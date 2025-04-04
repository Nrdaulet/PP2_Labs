import pygame
import datetime

pygame.init()

# Создаем окно
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Clock app')

# Загружаем изображения
clock_img = pygame.image.load('Lab_7/Clock app/images/clock.png')
min_hand = pygame.image.load('Lab_7/Clock app/images/min_hand.png')
sec_hand = pygame.image.load('Lab_7/Clock app/images/sec_hand.png')

# Координаты центра
center_x, center_y = 400, 300  # 800x600 делим пополам

running = True
while running:
    screen.blit(clock_img, (0, 0))  # Отображаем фон часов

    # Получаем текущее время
    now = datetime.datetime.now()
    minutes = now.minute 
    seconds = now.second

    # Вычисляем углы поворота (в °, по часовой стрелке)
    min_angle = -(minutes * 6)  # 6° за минуту
    sec_angle = -(seconds * 6)  # 6° за секунду

    # Поворачиваем стрелки
    min_rotated = pygame.transform.rotate(min_hand, min_angle)
    sec_rotated = pygame.transform.rotate(sec_hand, sec_angle)

    # Ставим центр вращения в основание стрелки (корректируем позицию)
    min_rect = min_rotated.get_rect(center=(center_x, center_y))
    sec_rect = sec_rotated.get_rect(center=(center_x, center_y))

    # Отображаем стрелки
    screen.blit(min_rotated, min_rect)
    screen.blit(sec_rotated, sec_rect)

    pygame.display.update()

    # Обрабатываем выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(100)  # Делаем небольшую задержку

pygame.quit()
