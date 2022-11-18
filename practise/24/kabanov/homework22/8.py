from fnmatch import fnmatch

k = 0
s = open("24 (6).txt").readline()

for i in range(len(s) - 4):
    if fnmatch(s[i : i + 5], "A?A?A"):
        k += 1
print(k)
