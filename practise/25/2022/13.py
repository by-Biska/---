def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)
  
def prime(x):
  return x>1 and all(x%i != 0 for i in range(2, int(x** 0.5) + 1))

for x in range(650_000, 660_000):
  d = [i for i in div(x) if prime(i)]
  S = sum(d)
  if S % 100 == 25:
    print(x, S)
  