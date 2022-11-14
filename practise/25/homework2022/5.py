def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
         d |= {i, x // i}
    return sorted(d)

c = 0
for x in range(250_200, 300_000):
    if len(div(x)) == 0:
        continue
    S = min(div(x)) + max(div(x))
    if S % 123 == 17:
        print(x, S)
        c += 1
        if c == 5:
            break
    