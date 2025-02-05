import pygame
import random
from pygame.locals import *




class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.background_image = pygame.image.load("assets/background.jpg")
        self.background_image_width, self.background_image_height = self.background_image.get_size()
        self.screen = pygame.display.set_mode((self.background_image_width, self.background_image_height))

        self.block = Block(self.background_image_width, self.background_image_height)
        self.apple = Apple(self.background_image_width, self.background_image_height)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[K_LEFT]:
                self.block.block_x -= self.block.speed
            if keys[K_RIGHT]:
                self.block.block_x += self.block.speed
            if keys[K_UP]:
                self.block.block_y -= self.block.speed
            if keys[K_DOWN]:
                self.block.block_y += self.block.speed

            self.block.block_x = max(50, min(self.block.block_x, self.background_image_width - 100))  
            self.block.block_y = max(50, min(self.block.block_y, self.background_image_height - 100))


            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.block.block_image, (self.block.block_x, self.block.block_y))
            self.screen.blit(self.apple.apple_image, (self.apple.apple_x, self.apple.apple_y))



            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()

    def collision(self, block, apple):
        if (block.block_x < apple.apple_x  or
        block.block_x > apple.apple_x or
        block.block_y < apple.apple_y  or
        block.block_y + 50 > apple.apple_y):
            print("collision")

class Block:
    def __init__(self, background_image_width, background_image_height):
        self.block_image = pygame.transform.scale(pygame.image.load("assets/block.png"), (50, 50))
        self.block_x, self.block_y = background_image_width // 2, background_image_height // 2
        self.speed = 5


class Apple:
    def __init__(self, background_image_width, background_image_height):
        self.apple_image = pygame.transform.scale(pygame.image.load("assets/apple.png"), (50, 50))
        self.apple_x = random.randint(50, background_image_width - 100)
        self.apple_y = random.randint(50, background_image_height - 100)



game = Game()
game.run()