from itertools import combinations

f = open('27A_7.txt')
n = int(f.readline())

m = [[] for i in range(11)]

for i in range(n):
    x = int(f.readline())
    m[x % 11] += [x]

a = []
for i in range(11):
    m[i].sort()
    a += m[i][:3]
ans = []
for x, y, z in combinations(a, 3):
    if (x + y + z) % 11 == 0: ans.append(x + y + z)
print(min(ans))
