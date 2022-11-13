from fnmatch import fnmatch

for x in range(169, 10**9, 169):
    if fnmatch(str(x), '345*789?'):
        print(x, x//169)