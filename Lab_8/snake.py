import pygame
from random import randrange

# --- Constants ---
WINDOW_SIZE = 800
CELL_SIZE = 40
GRID_SIZE = WINDOW_SIZE // CELL_SIZE
FPS_INITIAL = 8
FOOD_LIFETIME = 7000  # milliseconds

# --- Colors ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# --- Initialize Pygame ---
pygame.init()
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Snake Game with Levels")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 24)

# --- Load Images ---
snake_img = pygame.Surface((CELL_SIZE, CELL_SIZE))
snake_img.fill(GREEN)

apple_img = pygame.Surface((CELL_SIZE, CELL_SIZE))
apple_img.fill(RED)

banana_img = pygame.Surface((CELL_SIZE, CELL_SIZE))
banana_img.fill(YELLOW)

# --- Generate Random Food Position ---
def generate_food(snake, walls):
    while True:
        pos = randrange(0, GRID_SIZE) * CELL_SIZE, randrange(0, GRID_SIZE) * CELL_SIZE
        if pos not in snake and pos not in walls:
            return pos

# --- Main Game Loop ---
def main():
    # Snake starting position
    x, y = CELL_SIZE * 5, CELL_SIZE * 5
    snake = [(x, y)]
    dx, dy = 1, 0
    length = 1
    
    # Score, Level and Speed
    score = 0
    level = 1
    fps = FPS_INITIAL

    # Create wall borders
    walls = []
    for i in range(0, WINDOW_SIZE, CELL_SIZE):
        walls.append((i, 0))
        walls.append((i, WINDOW_SIZE - CELL_SIZE))
        walls.append((0, i))
        walls.append((WINDOW_SIZE - CELL_SIZE, i))

    # Food items
    apple = generate_food(snake, walls)
    banana = generate_food(snake, walls)
    apple_timer = pygame.time.get_ticks()
    banana_timer = pygame.time.get_ticks()

    running = True
    while running:
        clock.tick(fps)
        window.fill(BLACK)

        # Draw walls
        for wall in walls:
            pygame.draw.rect(window, WHITE, (*wall, CELL_SIZE, CELL_SIZE))

        # Draw snake
        for segment in snake:
            window.blit(snake_img, segment)

        # Draw food
        window.blit(apple_img, apple)
        window.blit(banana_img, banana)

        # Display score and level
        score_text = font.render(f"Score: {score}", True, WHITE)
        level_text = font.render(f"Level: {level}", True, WHITE)
        window.blit(score_text, (40, 60))
        window.blit(level_text, (40, 80))

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and dy == 0:
            dx, dy = 0, -1
        if keys[pygame.K_DOWN] and dy == 0:
            dx, dy = 0, 1
        if keys[pygame.K_LEFT] and dx == 0:
            dx, dy = -1, 0
        if keys[pygame.K_RIGHT] and dx == 0:
            dx, dy = 1, 0

        # Move snake
        x += dx * CELL_SIZE
        y += dy * CELL_SIZE
        new_head = (x, y)
        snake.append(new_head)
        snake = snake[-length:]

        # Check for collisions (wall or self)
        if new_head in walls or new_head in snake[:-1]:
            game_over = font.render("GAME OVER", True, RED)
            window.blit(game_over, (WINDOW_SIZE // 2 - 100, WINDOW_SIZE // 2))
            pygame.display.flip()
            pygame.time.delay(2000)
            break

        # Check apple collision
        if new_head == apple:
            apple = generate_food(snake, walls)
            apple_timer = pygame.time.get_ticks()
            length += 1
            score += 1

        # Check banana collision
        if new_head == banana:
            banana = generate_food(snake, walls)
            banana_timer = pygame.time.get_ticks()
            length += 2
            score += 2

        # Level Up every 4 points
        if score >= level * 4:
            level += 1
            fps += 2

        # Remove food if time expired
        current_time = pygame.time.get_ticks()
        if current_time - apple_timer > FOOD_LIFETIME:
            apple = generate_food(snake, walls)
            apple_timer = current_time
        if current_time - banana_timer > FOOD_LIFETIME:
            banana = generate_food(snake, walls)
            banana_timer = current_time

        pygame.display.flip()

# --- Run Game ---
main()
pygame.quit()

