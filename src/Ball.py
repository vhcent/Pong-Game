import pygame, random
from Player1 import Player1
from Player2 import Player2

class Ball():
    x = 400
    y = 300
    width = 10
    xSpeed = 6 * random.choice((-1, 1))
    ySpeed = 6 * random.choice((-1, 1))

    def __init__(self):
        pass

    def move(self, Player1, Player2):
        self.x += self.xSpeed
        self.y += self.ySpeed
        if pygame.Rect(self.x, self.y, self.width, self.width).top <= 0 or pygame.Rect(self.x, self.y, self.width, self.width).bottom >= 600:
            self.ySpeed *= -1
        if pygame.Rect(self.x, self.y, self.width, self.width).right >= 800 or pygame.Rect(self.x, self.y, self.width, self.width).left <= 0:
            if pygame.Rect(self.x, self.y, self.width, self.width).right >= 800:
                Player1.score += 1
            elif pygame.Rect(self.x, self.y, self.width, self.width).left <= 0:
                Player2.score +=1
            self.reset()
        if pygame.Rect(self.x, self.y, self.width, self.width).colliderect(pygame.Rect(Player1.x, Player1.y, Player1.width, Player1.height)) or pygame.Rect(self.x, self.y, self.width, self.width).colliderect(pygame.Rect(Player2.x, Player2.y, Player2.width, Player2.height)):
            self.xSpeed *= -1 
            
    def reset(self):
        self.x = 400
        self.y = 300
        self.xSpeed = 6 * random.choice((-1, 1))
        self.ySpeed = 6 * random.choice((-1, 1))
