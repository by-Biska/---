def f(c, end):
    if c > end or c == 43:
        return 0
    if c == end:
        return 1
    if c < end:
        return f(c + 2, end) + f(c + c - 1, end) + f(c + c + 1, end)


print(f(7, 63))
