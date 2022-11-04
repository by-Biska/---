for x in range(10001):
    s = 343 ** 8 + 49 ** 2 - x
    k = 0
    while s:
        if s % 7 == 0:
            k += 1
        s //= 7
    if k == 21:
        print(x)
