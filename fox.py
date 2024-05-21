import pygame

class Fox:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.image = pygame.image.load("orange-fox-sprite.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .1
        self.current_direction = "right"

    def move_direction(self, direction):
        if self.current_direction == "right" and direction == "left":
            self.image = pygame.transform.flip(self.image, True, False)
        if self.current_direction == "left" and direction == "right":
            self.image = pygame.transform.flip(self.image, True, False)
        if direction == "right":
            self.current_direction = "right"
            self.x = self.x + self.delta
        if direction == "left":
            self.current_direction = "left"
            self.x = self.x - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "up":
            self.y = self.y - self.delta
        if direction == "down":
            self.y = self.y+ self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

