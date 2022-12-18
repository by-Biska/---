from functools import lru_cache
import sys
sys.setrecursionlimit(10_000)

# @lru_cache(None)
def f(n):
    if n>=10000: return n
    if n<10000 and n%2==0: return f(n+2)-3
    if n<10000 and n%2!=0: return f(n+2)+1

# for n in range(1,100000):
#     f(n)

print(f(94)-f(80))