def f(c, end):
    if c > end:
        return 0
    if c == end:
        return 1
    if c < end:
        return f(c + 1, end) + f(c * 2, end) + f(c * 2 + 1, end) + f(c * 10, end)


print(f(1, 15))
