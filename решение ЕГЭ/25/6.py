import numpy


def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)


count = 0
for i in range(1_500_001, 1_601_000):
    d = div(i)
    if len(d) == 0:
        continue

    F = sum(d) // len(d)
    

    if str(F)[-1] == "9":
        print(i, F)
        count += 1
        if count == 5:
            break
