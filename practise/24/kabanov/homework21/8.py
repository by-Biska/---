s = open("24 (6).txt").readline()

while "PP" in s: s = s.replace("PP", "P P")

m = max(s.split(), key=len)
print(m, len(m))