from functools import lru_cache

@lru_cache()
def F(n):
    print("*")
    if n >= 1:
      print("*")
      F(n - 1)
      F(n - 2)
      print("*")


def f(n):
    if n < 1:
        return 1
    else:
        return 1 + 1 + f(n -1) + f(n - 2) + 1

print(f(35))