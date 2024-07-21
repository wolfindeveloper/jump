import pygame
from random import randint
from pygame import mixer
pygame.init()
mixer.init()
mixer.music.load("audio/jump.ogg")

WIDTH = 500
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = pygame.Rect(50, 300, 40, 60)
speed = 5
isJump = False
jumpCount = 10

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > 0 + 5:
        player.x -= speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - 5 - player.width:
        player.x += speed
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            mixer.music.play()
    else:
        if jumpCount >= -10:
            player.y -= jumpCount * abs(jumpCount) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    win.fill((20, 20, 20))
    pygame.draw.rect(win, (255, 0, 0), player)
    pygame.display.update()



