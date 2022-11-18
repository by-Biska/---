def f(c, end):
    if c > end:
        return 0
    if c == end:
        return 1
    if c < end:
        return f(c + 1, end) + f(c * 2, end)


print(f(1, 12) * f(12,30))