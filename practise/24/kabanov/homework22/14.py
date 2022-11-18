s = open("24 (12).txt").readline()
k = 0

for i in range(len(s) - 4):
    if s[i : i + 5] == s[i + 4] + s[i + 3] + s[i + 2] + s[i + 1] + s[i]:
        k += 1
print(k)
