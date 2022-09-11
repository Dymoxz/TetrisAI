
import random
import time
import os
import sys
#The board
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

#The board used to save the last state since a piece has been placed
BoardBackup = [
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
# ------------------------- #

#create a piece with a random shape
def createSpawnShape(shapeee):
    shape =shapeee
    defaultShape = shape[1]
    ynum = 0
    relCoords = []
    for y in defaultShape:
        xnum = 0
        for x in y:
            if x == '0':
                #the relative postions of the piece
                relX = xnum
                relY = ynum
                relCoord = [relX, relY]
                relCoords.append(relCoord)
            xnum += 1
        if '0' in y:
            ynum += 1
    #print(relCoords)
    return shape, defaultShape, relCoords

#spawn the piece at the top of the board
def spawnShape(relCoords):
    for i in relCoords:
        y = i[1]
        x = i[0]
        Board[y][x] = '0'
    return Board

#
def moveShape(xIn, yIn, bord):
    for i in relCoords:
        y = i[1]
        x = i[0]
        if not y+yIn-1 <0:
            bord[y+yIn-1][x] = '.'
    for i in relCoords:
        y = i[1]
        x = i[0]
        bord[y+yIn][x] = '0'
    # print(b)




allBoardStates = []
prevBoard = BoardBackup
#-------------------------#


#main game loop
while True:
    shape,defaultShape,relCoords = createSpawnShape(shapes[5])
    Board = spawnShape(relCoords)

    b = 0
    a = 0
    absCoords = []
    while True:
        underList = []
        absCoords = []
        xList = []
        yList = []
        for i in relCoords:
            xList.append(i[0])
            yList.append(i[1])        
        maxX = max(xList)
        minX = min(xList)
        maxY = max(yList)
        minY = min(yList)   
        height = maxY - minY + 1
        width = maxX - minX + 1

        print('H:W =', height, width )


        for coord in relCoords:
            absXCoord = coord[0]+b
            absYCoord = coord[1]+a
            absCoords.append([absXCoord, absYCoord])
        for y in Board:
            print(' '.join(y))
        time.sleep(0.2)
        print('\n'*10)
        os.system('cls')
        print(relCoords)
        print(absCoords)
        #bottom of the board
        if a <= 20 - height:
            for l in absCoords:
                try:
                    under = prevBoard[l[1] + 1][l[0]]
                    underList.append(under)
                    print(under)
                except:
                    pass
            moveShape(b , a, Board)
            if '0' not in underList:    
                a += 1
            else:
                break
        elif a == 21 - height:
            allBoardStates.append(Board)
            prevBoard = allBoardStates[-1]
            print('-----------------------', prevBoard)
            # print(prevBoard.index(['.', '.', '0', '0', '.', '.', '.', '.', '.', '.']))
            # Board = BoardBackup
            break