for x1 in "0123456789":
    for x2 in "0123456789":
        a = int(f'23{x1}456{x2}89')
        if a % 17 == 0:
            print(a, a//17)