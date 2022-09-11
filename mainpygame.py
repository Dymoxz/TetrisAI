from compileall import compile_path
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
# rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
# pygame.draw.rect(screen, currentColour, rect)    
def RenderShape(shapeCoords, color, startX, startY, rotation):
    blockSize = 48
    for coords in shapeCoords[rotation]:
        x = coords[0] + startX
        y = coords[1] + startY
        rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
        pygame.draw.rect(screen, color, rect)


def DrawBoard(placedShapes, usedColours, h, rot, cShape):
    global blockSize
    global boardColours
    #grid
    for x in range(0, width, blockSize):
        for y in range(0, height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, gray, rect, 1)
    

    print('----')
    print(f'placedShapes {placedShapes}')
    print(f'usedcolours {usedColours}')
    print(f'rotation {rot}')  
    for shape in placedShapes:
        for coords in shape:
            x = coords[0]
            y = coords[1] - h
            print('yyyyyyyyy', y)
            erect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            try:
                pygame.draw.rect(screen, usedColours[shapes.index(cShape)], erect)
            except:
                pass

    


def main():
    running = True
    dropping = True
    clock = pygame.time.Clock()
    tLast = 0
    board = []
    boardColours = []
    dimensionList = []
    boardRotations = []
    while running:
        currentShape = random.choice(shapes)
        rotation = 0
        allInShapeCoords = GetInShapeCoords(currentShape)
        dimensionList = GetDimensions(allInShapeCoords)
        w, h = dimensionList[rotation]
        x = random.randrange(0, 10 - w)
        y = 0
        for inShapeCoords in allInShapeCoords:
                print(inShapeCoords)
        absCoords = []
        while dropping:
            dt = clock.tick()
            tLast += dt
            screen.fill(black)
            RenderShape(allInShapeCoords, colours[shapes.index(currentShape)], x, y, rotation)
            DrawBoard(board, boardColours, h, boardRotations, currentShape)
            # print(y)
            # print(inShapeCoords)
            if tLast > 100:
                if y + h < height / blockSize:
                    y += 1
                else:

                    for coord in inShapeCoords:
                        x = coord[0] + x
                        y = coord[1] + y
                        absCoords.append([x, y])
                    board.append(absCoords)
                    boardColours.append(colours[shapes.index(currentShape)])
                    boardRotations.append(rotation)
                    break
                    y = 0
                tLast = 0  
            # detect events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    dropping = False

            pygame.display.update()
    pygame.quit()
main()
