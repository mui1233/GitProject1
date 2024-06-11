import pygame

class Enemy:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.image = pygame.image.load("finenemtank.png")
        self.image_size = self.image.get_size()

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 10
        self.facing_right = False
        self.health = 100
        #self.image = pygame.transform.scale(self.image, (100, 100))
    def move_right(self):
        self.x += self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move_left(self):
        self.x -= self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def update_image(self, facing_right):
        if facing_right != self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
            self.facing_right = facing_right