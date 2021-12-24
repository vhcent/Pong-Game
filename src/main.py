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
titleScreen = True
gameRunning = False
endScreen = False
player1Wins = False
player2Wins = False

delay = 50

ball = Ball()
player1 = Player1()
player2 = Player2()
titleButton = pygame.Rect(0, 0, 800, 175)
startButton = pygame.Rect(screenWidth / 2 - 70, screenHeight/2 - 50, 130, 50)
exitButton = pygame.Rect(screenWidth / 2 - 60, screenHeight/2 + 100, 110, 50)
endScreenButton = pygame.Rect(screenWidth / 2 - 60, screenHeight/2 + 100, 135, 50)

def drawGame():
    screen.fill(black)
    pygame.draw.circle(screen, white, (ball.x, ball.y), ball.width)
    pygame.draw.rect(screen, blue, (player1.x, player1.y, player1.width, player1.height))
    pygame.draw.rect(screen, red, (player2.x, player2.y, player2.width, player2.height))
    screen.blit(pygame.font.Font("freesansbold.ttf", 32).render(f"{player1.score}", False, grey), (0, 0))
    screen.blit(pygame.font.Font("freesansbold.ttf", 32).render(f"{player2.score}", False, grey), (785, 0))

def drawTitleScreen():
    pygame.draw.rect(screen, blue, titleButton)
    pygame.draw.rect(screen, red, startButton)
    pygame.draw.rect(screen, red, exitButton)
    screen.blit(pygame.font.Font("freesansbold.ttf", 80).render("Pong Game", False, grey), (screenWidth / 2 - 225, 50))
    screen.blit(pygame.font.SysFont("freesansbold.ttf",80).render('Start' , True , white) , (screenWidth / 2 - 70, screenHeight/2 - 50))
    screen.blit(pygame.font.SysFont("freesansbold.ttf",80).render('Exit' , True , white) , (screenWidth / 2 - 60, screenHeight/2 + 100))
    
def drawEndScreen():
    pygame.draw.rect(screen, white, (0, screenHeight / 2 - 200, 800, 125))
    if player1Wins:
        screen.blit(pygame.font.Font("freesansbold.ttf", 100).render("Player 1 Wins!", False, black), (screenWidth / 2 - 350, screenHeight / 2 - 200))
    elif player2Wins:
        screen.blit(pygame.font.Font("freesansbold.ttf", 100).render("Player 2 Wins!", False, black), (screenWidth / 2 - 350, screenHeight / 2 - 200))
    pygame.draw.rect(screen, grey, endScreenButton)
    screen.blit(pygame.font.SysFont("freesansbold.ttf",80).render('Back' , True , black) , (screenWidth / 2 - 60, screenHeight/2 + 100))
    
def resetScores():
    player1.score = 0
    player2.score = 0
            
        

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pong Game")
mouse = pygame.mouse.get_pos()

while True:
    while titleScreen:
        screen.fill(black)
        drawTitleScreen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = event.pos
                if exitButton.collidepoint(mousePosition):
                    pygame.quit()
                    sys.exit()
                if startButton.collidepoint(mousePosition):
                    titleScreen = False
                    gameRunning = True
        pygame.display.flip()
        clock.tick(10)

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
        drawGame()
        if player1.score == 10 or player2.score == 10:
            gameRunning = False
            endScreen = True
            if player1.score == 10:
                player1Wins = True
            elif player2.score == 10:
                player2Wins = True
        #Update window
        pygame.display.flip()
        clock.tick(60)
        
    while endScreen:
        screen.fill(black)
        drawEndScreen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePosition = event.pos
                    if endScreenButton.collidepoint(mousePosition):
                        endScreen = False
                        titleScreen = True
                        resetScores()
                        player1Wins = False
                        player2Wins = False
                        
        pygame.display.flip()
        clock.tick(10)

