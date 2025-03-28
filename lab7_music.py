import pygame
import os

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

MUSIC_FOLDER = "music"
tracks = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]

current_track = 0

def play_music():
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, tracks[current_track]))
    pygame.mixer.music.play()

play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.play()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(tracks)
                play_music()
            elif event.key == pygame.K_b: 
                current_track = (current_track - 1) % len(tracks)
                play_music()
    pygame.display.flip()
pygame.quit()
