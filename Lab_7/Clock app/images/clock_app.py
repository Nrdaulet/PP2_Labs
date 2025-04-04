import pygame
import os

pygame.init()
screen = pygame.display.set_mode((600,300)) #flags=pygame.NOFRAME
pygame.display.set_caption("Clock_app")

icon = pygame.image.load('/Users/TUF Gaming/OneDrive/Рабочий стол/PP2/Lab_7/Clock app/images/icon.png')
pygame.display.set_icon(icon)
pygame.display.update()

square = pygame.Surface((100,150))
square.fill('Blue')

my_font = pygame.font.Font('PP2/Boldonse-Regular.ttf', 40)
text_surface = my_font.render('Clock_app', False, 'Red')


running = True
while running:
    pygame.draw.circle(screen,"pink", (10, 7), 4)
    screen.blit(square,(7, 0))
    screen.blit(text_surface,(300, 100))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
