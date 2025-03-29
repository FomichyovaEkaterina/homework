import pygame
import random


pygame.init()
WIDTH, HEIGHT = 500, 500
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]  # Начальная позиция змейки
        self.direction = (CELL_SIZE, 0)  # Двигается вправо
        self.grow = False  # Флаг для роста змейки

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            return
        if new_head in self.body:
            return

        self.body.insert(0, new_head)  # Добавляем новую голову
        if not self.grow:
            self.body.pop()  # Если не растём, убираем хвост
        else:
            self.grow = False

    def change_direction(self, new_direction):
        if (new_direction[0] == -self.direction[0] and new_direction[1] == -self.direction[1]):
            return
        self.direction = new_direction

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

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

snake = Snake()
food = Food(snake)

score = 0
level = 1
speed = 5

running = True
clock = pygame.time.Clock()

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

    # Двигаем змейку
    snake.move()

    # Проверка на съедение еды
    if snake.body[0] == food.position:
        snake.grow = True
        food = Food(snake)
        score += 1
        if score % 3 == 0:
            level += 1
            speed += 1
    snake.draw()
    food.draw()

    # Отображение счета и уровня
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.update()  # Обновляем экран
    clock.tick(speed)  # Контролируем скорость

pygame.quit()
