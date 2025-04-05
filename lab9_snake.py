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
WHITE = (0, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)


class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]  # Начальное положение змеи
        self.direction = (CELL_SIZE, 0)           # Начальное направление движения
        self.grow = False                          # Флаг, указывающий, нужно ли увеличивать змею

    def move(self):
        head_x, head_y = self.body[0]             # Получаем координаты головы змеи
        dx, dy = self.direction                     # Получаем направление движения
        new_head = (head_x + dx, head_y + dy)     # Вычисляем новую голову

        # Проверка на столкновение со стеной или собой
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            self.game_over()                       # Игра окончена, если змея вышла за границы
        if new_head in self.body:
            self.game_over()                       # Игра окончена, если змея столкнулась сама с собой

        self.body.insert(0, new_head)             # Добавляем новую голову
        if not self.grow:
            self.body.pop()                        # Удаляем последний сегмент, если не растем
        else:
            self.grow = False                      # Сбрасываем флаг роста

    def change_direction(self, new_direction):
        # Избегаем поворота в противоположную сторону
        if (new_direction[0] == -self.direction[0] and new_direction[1] == -self.direction[1]):
            return
        self.direction = new_direction              # Меняем направление движения

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))  # Рисуем змею

    def game_over(self):
        pygame.quit()                              # Завершаем игру
        sys.exit()


class Food:
    def __init__(self, snake):
        self.position = self.generate_food_position(snake)  # Генерируем позицию еды
        self.weight = random.choice([1, 2, 3])               # Вес еды (1, 2 или 3)
        self.timer = random.randint(8, 15)                    # Таймер появления еды (от 8 до 15 секунд)
        self.spawn_time = pygame.time.get_ticks()            # Время появления еды
        self.font = pygame.font.Font(None, 24)               # Шрифт для отображения веса

    def generate_food_position(self, snake):
        # Генерация случайной позиции еды, которая не перекрывает тело змеи
        while True:
            x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in snake.body:
                return (x, y)

    def draw(self):
        # Рисуем еду
        pygame.draw.rect(screen, RED, (*self.position, CELL_SIZE, CELL_SIZE))
        # Отображаем вес еды на еде
        weight_text = self.font.render(str(self.weight), True, BLACK)
        text_rect = weight_text.get_rect(center=(self.position[0] + CELL_SIZE // 2, self.position[1] + CELL_SIZE // 2))
        screen.blit(weight_text, text_rect)  # Рисуем текст с весом

    def respawn(self, snake):
        self.position = self.generate_food_position(snake)  # Генерируем новую позицию еды
        self.weight = random.choice([1, 2, 3])               # Генерируем новый вес еды
        self.spawn_time = pygame.time.get_ticks()            # Обновляем время появления

    def update(self):
        # Проверка времени существования еды и её исчезновение
        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_time >= self.timer * 1000:
            self.respawn(snake)                               # Если время вышло, респаун еды


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
        snake.grow = True                         # Увеличиваем змею при поедании еды
        score += food.weight                      # Добавляем к счёту вес еды
        food.respawn(snake)                       # Респаун еды

        # Увеличиваем уровень и скорость каждые 3 очка
        if score % 3 == 0:
            level += 1
            speed += 1

    food.update()                                  # Обновляем состояние еды
    snake.draw()                                   # Рисуем змею
    food.draw()                                    # Рисуем еду

    # Отображение счёта и уровня
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()
