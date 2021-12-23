import pygame, sys
from pygame.constants import QUIT
from Ball import Ball
from Player1 import Player1
from Player2 import Player2

pygame.init()
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
grey = (211, 211, 211)
blue = (0,0,255)
red = (255,0,0)
screenWidth = 800
screenHeight = 600

delay = 50

ball = Ball()
player1 = Player1()
player2 = Player2()

def draw():
    screen.fill(black)
    pygame.draw.circle(screen, white, (ball.x, ball.y), ball.width)
    pygame.draw.rect(screen, blue, (player1.x, player1.y, player1.width, player1.height))
    pygame.draw.rect(screen, red, (player2.x, player2.y, player2.width, player2.height))
    screen.blit(pygame.font.Font("freesansbold.ttf", 32).render(f"{player1.score}", False, grey), (0, 0))
    screen.blit(pygame.font.Font("freesansbold.ttf", 32).render(f"{player2.score}", False, grey), (785, 0))

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pong Game")
gameRunning = True

while gameRunning:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1.speed -= player1.incrementSpeed
                if event.key == pygame.K_s:
                    player1.speed += player1.incrementSpeed
                if event.key == pygame.K_UP:
                    player2.speed -= player2.incrementSpeed
                if event.key == pygame.K_DOWN:
                    player2.speed += player2.incrementSpeed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player1.speed += player1.incrementSpeed
                if event.key == pygame.K_s:
                    player1.speed -= player1.incrementSpeed
                if event.key == pygame.K_UP:
                    player2.speed += player2.incrementSpeed
                if event.key == pygame.K_DOWN:
                    player2.speed -= player2.incrementSpeed
    
    ball.move(player1, player2)
    player1.move()
    player2.move()
    draw()
    
    #Update window
    pygame.display.flip()
    clock.tick(60)


