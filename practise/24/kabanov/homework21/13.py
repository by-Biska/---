s = open('24 (11).txt').readline()

c = m = s[0]

for i in range(1, len(s)):
    if ord(s[i]) < ord(s[i - 1]):
        c += s[i]
        m = max(m, c, key=len)
    else:
        c = s[i]
print(m, len(m))
