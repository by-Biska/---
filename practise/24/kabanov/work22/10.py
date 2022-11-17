s = open("24.txt").readline().strip()
d = {x: 0 for x in sorted(set(s))}
for i in range(len(s) - 1):
    if s[i] == "A":
        d[s[i + 1]] += 1

m = 0
c = ""
for x in d:
    if d[x] > m:
        m = d[x]
        c = x
print(c, m)
