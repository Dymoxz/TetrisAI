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

shapes = [S, Z, I, O, J, L, T]
shapeNames = ['S', 'Z', 'I', 'O', 'J', 'L', 'T']
fullShapes = []
colours = [red, green, blue, yellow, pink, orange, purple]

def pprint(shape):
    for row in shape:
        print(row)
    print('')



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
    return allNew


# get all the data from the shapes
allShapesCoordsREL = initShapes(shapes)


def DrawBoard():
    global blockSize
    global boardColours
    for x in range(0, width, blockSize):
        for y in range(0, height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, gray, rect, 1)


def RenderShape(shapeCoords, color, startX, startY, rotation):
    blockSize = 48
    for coords in shapeCoords[rotation]:
        x = coords[0] + startX
        y = coords[1] + startY
        rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
        pygame.draw.rect(screen, color, rect)





running = True
dropping = True
rotation = 0
beginShape = random.choice(allShapesCoordsREL)
while running:
    # Get Current and next shape to spawn
    try:
        currentShape = nextShape
    except:
        currentShape = beginShape
    nextShape = random.choice(allShapesCoordsREL)
    currentColour = colours[allShapesCoordsREL.index(currentShape)]

    print(shapeNames[allShapesCoordsREL.index(currentShape)], shapeNames[allShapesCoordsREL.index(nextShape)])
    print(allShapesCoordsREL[allShapesCoordsREL.index(currentShape)][rotation])
    
    RenderShape(currentShape, currentColour, 0, 0, rotation)


    while dropping:
        DrawBoard()
        pygame.display.update()


        for event in pygame.event.get():
            pygame.key.set_repeat(200, 100)
            if event.type == pygame.QUIT:
                running = False
                dropping = False

pygame.quit()


# def GetInShapeCoords(shapes):
#     defaultShape = shapes[0]
#     allInShapeCoords = []
#     for shape in shapes:
#         inShapeCoords = []
#         dy = 0
#         for y in shape:
#             dx = 0
#             for x in y:
#                 if x == '0':
#                     inShapeCoords.append([dx, dy])
#                 dx +=1
#             if '0' in y:
#                 dy += 1
#         allInShapeCoords.append(inShapeCoords)

#     return allInShapeCoords


# def GetDimensions(shapeCoords):
#     allShapeDimensions = []

#     for coords in shapeCoords:
#         xList = []
#         yList = []
#         for coord in coords:
#                 xList.append(coord[0])
#                 yList.append(coord[1])

#         maX = max(xList)
#         miX = min(xList)

#         maY = max(yList)
#         miY = min(yList)

#         w = maX - miX + 1  
#         h = maY - miY + 1 

#         allShapeDimensions.append([w,h])
   
#         return allShapeDimensions

# def GetCollisionPoints(shapeCoords):
#     allbottoms = []
#     for shape in shapeCoords:
#         bottom = []
#         for coords in shape:
#             x = coords[0]
#             y = coords[1]
#             if [x, y+1] not in shape:
#                 bottom.append([x,y])
#         allbottoms.append(bottom)

#     allLefts = []
#     for shape in shapeCoords:
#         left = []
#         for coords in shape:
#             x = coords[0]
#             y = coords[1]
#             if [x-1, y] not in shape:
#                 left.append([x,y])
#         allLefts.append(bottom)

#     allRights = []
#     for shape in shapeCoords:
#         right = []
#         for coords in shape:
#             x = coords[0]
#             y = coords[1]
#             if [x+1, y] not in shape:
#                 right.append([x,y])
#         allRights.append(bottom)



#     return allbottoms, allLefts, allRights
                


# # rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
# # pygame.draw.rect(screen, currentColour, rect)    
# def RenderShape(shapeCoords, color, startX, startY, rotation):
#     blockSize = 48
#     for coords in shapeCoords[rotation]:
#         x = coords[0] + startX
#         y = coords[1] + startY
#         rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
#         pygame.draw.rect(screen, color, rect)

# def DrawBoard():
#     global blockSize
#     global boardColours
#     #grid
#     for x in range(0, width, blockSize):
#         for y in range(0, height, blockSize):
#             rect = pygame.Rect(x, y, blockSize, blockSize)
#             pygame.draw.rect(screen, gray, rect, 1)

# def DrawPlacedShapes(boardDict):
#     global blockSize
#     c = boardDict["shapeCoords"]
#     col = boardDict["colours"]
#     rot = boardDict["rotations"]
#     i = 0
#     for shape in c:
#         for coords in shape:
#             x = coords[0]
#             y = coords[1]
#             rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
#             pygame.draw.rect(screen, col[i], rect)
#         i +=  1


# def saveBlockState(board, absCoords, currentShape, rotation):
#     board["shapeCoords"].append(absCoords)
#     board["colours"].append(colours[shapes.index(currentShape)])
#     board["rotations"].append(rotation)

# def remLastPos(abycordy):
#     for coord in abycordy:
#         aaa = coord[0] 
#         bbb = coord[1]
#         rect = pygame.Rect(aaa * blockSize, bbb * blockSize, blockSize, blockSize)
#         pygame.draw.rect(screen, black, rect)


# def main():
#     running = True
#     dropping = True
#     clock = pygame.time.Clock()
#     tLast = 0
#     board = []
#     board = {
#         "shapeCoords": [],
#         "colours": [],
#         "rotations": []
#     }

#     gogogo = True
#     while running:
#         currentShape = random.choice(shapes)
#         rotation = 0
#         allInShapeCoords = GetInShapeCoords(currentShape)
#         dimensionList = GetDimensions(allInShapeCoords)
#         w, h = dimensionList[rotation]
#         x = 3
#         y = 0
#         tLast = 0
#         absCoords = []

#         DrawPlacedShapes(board)
#         while dropping:
#             absCoords = []
#             absColPoints = {
#                 "bottoms": [],
#                 "lefts": [],
#                 "rights": []
#             }
#             for coord in allInShapeCoords[rotation]:
#                 absCoords.append([coord[0] + x, coord[1] + y])
#             dt = clock.tick()
#             tLast += dt
#            # screen.fill(black)
#             RenderShape(allInShapeCoords, colours[shapes.index(currentShape)], x, y, rotation)
#             DrawBoard()
#             # DrawPlacedShapes(board)
#             BottomCollision, LeftCollision, RightCollision  = GetCollisionPoints(allInShapeCoords)
#             BottomCollision = BottomCollision[rotation]
#             LeftCollision = LeftCollision[rotation]
#             RightCollision = RightCollision[rotation]

#             BOTcollisions = []
#             RIGHTCollisions = []
#             LEFTCollisions = []

#             if tLast > 100:
#                 remLastPos(absCoords)
#                 y += 1
#                 tLast = 0  
#             # detect events
#             for event in pygame.event.get():
#                 pygame.key.set_repeat(200, 100)
#                 if event.type == pygame.QUIT:
#                     running = False
#                     dropping = False
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_RIGHT:
#                         pass
#                     if event.key == pygame.K_LEFT:
#                         pass
#                     if event.key == pygame.K_DOWN:
#                         pass
                    

# main()
