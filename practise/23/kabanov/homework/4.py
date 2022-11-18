def f(c, end):
    if c < end:
        return 0
    if c == end:
        return 1
    if c > end:
        return f(c - 2, end) + f(c - 5, end)


print(f(23, 2))
