for x in range(1000):
    s = 125 ** 10 + 25 ** 2 - x
    k = 0
    while s:
        if s % 5 == 4:
            k += 1
        s //= 5
    if k == 27:
        print(x)
        break
