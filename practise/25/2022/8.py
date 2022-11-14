from multiprocessing import Pool

def f(x):
  x1 =x
  while x%2 == 0: x //= 2
  sq = int(x** 0.5)
  if sq**2 != x: return None
  d = set()
  for i in range(1, sq+1):
    if x % i == 0:
      d |= {i, x // i}
  d = [k for k in d if k % 2 != 0]
  if len(d) == 5:
    return [x1, max(d)]

if __name__ == '__main__':
  pool = Pool()
  result = pool.map(f, range(63_000_000, 75_000_001))
  result = [k for k in result if k!=None]
  for r in result:
    print(*r)