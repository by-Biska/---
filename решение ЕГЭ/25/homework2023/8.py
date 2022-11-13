from fnmatch import fnmatch

def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)

count = 0
for x in range(168, 1000000, 168):
    if fnmatch(str(x), '?6*6*?6'):
        d =div(x)
        if len(d) == 0:
            continue
        print(x, sum(d))
        count += 1
        if count ==7:
            break