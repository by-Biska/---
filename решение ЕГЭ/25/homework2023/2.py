from fnmatch import *

for x in range(141, 10**8,141):
    if fnmatch(str(x), '1234*7'):
        print(x, x//141)