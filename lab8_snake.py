import pygame, sys
import random

# Инициализация
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 500, 500
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)


class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (CELL_SIZE, 0)
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        # Проверка на столкновение со стеной или собой
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            self.game_over()
        if new_head in self.body:
            self.game_over()

        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_direction(self, new_direction):
        if (new_direction[0] == -self.direction[0] and new_direction[1] == -self.direction[1]):
            return
        self.direction = new_direction

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

    def game_over(self):
        pygame.quit()
        sys.exit()


class Food:
    def __init__(self, snake):
        self.position = self.generate_food_position(snake)

    def generate_food_position(self, snake):
        while True:
            x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in snake.body:
                return (x, y)

    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, CELL_SIZE, CELL_SIZE))

    def respawn(self, snake):
        self.position = self.generate_food_position(snake)


# Создание объектов
snake = Snake()
food = Food(snake)

score = 0
level = 1
speed = 5

clock = pygame.time.Clock()
running = True

# Игровой цикл
while running:
    screen.fill(WHITE)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -CELL_SIZE))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, CELL_SIZE))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-CELL_SIZE, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((CELL_SIZE, 0))

    snake.move()

    # Проверка коллизии головы змеи с едой
    snake_head_rect = pygame.Rect(*snake.body[0], CELL_SIZE, CELL_SIZE)
    food_rect = pygame.Rect(*food.position, CELL_SIZE, CELL_SIZE)

    if snake_head_rect.colliderect(food_rect):
        snake.grow = True
        food.respawn(snake)
        score += 1
        if score % 3 == 0:
            level += 1
            speed += 1

    snake.draw()
    food.draw()

    # Отображение счёта и уровня
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()
