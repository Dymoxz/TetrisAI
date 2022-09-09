import sys, pygame
import time
import random
pygame.init()

# Initialize the game screen
size = width, height = 380, 760
speed = [2, 2]
black = 0, 0, 0
grayValue = 70
gray = grayValue,grayValue,grayValue
red = 246, 0, 0
green = 105, 182, 38
blue = 3, 228, 255
yellow = 250, 252, 1
pink = 255, 81, 188
orange = 255, 141, 1
purple = 159, 0, 150

screen = pygame.display.set_mode(size)
# ------------------------- #

# Letterlijk de function naam
def drawGrid():
    blockSize = 38
    for x in range(0, width, blockSize):
        for y in range(0, height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, gray, rect, 1)

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]


# Get the opposite of the 2 rotations of the shapes
def reverseShape(shape): 
    b = list(reversed(shape))
    rShape = 0
    for row in b:
        b[rShape] = row[::-1]
        rShape += 1
    return b

# spawn the piece
    # blocksize == x amount of pixels
    # it checks for every point in the shape and see if there is a 0
    # if gridpoint == 0 then there is a piece there (it's position is relative)
def spawnShape(currentShape, iks, ei):
    reversedShape, reversedShape2  = reverseShape(currentShape[0]), reverseShape(currentShape[1])
    currentShape += [reversedShape] + [reversedShape2]
    defaultShape = currentShape[0]
    blockSize = 38
    y = ei
    for row in defaultShape:
        x = iks
        for gridpoint in row:
            if gridpoint == '0':
                rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
                pygame.draw.rect(screen, purple, rect)    
            x += 1
        if '0' in row:
            y += 1




spawnShape(S, 0, 0)
x = 0 
y = 0 
time_elapsed_since_last_action = 0
clock = pygame.time.Clock()
while True:
    screen.fill(black)
    drawGrid()

    dt = clock.tick() 

    time_elapsed_since_last_action += dt
    spawnShape(S, x, y)



    if time_elapsed_since_last_action > 1200:
        if y < 19:
            y += 1
        time_elapsed_since_last_action = 0

    


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if y < 19:
                    y += 1
            if event.key == pygame.K_LEFT:
                if x > 0:
                    x -= 1
            if event.key == pygame.K_RIGHT:
                if x < 9:
                    x += 1
        if event.type == pygame.QUIT: sys.exit()
    pygame.display.flip()