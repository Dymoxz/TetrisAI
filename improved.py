from ast import excepthandler
import pygame
import random
import time
#initalize pygame window
pygame.init()
width, height = 480, 960
blockSize = 48
screen = pygame.display.set_mode((width, height))

#colors
gray = (70, 70, 70,)
black = 0, 0, 0
red = 246, 0, 0
green = 105, 182, 38
blue = 3, 228, 255
yellow = 250, 252, 1
pink = 255, 81, 188
orange = 255, 141, 1
purple = 159, 0, 150

# 1. render bord
#     - achtergrond kleur ✓ 
#     - grid ✓
#
# 2. create shape
#     - random shape ✓
#     - bij shape horende kleur ✓
#     - pak rel coords van shape ✓
#----------------------------#
# 3. render shape
#     - random begin positie ✓
#     - default rotatie ✓
#     - get abs coords
#     - render op board
# 5. input
#     - detect input
#     - move shape to side or rotate if left right or up
# 4. gravitatie
#     - pak coords van laagste punten van shape
#     - check bij alle coords 1 er onder
#     - als onder, stop en spawn niewe shape
#     - als niet, verhoog y en render



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
bozo = [['00000',
    '00000',
    '00000',
    '00000',
    '00000']]
shapes = [S, Z, I, O, J, L, T]
shapeNames = ['S', 'Z', 'I', 'O', 'J', 'L', 'T']
fullShapes = []
colours = [red, green, blue, yellow, pink, orange, purple]


def initShapes(shapeee):

    # create rotated versions of shape
    # add the rotated version to a new list called fullShapes
    for shape in shapeee:
        shape2 = []
        for rotShape in shape:
            revRotShape = []
            for row in rotShape:
                revRotShape.append(row[::-1])
            revRotShape.reverse()
            shape2.append(rotShape)
            shape2.append(revRotShape)
        shape2 = [shape2[0], shape2[2], shape2[1], shape2[3]]

        fullShapes.append(shape2)

    # ger the relative coords of all the shapes
    fullShapesCoordsREL = []
    for shapes in fullShapes:
        shapeList = []
        for rotations in shapes:
            rotList = []
            for dy in range(len(rotations)):
                for dx in range(len(rotations[dy])):
                    if rotations[dy][dx] == '0':
                        coord = [dx,dy]
                        rotList.append(coord)
            shapeList.append(rotList)
        fullShapesCoordsREL.append(shapeList)

    # get all the minimum x and y values of all the shapes
    allMinXY = []
    for shape in fullShapesCoordsREL:
        shapeMinXY = []
        for rotation in shape:
            xList = []
            yList = []
            for coord in rotation:
                xList.append(coord[0])
                yList.append(coord[1])
            xMin = min(xList)
            yMin = min(yList)
            shapeMinXY.append([xMin,yMin])
        allMinXY.append(shapeMinXY)

    # move all the shapes so they are closest to the top left (0,0)
    allNew = []
    for shapeI in range(len(fullShapesCoordsREL)):
        newShape = []
        for rotI in range(len(fullShapesCoordsREL[shapeI])):
            newRotation = []
            for coordI in range(len(fullShapesCoordsREL[shapeI][rotI])):
                newCoord = []
                newCoord = [fullShapesCoordsREL[shapeI][rotI][coordI][0] - allMinXY[shapeI][rotI][0], fullShapesCoordsREL[shapeI][rotI][coordI][1] - allMinXY[shapeI][rotI][1]]
                newRotation.append(newCoord)
            newShape.append(newRotation)
        allNew.append(newShape)

        # get the width and height of all the shapes
    allWH = []
    for shape in allNew:
        shapeWH = []
        for rotation in shape:
            xList = []
            yList = []
            for coord in rotation:
                xList.append(coord[0])
                yList.append(coord[1])
            xMax = max(xList)
            yMax = max(yList)
            shapeWH.append([xMax + 1,yMax + 1])
        allWH.append(shapeWH)

    return allNew, allWH

# get all the data from the shapes
allShapesCoordsREL, allWH = initShapes(shapes)

