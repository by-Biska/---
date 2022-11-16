s = open('24 (1).txt').readline()
c = m = ''

for i in range(len(s)):
    if s[i] in 'ACDF':
        c += s[i]
        m = max(c, m, key=len)
    else:
        c = ''
print(m, len(m))
