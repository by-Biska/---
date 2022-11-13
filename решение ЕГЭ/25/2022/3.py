def div(n):
    d = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            d |= {i, n // i}
    return sorted(d)


for i in range(244143, 367822):
    if int(i ** 0.5) ** 2 == i:
        if len(div(i)) == 5:
            print(div(i)[-2], div(i)[-1])
