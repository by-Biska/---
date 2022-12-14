from fnmatch import fnmatch

def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)

for x in range(168,1000050,168):
    if fnmatch(str(x), '?8*8*?8'):
        print(x, sum(div(x)))