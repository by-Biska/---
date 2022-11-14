def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)


count = 0
for i in range(850001, 850100):
    if div(i) == []:
        continue
    F = max(div(i)) - min(div(i))
    if F != 0 and F % 3 == 0:
        print(i, F)
        count += 1
        if count == 6:
            break
