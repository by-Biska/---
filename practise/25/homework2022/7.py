def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
         d |= {i, x // i}
    return sorted(d)

c = 0
for x in range(400_000_000, 500_000_000):
    d = div(x)
    if len(d) < 5:
        continue
    P = d[0]*d[1]*d[2]*d[3]*d[4]
    if P % 100 == 17 and P < x:
        print(P, d[4])
        c += 1
        if c == 5:
            break
    