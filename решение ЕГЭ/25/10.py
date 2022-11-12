def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)

for i in range(333555, 777999 + 1):
  d = [i for i in div(i) if 10<=i<=99]
  if len(d) == 35:
    print(i, d[0], d[-1])