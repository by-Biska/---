from fnmatch import fnmatch


def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)


for x in range(1, 10 ** 7 + 1):
    if fnmatch(str(x), '3*52') and len(div(x)) % 2 != 0:
        print(x, max(div(x)))
