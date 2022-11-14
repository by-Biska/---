def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
         d |= {i, x // i}
    return sorted(d)

c = 0
for x in range(550_000, 1204380):
    d = [i for i in div(x) if i % 10 == 7]
    if len(d) == 3:
        print(x, d[-1])
        c += 1
        if c == 5:
            break
        