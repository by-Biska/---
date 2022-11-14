def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
         d |= {i, x // i}
    return sorted(d)

c = 0
for x in range(300_000, 1204380):
    d = [i for i in div(x) if i % 3 == 0]
    if len(d) == 5:
        print(x, d[-1])
        c += 1
        if c == 4:
            break
        