from fnmatch import fnmatch

for x in range(51, 10**6+1, 51):
    if fnmatch(str(x), '56*98*'):
        print(x, x//51)