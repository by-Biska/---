def f(c, end):
    if c > end or c == 6:
        return 0
    if c == end:
        return 1
    if c < end:
        return f(c + 2, end) + f(c * 3, end)


print(f(1, 25) * f(25, 63))