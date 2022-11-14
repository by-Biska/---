from fnmatch import *
for x in range(206, 10**8+1, 206):
    if fnmatch(str(x), '123*[13579][02468]56'):
        print(x, x//206)