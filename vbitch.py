# a =['.....',
#       '.0...',
#       '.000.',
#       '.....',
#       '.....']
# b = list(reversed(a))
# rI = 0
# for row in b:
#     b[rI] = row[::-1]
#     rI += 1
# print(b)


#[[0,0],[1,0],[0,1],[1,1]]


# a =['.....',
#       '.0...',
#       '.000.',
#       '.....',
#       '.....']
# blockcoords = []
# y = 0
# for row in a:
#     x = 0
#     for gridbox in row:
#         if gridbox == "0":
#             blockcoords.append([x,y])
#         x += 1
#     y += 1

# print(blockcoords)


# c1 =[[0, 1], [1, 1], [2, 1], [3, 1]]
# c2 = [[2, 1], [2, 2], [2, 3], [3, 3]]

# xList = []

# for i in c1:
#     xList.append(i[0])

# max = max(xList)
# min = min(xList)
# shapeWidth = max - min + 1
# print(shapeWidth)


# def getCoords(shape):
#     print(shape)
#     widthList = []
#     for y in shape:
#         xList = []
#         for i in y:
#             xList.append(i[0])
#         print(xList)
#         maxi = max(xList)
#         mini = min(xList)
#         shapeWidth = maxi - mini + 1
#         widthList.append(shapeWidth)
#     heightList = []
#     for y in shape:
#         yList = []
#         for i in y:
#             yList.append(i[1])
#         maxi1 = max(yList)
#         mini2 = min(yList)
#         shapeHeight = maxi1 - mini2 + 1
#         heightList.append(shapeHeight)
#     return widthList, heightList
# S = [['.....',
#       '......',
#       '..00..',
#       '.00...',
#       '.....'],
#      ['.....',
#       '..0..',
#       '..00.',
#       '...0.',
#       '.....']]

# # getCoords(S)

# xList = []

# for i in S[0]:
#     xList.append(i[0])
# maxi = max(xList)
# mini = min(xList)
    
# print(maxi, mini)


# Board = [
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]



import getch
def get_key():
    first_char = getch.getch()
    if first_char == '\x1b':
        return {'[A': 'up', '[B': 'down', '[C': 'right', '[D': 'left'}[getch.getch() + getch.getch()]
    else:
        return first_char


key = ''
while key != 'q':
    key = get_key()
    print(key)