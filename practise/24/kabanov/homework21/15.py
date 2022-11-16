s = open('24 (12).txt').readline()

c = ''
m = "100000000000000000000000000000000000000"
for i in range(len(s)):
    if s[i] == 'D':
        c += s[i]
    elif c != '':
        m = min(c, m, key=len)
        c = ''
print(m, len(m))
