s = open("../24.txt").readline()

c = m = ''

for i in s:
    if i == 'C':
        c += i
        m = max(c, m, key=len)
    else:
        c = ''
print(m, len(m))
