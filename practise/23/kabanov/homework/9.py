def f(c, end):
    if c < end:
        return 0
    if c == end:
        return 1
    if c > end:
        return f(c - 8, end) + f(c // 2, end)

print(f(102, 43) * f(43, 5))