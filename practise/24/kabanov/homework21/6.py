s = open("24 (4).txt").readline()

c = m = ''

for i in range(len(s)):
    if s[i].isdigit():
        c += s[i]
        m = max(c, m, key=len)
    else:
        c = ''
print(m, len(m))
