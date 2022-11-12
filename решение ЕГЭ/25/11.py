def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)
  
count = 0
for x in range(500001, 501000):
  d = [i for i in div(x) if i % 10 == 8 and i != 8]
  if len(d) == 0:
    continue
  print(x, min(d))
  count += 1
  if count == 5:
    break