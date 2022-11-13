def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)
  
def prime(x):
  return x>1 and all(x%i != 0 for i in range(2, int(x** 0.5) + 1))

count = 0
for x in range(450_000, 456_000):
  d = [i for i in div(x) if not(prime(i))]
  if len(d) == 0:
    continue
  print(x, d[-1])  
  count += 1
  if count == 5:
    break