#Table 6
#Group name: Ethan & Friends
#Submission:HumanEd Beginners Rubik's Cube Solving Challenge Task 1

import pygame,sys
from pygame.locals import *
pygame.init()

blue = 114,187,255
white = 230,230,255
yellow = 175,232,65
red = 178,71,61
orange = 255,129,66
green = 0,203,40

colors = [red,yellow,blue,white,green,orange]

def initialize(screen,x,y):
    #Draw the borders of the coloured squares.
    #A border is a white square frame.
    #A face is a 3x3 grid of the coloured squares on one face of a cube.

    #Prints borders on the top row of a face from left to right.
    pygame.draw.rect(screen, (255, 255, 255), (x - 40, y, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 40, y, 40, 40), 3)

    #Middle row
    pygame.draw.rect(screen, (255, 255, 255), (x - 40, y - 40, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x, y - 40, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 40, y - 40, 40, 40), 3)

    #Bottom row
    pygame.draw.rect(screen, (255, 255, 255), (x - 40, y + 40, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x, y + 40, 40, 40), 3)
    pygame.draw.rect(screen, (255, 255, 255), (x + 40, y + 40, 40, 40), 3)

 
def color_side(color,x,y,z,screen):
    #Draw the coloured squares on each face
    if (z==0 or z==1 or z==5):
        #Top row
        pygame.draw.rect(screen,colors[color[0]], (x - 40, y - 40, 34, 34), 0)
        pygame.draw.rect(screen,colors[color[1]], (x, y - 40, 34, 34), 0)
        pygame.draw.rect(screen,colors[color[2]], (x + 40, y - 40, 34, 34), 0)
        #Middle row
        pygame.draw.rect(screen,colors[color[3]], (x - 40, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[4]], (x, y, 34, 34), 0)
        pygame.draw.rect(screen,colors[color[5]], (x + 40, y, 34, 34), 0)
        #Bottom row
        pygame.draw.rect(screen,colors[color[6]], (x - 40, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[7]], (x, y + 40, 34, 34), 0)
        pygame.draw.rect(screen,colors[color[8]],(x + 40, y + 40, 34, 34), 0)

    elif(z==2):
        # Top row
        pygame.draw.rect(screen, colors[color[0]], (x - 40, y - 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[1]], (x, y - 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[2]], (x + 40, y - 40, 34, 34), 0)
        # Middle row
        pygame.draw.rect(screen, colors[color[3]], (x - 40, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[4]], (x, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[5]], (x + 40, y, 34, 34), 0)
        # Bottom row
        pygame.draw.rect(screen, colors[color[6]], (x - 40, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[7]], (x, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[8]], (x + 40, y + 40, 34, 34), 0)

    elif(z==3):
        # Top row
        pygame.draw.rect(screen, colors[color[0]], (x - 40, y - 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[1]], (x, y - 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[2]], (x + 40, y - 40, 34, 34), 0)
        # Middle row
        pygame.draw.rect(screen, colors[color[3]], (x - 40, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[4]], (x, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[5]], (x + 40, y, 34, 34), 0)
        # Bottom row
        pygame.draw.rect(screen, colors[color[6]], (x - 40, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[7]], (x, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[8]], (x + 40, y + 40, 34, 34), 0)

    elif(z==4):
        # Top row
        pygame.draw.rect(screen, colors[color[0]], (x - 40, y - 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[1]], (x, y - 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[2]], (x + 40, y - 40, 34, 34), 0)
        # Middle row
        pygame.draw.rect(screen, colors[color[3]], (x - 40, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[4]], (x, y, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[5]], (x + 40, y, 34, 34), 0)
        # Bottom row
        pygame.draw.rect(screen, colors[color[6]], (x - 40, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[7]], (x, y + 40, 34, 34), 0)
        pygame.draw.rect(screen, colors[color[8]], (x + 40, y + 40, 34, 34), 0)
     
def color_update(matrix,screen):
    #Calls the function used to draw the coloured squares in each face from face 0 to face 5.
    color_side(matrix[0],173,173,0,screen)
    color_side(matrix[1],173,293,1,screen)
    color_side(matrix[2],293,173,2,screen)
    color_side(matrix[3],173,53,3,screen)
    color_side(matrix[4],53,173,4,screen)
    color_side(matrix[5],173,413,5,screen)

def paint(matrix):
    screen = pygame.display.set_mode((380,500))
    pygame.display.set_caption("3x3 rubics cube")
    screen.fill((155,155,155))
    #Create the borders for the 6 faces.
    initialize(screen,170,170)
    initialize(screen,170,290)
    initialize(screen,290,170)
    initialize(screen,170,50)
    initialize(screen,50,170)
    initialize(screen,170,410)
    color_update(matrix,screen)
    pygame.display.update()

    #The close button is not functioning properly so we added this code.
    main_clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        main_clock.tick(60)
 
paint([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, 1, 1, 1, 1],
       [2, 2, 2, 2, 2, 2, 2, 2, 2],
       [3, 3, 3, 3, 3, 3, 3, 3, 3],
       [4, 4, 4, 4, 4, 4, 4, 4, 4],
       [5, 5, 5, 5, 5, 5, 5, 5, 5]])
