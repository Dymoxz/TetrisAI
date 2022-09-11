import sys, pygame
import time
import random
pygame.init()
def main():

    Board = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]



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

    def createShape(startX, startY):
        currentShape = random.choice(shapes)
        x, y = startX, startY
        if currentShape == O:
            reversedShape, reversedShape2 = O[0], O[1]
        else:
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

        widthList = []
        for y in currentShape:
            xList = []
            for i in allShapeCoords[currentShape.index(y)]:
                xList.append(i[0])
            maxi = max(xList)
            mini = min(xList)
            shapeWidth = maxi - mini + 1
            widthList.append(shapeWidth)
        print(widthList)

        heightList = []
        for y in currentShape:
            yList = []
            for i in allShapeCoords[currentShape.index(y)]:
                yList.append(i[1])
            maxi1 = max(yList)
            mini2 = min(yList)
            shapeHeight = maxi1 - mini2 + 1
            heightList.append(shapeHeight)
        print(heightList)
        if currentShape == I:
            shapeHeight = 1
        if currentShape == I:
            shapeWidth = 3
        
        randspawn = random.randrange(0, 10 - shapeWidth)
        return currentShape, allShapeCoords, randspawn, widthList, heightList


    #gwn de shape, kk domme
    def drawShape(shape, randspawn, globX, globY, rot, coords):
        currentColour = colours[shapes.index(shape)]
        blockSize = 38
        defaultShape = shape[rot]

        #spawn the shape on a valid location
        y = globY
        for row in defaultShape:
            x = globX
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
    lol, coords, spawnLoc, sWidth, sHeight = createShape(0, 0)
    print(sWidth)
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
    placed = False
    rotation = 0


    def moveAndGetRealCoords(x, y, dX, dY, coords, rot):
        yB = y
        xB = x
        y += dY
        x += dX
        if rot > 3:
            rot = 0
        for i in coords[rot]:
            i[1] += y - yB
            i[0] += x - xB
        print(coords[rot])







    while True:
        screen.fill(black)
        dt = clock.tick()
        tLast += dt

        drawGrid()
        try:
            drawShape(lol, spawnLoc, x, y, rotation, coords)
        except:
            rotation = 0
            drawShape(lol, spawnLoc, x, y, rotation, coords)
        
        if tLast > 1000:
            for i in coords[rotation]:
                Board[i[1] - 1][i[0]] = '.'
            moveAndGetRealCoords(x, y, 0, 1, coords, rotation)
            for i in coords[rotation]:
                Board[i[1] -1 ][i[0]] = 'O'
            y += 1
            for i in Board:
                print(i)

            # else:
            #     #placeShape()
            #     placed = True
            tLast = 0


        for event in pygame.event.get():
            # pygame.key.set_repeat(100, 100)
            if not placed:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        for i in coords[rotation]:
                            Board[i[1] - 1][i[0]] = '.'
                        rotation += 1
                        if rotation > 3:
                            rotation = 0
                        moveAndGetRealCoords(x, y, 0, 0, coords, rotation)
                        for i in coords[rotation]:
                            Board[i[1] - 1][i[0]] = 'O'
                        for i in Board:
                            print(i)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        # restart game
                        main() 
        if event.type == pygame.QUIT: sys.exit()
        pygame.display.flip()

        if placed:
            # main()
            pass
main()

