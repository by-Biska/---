def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
         d |= {i, x // i}
    return sorted(d)

c = 0
for x in range(550_000, 700_000):
    if len(div(x)) == 0:
        continue
    F = int(sum(div(x)) / len(div(x)))
    if F % 31 == 13:
        print(x, F)
        c += 1
        if c == 5:
            break
    