def DrawBoard():
    global blockSize
    global boardColours
    for x in range(0, width, blockSize):
        for y in range(0, height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, gray, rect, 1)

def RenderShape(shapeCoords, color):
    blockSize = 48
    for coords in shapeCoords:
        x = coords[0]
        y = coords[1]
        rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
        pygame.draw.rect(screen, color, rect)

def renderBoardAfterClear(shapeCoords, color):
    blockSize = 48
    for coords in range(len(shapeCoords)):
        x = shapeCoords[coords][0]
        y = shapeCoords[coords][1]
        rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
        pygame.draw.rect(screen, color[coords], rect)

def remLastPos(abycordy, ax, by,rotation):
    for coord in abycordy[rotation]:
        aaa = coord[0] + ax
        bbb = coord[1] + by
        eerect = pygame.Rect(aaa * blockSize, bbb * blockSize, blockSize, blockSize)
        pygame.draw.rect(screen, black, eerect)

def CheckCollision(shapeCoords, direction):
    downCollisions = []
    rightCollisions = []
    leftCollisions = []
    upCollisions = []
    for coord in shapeCoords:
        xCoord = coord[0]
        yCoord = coord[1]
        if direction == 'down':
            if [xCoord, yCoord + 1] in board['shapeCoords']:
                downCollisions.extend('collision')
        if direction == 'left':
            if [xCoord - 1, yCoord] in board['shapeCoords']:
                leftCollisions.extend('collision')
        if direction == 'right':
            if [xCoord + 1, yCoord] in board['shapeCoords']:
                rightCollisions.extend('collision')
        if direction == 'up':
            if [xCoord, yCoord] in board['shapeCoords'] or [xCoord, yCoord] in board['bottomCoords']:
                upCollisions.extend('collision')
    return downCollisions, rightCollisions, leftCollisions, upCollisions
        
def GetAbsCoords(shapeCoords, x, y, rotation):
    absCoords = []
    for coord in shapeCoords[rotation]:
        absCoords.append([coord[0] + x, coord[1] + y])
    return absCoords

def clearLines(lineCoords, lineY):
    for coord in lineCoords:
        board['colours'].pop(board['shapeCoords'].index(coord))
        board['shapeCoords'].remove(coord)
    screen.fill(black)
    DrawBoard()

    for coord in board['shapeCoords']:
        if coord[1] < min(lineY):
            board['shapeCoords'][board['shapeCoords'].index(coord)][1] += len(lineY)

    renderBoardAfterClear(board['shapeCoords'], board['colours'])


running = True
dropping = True
rotation = 0
beginShape = random.choice(allShapesCoordsREL)
clock = pygame.time.Clock()
board = {
    "shapeCoords": [],
    "colours": [],
    "rotations": [],
    "bottomCoords": []
}

board['bottomCoords'] = [[0,20],[1,20],[2,20],[3,20],[4,20],[5,20],[6,20],[7,20],[8,20],[9,20]]




# ------------------ SCORE ------------------ #
# 1 line = 100 points
# 2 lines = 300 points
# 3 lines = 500 points
# 4 lines = 800 points
# back to back = 1.5x
score = 0
scoreDict = {
    '1': 100,
    '2': 300,
    '3': 500,
    '4': 800
}
clearStreak = 0
thetStreak = 0
level = 1
# ------------------------------------------- #








