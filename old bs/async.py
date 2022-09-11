import msvcrt

num = 0
done = False
while not done:
    print(num)
    num += 1

    if msvcrt.kbhit():
        key = ord(msvcrt.getch())
        if key == 224:
            key = ord(msvcrt.getch())
            if key == 80:
                done = True
                print('down')
                break
            elif key == 72:
                done = True
                print('up')
            elif key == 75:
                done = True
                print('left')
            elif key == 77:
                done = True
                print('right')
            elif key == 83:
                done = True
                print('down')
            else:
                print('else')
                break


b'\xe0'