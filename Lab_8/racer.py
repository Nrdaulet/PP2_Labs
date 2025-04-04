import pygame, sys, random, time

pygame.init()

FPS = 60
clock = pygame.time.Clock()

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)

# Размеры экрана
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Car Game")

# Шрифт
font_big = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

# Скорость
speed = 5
score = 0
coins_collected = 0

# Фон
background = pygame.image.load("Lab_8/things/AnimatedStreet.png")
bg_y = 0  # координата для фона

# Игрок
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Lab_8/things/Player.png")
        self.rect = self.image.get_rect(center=(160, 520))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(5, 0)
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.move_ip(0, -5)
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.move_ip(0, 5)

# Враг
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Lab_8/things/Enemy.png")
        self.rect = self.image.get_rect(center=(random.randint(40, WIDTH - 40), 0))

    def update(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.top > HEIGHT:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)

# Монета
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Lab_8/things/coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.respawn()

    def respawn(self):
        self.rect.center = (random.randint(40, WIDTH - 40), random.randint(40, HEIGHT - 100))

# Объекты
player = Player()
enemy = Enemy()
coin = Coin()

# Группы
enemies = pygame.sprite.Group(enemy)
coins = pygame.sprite.Group(coin)
all_sprites = pygame.sprite.Group(player, enemy, coin)

# Игра
running = True
while running:
    # Движение фона
    bg_y += 5
    if bg_y >= HEIGHT:
        bg_y = 0
    screen.blit(background, (0, bg_y - HEIGHT))
    screen.blit(background, (0, bg_y))

    # Счёт
    score_text = font_small.render(f"Score: {score}", True, BLACK)
    coins_text = font_small.render(f"Coins: {coins_collected}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(coins_text, (WIDTH - 100, 10))

    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()

    # Отображение
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # Столкновение с монетой
    if pygame.sprite.spritecollideany(player, coins):
        coins_collected += 1
        coin.respawn()
        if coins_collected % 5 == 0:
            speed += 1

    # Столкновение с врагом
    if pygame.sprite.spritecollideany(player, enemies):
        crash_sound = pygame.mixer.Sound("Lab_8/things/crash.wav")
        crash_sound.play()
        time.sleep(1)
        screen.fill(RED)
        game_over_text = font_big.render("Game Over", True, BLACK)
        screen.blit(game_over_text, (30, 250))
        pygame.display.update()
        time.sleep(2)
        running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
