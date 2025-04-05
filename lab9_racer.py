import pygame, sys
from pygame.locals import *
import random, time

# Initialize Pygame
pygame.init()

# Set up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0
SPEED_INCREASE_THRESHOLD = 5  # Увеличивать скорость каждые 5 монетных очков

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load background
background = pygame.image.load("AnimatedStreet.png")

# Setup display
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Coin class with random weight
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.weight = random.randint(1, 3)  # Вес монеты от 1 до 3
        self.respawn()

    def respawn(self):
        self.weight = random.randint(1, 3)
        offset = random.choice([-50, 0, 50])
        new_x = max(0, min(SCREEN_WIDTH - 30, P1.rect.centerx + offset))
        self.rect.center = (new_x, P1.rect.centery)

    def update(self):
        pass

# Create instances
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    coins_text = font_small.render("Coins: " + str(COIN_SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 100, 10))

    # Move and draw sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    coins.update()
    for coin in coins:
        DISPLAYSURF.blit(coin.image, coin.rect)

    # Collision with enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Collision with coin
    if pygame.sprite.spritecollideany(P1, coins):
        COIN_SCORE += C1.weight  # Добавляем вес монеты к счёту
        if COIN_SCORE % SPEED_INCREASE_THRESHOLD == 0:
            SPEED += 1  # Увеличиваем скорость при достижении порога
        C1.respawn()

    pygame.display.update()
    FramePerSec.tick(FPS)
