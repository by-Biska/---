s = open("24 (14).txt").readline().strip()
k = 0

d = {x: s.count(x) for x in sorted(set(s))}

print(max(d.values()) - min(d.values()))
