from fnmatch import *

for x in range(17, 10**9, 17):
    if fnmatch(str(x), '23?456?89'):
        print(x, x//17)