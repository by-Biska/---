from itertools import combinations
f = open('27A.txt')
n = int(f.readline())
k = 0
a = [int(x) for x in f]
for x, y in combinations(a, 2):
    if (x+y)%131==0:
        k+=1
print(k)
