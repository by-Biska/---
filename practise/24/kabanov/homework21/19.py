s = open('24 (16).txt').readline()
c = 'DBAC'
while c in s: c += "DBAC"
while c not in s: c = c[:-1]
print(len(c))
