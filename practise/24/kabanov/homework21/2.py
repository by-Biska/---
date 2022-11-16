s = open("24.txt").readline()

c = m = ''

for i in range(len(s)):
    if s[i] != "C" and s[i] != 'D':
        c += s[i]
        m = max(c, m, key=len)
    else:
        c = ''

print(m, len(m))