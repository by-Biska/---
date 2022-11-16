s = open('24 (2).txt').readline()

# s = s.replace('ST','S T')
# m = max(s.split(), key=len)
# print(m, len(m))

c = m = s[0]

for i in range(1, len(s)):
    if s[i-1] + s[i] != 'ST':
        c += s[i]
        m = max(m, c, key=len)
    else:
        c = s[i]
print(len(m))