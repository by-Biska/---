s = open("24 (7).txt").readline()

s = s.replace("XZZY", "XZZ ZZY")

m = max(s.split(), key=len)

print(m, len(m))

