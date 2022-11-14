from fnmatch import fnmatch

def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)

for x in range(65000,1000000):
    if fnmatch(str(x), '6*97*5?'):
        d = [i for i in div(x) if i % 2 == 0]
        if len(d) < 4:
            continue
        print(x, sum(d))