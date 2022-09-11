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

# Get the opposite of the 2 rotations of the shapes
def reverseShape(shape): 
    b = list(reversed(shape))
    rI = 0
    for row in b:
        b[rI] = row[::-1]
        rI += 1
    return b

# The shapes and their rotations
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
Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
I = [['.....',
      '0000.',
      '.....',
      '.....',
      '.....'],
     ['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....']]
O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....'],
      ['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....']]
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....']]
T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....']]
shapes = [S, Z, I, O, J, L, T]
colours = [red, green, blue, yellow, pink, orange, purple]
# ------------------------- #

# make the shapes
def createShape(startX, startY):
    currentShape = random.choice(shapes)
    x, y = startX, startY

    reversedShape, reversedShape2  = reverseShape(currentShape[0]), reverseShape(currentShape[1])
    currentShape += [reversedShape] + [reversedShape2]

    allShapeCoords = []
    for shape in currentShape:
        localY = 0
        shapeCoords = []
        for row in shape:
            localX = 0
            for gridpoint in row:
                if gridpoint == '0':
                    gridpointCoords = [x + (localX), y + (localY)]
                    shapeCoords.append(gridpointCoords)
                localX += 1
            localY += 1
        allShapeCoords.append(shapeCoords)

        #get the width of the shape
    xList = []

    for i in allShapeCoords[0]:
        xList.append(i[0])
    maxi = max(xList)
    mini = min(xList)
        
    shapeWidth = maxi - mini + 1


    randspawn = random.randrange(0, 10 - shapeWidth)
    return currentShape, allShapeCoords, randspawn



#gwn de shape, kk domme
def drawShape(shape, randspawn, globX, globY):
    currentColour = colours[shapes.index(shape)]
    blockSize = 38
    defaultShape = shape[0]

    #spawn the shape on a valid location
    y = globY
    for row in defaultShape:
        x = randspawn + globX
        for gridpoint in row:
            if gridpoint == '0':
                rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
                pygame.draw.rect(screen, currentColour, rect)    
            x += 1
        if '0' in row:
            y += 1


#define in game time
clock = pygame.time.Clock()

#print the game in console
lol, coords, spawnLoc = createShape(0, 0)
for i in lol:
    for l in i:
        print(l)
    print('')
for c in coords:
    print(c)
    print('')

tLast = 0
y = 0
x = 0
#main game loop
while True:
    screen.fill(black)
    dt = clock.tick()
    tLast += dt



    drawGrid()
    drawShape(lol, spawnLoc, x, y)
    print(coords)
    
    if tLast > 300:
        y += 1
        tLast = 0


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if y < 19:
                    y += 1
            if event.key == pygame.K_LEFT:
                if x > 0 - spawnLoc:
                    x -= 1
            if event.key == pygame.K_RIGHT:
                if x < 9:
                    x += 1
        if event.type == pygame.QUIT: sys.exit()
    pygame.display.flip()
