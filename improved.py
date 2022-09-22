import pygame
import random
#initalize pygame window
pygame.init()
width, height = 680, 960
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
white = 255, 255, 255

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


# alle shapes van de Tetrominoes 
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
# init stuff
shapes = [S, Z, I, O, J, L, T]
shapeNames = ['S', 'Z', 'I', 'O', 'J', 'L', 'T']
fullShapes = []
colours = [red, green, blue, yellow, pink, orange, purple]


colourDict = {
    'S': red,
    'Z': green,
    'I': blue,
    'O': yellow,
    'J': pink,
    'L': orange,
    'T': purple
}

#----------------------------#
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

    # get the relative coords of all the shapes using complitated logic
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

# draw the tetris board in pygame
def DrawBoard():
    global blockSize
    global boardColours
    for x in range(0, 480, blockSize):
        for y in range(0, height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, gray, rect, 1)

#render the tetrominoes on the board in pygame
def RenderShape(shapeCoords, color):
    blockSize = 48
    for coords in shapeCoords:
        x = coords[0]
        y = coords[1]
        rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
        pygame.draw.rect(screen, color, rect)

#render the board in pygame after a line(s) has been cleared
def renderBoardAfterClear(shapeCoords, color):
    blockSize = 48
    for coords in range(len(shapeCoords)):
        x = shapeCoords[coords][0]
        y = shapeCoords[coords][1]
        rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
        pygame.draw.rect(screen, color[coords], rect)

#remove the coords of the tetrominoes' last postion from the board so that they wont render
def remLastPos(abycordy, ax, by,rotation):
    for coord in abycordy[rotation]:
        aaa = coord[0] + ax
        bbb = coord[1] + by
        eerect = pygame.Rect(aaa * blockSize, bbb * blockSize, blockSize, blockSize)
        pygame.draw.rect(screen, black, eerect)

#check if the tetrominoes can move down, left, or right depending on the key pressed
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
            if [xCoord, yCoord] in board['shapeCoords'] or [xCoord, yCoord] in board['bottomCoords'] or [xCoord, yCoord] in board['sideCoords']:
                upCollisions.extend('collision')
    return downCollisions, rightCollisions, leftCollisions, upCollisions

#get the absolute coords of the tetrominoes    
def GetAbsCoords(shapeCoords, x, y, rotation):
    absCoords = []
    for coord in shapeCoords[rotation]:
        absCoords.append([coord[0] + x, coord[1] + y])
    return absCoords

#clear a line and draw the board again
def clearLines(lineCoords, lineY):
    for coord in lineCoords:
        board['colours'].pop(board['shapeCoords'].index(coord))
        board['shapeCoords'].remove(coord)
    screen.fill(black)
    DrawBoard()
    lineY.sort(reverse=True)
    #move the tetrominoes down by 1 for every line cleared below it
    
    for clearedlines in range(len(lineY)):
        botLine = max(lineY)
        for coord in board['shapeCoords']:
            if coord[1] < botLine:
                coord[1] += 1
    lineY.remove(botLine)

    renderBoardAfterClear(board['shapeCoords'], board['colours'])

def DrawNextShape(shapeCoords, color):
    #draw a black rectangle to clear the next shape area
    rect = pygame.Rect(500, 0, 200, 200)
    pygame.draw.rect(screen, black, rect)
    blockSize = 30
    for coords in shapeCoords:
        x = coords[0] + 48/30 * 11
        y = coords[1] + 2
        rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
        pygame.draw.rect(screen, color, rect)
        

def initText():
    pygame.font.init()
    my_font = pygame.font.SysFont('Roboto', 40)
    text_surface = my_font.render('NEXT', True, (255, 255, 255))
    screen.blit(text_surface, (540,10))
    text = my_font.render('Score: ' + str(score), True, white)
    textRect = text.get_rect()
    textRect.center = (540, 50)
    screen.blit(text, textRect)


running = True
dropping = True
rotation = 0
beginShape = random.choice(allShapesCoordsREL)
clock = pygame.time.Clock()
board = {
    "shapeCoords": [],
    "colours": [],
    "rotations": [],
    "bottomCoords": [],
    "sideCoords": []
}
board['bottomCoords'] = [[0,20],[1,20],[2,20],[3,20],[4,20],[5,20],[6,20],[7,20],[8,20],[9,20]]
board['sideCoords'] = [[10,0],[10,1],[10,2],[10,3],[10, 4],[10,5],[10,6],[10,7],[10,8],[10,9],[10,10],[10,11],[10,12],[10,13],[10,14],[10,15],[10,16],[10,17],[10,18],[10,19]]



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

dictator = {
    'shapeCoords': allShapesCoordsREL,
    'colours': colours,
    'names': shapeNames,
}


def GetShapeSequence(inputy):
    aaaaa = list(zip(inputy['shapeCoords'], inputy['colours'], inputy['names']))
    random.shuffle(aaaaa)
    s, c, n = zip(*aaaaa)
    return s, c, n
dictator2 = dictator
dictator2['shapeCoords'],dictator2['colours'], dictator2['names'] = GetShapeSequence(dictator)
numero = 0
while running:

    currentShape = dictator2['shapeCoords'][numero]
    currentColour = dictator2['colours'][numero]
    currentName = dictator2['names'][numero]
    if numero < 6:
        numero += 1
    else:
        numero = 0
        dictator2['shapeCoords'],dictator2['colours'], dictator2['names'] = GetShapeSequence(dictator2)
        
    nextShape = dictator2['shapeCoords'][numero]
    nextColour = dictator2['colours'][numero]
    nextName = dictator2['names'][numero]

    


    DrawNextShape(nextShape[0], nextColour)
    
    y = 0
    x = 3
    tLast = 0
    bb = 0
    rotation = 0
    absCoords = GetAbsCoords(currentShape, x, y, rotation)
    RenderShape(absCoords, currentColour)
    dropping = True
    while dropping:
        dt = clock.tick(60)
        tLast += dt
        DrawBoard()
        pygame.display.update()
        ghostCoords = []
        underY = []
        for coord in ghostCoords:
            rect = pygame.Rect(coord[0] * blockSize, coord[1] * blockSize, blockSize, blockSize)
            pygame.draw.rect(screen, currentColour, rect)


        if tLast > 150:
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
                                    clearStreak = 0
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
                # if event.key == pygame.K_c:
                #     currentShape = shapeList[shapeNum + 1]
                #     currentColour = colours[0]
pygame.quit()