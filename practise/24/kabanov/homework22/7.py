from fnmatch import fnmatch

k = 0
s = open("24 (6).txt").readline()

for i in range(len(s) - 3):
    if fnmatch(s[i : i + 4], "G?ME"):
        k += 1
print(k)
