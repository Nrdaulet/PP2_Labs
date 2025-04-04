import pygame
import math

# Настройки
pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Shape Drawer")
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 18)

# Цвета
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

current_color = BLACK
current_tool = 'square'
drawing = False
start_pos = None

# Кнопки (текст, прямоугольник, цвет заливки, действие)
buttons = [
    {"text": "Square", "rect": pygame.Rect(10, 10, 80, 30), "action": "square"},
    {"text": "Right Triangle", "rect": pygame.Rect(100, 10, 130, 30), "action": "right_triangle"},
    {"text": "Equilateral", "rect": pygame.Rect(240, 10, 120, 30), "action": "equilateral_triangle"},
    {"text": "Rhombus", "rect": pygame.Rect(370, 10, 100, 30), "action": "rhombus"},
    {"text": "Clear", "rect": pygame.Rect(480, 10, 80, 30), "action": "clear"},
    {"text": "Black", "rect": pygame.Rect(570, 10, 70, 30), "color": BLACK},
    {"text": "Red", "rect": pygame.Rect(650, 10, 60, 30), "color": RED},
    {"text": "Green", "rect": pygame.Rect(720, 10, 70, 30), "color": GREEN},
    {"text": "Blue", "rect": pygame.Rect(800, 10, 70, 30), "color": BLUE},
]

# Функции рисования фигур
def draw_square(start, end):
    side = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
    rect = pygame.Rect(start[0], start[1], side, side)
    pygame.draw.rect(screen, current_color, rect, 2)

def draw_right_triangle(start, end):
    pygame.draw.polygon(screen, current_color, [start, (start[0], end[1]), end], 2)

def draw_equilateral_triangle(start, end):
    side = abs(end[0] - start[0])
    height = side * math.sqrt(3) / 2
    top = (start[0] + side / 2, start[1])
    left = (start[0], start[1] + height)
    right = (start[0] + side, start[1] + height)
    pygame.draw.polygon(screen, current_color, [top, left, right], 2)

def draw_rhombus(start, end):
    center_x = (start[0] + end[0]) // 2
    center_y = (start[1] + end[1]) // 2
    dx = abs(end[0] - start[0]) // 2
    dy = abs(end[1] - start[1]) // 2
    points = [
        (center_x, center_y - dy),
        (center_x + dx, center_y),
        (center_x, center_y + dy),
        (center_x - dx, center_y)
    ]
    pygame.draw.polygon(screen, current_color, points, 2)

# Главный цикл
screen.fill(WHITE)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            # Проверка нажатия на кнопку
            for btn in buttons:
                if btn["rect"].collidepoint(mx, my):
                    if "action" in btn:
                        if btn["action"] == "clear":
                            screen.fill(WHITE)
                        else:
                            current_tool = btn["action"]
                    elif "color" in btn:
                        current_color = btn["color"]
                    break
            else:
                drawing = True
                start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP and drawing:
            end_pos = event.pos
            drawing = False
            if current_tool == 'square':
                draw_square(start_pos, end_pos)
            elif current_tool == 'right_triangle':
                draw_right_triangle(start_pos, end_pos)
            elif current_tool == 'equilateral_triangle':
                draw_equilateral_triangle(start_pos, end_pos)
            elif current_tool == 'rhombus':
                draw_rhombus(start_pos, end_pos)

    # Панель кнопок
    pygame.draw.rect(screen, GRAY, (0, 0, 900, 50))
    for btn in buttons:
        pygame.draw.rect(screen, btn.get("color", GRAY), btn["rect"])
        text_surf = font.render(btn["text"], True, WHITE if "color" in btn else BLACK)
        screen.blit(text_surf, (btn["rect"].x + 5, btn["rect"].y + 5))

    pygame.display.flip()
    clock.tick(60)
