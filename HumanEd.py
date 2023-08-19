#Table 6
#Group name: Ethan & Friends
#Submission:HumanEd Beginners Rubik's Cube Solving Challenge Task 2

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


def color_side(color, x, y, z, screen):
    # Draw the coloured squares on each face
    if (z == 0 or z == 1 or z == 5):
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

    elif (z == 2):
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

    elif (z == 3):
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

    elif (z == 4):
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
    color_side(matrix[1],293,173,1,screen)
    color_side(matrix[2],173,53,2,screen) #2->3
    color_side(matrix[3],53,173,3,screen)
    color_side(matrix[4],173,293,4,screen)
    color_side(matrix[5],413,173,5,screen)

def paint(matrix):
    screen = pygame.display.set_mode((500,500))
    pygame.display.set_caption("3x3 Rubik's cube")
    screen.fill((155,155,155))
    #Create the borders for the 6 faces.
    initialize(screen,170,170) #pane 0
    initialize(screen,170,290) #pane 1
    initialize(screen,290,170) #pane 2
    initialize(screen,170,50) #pane 3
    initialize(screen,50,170) #pane 4
    initialize(screen,410,170) #pane 5
    #Add colour
    color_update(matrix,screen)
    pygame.display.update()

    main_clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        main_clock.tick(60)

code = input ("Enter the string representing the colour of the 3x3 Rubik cube (54 characters): ")
#code = "rywwybyroyoboooobrrgyybrwbggyowrgwybgggwgbwgbbrrwwryoo"
input_data = []
valid_input = True
for i in code:
    if len(code) != 54:
        print("Not the correct length of code")
        valid_input = False
        break
    if i == "r":
        input_data.append(0)
    elif i == "y":
        input_data.append(1)
    elif i == "b":
        input_data.append(2)
    elif i == "w":
        input_data.append(3)
    elif i == "g":
        input_data.append(4)
    elif i == "o":
        input_data.append(5)
    else:
        print("Invalid Input")
        valid_input = False
        break
if valid_input:
    paint([input_data[18:27], 
           input_data[27:36],
           input_data[0:9],
           input_data[9:18],
           input_data[45:],
           input_data[36:45]])


