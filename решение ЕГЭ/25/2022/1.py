def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)


for i in range(193136, 193224):
    if len(div(i)) == 6:
        print(i)
        print("\t")
        print(div(i))
        print("\n")
