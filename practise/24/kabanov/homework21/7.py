s = open("24 (5).txt").readline()

c = m = s[0]

for i in range(1, len(s)):
    if s[i-1] + s[i] != "XY" and s[i-1] + s[i] != "XZ":
        c += s[i]
        m = max(c,m,key=len)
    else:
        c = s[i]

print(m, len(m))