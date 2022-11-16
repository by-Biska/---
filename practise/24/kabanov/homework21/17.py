s = open('24 (14).txt').readline()

c = m = ''

s = s.split("D")

for i in range(len(s) - 2):
    c = s[i] + "A" + s[i + 1] + "A" + s[i + 2]
    m = max(m, c, key=len)
print(m, len(m))
