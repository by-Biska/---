def f(c, end):
    if c > end:
        return 0
    if c == end:
        return 1
    if c < end and c % 2 == 0:
        return f(c + 1, end) + f(c * 1.5, end)
    if c < end and c % 2 == 1:
        return f(c + 1, end)

print(f(1, 20))