while running:
    # Get Current and next shape to spawn
    try:
        currentShape = nextShape
    except:
        currentShape = beginShape
    currentShape = allShapesCoordsREL[2]
    nextShape = random.choice(allShapesCoordsREL)
    currentColour = colours[allShapesCoordsREL.index(currentShape)]

    # print(shapeNames[allShapesCoordsREL.index(currentShape)], shapeNames[allShapesCoordsREL.index(nextShape)])
    # print(allShapesCoordsREL[allShapesCoordsREL.index(currentShape)][rotation])
    
    y = 0
    x = 3
    tLast = 0
    bb = 0
    rotation = 0
    absCoords = GetAbsCoords(currentShape, x, y, rotation)
    RenderShape(absCoords, currentColour)
    dropping = True
    while dropping:
        dt = clock.tick()
        tLast += dt
        DrawBoard()
        pygame.display.update()
        ghostCoords = []
        underY = []
        for coord in ghostCoords:
            rect = pygame.Rect(coord[0] * blockSize, coord[1] * blockSize, blockSize, blockSize)
            pygame.draw.rect(screen, currentColour, rect)


        if tLast > 80:
            absCoords = GetAbsCoords(currentShape, x, y, rotation)
            down, right, left, up = CheckCollision(absCoords, 'down')
            w, h = allWH[allShapesCoordsREL.index(currentShape)][rotation][0], allWH[allShapesCoordsREL.index(currentShape)][rotation][1]
            if len(down) > 0 or y > 19 - h:
                bb += dt
                if bb > 500:
                    dropping = False
                    board['shapeCoords'].extend(absCoords)
                    board['colours'].extend([currentColour] * len(absCoords))
                    yFill = []
                    coordsToClear = []
                    linesToBeCleared = []
                    for coord in board['shapeCoords']:
                        yFill.append(coord[1])
                    for y in yFill:
                        if yFill.count(y) == 10 and y not in linesToBeCleared:
                            linesToBeCleared.append(y)
                    for line in linesToBeCleared:
                        for coord in board['shapeCoords']:
                            if coord[1] == line:
                                coordsToClear.append(coord)
                    if len(linesToBeCleared) > 0:
                        clearLines(coordsToClear, linesToBeCleared)
                        for i in scoreDict:
                            if len(linesToBeCleared) == int(i):
                                score += scoreDict[i]  * level
                                clearStreak += 1
                                if int(i) == 4:
                                    thetStreak += 1
                                elif int(i) < 4:
                                    thetStreak = 0
                                if int(i) == 4 and thetStreak > 1:
                                    score += round(scoreDict[i] * 0.5)
                                if clearStreak > 1:
                                    score += 50 * clearStreak * level
                                
                    else:
                        clearStreak = 0
                        thetStreak = 0
                    print('Score: ' + str(score) + '\n' +
                          ' Clear Streak: ' + str(clearStreak) + '\n' +
                          ' Tetris Streak: ' + str(thetStreak) +  '\n' +
                          ' Level: ' + str(level))

            else:
                remLastPos(currentShape, x, y,rotation)
                y += 1
                absCoords  =GetAbsCoords(currentShape, x, y, rotation)
                RenderShape(absCoords, currentColour)
                tLast = 0
                bb = 0

        for event in pygame.event.get():
            pygame.key.set_repeat(150, 150)
            if event.type == pygame.QUIT:
                running = False
                dropping = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    down, right,left, up = CheckCollision(absCoords, 'right')
                    if len(right) > 0:
                        pass
                    else:
                        if x < 10 - w:
                            remLastPos(currentShape, x, y,rotation)
                            x += 1
                            absCoords = GetAbsCoords(currentShape, x, y, rotation)
                    RenderShape(absCoords, currentColour) 
                if event.key == pygame.K_LEFT:
                    down, right,left, up = CheckCollision(absCoords, 'left')
                    if len(left) > 0:
                        pass
                    else:
                        if x > 0:
                            remLastPos(currentShape, x, y,rotation)
                            x -= 1
                            absCoords = GetAbsCoords(currentShape, x, y, rotation)
                    RenderShape(absCoords, currentColour) 
                if event.key == pygame.K_UP:
                    if rotation <3:
                        absCoords = GetAbsCoords(currentShape, x, y, rotation + 1)
                    else:
                        rabsCoords = GetAbsCoords(currentShape, x, y, rotation - 3)
                    down, right,left, up = CheckCollision(absCoords, 'up')
                    if len(up) > 0:
                        absCoords = GetAbsCoords(currentShape, x, y, rotation)
                    else:
                        remLastPos(currentShape, x, y,rotation)
                        rotation = rotation + 1 if rotation < 3 else 0     
                        absCoords = GetAbsCoords(currentShape, x, y, rotation)
                    RenderShape(absCoords, currentColour) 
                    w, h = allWH[allShapesCoordsREL.index(currentShape)][rotation][0], allWH[allShapesCoordsREL.index(currentShape)][rotation][1]
pygame.quit()