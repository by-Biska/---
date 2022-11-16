s = open("24 (3).txt").readline()

c = m = ''

for i in s:
    if i != 'A' and i != 'B' and i != 'C':
        c += i
        m = max(c, m, key=len)
    else:
        c = ''
print(m, len(m))
