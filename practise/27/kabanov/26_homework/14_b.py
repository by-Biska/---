from itertools import combinations
f = open('27B_8.txt')
n = int(f.readline())

m = [[] for i in range(12)]

for i in range(n):
    x = int(f.readline())
    m[x%12] += [x]

a = []
for i in range(12):
    m[i].sort()
    a += m[i][-4:]
ans = []

for x,y,z,w in combinations(a, 4):
    if x*y*z*w%36==0:
        ans.append(x+y+z+w)
print(max(ans))