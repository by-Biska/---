def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
         d |= {i, x // i}
    return sorted(d)

for x in range(1204300, 1204380):
    d = [i for i in div(x) if i % 2 == 0]
    if len(d) == 0:
        continue
    S = sum(d)
    if S % 10 == 0:
        print(x, S)
    