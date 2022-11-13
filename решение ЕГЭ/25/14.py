def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)
  
def prime(x):
  return x>1 and all(x%i != 0 for i in range(2, int(x** 0.5) + 1))

ans = []
for x in range(158928, 345294):
  d = [i for i in div(x) if prime(i)]
  if len(d) == 3 and d[0] * d[1] * d[2] == x:
    ans.append(x)
print(len(ans), min(ans))