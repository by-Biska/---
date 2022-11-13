from fnmatch import fnmatch

def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)

for x in range(217, 10**7+1, 217):
    if fnmatch(str(x), '14?4*'):
        d = [i for i in div(x) if i % 2 == 1]
        if len(d) == 0:
            continue
        print(x, sum(d))