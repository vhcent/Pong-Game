import pygame
class Player2():
    def __init__(self):
        self.x = 790
        self.y = 250
        self.width = 10
        self.height = 100
        self.speed = 0
        self.incrementSpeed = 5
        self.score = 0
        
    def move(self):
        self.y += self.speed
        if pygame.Rect(self.x, self.y, self.width, self.height).top <= 0:
            self.y = 0
        if pygame.Rect(self.x, self.y, self.width, self.height).bottom >= 600:
            self.y = 600 - self.height