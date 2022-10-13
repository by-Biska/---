from functools import lru_cache

@lru_cache()
def F(n):
  print(3*n)
  if n>1:
    print(n-2)
    F(n-1)
    F(n-2)
def f(n):
  if n<=1:
    return 3*n
  else:
    return 3*n + n - 2 + f(n-1) + f(n-2)
for n in range(1, 1000):
  print(n, f(n))
  if f(n) > 450000:
    print(n)
    break