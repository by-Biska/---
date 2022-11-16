s = open('24 (10).txt').readline()

c = m = s[0]

for i in range(len(s)):
    if s[i] > s[i - 1]:
        c += s[i]
        m = max(c, m, key=len)
    else:
        c = s[i]
print(m, len(m))