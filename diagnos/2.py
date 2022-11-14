for x in range(10000):
    n = x
    if n % 6 == 0:
        n //= 3
    else:
        n -= 1
    if n % 5 == 0:
        n //= 5
    else:
        n -= 1
    if n % 3 == 0:
        n //= 3
    else:
        n -= 1
    if n == 4:
        print(x)
