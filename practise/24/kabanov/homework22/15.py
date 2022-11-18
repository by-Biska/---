s = open('24 (13).txt').readline()
k = 0

d = {x: s.count(x) for x in sorted(set(s))}

m = max(d.values())
print(m)
print([x for x in d if d[x] == m])