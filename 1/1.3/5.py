def mod(a, b):
    return a % b


def f(n):
    if n == 0:
      return 1
    elif n > 0 and mod(n, 5) == 0:
      return n // 5 + f(n // 5)
    elif n > 0 and mod(n, 5) > 0:
      return mod(n, 5) + f(n-1)

for n in range(0, 10000000):
  print(n, f(n))
  if f(n) == 2021:
    print(n)
    break