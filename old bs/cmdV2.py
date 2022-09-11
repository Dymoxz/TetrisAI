import random
import time
import os
import msvcrt

Board = list(['.'*10]*20 + ['-'*10])
BoardBackup = list(['.'*10]*20 + ['-'*10])

# The shapes and their rotations--
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
# ------------------------- #


# Definitions
def getShapeCoords(shape, rot):
    y = 0
    allShapeCoords = []
    for row in shape[rot]:
        x = 0
        for block in row:
            if block == '0':
                allShapeCoords.append([x, y])
            x += 1
        if '0' in row:
            y += 1
    return allShapeCoords

def GetAbsCoords(coords, dx, dy):
    absCoords = []
    for coord in coords:
        absX = coord[0] + dx
        absY = coord[1] + dy
        absCoords.append([absX, absY])
    return absCoords
def placeShape(coords, locBoard, dy):
    for coord in coords:
        string = locBoard[coord[1] + dy] 
        string = string[:coord[0]] + '0' + string[coord[0]+1:]
        locBoard[coord[1] + dy] = string
        # return string, locBoard[coord[1]]


def removeShape(coords, locBoard, dy):
    for coord in coords:
        string = locBoard[coord[1] + dy - 1] 
        string = string[:coord[0]] + '.' + string[coord[0]+1:]
        locBoard[coord[1] + dy - 1] = string
        # return string, locBoard[coord[1]]


def GetShapeDimensions(coords):
    xList = []
    yList = []
    for i in coords:
        xList.append(i[0])
        yList.append(i[1])        
    maxX = max(xList)
    minX = min(xList)
    maxY = max(yList)
    minY = min(yList)   
    height = maxY - minY + 1
    width = maxX - minX + 1
    yBotList = []
    for i in coords:
        if i[1] == maxY:
            yBotList.append(i)


    return width, height, yBotList

def getKeyInput():
    if msvcrt.kbhit():
        key = ord(msvcrt.getch())
        if key == 224:
            # If the key is a special key
            key = ord(msvcrt.getch())
            if key == 80:
                return 'down'
            elif key == 72:
                return 'up'
            elif key == 75:
                return 'left'
            elif key == 77:
                return 'right'
            elif key == 83:
                return 'down'
            else:
                return 'else'
        else:
            return 'else'



y = 0
while True:
    curShapeCoords = getShapeCoords(random.choice(shapes), 0)
    print(curShapeCoords)   

    width, height, yBotList = GetShapeDimensions(curShapeCoords)
    print(width, height)
    collisionDetections = ['']
    
    while True:
        if getKeyInput() == 'down':
            y += 1
            placeShape(curShapeCoords, Board, y)
            for rows in Board:
                print(f'  {rows}  ')
        Board[-1] = '-'*10
        # os.system('cls')
        placeShape(curShapeCoords, Board, y)
        for rows in Board:
            print(f'  {rows}  ')
        absCoords = GetAbsCoords(curShapeCoords, 0, y)
        time.sleep(0.3) 
        collisionDetections = ['']

        absBottom = GetAbsCoords(yBotList, 0, y)

        for i in absBottom:
            if Board[i[1] + 1][i[0]] == '0':
                collisionDetections.append(f'COLLISION AT {i}')
            if Board[i[1] + 1][i[0]] == '-':
                collisionDetections.append(f'VLOER AT {i}')

        print(collisionDetections, '------------')
        if len(collisionDetections) != 1:
            collisionDetections = ['']
            break
        else:
            y += 0
        removeShape(curShapeCoords, Board, y)
    y = 0