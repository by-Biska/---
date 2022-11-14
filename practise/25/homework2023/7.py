from fnmatch import fnmatch

def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)

for x in range(1, 10**7+1):
    if fnmatch(str(x), '9?*55*7'):
        if len(div(x)) == 0:
            continue
        print(x, sum(div(x))%21)