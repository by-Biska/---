def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
         d |= {i, x // i}
    return sorted(d)

c = 0
for x in range(150_000, 200_000):
    S = sum(div(x))
    if S % 13 == 10:
        print(x, S)
        c += 1
        if c == 7:
            break
    