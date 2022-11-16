# print(len(max(open('24.txt').readline().replace("C", ' ').split(), key=len)))

s = open('24.txt').readline()

c = m =''

for i in range(len(s)):
    if s[i] != 'C':
        c += s[i]
        m = max(c, m, key=len)
    else:
        c = ''
print(len(m))