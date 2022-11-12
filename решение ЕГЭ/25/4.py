def div(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d |= {i, n // i}
    return sorted(d)


for i in range(135790, 163229):
    if sum(div(i)) > 460000:
        print(len(div(i)), sum(div(i)))
