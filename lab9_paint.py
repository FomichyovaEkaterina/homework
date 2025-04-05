import pygame

def main():
    # Инициализация Pygame
    pygame.init()
    screen = pygame.display.set_mode((640, 480))  # Установка размеров окна
    clock = pygame.time.Clock()

    radius = 15  # Радиус кисти
    mode = 'blue'  # Начальный цвет
    tool = 'line'  # Начальный инструмент: линия, круг, квадрат, треугольник, ромб, ластик
    points = []  # Список точек для рисования
    drawing = False  # Флаг, указывающий, идет ли процесс рисования
    start_pos = (0, 0)  # Начальная позиция для рисования

    while True:
        pressed = pygame.key.get_pressed()  # Получаем нажатые клавиши

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Выход из программы
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Выход из программы по нажатию ESC
                elif event.key == pygame.K_r:
                    mode = 'red'  # Изменение цвета на красный
                elif event.key == pygame.K_g:
                    mode = 'green'  # Изменение цвета на зеленый
                elif event.key == pygame.K_b:
                    mode = 'blue'  # Изменение цвета на синий
                elif event.key == pygame.K_e:
                    tool = 'eraser'  # Выбор инструмента "ластик"
                elif event.key == pygame.K_c:
                    tool = 'circle'  # Выбор инструмента "круг"
                elif event.key == pygame.K_s:
                    tool = 'square'  # Выбор инструмента "квадрат"
                elif event.key == pygame.K_l:
                    tool = 'line'  # Выбор инструмента "линия"
                elif event.key == pygame.K_t:
                    tool = 'triangle'  # Выбор инструмента "треугольник"
                elif event.key == pygame.K_h:
                    tool = 'rhombus'  # Выбор инструмента "ромб"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка мыши
                    drawing = True
                    start_pos = event.pos  # Запоминаем начальную позицию
                    if tool == 'line':
                        points = points + [event.pos]
                        points = points[-256:]  # Ограничиваем количество точек

                elif event.button == 3:  # Правая кнопка мыши
                    radius = max(1, radius - 1)  # Уменьшаем радиус

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Левая кнопка мыши
                    end_pos = event.pos  # Запоминаем конечную позицию
                    if tool == 'circle':
                        pygame.draw.circle(screen, get_color(mode), start_pos, abs(end_pos[0] - start_pos[0]), radius)
                    elif tool == 'square':
                        rect = pygame.Rect(*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
                        pygame.draw.rect(screen, get_color(mode), rect, radius)
                    elif tool == 'triangle':
                        draw_triangle(screen, start_pos, end_pos, get_color(mode))
                    elif tool == 'rhombus':
                        draw_rhombus(screen, start_pos, end_pos, get_color(mode))
                drawing = False

            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if tool == 'eraser':
                        pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)  # Рисуем ластиком
                    elif tool == 'line':
                        position = event.pos
                        points = points + [position]
                        points = points[-256:]  # Ограничиваем количество точек

        if tool == 'line':
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
                i += 1

        pygame.display.flip()  # Обновляем экран
        clock.tick(60)  # Ограничиваем FPS


def get_color(color_mode):
    # Функция для получения цвета в зависимости от режима
    if color_mode == 'blue':
        return (0, 0, 255)
    elif color_mode == 'red':
        return (255, 0, 0)
    elif color_mode == 'green':
        return (0, 255, 0)
    return (255, 255, 255)


def drawLineBetween(screen, index, start, end, width, color_mode):
    # Функция для рисования линий с градиентом цвета
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)  # Рисуем маленькие круги для сглаживания линии


def draw_triangle(screen, start_pos, end_pos, color):
    # Функция для рисования равнобедренного треугольника
    apex_x = (start_pos[0] + end_pos[0]) // 2  # Апекс треугольника по оси X
    apex_y = start_pos[1]  # Апекс треугольника по оси Y
    points = [start_pos, (end_pos[0], start_pos[1]), (apex_x, apex_y)]  # Определяем три вершины треугольника
    pygame.draw.polygon(screen, color, points)  # Рисуем треугольник


def draw_rhombus(screen, start_pos, end_pos, color):
    # Функция для рисования ромба
    mid_x = (start_pos[0] + end_pos[0]) // 2  # Центральная точка по оси X
    mid_y = (start_pos[1] + end_pos[1]) // 2  # Центральная точка по оси Y
    points = [start_pos, (mid_x, start_pos[1]), end_pos, (mid_x, end_pos[1])]  # Определяем вершины ромба
    pygame.draw.polygon(screen, color, points)  # Рисуем ромб


main()  # Запуск главной функции
