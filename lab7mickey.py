import pygame
import time
import math

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

minute_hand = pygame.image.load("рука_микки2.png")
second_hand = pygame.image.load("рука_микки2.png")
clock_face = pygame.image.load("mickeyclock_magic.jpeg")

minute_hand = pygame.transform.scale(minute_hand, (150, 100))
second_hand = pygame.transform.scale(second_hand, (150, 90))
clock_face = pygame.transform.scale(clock_face, (WIDTH, HEIGHT))


clock_center = (WIDTH // 2, HEIGHT // 2 )
def blit_rotate_pivot(surf, image, pivot, angle, hand_position):
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=pivot)
    new_pos = (hand_position[0] - rotated_rect.width // 2, hand_position[1] - rotated_rect.height // 2)
    surf.blit(rotated_image, new_pos)

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_face, (0, 0))
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    minute_angle = - (minutes * 6) + 90
    second_angle = - (seconds * 6) + 90
    minute_hand_position = (clock_center[0], clock_center[1] - 50)  
    second_hand_position = (clock_center[0], clock_center[1] - 50)
    blit_rotate_pivot(screen, minute_hand, clock_center, minute_angle, minute_hand_position)
    blit_rotate_pivot(screen, second_hand, clock_center, second_angle, second_hand_position)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(1000)

pygame.quit()
