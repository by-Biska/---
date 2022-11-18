def f(c, end):
    if c > end:
        return 0
    if c == end:
        return 1
    if c < end and c%10 != 9:
        return f(c + 1, end) + f(c + 11, end)
    if c < end and c%10 == 9:
		    return f(c + 1, end) + f(c + 10, end)

print(f(25, 51))