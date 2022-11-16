s = open('24 (8).txt').readline()

while "XX" in s: s = s.replace("XX", 'X X')
while "YY" in s: s = s.replace("YY", 'Y Y')
while "ZZ" in s: s = s.replace("ZZ", 'Z Z')

m = max(s.split(), key=len)

print(m, len(m))
