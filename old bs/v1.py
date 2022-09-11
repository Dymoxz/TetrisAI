import sys, pygame
import time
pygame.init()

size = width, height = 380, 760
speed = [2, 2]
black = 0, 0, 0
white = 80,80,80
red = 255, 0, 0

screen = pygame.display.set_mode(size)

def drawGrid():
    blockSize = 38 #Set the size of the grid block
    for x in range(0, width, blockSize):
        for y in range(0, height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, white, rect, 1)

def reversePiece(piece):
    b = list(reversed(piece))
    rI = 0
    for row in b:
        b[rI] = row[::-1]
        rI += 1
    return b

sel = 0
S = [[".....",
      "......",
      "..00..",
      ".00...",
      "....."],
     [".....",
      "..0..",
      "..00.",
      "...0.",
      "....."]]



def drawPiece(color, startY, startX):
    global sel
    global S
    blockSize = 38 #Set the size of the grid block
    #rect = pygame.Rect(190-(width/2), 0, blockSize, blockSize)
    piececoords = []
    try:
        spawnpiece = S[sel]
    except:
        if sel == 2:
            spawnpiece = reversePiece(S[0])
        elif sel == 3:
            spawnpiece = reversePiece(S[1])
        else:
            sel = 0
            spawnpiece = S[sel]
    y = startY
    for row in spawnpiece:
        x = startX
        for gridbox in row:
            xPos = x * 38
            yPos = y * 38
            if gridbox == "0":
                piececoords = [x,y]
                rect = pygame.Rect(xPos, yPos, blockSize, blockSize)
                pygame.draw.rect(screen, color, rect, 0)
            x += 1
        if '0' in row:
            y += 1
    print(piececoords)
q =0 
p = 3
time_elapsed_since_last_action = 0
clock = pygame.time.Clock()
while 1:
    screen.fill(black)
    drawGrid()

    dt = clock.tick() 

    time_elapsed_since_last_action += dt
    drawPiece(red, q, p)



    if time_elapsed_since_last_action > 1200:
        if q < 19:
            q += 1
        time_elapsed_since_last_action = 0


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if q < 19:
                    q += 1
            if event.key == pygame.K_LEFT:
                if p > 0:
                    p -= 1
            if event.key == pygame.K_RIGHT:
                if p < 9:
                    p += 1
            if event.key == pygame.K_UP:
                sel += 1
                drawPiece(red, q, p)
        if event.type == pygame.QUIT: sys.exit()
    pygame.display.flip()

