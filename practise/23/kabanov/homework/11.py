def f(c, end):
    if c > end or c == 11 or c == 18:
        return 0
    if c == end:
        return 1
    if c < end:
        return f(c + 1, end) + f(c + 2, end) + f(c * 3, end)


print(f(4, 8) * f(8, 23))