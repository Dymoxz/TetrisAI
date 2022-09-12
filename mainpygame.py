import collections
from compileall import compile_path
from distutils.util import Mixin2to3
from tarfile import BLOCKSIZE
import pygame
import random

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
shapes = [S, Z, I, O, J, L, T]
colours = [red, green, blue, yellow, pink, orange, purple]

def GetInShapeCoords(shapes):
    defaultShape = shapes[0]
    allInShapeCoords = []
    for shape in shapes:
        inShapeCoords = []
        dy = 0
        for y in shape:
            dx = 0
            for x in y:
                if x == '0':
                    inShapeCoords.append([dx, dy])
                dx +=1
            if '0' in y:
                dy += 1
        allInShapeCoords.append(inShapeCoords)

    return allInShapeCoords


def GetDimensions(shapeCoords):
    allShapeDimensions = []

    for coords in shapeCoords:
        xList = []
        yList = []
        for coord in coords:
                xList.append(coord[0])
                yList.append(coord[1])

        maX = max(xList)
        miX = min(xList)

        maY = max(yList)
        miY = min(yList)

        w = maX - miX + 1  
        h = maY - miY + 1 

        allShapeDimensions.append([w,h])
   
        return allShapeDimensions

def GetCollisionPoints(shapeCoords):
    allbottoms = []
    for shape in shapeCoords:
        bottom = []
        for coords in shape:
            x = coords[0]
            y = coords[1]
            if [x, y+1] not in shape:
                bottom.append([x,y])
        allbottoms.append(bottom)

    allLefts = []
    for shape in shapeCoords:
        left = []
        for coords in shape:
            x = coords[0]
            y = coords[1]
            if [x-1, y] not in shape:
                left.append([x,y])
        allLefts.append(bottom)

    allRights = []
    for shape in shapeCoords:
        right = []
        for coords in shape:
            x = coords[0]
            y = coords[1]
            if [x+1, y] not in shape:
                right.append([x,y])
        allRights.append(bottom)



    return allbottoms, allLefts, allRights
                


# rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
# pygame.draw.rect(screen, currentColour, rect)    
def RenderShape(shapeCoords, color, startX, startY, rotation):
    blockSize = 48
    for coords in shapeCoords[rotation]:
        x = coords[0] + startX
        y = coords[1] + startY
        rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
        pygame.draw.rect(screen, color, rect)

def DrawBoard():
    global blockSize
    global boardColours
    #grid
    for x in range(0, width, blockSize):
        for y in range(0, height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, gray, rect, 1)

def DrawPlacedShapes(boardDict):
    global blockSize
    c = boardDict["shapeCoords"]
    col = boardDict["colours"]
    rot = boardDict["rotations"]
    i = 0
    for shape in c:
        for coords in shape:
            x = coords[0]
            y = coords[1]
            rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            pygame.draw.rect(screen, col[i], rect)
        i +=  1


def saveBlockState(board, absCoords, currentShape, rotation):
    board["shapeCoords"].append(absCoords)
    board["colours"].append(colours[shapes.index(currentShape)])
    board["rotations"].append(rotation)

def main():
    running = True
    dropping = True
    clock = pygame.time.Clock()
    tLast = 0
    board = []
    board = {
        "shapeCoords": [],
        "colours": [],
        "rotations": []
    }


    gogogo = True
    while running:
        currentShape = random.choice(shapes)
        rotation = 0
        allInShapeCoords = GetInShapeCoords(currentShape)
        dimensionList = GetDimensions(allInShapeCoords)
        w, h = dimensionList[rotation]
        x = 3
        y = 0
        tLast = 0
        absCoords = []
        while dropping:
            # for bottom in bottoms:



            absCoords = []
            absColPoints = {
                "bottoms": [],
                "lefts": [],
                "rights": []
            }
            for coord in allInShapeCoords[rotation]:
                absCoords.append([coord[0] + x, coord[1] + y])
            dt = clock.tick()
            tLast += dt
            screen.fill(black)
            RenderShape(allInShapeCoords, colours[shapes.index(currentShape)], x, y, rotation)
            DrawBoard()
            DrawPlacedShapes(board)
            BottomCollision, LeftCollision, RightCollision  = GetCollisionPoints(allInShapeCoords)
            BottomCollision = BottomCollision[rotation]
            LeftCollision = LeftCollision[rotation]
            RightCollision = RightCollision[rotation]

            BOTcollisions = []
            RIGHTCollisions = []
            LEFTCollisions = []
            if tLast > 500:
                if y + h < height / blockSize:
                    for coord in BottomCollision:
                        absX = coord[0] + x
                        absY = coord[1] + y
                        absColPoints['bottoms'].append([absX, absY + 1])
                        absColPoints['lefts'].append([absX, absY])
                        absColPoints['rights'].append([absX, absY])
                    for direction in absColPoints:
                        for point in absColPoints[direction]:
                            
                            if point in board["shapeCoords"]:
                                BOTcollisions.append(direction)
                                break
                            for shape in board["shapeCoords"]:
                                if point in shape:
                                    BOTcollisions.append('x')

                    if len(BOTcollisions) == 0:
                        y += 1
                    else:
                        saveBlockState(board, absCoords, currentShape, rotation)
                        break
                else:                    
                    saveBlockState(board, absCoords, currentShape, rotation)
                    break
                tLast = 0  
            # detect events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    dropping = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if x + w  + 1 < width / blockSize:
                            for coord in BottomCollision:
                                absX = coord[0] + x
                                absY = coord[1] + y
                                absColPoints['bottoms'].append([absX, absY + 1])
                                absColPoints['lefts'].append([absX, absY])
                                absColPoints['rights'].append([absX, absY])
                            for direction in absColPoints:
                                for point in absColPoints[direction]:
                                    if point in board["shapeCoords"]:
                                        RIGHTCollisions.append(direction)
                                        break
                                    for shape in board["shapeCoords"]:
                                        if point in shape:
                                            RIGHTCollisions.append('x')

                            if len(RIGHTCollisions) == 0:
                                x += 1
                            else:
                                saveBlockState(board, absCoords, currentShape, rotation)
                                break
                    if event.key == pygame.K_LEFT:
                        if x  >= 0:
                            x -= 1
            pygame.display.update()
    pygame.quit()
main()
