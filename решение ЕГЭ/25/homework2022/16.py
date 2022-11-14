def div(x):
    d = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
         d |= {i, x // i}
    return sorted(d)

def p(x):
    return x>1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))

for x in range(125697, 125721+1):
    d = [i for i in div(x) if p(i)]
    if len(d) == 2 and d[0]*d[1]==x:
        print(d[0], d[1], d[0]*d[1])