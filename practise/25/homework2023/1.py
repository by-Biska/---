from fnmatch import fnmatch

for x in range(17, 10**9+1, 17):
    if fnmatch(str(x), '12345?6?8'):
        print(x, x//17)