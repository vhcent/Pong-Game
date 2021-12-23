import pygame, sys

from pygame.constants import QUIT
from Ball import Ball
from Player1 import Player1
from Player2 import Player2

pygame.init()
clock = pygame.time.Clock()
white = (255, 255, 255)
blue = (0,0,255)
red = (255,0,0)

screenWidth = 800
screenHeight = 600

delay = 50

ball = Ball()
player1 = Player1()
player2 = Player2()

def draw():
    pygame.draw.circle(screen, white, (ball.x, ball.y), ball.width)
    pygame.draw.rect(screen, blue, (player1.x, player1.y, player1.width, player1.height))
    pygame.draw.rect(screen, red, (player2.x, player2.y, player2.width, player2.height))

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pong Game")
gameRunning = True
while gameRunning:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            draw()
    draw()
    
    pygame.display.flip()
    clock.tick(60)


