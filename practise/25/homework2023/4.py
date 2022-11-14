from fnmatch import fnmatch

for x in range(51,10**6,51):
    if fnmatch(str(x), '12*45*'):
        print(x, x//51)