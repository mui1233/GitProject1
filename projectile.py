import pygame
from fox import Fox
class Projectile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("projectle.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .1

    def move_right(self):
        self.x += self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move_left(self):
        self.x -= self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


