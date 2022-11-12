def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)


for i in range(81234, 134690):
    if len(div(i)) == 3:
        print(div(i)[0], div(i)[-1])
