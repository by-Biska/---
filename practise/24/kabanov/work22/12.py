# min_A = 10000000000000
# c=''
# m = 0
# for s in open('24 (4).txt'):
# 	d = {x: s.count(x) for x in sorted(set(s))}
# 	print(d)
# 	if d["A"]<min_A:
# 		min_A = d["A"]
# 		s_A = s
# print(min_A, s_A)

# s = open("24 (4_5).txt").readline().strip()
# d = {x: s.count(x) for x in sorted(set(s))}

# m = max(d.values())
# print(m)
# print([x for x in d if d[x] == m])