import pygame
import random
from pygame.locals import *


pygame.init()

clock = pygame.time.Clock()
running = True

background_image = pygame.image.load("assets/background.jpg")
background_image_width, background_image_height = background_image.get_size()
screen = pygame.display.set_mode((background_image_width, background_image_height))

block_image = pygame.transform.scale(pygame.image.load("assets/block.png"), (50, 50))
block_x, block_y = background_image_width // 2, background_image_height // 2
speed = 5

apple_image = pygame.transform.scale(pygame.image.load("assets/apple.png"), (50, 50))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        block_x -= speed
    if keys[K_RIGHT]:
        block_x += speed
    if keys[K_UP]:
        block_y -= speed
    if keys[K_DOWN]:
        block_y += speed

    block_x = max(50, min(block_x, background_image_width - 100))  
    block_y = max(50, min(block_y, background_image_height - 100))


    screen.blit(background_image, (0, 0))
    screen.blit(block_image, (block_x, block_y))



    pygame.display.flip()

    clock.tick(60)

pygame.quit()


